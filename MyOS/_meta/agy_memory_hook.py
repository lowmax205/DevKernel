#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agy_memory_hook.py - Antigravity Lifecycle Hook for Automatic Zentora Memory & Graphify Recall.

Supports:
  --event SessionStart  : Injects active ICM Project Card + latest Obsidian Session summary.
  --event PreInvocation : Injects transient ephemeralMessage with Federated Graphify Context Capsule
                          (matching lastUserInput across MyOS Vault + Child Repo AST graph.json).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

MYOS_DIR = SCRIPT_DIR.parent
ZENTORA_ROOT = Path(os.environ.get("ZENTORA_ROOT") or SCRIPT_DIR.parents[1]).resolve()
PROJECTS_DIR = MYOS_DIR / "projects"
VAULT_PROJECTS_DIR = MYOS_DIR / "ObsidianVault" / "10 - Projects"
REPOS_DIR = ZENTORA_ROOT / "Repos"

TRIVIAL_INPUTS = {
    "yes", "y", "no", "n", "ok", "okay", "sure", "proceed", "continue",
    "go", "go ahead", "done", "thanks", "thank you", "lgtm", "approved"
}


def _find_child_repo_from_path(p: Path) -> Optional[Path]:
    try:
        resolved = p.resolve()
        for candidate in [resolved] + list(resolved.parents):
            if candidate == REPOS_DIR or candidate == ZENTORA_ROOT or candidate == MYOS_DIR:
                break
            if candidate.parent == REPOS_DIR or (candidate.parent.parent == REPOS_DIR):
                if (candidate / ".git").exists() or (candidate / "AGENTS.md").exists():
                    return candidate
    except Exception:
        pass
    return None


def _find_child_repo_by_name(query_text: str) -> Optional[Path]:
    if not REPOS_DIR.exists() or not query_text:
        return None
    q_low = query_text.lower()
    q_tokens = set(re.findall(r"[a-z0-9]+", q_low))

    candidates: List[Path] = []
    for l1 in sorted(REPOS_DIR.iterdir()):
        if not l1.is_dir() or l1.name.lower() in {"node_modules", ".git", "devkernel"}:
            continue
        if (l1 / ".git").exists():
            candidates.append(l1)
        else:
            for l2 in sorted(l1.iterdir()):
                if l2.is_dir() and (l2 / ".git").exists() and l2.name.lower() != "devkernel":
                    candidates.append(l2)

    for repo in candidates:
        r_low = repo.name.lower()
        r_slug = re.sub(r"[^a-z0-9]+", "-", r_low).strip("-")
        if r_low in q_low or r_slug in q_low:
            return repo
        parts = [p for p in re.findall(r"[a-z0-9]+", r_low) if len(p) >= 4 and p not in {"custom", "management", "transaction"}]
        if parts and any(p in q_tokens for p in parts):
            return repo
    return None


def _detect_active_repo(payload: Dict[str, Any], last_user_input: str) -> Optional[Path]:
    # 1. Check workspacePaths from hook payload
    for wp in payload.get("workspacePaths") or []:
        if isinstance(wp, str) and wp.strip():
            found = _find_child_repo_from_path(Path(wp))
            if found:
                return found

    # 2. Check current working directory
    found_cwd = _find_child_repo_from_path(Path.cwd())
    if found_cwd:
        return found_cwd

    # 3. Check if user prompt names a child repository
    return _find_child_repo_by_name(last_user_input)


def _get_latest_session_summary(project_name: str) -> str:
    vault_proj = VAULT_PROJECTS_DIR / project_name
    if not vault_proj.exists():
        # Try case-insensitive match
        if VAULT_PROJECTS_DIR.exists():
            for d in VAULT_PROJECTS_DIR.iterdir():
                if d.is_dir() and d.name.lower() == project_name.lower():
                    vault_proj = d
                    break
    if not vault_proj.exists():
        return ""

    session_files = sorted(
        [
            f for f in vault_proj.glob("*.md")
            if f.name != f"{vault_proj.name} Hub.md" and not f.name.endswith("Changelog Archive.md")
        ],
        key=lambda f: f.name,
        reverse=True
    )
    if not session_files:
        return ""

    latest = session_files[0]
    try:
        text = latest.read_text(encoding="utf-8", errors="replace")
        m_sum = re.search(r"^summary:\s*(.+)$", text, re.MULTILINE)
        summary_line = m_sum.group(1).strip() if m_sum else ""
        bullets: List[str] = []
        in_built = False
        for line in text.splitlines():
            if line.strip().startswith("## What was built"):
                in_built = True
                continue
            if in_built:
                if line.strip().startswith("## "):
                    break
                if line.strip().startswith("- ") and len(line.strip()) > 3:
                    bullets.append(line.strip())
                    if len(bullets) >= 3:
                        break
        parts = [f"- Latest Session Note: `[[{latest.stem}]]`"]
        if summary_line:
            parts.append(f"  - Summary: {summary_line}")
        for b in bullets:
            parts.append(f"  {b[:180]}")
        return "\n".join(parts)
    except Exception:
        return ""


