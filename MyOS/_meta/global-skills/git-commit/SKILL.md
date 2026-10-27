---
name: git-commit
description: Universal atomic conventional git commits with automatic CHANGELOG.md Unreleased maintenance and integrated patch/minor/major release pipeline (production branch sync, annotated git tags from CHANGELOG.md, and major-only GitHub Releases).
---

# The /git-commit Skill (Unreleased + Production Release Pipeline)

Use this skill whenever asked to commit repository changes (`/git-commit`) or trigger a version release using inline or follow-up keywords (`patch`, `minor`, `major`).

---

## Core Invariants

1. **Decision Rule — Unreleased vs. Version Bump & Release**:
   - **No Version Keyword (`/git-commit` without `major`, `minor`, `patch`)**:
     - Treat as an **Unreleased Commit** (Phase 1 only).
     - Create or update `## [Unreleased]` in `CHANGELOG.md` following the repository's existing `CHANGELOG.md` format, stage all scoped files + `CHANGELOG.md`, and commit atomically. Do **not** bump versions, do **not** create tags, and do **not** merge to `production`.
   - **With Version Keyword (`/git-commit patch`, `/git-commit minor`, `/git-commit major`, or follow-up `patch` / `minor` / `major`)**:
     - If uncommitted changes exist in the working tree, execute **Phase 1 (Unreleased Commit)** first so `## [Unreleased]` is created/updated in `CHANGELOG.md` and committed cleanly.
     - Then execute **Phase 2 (Version Bump, `production` Branch Sync, Annotated Tag & Major-Only GitHub Release)**.

2. **Preserve Each Repository's Existing `CHANGELOG.md` Format**:
   - Inspect `CHANGELOG.md` before editing. Never force an alien format onto a repo that already has an established structure:
     - If the repo uses app/subsystem subsections under `## [Unreleased]` (e.g., `### Mobile | Web | Backend | Repo` or `### Frontend | Backend | Deploy / Infra | Docs & Rules | Tooling & Scripts` with `#### Added | Changed | Fixed | Removed | Security`), append bullets under the matching subsection.
     - If the repo uses standard single-level Keep a Changelog headers (`### Added | Changed | Fixed | Removed | Security` directly under `## [Unreleased]`), append bullets under those headers.
     - If `CHANGELOG.md` or `## [Unreleased]` does not exist yet, initialize a clean Keep a Changelog `## [Unreleased]` block at the top of `CHANGELOG.md`.

3. **PowerShell & Encoding Safety**:
   - Always write `CHANGELOG.md` and commit message temp files as **UTF-8 without BOM** using ASCII-safe punctuation (`-`, `--`, `->`, `...`).
   - Pass multi-line commit and tag messages via a temporary file (`git commit -F $tempFile` / `git tag -a <tag> -F $tempFile`) to prevent PowerShell quote-escaping bugs.

---

## Phase 1: Unreleased Commit Workflow (Always Runs When Working Tree Is Dirty)

1. **Pre-Commit Verification**:
   - Ensure mandatory lint/build/test gates (`$verification-before-completion`) have passed for modified packages.
2. **Inspect & Partition Working Tree**:
   - Run `git status --short` and `git diff --stat`.
   - Partition unrelated app/package changes into atomic Conventional Commits (`<type>(<scope>): <concise lowercase imperative summary>`).
3. **Create or Update `## [Unreleased]` in `CHANGELOG.md`**:
   - Add concise technical bullets under `## [Unreleased]` matching the repository's existing format.
   - Stage `CHANGELOG.md` alongside the scoped code changes so `CHANGELOG.md` rides in the same commit.
