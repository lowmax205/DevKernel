$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
foreach ($rel in @('setup.ps1', 'MyOS\_meta\bootstrap_repo.ps1', 'MyOS\_meta\setup_agent.ps1', 'MyOS\_meta\bootstrap_machine.ps1', 'tests\verify-powershell.ps1')) {
    $tokens = $null
    $parseErrors = $null
    [System.Management.Automation.Language.Parser]::ParseFile((Join-Path $root $rel), [ref]$tokens, [ref]$parseErrors) | Out-Null
    if ($parseErrors.Count -gt 0) { throw ($parseErrors | Out-String) }
    Write-Host "[OK] PowerShell syntax: $rel"
}
