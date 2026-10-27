#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_vault_links.py - Scan all markdown files in ObsidianVault for broken wiki-links.
"""

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VAULT = ROOT / "MyOS" / "ObsidianVault"

WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

def get_vault_stems_and_names():
    names = set()
    stems = set()
    for f in VAULT.rglob("*"):
        if f.is_file():
            names.add(f.name.lower())
            stems.add(f.stem.lower())
    return names, stems

def check_links():
    names, stems = get_vault_stems_and_names()
    broken = []
    
    # Ignored link patterns like templates or placeholders or external docs
    ignored_targets = {
        "system-architecture.html", "system-architecture.mmd",
        "atomic insight note title", "project name hub", "focus title"
    }

    for md in VAULT.rglob("*.md"):
        # Ignore Templates/
        if "Templates" in md.parts:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for lineno, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("<!--") or line.strip().endswith("-->"):
                continue
            for match in WIKI_LINK_PATTERN.finditer(line):
                target = match.group(1).strip()
                t_lower = target.lower()
                if t_lower in ignored_targets or t_lower.startswith("http"):
                    continue
                # Check stem or name
                if t_lower not in stems and t_lower not in names and (t_lower + ".md") not in names:
                    broken.append((str(md.relative_to(ROOT)), lineno, target))

    return broken

if __name__ == "__main__":
    broken = check_links()
    if not broken:
        print("[verify-links] OK: 0 broken wiki-links found across ObsidianVault!")
        exit(0)
    else:
        print(f"[verify-links] Found {len(broken)} broken link(s):")
        for f, line, t in broken:
            print(f"  {f}:{line} -> [[{t}]]")
        exit(1)
