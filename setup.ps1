[CmdletBinding()]
param(
    [string]$WorkspacePath,
    [string]$RepoPath,
    [ValidateSet('codex', 'chatgpt', 'claude', 'cursor', 'copilot', 'antigravity')]
    [string]$Agent,
    [switch]$EngineeringProfile,
    [switch]$ResetAgentConfig,
    [switch]$DryRun,
    [switch]$NonInteractive
)
$ErrorActionPreference = 'Stop'
foreach ($tool in @('git', 'python')) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        throw "Missing $tool. Install Git for Windows and Python 3.9+ with PATH enabled, reopen PowerShell, and rerun. See README.md."
    }
}
if (-not $WorkspacePath) {
    if ($NonInteractive) { throw '-WorkspacePath is required.' }
    $WorkspacePath = Read-Host 'New workspace path (any name), or path to an existing DevKernel workspace'
}
if (-not $RepoPath) {
    if ($NonInteractive) { throw '-RepoPath is required.' }
    $RepoPath = Read-Host 'Existing Git repository root (inside Repos or anywhere else)'
}
if (-not $Agent) {
    if ($NonInteractive) { throw '-Agent is required.' }
    $Agent = Read-Host 'Agent: codex, claude, cursor, copilot, antigravity'
}
if ($Agent -eq 'chatgpt') { $Agent = 'codex' }
if (@('codex', 'claude', 'cursor', 'copilot', 'antigravity') -notcontains $Agent) { throw 'Unknown agent.' }
if (-not $NonInteractive) {
    if (-not $EngineeringProfile) {
        $EngineeringProfile = (Read-Host 'Enable optional engineering profile? [y/N]') -eq 'y'
    }
    if (-not $ResetAgentConfig) {
        $ResetAgentConfig = (Read-Host 'Back up and clear ALL repository agent instructions and local skills? [y/N]') -eq 'y'
    }
}
$setupArgs = @((Join-Path $PSScriptRoot 'MyOS\_meta\devkernel.py'), 'setup', '--workspace', $WorkspacePath, '--repo', $RepoPath, '--agent', $Agent)
if ($EngineeringProfile) { $setupArgs += '--engineering' }
if ($ResetAgentConfig) { $setupArgs += '--reset-agent-config' }
if ($DryRun) { $setupArgs += '--dry-run' }
& python @setupArgs
if ($LASTEXITCODE -ne 0) { throw 'DevKernel setup failed. See the error above.' }
