param(
    [Parameter(Mandatory = $true)]
    [string]$RepoPath,
    [switch]$ForceAgentsMd
)

$ErrorActionPreference = "Stop"
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

# Dynamically detect ZentoraDev and MyOS root
$ZentoraRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$MyOSRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$GlobalSkillsDir = Join-Path $HOME ".agents\skills"
# Template and starter directory located at MyOS\ObsidianVault\Templates\repo-agents-starter
$StarterDir = Join-Path $MyOSRoot "ObsidianVault\Templates\repo-agents-starter"

# Resolve RepoPath (accepts full path or repo name under Repos/2026 or Repos)
if (-not (Test-Path $RepoPath)) {
    $candidate2026 = Join-Path $ZentoraRoot "Repos\2026\$RepoPath"
    $candidateRoot = Join-Path $ZentoraRoot "Repos\$RepoPath"
    if (Test-Path $candidate2026) {
        $RepoPath = $candidate2026
    } elseif (Test-Path $candidateRoot) {
        $RepoPath = $candidateRoot
    } else {
        New-Item -ItemType Directory -Path $candidate2026 -Force | Out-Null
        $RepoPath = $candidate2026
        Write-Host "[INFO] Created new repository directory: $RepoPath"
    }
}
$RepoPath = (Resolve-Path $RepoPath).Path
$ProjectName = Split-Path -Leaf $RepoPath
$ProjectSlug = ($ProjectName.ToLower() -replace '[^a-z0-9]+', '-').Trim('-')
$Today = (Get-Date).ToString("yyyy-MM-dd")

Write-Host "[INFO] Bootstrapping Zentora Dev + AI Hero for '$ProjectName' (slug: '$ProjectSlug') at $RepoPath"

# 1. Ensure .agents/rules and .agents/skills exist
$RepoRulesDir = Join-Path $RepoPath ".agents\rules"
$RepoSkillsDir = Join-Path $RepoPath ".agents\skills"
New-Item -ItemType Directory -Path $RepoRulesDir -Force | Out-Null
New-Item -ItemType Directory -Path $RepoSkillsDir -Force | Out-Null

# 2. Deduplicate local .agents/skills against global ~/.agents/skills (+ remove duplicate graphify/bump-version)
$GlobalSkillNames = @("graphify", "bump-version", "git-commit")
if (Test-Path $GlobalSkillsDir) {
    $GlobalSkillNames += (Get-ChildItem $GlobalSkillsDir -Directory | ForEach-Object { $_.Name })
}
Get-ChildItem $RepoSkillsDir -Directory | ForEach-Object {
    if ($GlobalSkillNames -contains $_.Name) {
        Remove-Item $_.FullName -Recurse -Force
        Write-Host "[CLEANED] Removed duplicate global skill from repo: .agents/skills/$($_.Name)"
    }
}

# 3. Clean legacy duplicate graphify rule/workflow files
foreach ($legacyRel in @(
    ".agents\rules\graphify.md",
    ".agents\rules\graphify.mdc",
    ".agents\rules\zentora-delegation.md",
    ".agents\workflows\graphify.md",
    ".cursor\rules\graphify.mdc",
    ".cursor\rules\graphify.md"
)) {
    $legacyFile = Join-Path $RepoPath $legacyRel
    if (Test-Path $legacyFile) {
        Remove-Item $legacyFile -Force
        Write-Host "[CLEANED] Removed redundant rule/workflow: $legacyRel"
    }
}

# 4. Write canonical 00-zentora-and-ai-hero.md rule and .agents/skills.json
$RuleTemplate = [System.IO.File]::ReadAllText((Join-Path $StarterDir "00-zentora-and-ai-hero.md"), $Utf8NoBom)
$RuleContent = $RuleTemplate.
    Replace("<Project Name>", $ProjectName).
    Replace("{{Project Name}}", $ProjectName).
    Replace("<project-slug>", $ProjectSlug).
    Replace("{{project-slug}}", $ProjectSlug)
$TargetRulePath = Join-Path $RepoRulesDir "00-zentora-and-ai-hero.md"
[System.IO.File]::WriteAllText($TargetRulePath, $RuleContent, $Utf8NoBom)
Write-Host "[UPDATED] Canonical rule: .agents/rules/00-zentora-and-ai-hero.md"

$SkillsJsonSrc = Join-Path $StarterDir "skills.json"
$SkillsJsonDst = Join-Path $RepoPath ".agents\skills.json"
if (Test-Path $SkillsJsonSrc) {
    Copy-Item -Path $SkillsJsonSrc -Destination $SkillsJsonDst -Force
    Write-Host "[UPDATED] Skill manifest: .agents/skills.json"
}

