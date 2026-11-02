# scripts/graphify.ps1 - Fast Repo-Local AST Indexer & Federated Graph Recall
[CmdletBinding()]
param(
    [Parameter(Position = 0, Mandatory = $true)]
    [ValidateSet("update", "query", "path", "explain", "sync", "mcp")]
    [string]$Action,

    [Parameter(Position = 1)]
    [string]$QueryText,

    [Parameter(Position = 2)]
    [string]$TargetText,

    [switch]$Force,
    [switch]$NoCluster,
    [switch]$SyncToMyOS
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
if (-not $RepoRoot) { $RepoRoot = (Get-Location).Path }
$ZentoraRoot = $env:ZENTORA_ROOT
if (-not $ZentoraRoot) {
    $cursor = $RepoRoot
    while ($cursor -and (Test-Path $cursor)) {
        if (Test-Path (Join-Path $cursor "MyOS")) {
            $ZentoraRoot = $cursor
            break
        }
        $parent = Split-Path -Parent $cursor
        if ($parent -eq $cursor) { break }
        $cursor = $parent
    }
}

switch ($Action) {
    "update" {
        Write-Host "[Graphify] Running fast AST code re-index for repo: $RepoRoot" -ForegroundColor Cyan
        $graphifyArgs = @("update", $RepoRoot)
        if ($Force) { $graphifyArgs += "--force" }
        if ($NoCluster) { $graphifyArgs += "--no-cluster" }
        & graphify @graphifyArgs

        if ($SyncToMyOS -and $ZentoraRoot) {
            Write-Host "[Graphify] Syncing local repo nodes to central MyOS graph..." -ForegroundColor Yellow
            $syncScript = Join-Path $ZentoraRoot "MyOS\_meta\zentora_sync.py"
            if (Test-Path $syncScript) {
                python $syncScript --once
            }
        }
    }
    "query" {
        if (-not $QueryText) {
            Write-Error "Please specify a query string: .\scripts\graphify.ps1 query '<english keywords>'"
            exit 1
        }
        $recallScript = if ($ZentoraRoot) { Join-Path $ZentoraRoot "MyOS\_meta\graph_recall.py" } else { $null }
        if ($recallScript -and (Test-Path $recallScript)) {
            python $recallScript "$QueryText" --repo "$RepoRoot" --hops 2
        } else {
            & graphify query "$QueryText"
        }
    }
    "path" {
        if (-not $QueryText -or -not $TargetText) {
            Write-Error "Usage: .\scripts\graphify.ps1 path '<FromNode>' '<ToNode>'"
            exit 1
        }
        & graphify path "$QueryText" "$TargetText"
    }
    "explain" {
        if (-not $QueryText) {
            Write-Error "Usage: .\scripts\graphify.ps1 explain '<NodeOrConcept>'"
            exit 1
        }
        & graphify explain "$QueryText"
    }
    "mcp" {
        $graphJson = Join-Path $RepoRoot "graphify-out\graph.json"
        if (Test-Path $graphJson) {
            python -m graphify.serve "$graphJson"
        } else {
            python -m graphify.serve
        }
    }
    "sync" {
        if ($ZentoraRoot) {
            $syncScript = Join-Path $ZentoraRoot "MyOS\_meta\zentora_sync.py"
            if (Test-Path $syncScript) {
                python $syncScript --once
            }
        }
    }
}