def _build_session_start_message(active_repo: Optional[Path]) -> str:
    lines = ["[ZENTORA MEMORY & GRAPHIFY ACTIVE]"]
    if active_repo:
        slug = re.sub(r"[^a-z0-9]+", "-", active_repo.name.lower()).strip("-")
        card_path = PROJECTS_DIR / f"{slug}.md"
        if card_path.exists():
            card_txt = card_path.read_text(encoding="utf-8", errors="replace")
            m_stat = re.search(r"^status:\s*(.+)$", card_txt, re.MULTILINE)
            m_next = re.search(r"^next:\s*(.+)$", card_txt, re.MULTILINE)
            m_upd = re.search(r"^updated:\s*(.+)$", card_txt, re.MULTILINE)
            lines.append(
                f"- Active Project: `{active_repo.name}` (`MyOS/projects/{slug}.md`) | "
                f"Status: `{m_stat.group(1).strip() if m_stat else 'active'}` | "
                f"Updated: `{m_upd.group(1).strip() if m_upd else 'unknown'}`"
            )
            if m_next:
                lines.append(f"- Immediate Next Step: {m_next.group(1).strip()}")
        sess_summary = _get_latest_session_summary(active_repo.name)
        if sess_summary:
            lines.append(sess_summary)
    else:
        lines.append("- Scope: `ZentoraDev Workspace Root` (`MyOS/projects/*.md`)")
        if PROJECTS_DIR.exists():
            proj_summaries = []
            for card in sorted(PROJECTS_DIR.glob("*.md")):
                txt = card.read_text(encoding="utf-8", errors="replace")
                m_next = re.search(r"^next:\s*(.+)$", txt, re.MULTILINE)
                nxt = (m_next.group(1).strip()[:100] + "...") if m_next and len(m_next.group(1).strip()) > 100 else (m_next.group(1).strip() if m_next else "")
                proj_summaries.append(f"  - `{card.stem}`: {nxt}")
            if proj_summaries:
                lines.append("- Active Projects Next Steps:\n" + "\n".join(proj_summaries[:8]))
        zentora_sess = _get_latest_session_summary("ZentoraDev")
        if zentora_sess:
            lines.append(zentora_sess)

    lines.append(
        "- Mandatory Recall Rule: Use the auto-injected `[ZENTORA CONTEXT CAPSULE]`, `graphify` MCP tools "
        "(`query_graph`, `get_node`, `get_neighbors` with `project_path`), or `graph_recall.py` BEFORE raw `grep` or directory scans."
    )
    return "\n".join(lines)


def _clean_user_input(raw: str) -> str:
    text = re.sub(r"</?USER_REQUEST>", "", raw or "").strip()
    text = re.sub(r"^/[a-zA-Z0-9_-]+\s*", "", text).strip()
    return text


def handle_hook(event: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    raw_input = str(payload.get("lastUserInput") or "")
    cleaned_input = _clean_user_input(raw_input)
    active_repo = _detect_active_repo(payload, cleaned_input)

    if event == "SessionStart":
        msg = _build_session_start_message(active_repo)
        return {
            "injectSteps": [
                {
                    "systemMessage": {
                        "systemMessage": msg
                    }
                }
            ]
        }

    if event == "PreInvocation":
        if not cleaned_input or cleaned_input.lower() in TRIVIAL_INPUTS:
            return {}

        from graph_recall import extract_keywords, run_federated_recall

        keywords = extract_keywords(cleaned_input)
        if not keywords:
            return {}

        capsule = run_federated_recall(
            cleaned_input,
            repo_override=active_repo,
            max_hops=2,
            max_results=8
        )
        if "[graphify capsule] Zero graph matches" in capsule or "[graphify capsule] No significant keywords" in capsule:
            return {}

        extra_session = ""
        if active_repo:
            sess = _get_latest_session_summary(active_repo.name)
            if sess:
                extra_session = f"\n\n## 4. Latest Project Session Memory (`{active_repo.name}`)\n{sess}"

        guidance = (
            "\n\n> [Zentora Hook Directive] Start from the AST symbol file:line locations and Obsidian notes above "
            "before falling back to broad file searches. For deeper graph traversal, call the `graphify` MCP tools "
            "(`query_graph`, `get_node`, `get_neighbors`) or run `python \"<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py\" \"<keywords>\" --hops 2`."
        )
        return {
            "injectSteps": [
                {
                    "ephemeralMessage": capsule + extra_session + guidance
                }
            ]
        }

    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Antigravity Memory & Graphify Lifecycle Hook")
    parser.add_argument("--event", choices=["SessionStart", "PreInvocation"], required=True)
    args, _ = parser.parse_known_args()

    try:
        raw_stdin = ""
        if not sys.stdin.isatty():
            raw_stdin = sys.stdin.read()
        payload = json.loads(raw_stdin) if raw_stdin.strip() else {}
        result = handle_hook(args.event, payload)
        sys.stdout.write(json.dumps(result, ensure_ascii=True) + "\n")
    except Exception:
        sys.stdout.write("{}\n")


if __name__ == "__main__":
    main()