# 4b. Deploy scripts/graphify.ps1 and .graphifyignore
$RepoScriptsDir = Join-Path $RepoPath "scripts"
if (-not (Test-Path $RepoScriptsDir)) { New-Item -ItemType Directory -Path $RepoScriptsDir -Force | Out-Null }
$GraphifyScriptSrc = Join-Path $StarterDir "scripts\graphify.ps1"
$GraphifyScriptDst = Join-Path $RepoScriptsDir "graphify.ps1"
if (Test-Path $GraphifyScriptSrc) {
    Copy-Item -Path $GraphifyScriptSrc -Destination $GraphifyScriptDst -Force
    Write-Host "[UPDATED] Repo graphify runner: scripts/graphify.ps1"
}

$GraphifyIgnoreSrc = Join-Path $StarterDir ".graphifyignore"
$GraphifyIgnoreDst = Join-Path $RepoPath ".graphifyignore"
if (Test-Path $GraphifyIgnoreSrc) {
    if (-not (Test-Path $GraphifyIgnoreDst)) {
        Copy-Item -Path $GraphifyIgnoreSrc -Destination $GraphifyIgnoreDst -Force
        Write-Host "[CREATED] Graphify ignore file: .graphifyignore"
    }
}

# 5. Create or update root AGENTS.md & .docs/agents/*.md
$StarterDocsAgents = Join-Path $StarterDir ".docs\agents"
$RepoDocsAgents = Join-Path $RepoPath ".docs\agents"
if (Test-Path $StarterDocsAgents) {
    New-Item -ItemType Directory -Path $RepoDocsAgents -Force | Out-Null
    Copy-Item "$StarterDocsAgents\*" -Destination $RepoDocsAgents -Force
    Write-Host "[UPDATED] AI Hero agent docs: .docs/agents/{issue-tracker,triage-labels,domain}.md"
}

$AgentsMdPath = Join-Path $RepoPath "AGENTS.md"
if ((-not (Test-Path $AgentsMdPath)) -or $ForceAgentsMd) {
    $AgentsTemplate = [System.IO.File]::ReadAllText((Join-Path $StarterDir "AGENTS.md"), $Utf8NoBom)
    $AgentsContent = $AgentsTemplate.
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug)
    [System.IO.File]::WriteAllText($AgentsMdPath, $AgentsContent, $Utf8NoBom)
    Write-Host "[UPDATED] Root entrypoint: AGENTS.md"
} else {
    $ExistingAgents = [System.IO.File]::ReadAllText($AgentsMdPath, $Utf8NoBom)
    if ($ExistingAgents -notmatch "## Agent skills") {
        $AgentSkillsBlock = @'


## Agent skills

### Issue tracker

Local markdown files under `.scratch/<feature-slug>/`. See `.docs/agents/issue-tracker.md`.

### Triage labels

Default five canonical triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `.docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`GLOSSARY.md` at repo root and ADRs in `.docs/decisions/`). See `.docs/agents/domain.md`.
'@
        [System.IO.File]::WriteAllText($AgentsMdPath, $ExistingAgents.TrimEnd() + $AgentSkillsBlock + "`n", $Utf8NoBom)
        Write-Host "[UPDATED] Appended '## Agent skills' block to existing AGENTS.md"
    } else {
        Write-Host "[KEPT] Existing root AGENTS.md (already contains '## Agent skills')"
    }
}

# 5b. Deploy Multi-Agent Adapters (Claude Code, GitHub Copilot, Cursor)
$ClaudeDst = Join-Path $RepoPath "CLAUDE.md"
if (-not (Test-Path $ClaudeDst)) {
    $ClaudeTpl = [System.IO.File]::ReadAllText((Join-Path $StarterDir "CLAUDE.md"), $Utf8NoBom)
    $ClaudeContent = $ClaudeTpl.
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug)
    [System.IO.File]::WriteAllText($ClaudeDst, $ClaudeContent, $Utf8NoBom)
    Write-Host "[CREATED] Multi-Agent Adapter: CLAUDE.md"
}

$GithubDir = Join-Path $RepoPath ".github"
$CopilotDst = Join-Path $GithubDir "copilot-instructions.md"
if (-not (Test-Path $CopilotDst)) {
    if (-not (Test-Path $GithubDir)) { New-Item -ItemType Directory -Path $GithubDir -Force | Out-Null }
    $CopilotTpl = [System.IO.File]::ReadAllText((Join-Path $StarterDir "copilot-instructions.md"), $Utf8NoBom)
    $CopilotContent = $CopilotTpl.
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug)
    [System.IO.File]::WriteAllText($CopilotDst, $CopilotContent, $Utf8NoBom)
    Write-Host "[CREATED] Multi-Agent Adapter: .github/copilot-instructions.md"
}

$CursorRulesDir = Join-Path $RepoPath ".cursor\rules"
$AdapterCursorDir = Join-Path $PSScriptRoot "agent-adapters\cursor"
if (Test-Path $AdapterCursorDir) {
    if (-not (Test-Path $CursorRulesDir)) { New-Item -ItemType Directory -Path $CursorRulesDir -Force | Out-Null }
    Get-ChildItem $AdapterCursorDir -Filter "*.mdc" | ForEach-Object {
        $dest = Join-Path $CursorRulesDir $_.Name
        if (-not (Test-Path $dest)) {
            Copy-Item -Path $_.FullName -Destination $dest -Force
            Write-Host "[CREATED] Multi-Agent Adapter: .cursor/rules/$($_.Name)"
        }
    }
}

