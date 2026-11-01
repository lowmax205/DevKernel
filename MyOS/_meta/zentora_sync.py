"""Read-only reconciliation of explicitly registered repositories. No hooks or installs."""
import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--once', action='store_true', help='Check registered paths once (default)')
    parser.add_argument('--no-graphify', action='store_true', help='Compatibility flag; Graphify is always explicit')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config = root / '.devkernel/local.json'
    if not config.exists():
        print('[INFO] No repositories registered. Run setup.ps1 to register the first repository.')
        return 0
    try:
        entries = json.loads(config.read_text(encoding='utf-8'))['repositories']
        for slug, entry in entries.items():
            repo = Path(entry['path'])
            if not repo.exists():
                print('[WARN] Missing repository: ' + slug + '; keeping its card and registration.')
            elif not (root / 'MyOS/projects' / (slug + '.md')).exists():
                print('[WARN] Missing card: ' + slug + '; rerun registration to recreate it.')
            else:
                print('[OK] ' + slug)
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print('[ERROR] ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