4. **Commit via Temp File**:
   ```powershell
   $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
   $tempMsg = Join-Path $env:TEMP "zentora_commit_msg.txt"
   [System.IO.File]::WriteAllText($tempMsg, "<type>(<scope>): <summary>`n`nSee CHANGELOG.md for full details.`n", $utf8NoBom)
   git add <scoped-files> CHANGELOG.md
   git commit -F $tempMsg
   Remove-Item $tempMsg -Force
   ```
5. **If No `patch | minor | major` Keyword Was Requested**:
   - Push to current branch (`git push origin HEAD` if desired by repo workflow) and stop here.

---

## Phase 2: Release, `production` Branch Sync, Tagging & Major-Only GitHub Release (`patch` | `minor` | `major`)

When `patch`, `minor`, or `major` is specified:

### Step 1: Promote `## [Unreleased]` & Bump Version Manifests
- **If the repo has a dedicated release script (e.g., `scripts/release.ps1`)**:
  - Run `.\scripts\release.ps1 -Type <patch|minor|major> -Title "<Release Title>" -Summary "<Summary>"` (which promotes `## [Unreleased]`, updates `frontend/package.json`, `backend/package.json`, `release-manifest.json`, `AGENTS.md`, commits `chore(release)`, creates tag `vX.Y.Z`, syncs/creates `production` branch, and triggers `gh release create` only on `major`).
- **If the repo has a multi-package version manager (e.g., `scripts/bump-version.mjs`)**:
  - Run the target bump script (`npm run version:web -- <bump>`, `npm run version:backend -- <bump>`, or `npm run mobile:release -- <bump>`), then execute Steps 2–4 below to tag, sync `production`, and (if `major`) create the GitHub Release.
- **Standard Repositories (`package.json` or standalone repo)**:
  1. Compute the next SemVer (`patch`, `minor`, or `major`) from `package.json` or the latest `## [X.Y.Z]` in `CHANGELOG.md` (defaulting to `0.1.0`).
  2. Update `"version"` in `package.json` (if present).
  3. Promote all bullets under `## [Unreleased]` into `## [<newVersion>] - YYYY-MM-DD` in `CHANGELOG.md`, leaving an empty `## [Unreleased]` section above it.
  4. Stage `CHANGELOG.md` and `package.json` (plus any lockfile/manifest) and commit:
     `git commit -m "chore(release): publish v<newVersion>"`

### Step 2: Create Annotated Git Tag Linked to Latest `CHANGELOG.md` Section
Extract the newly promoted `## [<newVersion>]` release notes from `CHANGELOG.md` into `$env:TEMP\zentora_release_notes.md` (UTF-8 no-BOM) and create an annotated git tag:
```powershell
git tag -a "v$newVersion" -F "$env:TEMP\zentora_release_notes.md"
```

### Step 3: Ensure & Update `production` Branch from `main`
Verify whether the `production` branch exists locally or on `origin`. If it does not exist, create it from `main`; if it exists, fast-forward/update it from `main`:
```powershell
$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
$hasLocalProd = git branch --list production
$hasRemoteProd = git ls-remote --heads origin production

if (-not $hasLocalProd -and -not $hasRemoteProd) {
    Write-Host "[INFO] Creating 'production' branch from '$currentBranch'..."
    git branch production $currentBranch
} else {
    Write-Host "[INFO] Updating 'production' branch from '$currentBranch'..."
    git checkout production
    git merge $currentBranch --ff-only
    git checkout $currentBranch
}

git push origin $currentBranch production --tags
git fetch --tags origin
```

### Step 4: GitHub Release — Trigger ONLY on `major` Updates
- **If Bump Type is `patch` or `minor`**:
  - Do **NOT** create a GitHub Release (`gh release create` is skipped). The annotated git tag `vX.Y.Z` and updated `production` branch are already pushed.
- **If Bump Type is `major`**:
  - Publish an official GitHub Release using the extracted `CHANGELOG.md` notes:
    ```powershell
    if (Get-Command gh -ErrorAction SilentlyContinue) {
        gh release create "v$newVersion" --title "Release v$newVersion" --notes-file "$env:TEMP\zentora_release_notes.md"
    } else {
        Write-Warning "[WARN] GitHub CLI (gh) not installed; create major release v$newVersion on GitHub from tag v$newVersion."
    }
    ```