# 6. Create root CHANGELOG.md if missing, or ensure ## [Unreleased] exists
$ChangelogPath = Join-Path $RepoPath "CHANGELOG.md"
if (-not (Test-Path $ChangelogPath)) {
    $ChangelogTemplate = [System.IO.File]::ReadAllText((Join-Path $StarterDir "CHANGELOG.md"), $Utf8NoBom)
    $ChangelogContent = $ChangelogTemplate.
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug)
    [System.IO.File]::WriteAllText($ChangelogPath, $ChangelogContent, $Utf8NoBom)
    Write-Host "[CREATED] Root CHANGELOG.md with ## [Unreleased] section"
} else {
    $ExistingChangelog = [System.IO.File]::ReadAllText($ChangelogPath, $Utf8NoBom)
    if ($ExistingChangelog -notmatch "## \[Unreleased\]") {
        if ($ExistingChangelog -match "(?m)^# .*\r?\n") {
            $ExistingChangelog = $ExistingChangelog -replace "(?m)^(# .*\r?\n)", "`$1`n## [Unreleased]`n"
        } else {
            $ExistingChangelog = "# Changelog`n`n## [Unreleased]`n`n" + $ExistingChangelog
        }
        [System.IO.File]::WriteAllText($ChangelogPath, $ExistingChangelog, $Utf8NoBom)
        Write-Host "[UPDATED] Ensured ## [Unreleased] block in existing CHANGELOG.md"
    } else {
        Write-Host "[KEPT] Existing root CHANGELOG.md (already contains '## [Unreleased]')"
    }
}

# 7. Ensure ICM Project Card exists in MyOS/projects/<project-slug>.md
$CardPath = Join-Path $MyOSRoot "projects\$ProjectSlug.md"
if (-not (Test-Path $CardPath)) {
    $CardTemplatePath = Join-Path $MyOSRoot "ObsidianVault\Templates\icm-project-card.md"
    $CardContent = ([System.IO.File]::ReadAllText($CardTemplatePath, $Utf8NoBom)).
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug).
        Replace("YYYY-MM-DD", $Today).
        Replace("<Immediate next actionable task>", "Run initial architecture review and define next milestone").
        Replace("{{Immediate next actionable task}}", "Run initial architecture review and define next milestone")
    # Point Graph path to MyOS/graphify-out/graph.json
    $GraphPath = "<ZENTORA_ROOT>/MyOS/graphify-out/graph.json"
    $CardContent = $CardContent.Replace("<ZENTORA_ROOT>/graphify-out/graph.json", $GraphPath)
    [System.IO.File]::WriteAllText($CardPath, $CardContent, $Utf8NoBom)
    Write-Host "[CREATED] ICM Project Card: MyOS/projects/$ProjectSlug.md"
}

# 8. Ensure Obsidian Project Hub folder & note exist in MyOS/ObsidianVault/10 - Projects/<Project Name>/
$ObsidianProjectDir = Join-Path $MyOSRoot "ObsidianVault\10 - Projects\$ProjectName"
New-Item -ItemType Directory -Path $ObsidianProjectDir -Force | Out-Null
$HubPath = Join-Path $ObsidianProjectDir "$ProjectName Hub.md"
if (-not (Test-Path $HubPath)) {
    $HubTemplatePath = Join-Path $MyOSRoot "ObsidianVault\Templates\project-hub-note.md"
    $HubContent = ([System.IO.File]::ReadAllText($HubTemplatePath, $Utf8NoBom)).
        Replace("<Project Name>", $ProjectName).
        Replace("{{Project Name}}", $ProjectName).
        Replace("<project-slug>", $ProjectSlug).
        Replace("{{project-slug}}", $ProjectSlug).
        Replace("YYYY-MM-DD", $Today)
    [System.IO.File]::WriteAllText($HubPath, $HubContent, $Utf8NoBom)
    Write-Host "[CREATED] Obsidian Hub Note: MyOS/ObsidianVault/10 - Projects/$ProjectName/$ProjectName Hub.md"
}

# 9. Install post-commit hook into .git/hooks/post-commit
$GitDir = Join-Path $RepoPath ".git"
if (Test-Path $GitDir) {
    $GitHooksDir = Join-Path $GitDir "hooks"
    if (-not (Test-Path $GitHooksDir)) {
        New-Item -ItemType Directory -Path $GitHooksDir -Force | Out-Null
    }
    $HookSrc = Join-Path $PSScriptRoot "git-hooks\post-commit"
    if (Test-Path $HookSrc) {
        $HookDst = Join-Path $GitHooksDir "post-commit"
        Copy-Item -Path $HookSrc -Destination $HookDst -Force
        Write-Host "[INSTALLED] Post-commit git hook: .git/hooks/post-commit"
    }
}

Write-Host "[SUCCESS] Bootstrap complete for '$ProjectName'!"
