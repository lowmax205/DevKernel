[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][ValidateSet('codex','chatgpt','claude','cursor','copilot','antigravity')][string]$Agent,
    [Parameter(Mandatory = $true)][string]$TargetRepo,
    [switch]$EngineeringProfile,
    [switch]$ResetAgentConfig,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'bootstrap_repo.ps1') -RepoPath $TargetRepo -Agent $Agent -EngineeringProfile:$EngineeringProfile -ResetAgentConfig:$ResetAgentConfig -DryRun:$DryRun
