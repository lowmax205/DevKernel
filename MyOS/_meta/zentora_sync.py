#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zentora Dev Autonomous Reconciliation & Watcher Engine
Pure Python 3 standard library, dynamic roots, UTF-8 without BOM.

Key Features:
- Multi-level Git repository and vault-only project discovery
- Autonomous project onboarding (ICM cards, Hub notes, starter files, post-commit hooks)
- Manifest synchronization (.sync_state.json) and safe archival on deletion
- Active Projects Registry maintenance (AGENTS.md and tracker.md)
- Debounced (10s) filesystem watcher and Graphify knowledge graph sync
"""

import os
import sys
import re
import json
import time
import shutil
import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Set

# Dynamic Path Resolution (Pure Standard Library)
SCRIPT_PATH = Path(__file__).resolve()
META_DIR = SCRIPT_PATH.parent
MYOS_ROOT = SCRIPT_PATH.parents[1]
ZENTORA_ROOT = Path(os.environ.get("ZENTORA_ROOT") or SCRIPT_PATH.parents[2]).resolve()

REPOS_DIR = ZENTORA_ROOT / "Repos"
PROJECTS_DIR = MYOS_ROOT / "projects"
VAULT_DIR = MYOS_ROOT / "ObsidianVault"
VAULT_PROJECTS = VAULT_DIR / "10 - Projects"
VAULT_ARCHIVE = VAULT_DIR / "40 - Archive"
TEMPLATES_DIR = VAULT_DIR / "Templates"
TEMPLATES_STARTER = TEMPLATES_DIR / "repo-agents-starter"
POST_COMMIT_SRC = META_DIR / "git-hooks" / "post-commit"
STATE_MANIFEST = META_DIR / ".sync_state.json"
AGENTS_MD_PATH = ZENTORA_ROOT / "AGENTS.md"
DASHBOARDS_DIR = MYOS_ROOT / "dashboards"
TRACKER_MD_PATH = DASHBOARDS_DIR / "tracker.md"
ENV_GRAPHIFY_MYOS = MYOS_ROOT / ".env.graphify"
ENV_GRAPHIFY_ROOT = ZENTORA_ROOT / ".env.graphify"

# Portable placeholder written into committed docs (never a literal drive letter)
ROOT_TOKEN = "<ZENTORA_ROOT>"


def load_env_graphify() -> Dict[str, str]:
    """Load environment variables from MyOS/.env.graphify (fallback: root .env.graphify)."""
    env_vars: Dict[str, str] = {}
    target_env = ENV_GRAPHIFY_MYOS if ENV_GRAPHIFY_MYOS.exists() else ENV_GRAPHIFY_ROOT
    if target_env.exists():
        try:
            with open(target_env, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip("'\"")
                        env_vars[k] = v
                        os.environ[k] = v
        except Exception as exc:
            print(f"[zentora_sync] Note: could not load .env.graphify: {exc}")
    return env_vars


def _repo_rel_from_path(repo_path: Optional[str]) -> Optional[str]:
    """Return repo path relative to Repos/ (posix), independent of drive letter or root."""
    if not repo_path:
        return None
    parts = str(repo_path).replace("\\", "/").split("/")
    lowered = [x.lower() for x in parts]
    if "repos" in lowered:
        idx = len(lowered) - 1 - lowered[::-1].index("repos")
        rest = parts[idx + 1:]
        return "/".join(rest) if rest else None
    return None


def register_git_safe_directory(repo_path: Path) -> None:
    """Register repository path in git global safe.directory to prevent dubious ownership errors."""
    try:
        posix = repo_path.as_posix()
        proc = subprocess.run(
            ["git", "config", "--global", "--get-all", "safe.directory"],
            capture_output=True, text=True, check=False
        )
        existing = [line.strip().replace("\\", "/").lower() for line in (proc.stdout or "").splitlines()]
        if posix.lower() not in existing:
            subprocess.run(
                ["git", "config", "--global", "--add", "safe.directory", posix],
                capture_output=True, text=True, check=False
            )
    except Exception:
        pass


def move_dir_safe(src: Path, dest: Path) -> None:
    """Safely move directory tree from src to dest handling permissions and collisions."""
    dest.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        target_dir = dest / rel
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            src_f = Path(root) / f
            dest_f = target_dir / f
            if dest_f.exists():
                try:
                    os.chmod(dest_f, 0o777)
                    dest_f.unlink()
                except Exception:
                    pass
            shutil.copy2(src_f, dest_f)

    def on_rm_error(func, p, exc_info):
        try:
            os.chmod(p, 0o777)
            func(p)
        except Exception:
            pass

    shutil.rmtree(src, onerror=on_rm_error)


def discover_projects(manifest: Optional[Dict[str, Any]] = None) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Discover git repositories in Repos/* and Repos/*/* (without unbounded rglob).
    Verifies git presence via direct filesystem inspection (.git directory or file).
    Discovers vault-only projects from MyOS/ObsidianVault/10 - Projects/*.
    """
    repo_projects: List[Dict[str, Any]] = []
    vault_only_projects: List[Dict[str, Any]] = []
    discovered_names: Set[str] = set()

    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", "archive", "templates", "cache", "zentoradev", "myos", "devkernel"}
    known_repo_slugs: Set[str] = set()
    if manifest:
        for slug, p in manifest.get("projects", {}).items():
            if p.get("is_repo_backed"):
                known_repo_slugs.add(slug.lower())
                known_repo_slugs.add(p.get("name", "").lower())

    if REPOS_DIR.exists():
        # Level 1: Repos/*
        for l1 in sorted(REPOS_DIR.iterdir()):
            if not l1.is_dir() or l1.name.lower() in ignored_dirs:
                continue
            dot_git_l1 = l1 / ".git"
            if dot_git_l1.exists():
                register_git_safe_directory(l1)
                discovered_names.add(l1.name.lower())
                repo_projects.append({
                    "name": l1.name,
                    "slug": l1.name.lower(),
                    "repo_path": str(l1),
                    "is_repo_backed": True,
                    "status": "active"
                })
            else:
                # Level 2: Repos/*/* (e.g. Repos/2026/*)
                for l2 in sorted(l1.iterdir()):
                    if not l2.is_dir() or l2.name.lower() in ignored_dirs:
                        continue
                    dot_git_l2 = l2 / ".git"
                    if dot_git_l2.exists():
                        register_git_safe_directory(l2)
                        discovered_names.add(l2.name.lower())
                        repo_projects.append({
                            "name": l2.name,
                            "slug": l2.name.lower(),
                            "repo_path": str(l2),
                            "is_repo_backed": True,
                            "status": "active"
                        })

    # Vault-only projects from MyOS/ObsidianVault/10 - Projects/*
    if VAULT_PROJECTS.exists():
        for vp in sorted(VAULT_PROJECTS.iterdir()):
            if not vp.is_dir() or vp.name.lower() in ignored_dirs:
                continue
            if vp.name.lower() not in discovered_names and vp.name.lower() not in known_repo_slugs:
                vault_only_projects.append({
                    "name": vp.name,
                    "slug": vp.name.lower(),
                    "repo_path": None,
                    "is_repo_backed": False,
                    "status": "active"
                })

    return repo_projects, vault_only_projects


