[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$RepoPath,
    [ValidateSet('codex','chatgpt','claude','cursor','copilot','antigravity')][string]$Agent = 'codex',
    [switch]$EngineeringProfile,
    [switch]$ResetAgentConfig,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
& (Join-Path $workspace 'setup.ps1') -WorkspacePath $workspace -RepoPath $RepoPath -Agent $Agent -EngineeringProfile:$EngineeringProfile -ResetAgentConfig:$ResetAgentConfig -DryRun:$DryRun -NonInteractive
