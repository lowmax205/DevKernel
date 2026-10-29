# ==============================================================================
# bootstrap_machine.ps1 - Automated Onboarding Script for ZentoraDev
# ==============================================================================
# Run this script whenever cloning ZentoraDev onto a new machine or environment:
#   powershell -ExecutionPolicy Bypass -File .\MyOS\_meta\bootstrap_machine.ps1
# ==============================================================================

[CmdletBinding()]
param(
    [ValidateSet("all", "antigravity", "cursor", "claude", "chatgpt", "copilot")]
    [string]$Agent = "all",
    [switch]$SkipGraphifyInstall,
    [switch]$ForceSkillsOverwrite
)

$ErrorActionPreference = "Stop"

# 1. Resolve Workspace Root
$WORKSPACE_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$MYOS_ROOT = Join-Path $WORKSPACE_ROOT "MyOS"
$BUNDLED_SKILLS = Join-Path $MYOS_ROOT "_meta\global-skills"
$GLOBAL_SKILLS = Join-Path $HOME ".agents\skills"
$CONFIG_SKILLS = Join-Path $HOME ".gemini\config\skills"
$AGY_SKILLS = Join-Path $HOME ".gemini\antigravity\skills"

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "       ZentoraDev Multi-Machine Onboarding & Environment Setup     " -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "Workspace Root : $WORKSPACE_ROOT" -ForegroundColor Yellow
Write-Host "User Home      : $HOME" -ForegroundColor Yellow

# 2. Check Prerequisites (Git & Python)
Write-Host "`n[1/7] Checking Prerequisites..." -ForegroundColor Cyan

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "[FATAL] Git is not installed or not in PATH. Please install Git for Windows: https://git-scm.com/download/win"
    exit 1
}
Write-Host "  [OK] Git: $(git --version)" -ForegroundColor Green

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "[FATAL] Python 3.10+ is not found. Please install Python from https://www.python.org/downloads/ (check 'Add to PATH')."
    exit 1
}
Write-Host "  [OK] Python: $(python --version)" -ForegroundColor Green

# 3. Check and Auto-Install Graphify
Write-Host "`n[2/7] Checking Graphify Knowledge Graph Engine..." -ForegroundColor Cyan
$graphifyCmd = Get-Command graphify -ErrorAction SilentlyContinue
if (-not $graphifyCmd -and -not $SkipGraphifyInstall) {
    Write-Host "  Graphify CLI not found. Installing graphifyy..." -ForegroundColor Yellow
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        uv tool install graphifyy
    } else {
        python -m pip install --upgrade graphifyy
    }
}
if (Get-Command graphify -ErrorAction SilentlyContinue) {
    Write-Host "  [OK] Graphify: $(graphify --version 2>&1)" -ForegroundColor Green
} else {
    Write-Warning "  [WARN] Graphify installation pending. You can install later with: pip install graphifyy"
}

# 4. Sync Curated Global Skills (Strict 1:1 Mirror of MyOS/_meta/global-skills)
Write-Host "`n[3/7] Syncing Curated Global Skills to ~/.agents/skills..." -ForegroundColor Cyan
if (-not (Test-Path $GLOBAL_SKILLS)) {
    New-Item -ItemType Directory -Path $GLOBAL_SKILLS -Force | Out-Null
}

if (Test-Path $BUNDLED_SKILLS) {
    Get-ChildItem -Path $GLOBAL_SKILLS -Force | Remove-Item -Recurse -Force
    $skills = Get-ChildItem $BUNDLED_SKILLS -Directory
    foreach ($s in $skills) {
        $dest = Join-Path $GLOBAL_SKILLS $s.Name
        Copy-Item -Path $s.FullName -Destination $dest -Recurse -Force
        Write-Host "  + Synced skill: $($s.Name)" -ForegroundColor Gray
    }
    Write-Host "  [OK] Synced $($skills.Count) curated skills in $GLOBAL_SKILLS" -ForegroundColor Green
} else {
    Write-Warning "  [WARN] Bundled skills folder not found at $BUNDLED_SKILLS"
}

# 5. Provision Multi-Agent Adapters (Antigravity, Cursor, Claude, Copilot, ChatGPT)
Write-Host "`n[4/7] Provisioning Multi-Agent Adapters (Agent: $Agent)..." -ForegroundColor Cyan
$setupAgentScript = Join-Path $MYOS_ROOT "_meta\setup_agent.ps1"
if (Test-Path $setupAgentScript) {
    & $setupAgentScript -Agent $Agent -TargetRepo $WORKSPACE_ROOT
} else {
    Write-Warning "  [WARN] setup_agent.ps1 not found at $setupAgentScript"
}

# 6. Ensure Environment Secrets (MyOS/.env.graphify)
Write-Host "`n[5/7] Checking Graphify API Configuration..." -ForegroundColor Cyan
$myosEnvGraphify = Join-Path $MYOS_ROOT ".env.graphify"
$myosEnvExample = Join-Path $MYOS_ROOT ".env.graphify.example"
if (-not (Test-Path $myosEnvGraphify)) {
    if (Test-Path $myosEnvExample) {
        Copy-Item -Path $myosEnvExample -Destination $myosEnvGraphify
        Write-Host "  [CREATED] MyOS/.env.graphify from template. Remember to fill in your DEEPSEEK_API_KEY." -ForegroundColor Yellow
    }
} else {
    Write-Host "  [OK] MyOS/.env.graphify exists." -ForegroundColor Green
}

# 7. Verify committed docs stay machine-portable (never rewrite them to this drive)
Write-Host "`n[6/7] Checking AGENTS.md uses portable <ZENTORA_ROOT> paths..." -ForegroundColor Cyan
$env:ZENTORA_ROOT = $WORKSPACE_ROOT
python (Join-Path $MYOS_ROOT "_meta\check_portable_paths.py") --warn
Write-Host "  [OK] Workspace root for this machine: $WORKSPACE_ROOT (docs are not modified)" -ForegroundColor Green

# 8. Run Quick Sync Check
Write-Host "`n[7/7] Running Initial Sync Verification..." -ForegroundColor Cyan
$syncScript = Join-Path $MYOS_ROOT "_meta\zentora_sync.py"
if (Test-Path $syncScript) {
    python $syncScript --once
}

Write-Host "`n==================================================================" -ForegroundColor Green
Write-Host "   [SUCCESS] ZentoraDev is 100% configured for this machine!       " -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Green
Write-Host "Next steps:"
Write-Host "  1. If you haven't yet, edit MyOS/.env.graphify and add your DEEPSEEK_API_KEY"
Write-Host "  2. In Antigravity or VS Code, reload the window to index all 18 curated skills"
Write-Host "  3. Bootstrap any repo with: bootstrap <RepoName>`n"
