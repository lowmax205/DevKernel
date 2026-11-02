"""Windows starter setup and clean export. Python 3.9+, standard library only."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import date, datetime

SOURCE = Path(__file__).resolve().parents[2]
BEGIN = '<!-- devkernel:start -->'
END = '<!-- devkernel:end -->'
AGENTS = ('codex', 'claude', 'cursor', 'copilot', 'antigravity')
DOC_NAMES = ('PRD.md', 'ARCHITECTURE.md', 'RULES.md', 'DESIGN.md', 'TASKS.md', 'MEMORY.md')
DOC_FILES = tuple('.docs/' + name for name in DOC_NAMES) + ('.docs/agents/documentation-onboarding.md',)
DOC_TEMPLATES = 'MyOS/ObsidianVault/Templates/repo-agents-starter/'
# Explicit third-party exception; do not export the other historical skill bundles.
SECURITY_FILES = (
    'SKILL.md', 'AI-AND-LLM.md', 'ATTACK-CLASSES.md', 'CLIENT-SIDE.md',
    'CLOUD-AND-DEPLOYMENT.md', 'DATA-ISOLATION-AND-LIFECYCLE.md',
    'DESKTOP-MOBILE-AND-LOCAL-IPC.md', 'HUNTING.md', 'MEMORY-SAFETY-AND-BINARY.md',
    'PROTOCOLS-RPC-AND-MESSAGING.md', 'RECONNAISSANCE.md',
    'RESOURCE-EXHAUSTION-AND-AVAILABILITY.md', 'SUPPLY-CHAIN-AND-RELEASE.md',
    'VALIDATION-AND-REPORTING.md', 'WEB-PROTOCOL-AND-AUTH.md', 'report-schema.json',
    'validate-coverage-ledger.cjs', 'validate-coverage-ledger.test.cjs',
    'validate-findings.cjs', 'validate-findings.test.cjs', 'LICENSE', 'UPSTREAM.md',
)
# Only repository-local instructions and skills. Never entire .github or user homes.
RESET_PATHS = (
    'AGENTS.md', 'AGENTS.override.md', 'CLAUDE.md', 'GEMINI.md', '.cursorrules',
    '.agents/rules', '.agents/skills', '.agents/skills.json',
    '.cursor/rules', '.cursor/skills', '.claude/skills', '.claude/rules',
    '.github/copilot-instructions.md', '.github/instructions', '.github/skills',
    '.gemini/skills', '.github/agents', '.claude/agents', '.claude/commands',
    '.cursor/commands', '.agents/workflows',
)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write(content)


def check_prerequisites():
    if sys.version_info < (3, 9):
        raise ValueError('Python 3.9+ required. Install Python, enable PATH, then rerun setup.')
    if not shutil.which('git'):
        raise ValueError('Git is missing. Install Git for Windows, reopen PowerShell, then rerun setup.')


def git_root(repo):
    result = subprocess.run(['git', '-C', str(repo), 'rev-parse', '--show-toplevel'],
                            capture_output=True, text=True)
    if result.returncode:
        raise ValueError('Choose an existing Git repository: ' + str(repo))
    root = Path(result.stdout.strip()).resolve()
    if root != repo:
        raise ValueError('Use the repository root: ' + str(root))
    return root


def load_config(workspace):
    path = workspace / '.devkernel/local.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'repositories': {}}


def ensure_local_ignore(root, entry):
    path = root / '.gitignore'
    content = path.read_text(encoding='utf-8') if path.exists() else ''
    if entry not in content.splitlines():
        write(path, content + ('\n' if content and not content.endswith('\n') else '') + entry + '\n')


def validate_target(repo):
    # Refuse links and junctions rather than touching paths outside the chosen repository.
    for rel in (*RESET_PATHS, *DOC_FILES, '.gitignore', '.devkernel', '.devkernel/workspace.json',
                '.cursor/rules/devkernel.mdc'):
        path = repo / rel
        for part in (path, *path.parents):
            if part == repo:
                break
            if part.is_symlink() or getattr(part, 'is_junction', lambda: False)():
                raise ValueError('Linked agent configuration must be handled manually: ' + str(part))
            # Windows junction detection on Python versions before 3.12.
            if part.exists() and os.name == 'nt':
                import stat
                if part.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                    raise ValueError('Reparse point must be handled manually: ' + str(part))
            if repo not in part.resolve().parents and part.resolve() != repo:
                raise ValueError('Configuration escapes repository: ' + str(part))


def merge_preview(path, body):
    content = path.read_text(encoding='utf-8') if path.exists() else ''
    block = BEGIN + '\n' + body.rstrip() + '\n' + END
    if BEGIN in content or END in content:
        if content.count(BEGIN) != 1 or content.count(END) != 1 or content.index(BEGIN) > content.index(END):
            raise ValueError('Malformed DevKernel markers; resolve manually: ' + str(path))
        return content[:content.index(BEGIN)] + block + content[content.index(END) + len(END):]
    if content.strip():
        print('[REVIEW] Existing instructions preserved; review for policy conflicts: ' + str(path))
    return content + ('\n\n' if content and not content.endswith('\n\n') else '') + block + '\n'


def core_rules():
    return (SOURCE / 'MyOS/_meta/profiles/core.md').read_text(encoding='utf-8')


def documentation_preview(repo, name, slug):
    """Render missing documents before any registration writes; preserve authored files."""
    files = {}
    for rel in DOC_FILES:
        target = repo / rel
        if target.exists():
            if not target.is_file():
                raise ValueError('Documentation target must be a file: ' + str(target))
            continue
        content = (SOURCE / DOC_TEMPLATES / rel).read_text(encoding='utf-8')
        files[rel] = content.replace('{{Project Name}}', name).replace('{{project-slug}}', slug)
    return files


def adapter_files(agent, body):
    files = {'AGENTS.md': body}
    pointer = 'Read AGENTS.md in this repository and follow its DevKernel routing section.\n'
    if agent == 'claude':
        files['CLAUDE.md'] = pointer
    elif agent == 'cursor':
        # Frontmatter must stay at the beginning of an MDC file, outside merge markers.
        files['.cursor/rules/devkernel.mdc'] = pointer
    elif agent == 'copilot':
        files['.github/copilot-instructions.md'] = pointer
    elif agent == 'antigravity':
        files['GEMINI.md'] = pointer
    return files


def backup_reset(repo):
    backup = repo / '.devkernel/backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    existing = [rel for rel in RESET_PATHS if (repo / rel).exists()]
    # Back up every target successfully before clearing any of them.
    for rel in existing:
        src, dst = repo / rel, backup / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            # Reject nested links too, to keep backups and reset inside the target.
            for item in src.rglob('*'):
                if item.is_symlink() or (os.name == 'nt' and item.lstat().st_file_attributes & 1024):
                    raise ValueError('Nested link in reset target: ' + str(item))
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    if existing:
        write(backup / 'manifest.json', json.dumps({'paths': existing}, indent=2) + '\n')
    for rel in existing:
        path = repo / rel
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    if existing:
        print('[BACKUP] ' + str(backup))


def register(workspace, repo, agent, engineering=False, reset=False, dry_run=False):
    check_prerequisites()
    workspace, repo = workspace.resolve(), repo.resolve()
    git_root(repo)
    if not (workspace / 'MyOS/_meta/devkernel.py').is_file():
        raise ValueError('Workspace is not initialized. Run setup first.')
    if workspace == repo:
        raise ValueError('Register a project repository, not the DevKernel workspace itself.')
    validate_target(repo)
    name = repo.name
    slug = re.sub('[^a-z0-9]+', '-', name.lower()).strip('-')
    if not slug:
        raise ValueError('Repository name must contain an ASCII letter or digit.')
    config = load_config(workspace)
    entries = config['repositories']
    if slug in entries and Path(entries[slug]['path']).resolve() != repo:
        raise ValueError('Project slug already registered at another path: ' + slug)
    card = workspace / 'MyOS/projects' / (slug + '.md')
    if card.exists() and slug not in entries:
        raise ValueError('An unregistered project card already uses this name: ' + slug)
    relative_workspace = os.path.relpath(workspace, repo).replace('\\', '/') if workspace.drive == repo.drive else str(workspace)
    # Local-only pointer holds machine paths; committed instructions have portable references.
    body = '## DevKernel\n\nRead `.devkernel/workspace.json` for this machine\'s workspace location.\n'
    body += 'Project card: `MyOS/projects/' + slug + '.md` in that workspace.\n\n' + core_rules()
    if engineering:
        body += '\n' + (SOURCE / 'MyOS/_meta/profiles/engineering.md').read_text(encoding='utf-8')
    files = adapter_files(agent, body)
    # Validate all merges before changing files, unless reset intentionally discards them.
    previews = {rel: merge_preview(repo / rel, content) if not reset else BEGIN + '\n' + content.rstrip() + '\n' + END + '\n'
                for rel, content in files.items()}
    docs = documentation_preview(repo, name, slug)
    for rel in previews:
        if rel.endswith('.mdc') and not previews[rel].startswith('---\n'):
            previews[rel] = '---\ndescription: DevKernel workspace routing\nalwaysApply: true\n---\n' + previews[rel]
    print('[PLAN] Register ' + str(repo) + ' with ' + agent + ('; reset ALL local agent configuration' if reset else '; preserve existing configuration'))
    if dry_run:
        return
    ensure_local_ignore(repo, '/.devkernel/')
    if reset:
        backup_reset(repo)
    for rel, content in {**previews, **docs}.items():
        write(repo / rel, content)
    write(repo / '.devkernel/workspace.json', json.dumps({'workspace': relative_workspace}, indent=2) + '\n')
    entries[slug] = {'path': str(repo), 'agent': agent, 'engineering': engineering}
    write(workspace / '.devkernel/local.json', json.dumps(config, indent=2) + '\n')
    if not card.exists():
        write(card, '---\nstatus: active\nnext: Define the first project milestone\nupdated: ' + date.today().isoformat() + '\n---\n# ' + name + '\n\nRepository location: `.devkernel/local.json` in the workspace.\n')
    hub = workspace / 'MyOS/ObsidianVault/10 - Projects' / name / (name + ' Hub.md')
    if not hub.exists():
        write(hub, '# ' + name + ' Hub\n\nLive status and next steps: `MyOS/projects/' + slug + '.md`.\n\n## Architecture\n\nLink project architecture here.\n\n## Sessions\n\nKeep one consolidated session note per day in this folder.\n')
    print('[NEXT] Ask your coding agent: Follow .docs/agents/documentation-onboarding.md; inspect this repo, draft the six docs, and interview me before planned feature work.')


def export_starter(destination):
    destination = destination.resolve()
    if destination.exists():
        raise ValueError('Export destination must not exist: ' + str(destination))
    if destination == SOURCE or SOURCE in destination.parents:
        raise ValueError('Export outside the source repository.')
    # Explicit allowlist: never copy personal notes, graphs, credentials, or unapproved skills.
    files = ['README.md', 'STARTER-AGENTS.md', 'setup.ps1', '.gitignore',
             '.docs/starter-decisions.md', '.docs/external-skills.md',
             'MyOS/_meta/devkernel.py', 'MyOS/_meta/profiles/core.md',
             'MyOS/_meta/profiles/engineering.md', 'MyOS/_meta/graph_recall.py',
             'MyOS/_meta/zentora_sync.py', 'MyOS/_meta/bootstrap_repo.ps1',
             'MyOS/_meta/setup_agent.ps1', 'MyOS/_meta/bootstrap_machine.ps1',
             'MyOS/_meta/global-skills/devkernel-manager/SKILL.md',
             'MyOS/_meta/global-skills/setup-agent/SKILL.md',
             'MyOS/_meta/check_portable_paths.py',
             'tests/test_starter.py', 'tests/verify-powershell.ps1']
    files += [DOC_TEMPLATES + rel for rel in DOC_FILES]
    files += ['MyOS/_meta/global-skills/security-audit/' + name for name in SECURITY_FILES]
    for rel in files:
        if not (SOURCE / rel).is_file():
            raise ValueError('Missing export source: ' + rel)
    destination.mkdir(parents=True)
    for rel in files:
        target = destination / ('AGENTS.md' if rel == 'STARTER-AGENTS.md' else rel)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE / rel, target)
    shutil.copy2(SOURCE / 'STARTER-AGENTS.md', destination / 'STARTER-AGENTS.md')
    for rel in ('Repos', 'MyOS/projects', 'MyOS/ObsidianVault/10 - Projects',
                'MyOS/ObsidianVault/30 - Resources/Atomic Insights', 'MyOS/graphify-out'):
        (destination / rel).mkdir(parents=True, exist_ok=True)
    write(destination / 'MyOS/ObsidianVault/Templates/session-note.md',
          '# [CODE] YYYY-MM-DD - Focus\n\n## What was built\n\n## Decisions\n\n## Verification\n')
    write(destination / 'MyOS/ObsidianVault/Templates/atomic-insight-note.md',
          '# Concept\n\n## Context\n\n## Insight\n\n## Evidence\n')
    print('[EXPORTED] ' + str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    export = sub.add_parser('export', help='Create a clean starter in a new directory')
    export.add_argument('--destination', type=Path, required=True)
    for action in ('setup', 'register'):
        command = sub.add_parser(action)
        command.add_argument('--workspace', type=Path, required=True)
        command.add_argument('--repo', type=Path, required=True)
        command.add_argument('--agent', choices=AGENTS, required=True)
        command.add_argument('--engineering', action='store_true')
        command.add_argument('--reset-agent-config', action='store_true')
        command.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'export':
            export_starter(args.destination)
        else:
            check_prerequisites()
            git_root(args.repo.resolve())
            if args.command == 'setup' and not (args.workspace / 'MyOS/_meta/devkernel.py').exists():
                if args.dry_run:
                    print('[PLAN] Export starter to ' + str(args.workspace.resolve()))
                    validate_target(args.repo.resolve())
                    return 0
                export_starter(args.workspace)
            register(args.workspace, args.repo, args.agent, args.engineering,
                     args.reset_agent_config, args.dry_run)
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print('[ERROR] ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