def load_state_manifest() -> Dict[str, Any]:
    """Load or initialize .sync_state.json with error tolerance."""
    if not STATE_MANIFEST.exists():
        return {
            "version": 1,
            "last_synced": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "projects": {}
        }
    try:
        with open(STATE_MANIFEST, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Manifest root must be an object")
            if "projects" not in data:
                data["projects"] = {}
            if "version" not in data:
                data["version"] = 1
            return data
    except Exception:
        return {
            "version": 1,
            "last_synced": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "projects": {}
        }


def save_state_manifest(manifest: Dict[str, Any]) -> None:
    """Persist .sync_state.json."""
    manifest["last_synced"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    STATE_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)


def get_post_commit_hook_script() -> str:
    """Generate the hardened dynamic post-commit hook script."""
    return """#!/bin/sh
# Git post-commit hook for Zentora Dev (Dynamic Root Resolution)

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
PROJECT_NAME=$(basename "$REPO_ROOT")
DATE_TODAY=$(date +%Y-%m-%d)
COMMIT_HASH=$(git rev-parse --short HEAD)
COMMIT_MSG=$(git log -1 --pretty=%B | head -n 1)
CHANGED_FILES=$(git diff-tree --no-commit-id --name-only -r HEAD | tr '\\n' ', ' | sed 's/,$//')

RESOLVE_START="${REPO_ROOT:-$(cd "$(dirname "$0")" && pwd)}"
CUR="$RESOLVE_START"
ZENTORA_ROOT=""
MYOS_ROOT=""

while [ "$CUR" != "/" ] && [ "$CUR" != "." ] && [ -n "$CUR" ]; do
  if [ -d "$CUR/MyOS" ]; then
    ZENTORA_ROOT="$CUR"
    MYOS_ROOT="$CUR/MyOS"
    break
  fi
  CUR=$(dirname "$CUR")
done

if [ -z "$MYOS_ROOT" ] || [ ! -d "$MYOS_ROOT" ]; then
  echo "[post-commit hook] Error: Unable to locate MyOS directory from $RESOLVE_START" >&2
  exit 0
fi

if [ "$REPO_ROOT" = "$ZENTORA_ROOT" ] || [ "$PROJECT_NAME" = "ZentoraDev" ] || [ "$PROJECT_NAME" = "MyOS" ]; then
  exit 0
fi

VAULT_PROJECT_DIR="$MYOS_ROOT/ObsidianVault/10 - Projects/$PROJECT_NAME"
SESSION_FILE="$VAULT_PROJECT_DIR/$PROJECT_NAME Session $DATE_TODAY.md"
mkdir -p "$VAULT_PROJECT_DIR"

if [ ! -f "$SESSION_FILE" ]; then
cat <<EOF> "$SESSION_FILE"
---
type: session
status: active
tags:
  - project/$PROJECT_NAME
  - session-log
created: $DATE_TODAY
summary: Automated session log for $PROJECT_NAME on $DATE_TODAY.
---
# $PROJECT_NAME - Session $DATE_TODAY

Parent: [[$PROJECT_NAME Hub]]

## Focus
- Active development on $PROJECT_NAME

## What was built
- **[$COMMIT_HASH]** $COMMIT_MSG (Files: \\`$CHANGED_FILES\\`)

## Mistakes
- 

## Decisions
- 

## Wins
- 
EOF
else
  awk -v entry="- **[$COMMIT_HASH]** $COMMIT_MSG (Files: \\`$CHANGED_FILES\\`)" '
    /^## What was built/ { print; print entry; next }
    { print }
  ' "$SESSION_FILE" > "$SESSION_FILE.tmp" && mv "$SESSION_FILE.tmp" "$SESSION_FILE"
fi

if command -v python >/dev/null 2>&1; then
  python "$MYOS_ROOT/_meta/zentora_sync.py" --once >/dev/null 2>&1 &
fi

exit 0
"""


def sync_project_card(proj: Dict[str, Any]) -> None:
    """Create or update project card in MyOS/projects/<slug>.md."""
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    slug = proj["slug"]
    name = proj["name"]
    is_repo = proj["is_repo_backed"]
    r_path = proj["repo_path"]
    today_str = datetime.now().strftime("%Y-%m-%d")

    card_path = PROJECTS_DIR / f"{slug}.md"

    if is_repo and r_path:
        try:
            rel_repo = Path(r_path).relative_to(REPOS_DIR).as_posix()
            repo_display = f"{ROOT_TOKEN}/Repos/{rel_repo}"
        except Exception:
            repo_display = f"{ROOT_TOKEN}/Repos/{Path(r_path).name}"
    else:
        repo_display = "Vault-Only (No Repo)"

    vault_display = f"{ROOT_TOKEN}/MyOS/ObsidianVault/10 - Projects/{name}"
    graph_display = f"{ROOT_TOKEN}/MyOS/graphify-out/graph.json"
    memory_display = f"{ROOT_TOKEN}/MyOS/projects/{slug}.md"

    next_task = "Run initial architecture review and define next milestone"

    if card_path.exists():
        text = card_path.read_text(encoding="utf-8", errors="replace")
        original_text = text
        m_next = re.search(r"^next:\s*(.+)$", text, flags=re.MULTILINE)
        if m_next and m_next.group(1).strip() and not m_next.group(1).strip().startswith("{{"):
            next_task = m_next.group(1).strip()

        # Update metadata while preserving existing body content and updated timestamp
        text = re.sub(r"^status:\s*[A-Za-z0-9_-]+", "status: active", text, flags=re.MULTILINE)
        # Note: Do not overwrite updated: on existing cards during sync; updated is maintained via save progress / sessions
        text = re.sub(r"(\|\s*Repo\s*\|\s*`)[^`]+(`\s*\|)", lambda m: f"{m.group(1)}{repo_display}{m.group(2)}", text)
        text = re.sub(r"(\|\s*Vault Folder\s*\|\s*`)[^`]+(`\s*\|)", lambda m: f"{m.group(1)}{vault_display}{m.group(2)}", text)
        text = re.sub(r"(\|\s*Graph\s*\|\s*`)[^`]+(`\s*\|)", lambda m: f"{m.group(1)}{graph_display}{m.group(2)}", text)
        text = re.sub(r"(\|\s*Memory\s*\|\s*`)[^`]+(`\s*\|)", lambda m: f"{m.group(1)}{memory_display}{m.group(2)}", text)

        # Legacy path cleanups
        text = re.sub(r"[A-Za-z]:[\\\\/]+ZentoraDev/", lambda _m: ROOT_TOKEN + "/", text)
        text = text.replace(ROOT_TOKEN + "/ObsidianVault/", ROOT_TOKEN + "/MyOS/ObsidianVault/")
        text = text.replace(ROOT_TOKEN + "/graphify-out/", ROOT_TOKEN + "/MyOS/graphify-out/")
        if text != original_text:
            card_path.write_text(text, encoding="utf-8")
    else:
        diag_row = ""
        mermaid_row = ""
        if is_repo and r_path:
            try:
                rel_repo = Path(r_path).relative_to(REPOS_DIR).as_posix()
                diag_row = f"| Architecture Diagram | `{ROOT_TOKEN}/Repos/{rel_repo}/.docs/architecture/system-architecture.html` |\n"
                mermaid_row = f"| Architecture Mermaid | `{ROOT_TOKEN}/Repos/{rel_repo}/.docs/architecture/system-architecture.mmd` |\n"
            except Exception:
                pass

        skills_str = "`zentora-dev-manager`, `archify`" if is_repo else "`zentora-dev-manager`"

        card_content = f"""---
type: project
status: active
next: {next_task}
updated: {today_str}
---
# {name}

## Home
| Source | Path |
| :--- | :--- |
| Repo | `{repo_display}` |
| Memory | `{memory_display}` |
| Vault Folder | `{vault_display}` |
{diag_row}{mermaid_row}| Graph | `{graph_display}` |
| Skills | {skills_str} |
"""
        card_path.write_text(card_content, encoding="utf-8")


def sync_hub_note(proj: Dict[str, Any]) -> None:
    """Create or update project Hub note in MyOS/ObsidianVault/10 - Projects/<Name>/<Name> Hub.md."""
    name = proj["name"]
    slug = proj["slug"]
    is_repo = proj["is_repo_backed"]
    r_path = proj["repo_path"]
    proj_vault_dir = VAULT_PROJECTS / name
    proj_vault_dir.mkdir(parents=True, exist_ok=True)
    hub_path = proj_vault_dir / f"{name} Hub.md"
    today_str = datetime.now().strftime("%Y-%m-%d")

    session_files = sorted([
        f.stem for f in proj_vault_dir.glob("*.md")
        if f.name != f"{name} Hub.md" and not f.name.endswith("Changelog Archive.md")
    ])

    session_links_lines = [f"- [[{sf}]]" for sf in session_files]
    session_links_block = "\n".join(session_links_lines) if session_links_lines else f"<!-- - `[[{name} Session YYYY-MM-DD]]` -->"

    if hub_path.exists():
        original_text = hub_path.read_text(encoding="utf-8", errors="replace")
        text = original_text
        if session_files:
            if "## Session History" in text:
                parts = text.split("## Session History")
                top = parts[0]
                bottom = parts[1]
                m_next = re.search(r"\n##\s+", bottom)
                subsequent = bottom[m_next.start():] if m_next else "\n"
                text = f"{top}## Session History\n{session_links_block}{subsequent}"
        # Sanitize ghost node placeholders
        text = text.replace("<project-slug>", slug)
        text = text.replace("<Project Name>", name)
        text = text.replace("<Zettelkasten Note 1>", "One Home Per Fact")
        text = text.replace("Zettelkasten", "Atomic Insights")
        text = re.sub(r"\[\[<([^>]+)>\]\]", r"[[\1]]", text)
        if text != original_text:
            hub_path.write_text(text, encoding="utf-8")
    else:
        arch_block = ""
        if is_repo and r_path:
            try:
                rel_repo = Path(r_path).relative_to(REPOS_DIR).as_posix()
                arch_block = f"""
## Architecture
- **Interactive Standalone Viewer (Archify):** `system-architecture.html` (`{ROOT_TOKEN}/Repos/{rel_repo}/.docs/architecture/system-architecture.html`)
- **Mermaid Source:** `system-architecture.mmd` (`{ROOT_TOKEN}/Repos/{rel_repo}/.docs/architecture/system-architecture.mmd`)
"""
            except Exception:
                pass

        content = f"""---
type: project-hub
status: active
tags:
  - project/hub
  - project/{slug}
created: {today_str}
summary: Central hub note for {name} linking all dated coding sessions, architectural decisions, and Atomic Insights notes.
---
# {name} Hub

> **Note:** Live project status and next steps live in `{ROOT_TOKEN}/MyOS/projects/{slug}.md` (One Home Per Fact).

## Overview
Brief 1-2 sentence description of what `{name}` does and why it exists.
{arch_block}
## Architecture & Key Decisions
<!-- - `[[Atomic Insight Note Title]]` -->

## Session History
{session_links_block}
"""
        hub_path.write_text(content, encoding="utf-8")


def sync_repo_starter_files(proj: Dict[str, Any]) -> None:
    """Inject missing starter delegation files and install post-commit hook."""
    if not proj["is_repo_backed"] or not proj["repo_path"]:
        return
    repo_path = Path(proj["repo_path"])
    if not repo_path.exists():
        return

    name = proj["name"]
    slug = proj["slug"]

    # 1. AGENTS.md
    target_agents = repo_path / "AGENTS.md"
    if not target_agents.exists() and TEMPLATES_STARTER.exists():
        src_agents = TEMPLATES_STARTER / "AGENTS.md"
        if src_agents.exists():
            shutil.copy2(src_agents, target_agents)

    # 2. .agents/skills.json
    target_skills = repo_path / ".agents" / "skills.json"
    if not target_skills.exists() and TEMPLATES_STARTER.exists():
        target_skills.parent.mkdir(parents=True, exist_ok=True)
        src_skills = TEMPLATES_STARTER / "skills.json"
        if src_skills.exists():
            shutil.copy2(src_skills, target_skills)

    # 3. .agents/rules/00-zentora-and-ai-hero.md
    target_rule = repo_path / ".agents" / "rules" / "00-zentora-and-ai-hero.md"
    if not target_rule.exists() and TEMPLATES_STARTER.exists():
        target_rule.parent.mkdir(parents=True, exist_ok=True)
        src_rule = TEMPLATES_STARTER / "00-zentora-and-ai-hero.md"
        if src_rule.exists():
            rule_txt = src_rule.read_text(encoding="utf-8")
            rule_txt = rule_txt.replace("{{Project Name}}", name)
            rule_txt = rule_txt.replace("{{project-slug}}", slug)
            target_rule.write_text(rule_txt, encoding="utf-8")

    # 4. .docs/agents/{domain.md, issue-tracker.md, triage-labels.md}
    docs_agents_dir = repo_path / ".docs" / "agents"
    docs_agents_dir.mkdir(parents=True, exist_ok=True)
    src_docs_dir = TEMPLATES_STARTER / ".docs" / "agents"
    if src_docs_dir.exists():
        for doc_name in ["domain.md", "issue-tracker.md", "triage-labels.md"]:
            t_doc = docs_agents_dir / doc_name
            s_doc = src_docs_dir / doc_name
            if not t_doc.exists() and s_doc.exists():
                shutil.copy2(s_doc, t_doc)

    # 5. CHANGELOG.md
    target_changelog = repo_path / "CHANGELOG.md"
    if not target_changelog.exists() and TEMPLATES_STARTER.exists():
        src_changelog = TEMPLATES_STARTER / "CHANGELOG.md"
        if src_changelog.exists():
            shutil.copy2(src_changelog, target_changelog)

    # 6. .git/hooks/post-commit
    dot_git = repo_path / ".git"
    if dot_git.is_dir():
        hooks_dir = dot_git / "hooks"
        hooks_dir.mkdir(parents=True, exist_ok=True)
        hook_path = hooks_dir / "post-commit"
        if not hook_path.exists() or "zentora_sync.py" not in hook_path.read_text(encoding="utf-8", errors="replace"):
            hook_script = get_post_commit_hook_script()
            hook_path.write_text(hook_script, encoding="utf-8", newline="\n")
            try:
                os.chmod(hook_path, 0o755)
            except Exception:
                pass


def generate_registry_table(active_projects: List[Dict[str, Any]]) -> str:
    """Generate Active Projects Registry markdown table sorted deterministically by project name."""
    sorted_projs = sorted(active_projects, key=lambda x: x["name"])
    lines = [
        "## Active Projects Registry",
        "",
        "| Project | Type | Repo Path | Vault Folder | Status |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for p in sorted_projs:
        name = p["name"]
        is_repo = p["is_repo_backed"]
        p_type = "Repo" if is_repo else "Vault-Only"
        if is_repo and p["repo_path"]:
            try:
                rel_repo = Path(p["repo_path"]).relative_to(REPOS_DIR).as_posix()
                repo_path_str = f"`{ROOT_TOKEN}/Repos/{rel_repo}`"
            except Exception:
                repo_path_str = f"`{ROOT_TOKEN}/Repos/{Path(p['repo_path']).name}`"
        else:
            repo_path_str = "`Vault-Only (No Repo)`"

        vault_folder_str = f"`{ROOT_TOKEN}/MyOS/ObsidianVault/10 - Projects/{name}`"
        status_str = "Active"
        lines.append(f"| `{name}` | {p_type} | {repo_path_str} | {vault_folder_str} | {status_str} |")

    return "\n".join(lines)


def sync_registries(active_projects: List[Dict[str, Any]]) -> None:
    """Synchronize ## Active Projects Registry in AGENTS.md and tracker.md."""
    registry_table = generate_registry_table(active_projects)

    # 1. Update tracker.md
    DASHBOARDS_DIR.mkdir(parents=True, exist_ok=True)
    if TRACKER_MD_PATH.exists():
        tracker_text = TRACKER_MD_PATH.read_text(encoding="utf-8", errors="replace")
        if "## Active Projects Registry" in tracker_text:
            parts = tracker_text.split("## Active Projects Registry")
            prefix = parts[0]
            rest = parts[1]
            m_next = re.search(r"\n##\s+", rest)
            suffix = rest[m_next.start():].lstrip("\r\n") if m_next else ""
            new_tracker = prefix.rstrip() + "\n\n" + registry_table + ("\n\n" + suffix if suffix else "\n")
        else:
            new_tracker = tracker_text.rstrip() + "\n\n" + registry_table + "\n"
        if new_tracker != tracker_text:
            TRACKER_MD_PATH.write_text(new_tracker, encoding="utf-8")
    else:
        new_tracker = f"# Zentora Dev Tracker\n\nLast synced: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n\n{registry_table}\n"
        TRACKER_MD_PATH.write_text(new_tracker, encoding="utf-8")

    # 2. Update AGENTS.md
    if AGENTS_MD_PATH.exists():
        agents_text = AGENTS_MD_PATH.read_text(encoding="utf-8", errors="replace")
        if "## Active Projects Registry" in agents_text:
            parts = agents_text.split("## Active Projects Registry")
            prefix = parts[0]
            rest = parts[1]
            m_next = re.search(r"\n##\s+", rest)
            suffix = rest[m_next.start():].lstrip("\r\n") if m_next else ""
            new_agents = prefix.rstrip() + "\n\n" + registry_table + ("\n\n" + suffix if suffix else "\n")
        else:
            if "## Agent skills" in agents_text:
                parts = agents_text.split("## Agent skills")
                new_agents = parts[0].rstrip() + "\n\n" + registry_table + "\n\n## Agent skills" + parts[1]
            else:
                new_agents = agents_text.rstrip() + "\n\n" + registry_table + "\n"
        if new_agents != agents_text:
            AGENTS_MD_PATH.write_text(new_agents, encoding="utf-8")


def reconcile_all(no_graphify: bool = False) -> None:
    """Run full reconciliation pass across filesystem, manifest, cards, hubs, and registries."""
    print("[zentora_sync] Starting reconciliation pass...")
    manifest = load_state_manifest()

    # Missing-repo guard: warn only. A repo can legitimately be absent on this machine
    # (different drive/path or not cloned yet); never archive or demote the project.
    missing_tracked: List[Dict[str, Any]] = []
    candidates: Dict[str, Dict[str, Any]] = dict(manifest.get("projects", {}))
    # Fresh machine (no local manifest): infer repo-backed projects from committed cards
    if PROJECTS_DIR.exists():
        for card in sorted(PROJECTS_DIR.glob("*.md")):
            if card.stem in candidates:
                continue
            m_repo = re.search(r"\|\s*Repo\s*\|\s*`([^`]+)`", card.read_text(encoding="utf-8", errors="replace"))
            if not m_repo or m_repo.group(1).startswith("Vault-Only"):
                continue
            rel_card = _repo_rel_from_path(m_repo.group(1))
            if rel_card:
                candidates[card.stem] = {
                    "name": rel_card.split("/")[-1], "is_repo_backed": True,
                    "status": "active", "repo_rel": rel_card,
                }
    for slug, tracked in list(candidates.items()):
        if not tracked.get("is_repo_backed", True) or tracked.get("status") != "active":
            continue
        rel = tracked.get("repo_rel") or _repo_rel_from_path(tracked.get("repo_path"))
        if not rel:
            continue
        rpath = REPOS_DIR / rel
        if not (rpath / ".git").exists():
            print(f"[zentora_sync] WARN: repo for {tracked.get('name', slug)} not found at {ROOT_TOKEN}/Repos/{rel}; keeping project active (not archived).")
            missing_tracked.append({
                "name": tracked.get("name", slug),
                "slug": slug,
                "repo_path": str(rpath),
                "is_repo_backed": True,
                "status": "active",
            })

    # Discover Projects after safe archival
    repo_projects, vault_only_projects = discover_projects(manifest)
    found = {p["slug"] for p in repo_projects}
    repo_projects += [m for m in missing_tracked if m["slug"] not in found]
    repo_slugs = {p["slug"] for p in repo_projects}
    vault_only_projects = [v for v in vault_only_projects if v["slug"] not in repo_slugs]
    active_projects = repo_projects + vault_only_projects

    # Onboard & Synchronize Active Projects
    for proj in active_projects:
        slug = proj["slug"]
        sync_project_card(proj)
        sync_hub_note(proj)
        sync_repo_starter_files(proj)

        manifest["projects"][slug] = {
            "name": proj["name"],
            "slug": slug,
            "repo_path": str(Path(proj["repo_path"])) if proj["repo_path"] else None,
            "repo_rel": _repo_rel_from_path(proj["repo_path"]),
            "vault_folder": str(VAULT_PROJECTS / proj["name"]),
            "is_repo_backed": proj["is_repo_backed"],
            "status": "active"
        }

    # Update Registries
    sync_registries(active_projects)

    # Persist State Manifest
    save_state_manifest(manifest)
    print(f"[zentora_sync] Reconciled {len(active_projects)} active projects successfully.")

    # Portability guard: warn if committed files hardcode a drive path
    try:
        subprocess.run([sys.executable, str(META_DIR / "check_portable_paths.py"), "--warn"], check=False, timeout=60)
    except Exception as exc:
        print(f"[zentora_sync] Note: portable-path check skipped: {exc}")

    # Trigger Graphify Knowledge Graph Sync
    if not no_graphify:
        run_graphify_sync()


def run_graphify_sync() -> None:
    """Execute Graphify extract or update subprocess safely."""
    env_vars = load_env_graphify()
    api_key = env_vars.get("DEEPSEEK_API_KEY", "").strip()
    is_valid_key = bool(api_key and api_key.startswith("sk-") and "your" not in api_key.lower())

    try:
        run_env = os.environ.copy()
        run_env.update(env_vars)
        if is_valid_key:
            cmd = ["graphify", "extract", str(MYOS_ROOT), "--backend", "deepseek", "--output", str(MYOS_ROOT)]
        else:
            cmd = ["graphify", "update", str(MYOS_ROOT), "--force"]

        print(f"[zentora_sync] Running {' '.join(cmd)}...")
        proc = subprocess.run(
            cmd,
            env=run_env,
            capture_output=True,
            text=True,
            timeout=120,
            check=False
        )
        if proc.returncode != 0:
            if is_valid_key:
                retry_cmd = cmd + ["--allow-partial"]
                retry_proc = subprocess.run(
                    retry_cmd,
                    env=run_env,
                    capture_output=True,
                    text=True,
                    timeout=120,
                    check=False
                )
                if retry_proc.returncode == 0:
                    return
            print(f"[zentora_sync] Note: graphify returned {proc.returncode}")
            if is_valid_key:
                subprocess.run(
                    ["graphify", "update", str(MYOS_ROOT)],
                    env=run_env,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False
                )
    except Exception as exc:
        print(f"[zentora_sync] Note: graphify execution handled: {exc}")


def get_filesystem_snapshot(directories: List[Path], ignored_patterns: List[str]) -> Dict[str, float]:
    """Capture mtime snapshot of files across monitored directories."""
    snapshot: Dict[str, float] = {}
    for d in directories:
        if not d.exists():
            continue
        try:
            for root, dirs, files in os.walk(d):
                dirs[:] = [
                    dir_name for dir_name in dirs
                    if not any(ign in dir_name for ign in ignored_patterns)
                ]
                for file_name in files:
                    if any(ign in file_name for ign in ignored_patterns):
                        continue
                    file_path = Path(root) / file_name
                    try:
                        if file_path.exists():
                            snapshot[str(file_path)] = file_path.stat().st_mtime
                    except (PermissionError, OSError):
                        pass
        except (PermissionError, OSError):
            pass
    return snapshot


def watch_loop(no_graphify: bool = False, debounce_seconds: float = 10.0) -> None:
    """Continuously poll and monitor filesystem with a 10-second debounce window."""
    monitored = [MYOS_ROOT / "ObsidianVault", MYOS_ROOT / "projects", ZENTORA_ROOT / "Repos"]
    ignored = [
        ".git", "node_modules", ".next", "dist", "build", ".turbo",
        "graphify-out", ".obsidian", "cache", "__pycache__"
    ]

    print(f"[zentora_sync] Starting filesystem watcher with 10s debounce...")
    last_snapshot = get_filesystem_snapshot(monitored, ignored)

    pending_event = False
    last_event_time = 0.0

    try:
        while True:
            time.sleep(1.0)
            current_snapshot = get_filesystem_snapshot(monitored, ignored)

            if current_snapshot != last_snapshot:
                pending_event = True
                last_event_time = time.time()
                last_snapshot = current_snapshot
                print(f"[zentora_sync] Filesystem change detected; debouncing (10s)...")

            if pending_event and (time.time() - last_event_time >= debounce_seconds):
                print("[zentora_sync] Debounce period elapsed. Reconciling workspace and knowledge graph...")
                reconcile_all(no_graphify=no_graphify)
                pending_event = False
                last_snapshot = get_filesystem_snapshot(monitored, ignored)

    except (KeyboardInterrupt, SystemExit):
        print("\n[zentora_sync] Watcher stopped gracefully.")


def main():
    parser = argparse.ArgumentParser(description="Zentora Dev Autonomous Reconciliation & Watcher Engine")
    parser.add_argument("--once", action="store_true", help="Run a single reconciliation cycle and exit")
    parser.add_argument("--no-graphify", action="store_true", help="Skip Graphify knowledge graph extraction")
    parser.add_argument("--watch", action="store_true", help="Start continuous debounced filesystem watcher")

    args = parser.parse_args()

    if args.watch:
        reconcile_all(no_graphify=args.no_graphify)
        watch_loop(no_graphify=args.no_graphify, debounce_seconds=10.0)
    else:
        reconcile_all(no_graphify=args.no_graphify)

    return 0


if __name__ == "__main__":
    sys.exit(main())
