# ==============================================================================
# setup_agent.ps1 - Multi-Agent Environment & Adapter Provisioner for ZentoraDev
# ==============================================================================
# Provisions and configures ZentoraDev or child repositories for specific AI agents:
#   powershell -ExecutionPolicy Bypass -File .\MyOS\_meta\setup_agent.ps1 -Agent <name>
#
# Supported Agents:
#   antigravity | cursor | claude | chatgpt | copilot | all
# ==============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("antigravity", "cursor", "claude", "chatgpt", "copilot", "all")]
    [string]$Agent,

    [string]$TargetRepo,

    [switch]$Force
)

$ErrorActionPreference = "Stop"
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

# 1. Resolve Paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$MyOSRoot = (Resolve-Path (Join-Path $ScriptDir "..")).Path
$WorkspaceRoot = (Resolve-Path (Join-Path $MyOSRoot "..")).Path
$AdaptersDir = Join-Path $ScriptDir "agent-adapters"

if (-not $TargetRepo) {
    $TargetRepo = $WorkspaceRoot
} else {
    if (-not (Test-Path $TargetRepo)) {
        # Check Repos/2026 or Repos
        $cand2026 = Join-Path $WorkspaceRoot "Repos\2026\$TargetRepo"
        $candRoot = Join-Path $WorkspaceRoot "Repos\$TargetRepo"
        if (Test-Path $cand2026) {
            $TargetRepo = $cand2026
        } elseif (Test-Path $candRoot) {
            $TargetRepo = $candRoot
        } else {
            Write-Error "[FATAL] Target repository not found: $TargetRepo"
            exit 1
        }
    }
    $TargetRepo = (Resolve-Path $TargetRepo).Path
}

$RepoName = Split-Path -Leaf $TargetRepo
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "       ZentoraDev Multi-Agent Adapter Provisioner                 " -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "Target Repository : $TargetRepo ($RepoName)" -ForegroundColor Yellow
Write-Host "Selected Agent    : $Agent" -ForegroundColor Yellow
Write-Host ""

function Install-Antigravity {
    param([string]$Path)
    Write-Host "[Agent: Antigravity] Configuring Antigravity / Gemini integration..." -ForegroundColor Cyan

    $globalSkills = Join-Path $HOME ".agents\skills"
    $geminiConfigDir = Join-Path $HOME ".gemini\config"
    $geminiAgyDir = Join-Path $HOME ".gemini\antigravity"
    $configSkills = Join-Path $geminiConfigDir "skills"
    $agySkills = Join-Path $geminiAgyDir "skills"

    # Ensure directories exist
    if (-not (Test-Path $geminiConfigDir)) { New-Item -ItemType Directory -Path $geminiConfigDir -Force | Out-Null }
    if (-not (Test-Path $geminiAgyDir)) { New-Item -ItemType Directory -Path $geminiAgyDir -Force | Out-Null }
    if (-not (Test-Path $globalSkills)) { New-Item -ItemType Directory -Path $globalSkills -Force | Out-Null }

    # Setup junctions to ~/.agents/skills
    if (Test-Path $configSkills) {
        $item = Get-Item $configSkills
        if ($item.LinkType -ne 'Junction') { Remove-Item $configSkills -Recurse -Force }
    }
    if (-not (Test-Path $configSkills)) {
        New-Item -ItemType Junction -Path $configSkills -Target $globalSkills | Out-Null
    }
    Write-Host "  + Junction: $configSkills -> $globalSkills" -ForegroundColor Green

    if (Test-Path $agySkills) {
        $item = Get-Item $agySkills
        if ($item.LinkType -ne 'Junction') { Remove-Item $agySkills -Recurse -Force }
    }
    if (-not (Test-Path $agySkills)) {
        New-Item -ItemType Junction -Path $agySkills -Target $globalSkills | Out-Null
    }
    Write-Host "  + Junction: $agySkills -> $globalSkills" -ForegroundColor Green

    # Global skills.json manifest
    $globalSkillsJson = Join-Path $geminiConfigDir "skills.json"
    $skillsManifest = @"
{
  "entries": [
    {
      "path": "~/.agents/skills"
    }
  ]
}
"@
    [System.IO.File]::WriteAllText($globalSkillsJson, $skillsManifest, $Utf8NoBom)
    Write-Host "  + Manifest: $globalSkillsJson" -ForegroundColor Green

    # Target repository skills.json
    $repoAgentsDir = Join-Path $Path ".agents"
    if (-not (Test-Path $repoAgentsDir)) { New-Item -ItemType Directory -Path $repoAgentsDir -Force | Out-Null }
    $repoSkillsJson = Join-Path $repoAgentsDir "skills.json"
    $adapterSkillsJson = Join-Path $AdaptersDir "antigravity\skills.json"
    if (Test-Path $adapterSkillsJson) {
        Copy-Item -Path $adapterSkillsJson -Destination $repoSkillsJson -Force
        Write-Host "  + Repo Manifest: $repoSkillsJson" -ForegroundColor Green
    }

    # Target repository rules
    $repoRulesDir = Join-Path $repoAgentsDir "rules"
    if (-not (Test-Path $repoRulesDir)) { New-Item -ItemType Directory -Path $repoRulesDir -Force | Out-Null }
    Get-ChildItem (Join-Path $AdaptersDir "antigravity") -Filter "*portable-paths.md" | ForEach-Object {
        Copy-Item -Path $_.FullName -Destination (Join-Path $repoRulesDir $_.Name) -Force
        Write-Host "  + Rule: .agents/rules/$($_.Name)" -ForegroundColor Green
    }
}

