<#
.SYNOPSIS
    Installs and configures Ponytail (pinned skill) and OmniRoute (local AI gateway).
.DESCRIPTION
    Ponytail: vendored at MyOS/_meta/global-skills/ponytail (upstream commit 96608e0, permanent pin).
      - Injects a managed <!-- ponytail:begin/end --> block into the global-skills copy of
        surgical-coding, then distributes via setup_agent.ps1 (global skills mirror).
    OmniRoute: npm i -g omniroute, creates MyOS/.env.omniroute from the example if missing.
      Does NOT start the gateway; prints the commands instead.
.PARAMETER Only
    ponytail | omniroute | all (default)
.PARAMETER Agent
    Agent adapter passed to setup_agent.ps1 (default: all).
.PARAMETER DryRun
    Print what would happen without changing anything.
#>
param(
    [ValidateSet("ponytail", "omniroute", "all")]
    [string]$Only = "all",
    [ValidateSet("antigravity", "cursor", "claude", "chatgpt", "copilot", "all")]
    [string]$Agent = "all",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$MyOS = Split-Path -Parent $ScriptDir
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Step($msg) { Write-Host $msg -ForegroundColor Cyan }
function Act($msg) { if ($DryRun) { Write-Host "  [DRY-RUN] $msg" -ForegroundColor Yellow } else { Write-Host "  + $msg" -ForegroundColor Green } }

function Install-Ponytail {
    Step "[Ponytail] Vendored skill + surgical-coding integration"
    $skill = Join-Path $ScriptDir "global-skills\ponytail\SKILL.md"
    $surg = Join-Path $ScriptDir "global-skills\surgical-coding\SKILL.md"
    if (-not (Test-Path $skill)) { throw "Vendored Ponytail missing: $skill" }
    if (-not (Test-Path $surg)) { throw "surgical-coding source missing: $surg" }

    $begin = "<!-- ponytail:begin -->"
    $end = "<!-- ponytail:end -->"
    $block = @"
$begin
## Ponytail Integration (managed by install_devtools.ps1 - do not edit)

Ponytail (skill ``ponytail``, pinned upstream 96608e0) decides **how much** to write; this skill decides **how** to edit.
Before writing code, take the first option that fully works:
1. Skip it if nobody asked for it (name what you skipped in one line).
2. Reuse what already exists in the codebase.
3. Use the standard library or a platform feature.
4. Use an already-installed dependency (never add one for a few lines).
5. Otherwise write the minimum code that works.

Never cut validation, error handling, security, or accessibility. On conflict: Ponytail wins on size, surgical-coding wins on scope of edits.
$end
"@
    $text = [System.IO.File]::ReadAllText($surg)
    $pattern = "(?s)" + [regex]::Escape($begin) + ".*?" + [regex]::Escape($end)
    if ($text -match $pattern) {
        $new = [regex]::Replace($text, $pattern, { param($m) $block.TrimEnd() })
    } else {
        $new = $text.TrimEnd() + "`r`n`r`n---`r`n`r`n" + $block.TrimEnd() + "`r`n"
    }
    if ($new -eq $text) {
        Write-Host "  = surgical-coding already up to date" -ForegroundColor Gray
    } else {
        Act "Inject Ponytail block into $surg"
        if (-not $DryRun) {
            $bak = "$surg.bak"
            if (-not (Test-Path $bak)) { Copy-Item $surg $bak }
            [System.IO.File]::WriteAllText($surg, $new, $Utf8NoBom)
        }
    }

    $setup = Join-Path $ScriptDir "setup_agent.ps1"
    Act "Distribute global skills: setup_agent.ps1 -Agent $Agent"
    if (-not $DryRun) {
        & powershell -ExecutionPolicy Bypass -File $setup -Agent $Agent
        if ($LASTEXITCODE -ne 0) { throw "setup_agent.ps1 failed (exit $LASTEXITCODE)" }
    }
}

function Install-OmniRoute {
    Step "[OmniRoute] Install + configure"
    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) { throw "npm not found. Install Node.js first." }

    if (Get-Command omniroute -ErrorAction SilentlyContinue) {
        Write-Host "  = omniroute already installed" -ForegroundColor Gray
    } else {
        Act "npm install -g omniroute"
        if (-not $DryRun) {
            npm install -g omniroute
            if ($LASTEXITCODE -ne 0) { throw "npm install -g omniroute failed" }
        }
    }

    $envFile = Join-Path $MyOS ".env.omniroute"
    $example = Join-Path $MyOS ".env.omniroute.example"
    if (Test-Path $envFile) {
        Write-Host "  = .env.omniroute exists (not modified)" -ForegroundColor Gray
    } else {
        Act "Create $envFile from example"
        if (-not $DryRun) {
            $content = [System.IO.File]::ReadAllText($example)
            $secure = Read-Host "  OmniRoute API key (from the dashboard; Enter to skip)" -AsSecureString
            $key = [System.Net.NetworkCredential]::new("", $secure).Password
            if ($key) { $content = $content -replace 'OMNIROUTE_API_KEY=""', "OMNIROUTE_API_KEY=`"$key`"" }
            [System.IO.File]::WriteAllText($envFile, $content, $Utf8NoBom)
        }
    }

    $up = $false
    try { $null = Invoke-WebRequest "http://127.0.0.1:20128" -TimeoutSec 3 -UseBasicParsing; $up = $true } catch { }
    if ($up) { Write-Host "  = gateway responding on :20128" -ForegroundColor Gray }
    else {
        Write-Host "  Gateway not running. Start it with:   omniroute" -ForegroundColor Yellow
        Write-Host "  Then add provider keys in the dashboard: http://localhost:20128" -ForegroundColor Yellow
        Write-Host "  Research session:   $(Join-Path $ScriptDir 'launch_research_omni.ps1')" -ForegroundColor Yellow
    }
}

if ($Only -in "ponytail", "all") { Install-Ponytail }
if ($Only -in "omniroute", "all") { Install-OmniRoute }
Step "Done."

