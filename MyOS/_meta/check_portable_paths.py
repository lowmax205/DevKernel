#!/usr/bin/env python3
"""check_portable_paths.py - fail/warn when committed files hardcode a Windows drive path.

Usage:
    python MyOS/_meta/check_portable_paths.py          # scan git-tracked files (exit 1 on findings)
    python MyOS/_meta/check_portable_paths.py --warn   # always exit 0 (used by zentora_sync)

The workspace root is derived from this script's location (or ZENTORA_ROOT), never hardcoded.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(os.environ.get("ZENTORA_ROOT") or Path(__file__).resolve().parents[2]).resolve()

# A single letter (not part of a word, so URLs like https:// are ignored) followed by ':' and a path separator.
DRIVE_PATH = re.compile(r"(?<![A-Za-z0-9<])[A-Za-z]:[\\/](?![\\/])")

# Optional path prefixes to skip (none: generated graph output is scrubbed too).
ALLOW_PREFIXES = ()
SKIP_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2", ".ttf", ".zip", ".pdf", ".lock")


def tracked_files(staged_only: bool = False):
    try:
        cmd = ["git", "diff", "--cached", "--name-only", "-z"] if staged_only else ["git", "ls-files", "-z"]
        out = subprocess.run(cmd, cwd=ROOT, capture_output=True, check=True).stdout
        return [x for x in out.decode("utf-8", "replace").split("\0") if x]
    except Exception:
        return [str(p.relative_to(ROOT)).replace("\\", "/") for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def scan(staged_only: bool = False):
    drive_findings = []
    bom_findings = []
    for rel in tracked_files(staged_only=staged_only):
        norm = rel.replace("\\", "/")
        if norm.startswith(ALLOW_PREFIXES) or norm.lower().endswith(SKIP_SUFFIXES):
            continue
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            raw_bytes = path.read_bytes()
        except Exception:
            continue
        
        # Check for UTF-8 Byte Order Mark (BOM)
        if raw_bytes.startswith(b"\xef\xbb\xbf"):
            bom_findings.append(norm)

        try:
            text = raw_bytes.decode("utf-8", errors="replace")
        except Exception:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if DRIVE_PATH.search(line):
                drive_findings.append((norm, lineno, line.strip()[:140]))
    return drive_findings, bom_findings


def main():
    warn_only = "--warn" in sys.argv
    staged_only = "--staged" in sys.argv
    drive_findings, bom_findings = scan(staged_only=staged_only)

    if not drive_findings and not bom_findings:
        scope = "staged" if staged_only else "tracked"
        print(f"[portable-paths] OK: no hardcoded drive paths or BOMs in {scope} files.")
        return 0

    if bom_findings:
        print(f"[portable-paths] {len(bom_findings)} file(s) with UTF-8 BOM detected (must be UTF-8 without BOM):")
        for rel in bom_findings:
            print(f"  [{rel}] [BOM_ERROR] UTF-8 with BOM detected")

    if drive_findings:
        print(f"[portable-paths] {len(drive_findings)} hardcoded drive path(s) found; use <ZENTORA_ROOT>/... or relative paths:")
        for rel, lineno, snippet in drive_findings[:50]:
            print(f"  [{rel}:{lineno}] [PORTABILITY_ERROR] Hardcoded drive letter detected: {snippet}")

    return 0 if warn_only else 1


if __name__ == "__main__":
    sys.exit(main())