function Install-Cursor {
    param([string]$Path)
    Write-Host "[Agent: Cursor] Deploying Cursor rules (.cursor/rules/*.mdc)..." -ForegroundColor Cyan

    $cursorRulesDir = Join-Path $Path ".cursor\rules"
    if (-not (Test-Path $cursorRulesDir)) { New-Item -ItemType Directory -Path $cursorRulesDir -Force | Out-Null }

    $adapterCursorDir = Join-Path $AdaptersDir "cursor"
    if (Test-Path $adapterCursorDir) {
        Get-ChildItem $adapterCursorDir -Filter "*.mdc" | ForEach-Object {
            $destFile = Join-Path $cursorRulesDir $_.Name
            if (-not (Test-Path $destFile) -or $Force) {
                Copy-Item -Path $_.FullName -Destination $destFile -Force
                Write-Host "  + Deployed: .cursor/rules/$($_.Name)" -ForegroundColor Green
            } else {
                Write-Host "  = Already present: .cursor/rules/$($_.Name)" -ForegroundColor DarkGray
            }
        }
    }
}

function Install-Claude {
    param([string]$Path)
    Write-Host "[Agent: Claude Code] Deploying CLAUDE.md..." -ForegroundColor Cyan

    $targetClaudeMd = Join-Path $Path "CLAUDE.md"
    $adapterClaudeMd = Join-Path $AdaptersDir "claude\CLAUDE.md"

    if (Test-Path $adapterClaudeMd) {
        if (-not (Test-Path $targetClaudeMd) -or $Force) {
            Copy-Item -Path $adapterClaudeMd -Destination $targetClaudeMd -Force
            Write-Host "  + Deployed: CLAUDE.md" -ForegroundColor Green
        } else {
            Write-Host "  = Already present: CLAUDE.md" -ForegroundColor DarkGray
        }
    }
}

function Install-Copilot {
    param([string]$Path)
    Write-Host "[Agent: GitHub Copilot] Deploying .github/copilot-instructions.md..." -ForegroundColor Cyan

    $targetGithubDir = Join-Path $Path ".github"
    if (-not (Test-Path $targetGithubDir)) { New-Item -ItemType Directory -Path $targetGithubDir -Force | Out-Null }

    $targetCopilotMd = Join-Path $targetGithubDir "copilot-instructions.md"
    $adapterCopilotMd = Join-Path $AdaptersDir "copilot\copilot-instructions.md"

    if (Test-Path $adapterCopilotMd) {
        if (-not (Test-Path $targetCopilotMd) -or $Force) {
            Copy-Item -Path $adapterCopilotMd -Destination $targetCopilotMd -Force
            Write-Host "  + Deployed: .github/copilot-instructions.md" -ForegroundColor Green
        } else {
            Write-Host "  = Already present: .github/copilot-instructions.md" -ForegroundColor DarkGray
        }
    }
}

function Install-ChatGPT {
    param([string]$Path)
    Write-Host "[Agent: ChatGPT CLI / Codex] Verifying AGENTS.md readiness..." -ForegroundColor Cyan

    $targetAgentsMd = Join-Path $Path "AGENTS.md"
    if (Test-Path $targetAgentsMd) {
        Write-Host "  + Verified: AGENTS.md is present and active for ChatGPT CLI." -ForegroundColor Green
    } else {
        Write-Warning "  [WARN] AGENTS.md missing in $Path. ChatGPT CLI reads AGENTS.md natively."
    }
}

# Execute installation based on selection
switch ($Agent) {
    "antigravity" { Install-Antigravity -Path $TargetRepo }
    "cursor"      { Install-Cursor -Path $TargetRepo }
    "claude"      { Install-Claude -Path $TargetRepo }
    "copilot"     { Install-Copilot -Path $TargetRepo }
    "chatgpt"     { Install-ChatGPT -Path $TargetRepo }
    "all"         {
        Install-Antigravity -Path $TargetRepo
        Install-Cursor -Path $TargetRepo
        Install-Claude -Path $TargetRepo
        Install-Copilot -Path $TargetRepo
        Install-ChatGPT -Path $TargetRepo
    }
}

Write-Host "`n[SUCCESS] Setup for agent '$Agent' completed in $RepoName." -ForegroundColor Green
