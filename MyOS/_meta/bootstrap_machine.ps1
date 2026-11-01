[CmdletBinding()]
param(
    [string]$WorkspacePath,
    [string]$RepoPath,
    [ValidateSet('codex','chatgpt','claude','cursor','copilot','antigravity')][string]$Agent,
    [switch]$EngineeringProfile,
    [switch]$ResetAgentConfig,
    [switch]$DryRun,
    [switch]$NonInteractive
)
$ErrorActionPreference = 'Stop'
$setup = Join-Path $PSScriptRoot '..\..\setup.ps1'
& $setup @PSBoundParameters
