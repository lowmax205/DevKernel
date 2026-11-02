"""Integration checks against disposable Git repositories, with no external packages."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('devkernel', ROOT / 'MyOS/_meta/devkernel.py')
dk = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dk)


class StarterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='devkernel-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.workspace = self.root / 'Workspace with spaces'
        self.repo = self.root / 'External project'
        self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        dk.export_starter(self.workspace)

    def register(self, agent='codex', **kwargs):
        dk.register(self.workspace, self.repo, agent, **kwargs)

    def test_all_five_adapters_and_idempotent_merge(self):
        (self.repo / 'AGENTS.md').write_text('# Existing rules\nPreserve me.\n', encoding='utf-8')
        for agent in dk.AGENTS:
            self.register(agent)
        for rel in ('AGENTS.md', 'CLAUDE.md', 'GEMINI.md', '.cursor/rules/devkernel.mdc',
                    '.github/copilot-instructions.md'):
            content = (self.repo / rel).read_text(encoding='utf-8')
            self.assertEqual(content.count(dk.BEGIN), 1)
        before = (self.repo / 'AGENTS.md').read_bytes()
        self.register('antigravity')
        self.assertEqual(before, (self.repo / 'AGENTS.md').read_bytes())
        self.assertTrue(before.startswith(b'# Existing rules\nPreserve me.\n'))
        self.assertTrue((self.repo / '.cursor/rules/devkernel.mdc').read_text().startswith('---\n'))
        self.assertNotIn(str(self.workspace), (self.repo / 'AGENTS.md').read_text())

    def test_reset_backups_and_preserves_unrelated_content(self):
        originals = {'AGENTS.md': b'# old rules\n', '.claude/skills/private/SKILL.md': b'private skill',
                     '.github/instructions/review.instructions.md': b'review policy',
                     '.cursor/rules/custom.mdc': b'custom rules'}
        for rel, content in originals.items():
            path = self.repo / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        ci = self.repo / '.github/workflows/ci.yml'
        ci.parent.mkdir(parents=True)
        ci.write_text('name: CI\n')
        hook = self.repo / '.git/hooks/post-commit'
        hook.write_text('# keep my hook\n')
        self.register(reset=True)
        backups = list((self.repo / '.devkernel/backups').iterdir())
        self.assertEqual(len(backups), 1)
        for rel, content in originals.items():
            self.assertEqual((backups[0] / rel).read_bytes(), content)
        self.assertFalse((self.repo / '.claude/skills').exists())
        self.assertEqual(ci.read_text(), 'name: CI\n')
        self.assertEqual(hook.read_text(), '# keep my hook\n')
        self.assertTrue((backups[0] / 'manifest.json').exists())
        result = subprocess.run(['git', '-C', str(self.repo), 'check-ignore', '.devkernel/workspace.json'], capture_output=True)
        self.assertEqual(result.returncode, 0)

    def test_dry_run_writes_nothing_and_malformed_merge_fails_early(self):
        self.register(dry_run=True)
        self.assertFalse((self.repo / 'AGENTS.md').exists())
        self.assertFalse((self.repo / '.docs').exists())
        self.assertFalse((self.workspace / '.devkernel').exists())
        (self.repo / 'AGENTS.md').write_text(dk.BEGIN)
        with self.assertRaisesRegex(ValueError, 'Malformed'):
            self.register()
        self.assertFalse((self.repo / '.gitignore').exists())

    def test_nested_repository_and_collision(self):
        internal = self.workspace / 'Repos/2026/Internal'
        internal.mkdir(parents=True)
        subprocess.run(['git', 'init', '-q', str(internal)], check=True)
        dk.register(self.workspace, internal, 'cursor')
        self.register()
        other = self.root / 'another/External project'
        other.mkdir(parents=True)
        subprocess.run(['git', 'init', '-q', str(other)], check=True)
        with self.assertRaisesRegex(ValueError, 'slug already'):
            dk.register(self.workspace, other, 'codex')

    def test_profile_opt_in_and_card_preserved(self):
        self.register()
        self.assertNotIn('Optional engineering profile', (self.repo / 'AGENTS.md').read_text())
        card = self.workspace / 'MyOS/projects/external-project.md'
        card.write_text('User maintained status\n')
        self.register(engineering=True)
        self.assertIn('Optional engineering profile', (self.repo / 'AGENTS.md').read_text())
        self.assertEqual(card.read_text(), 'User maintained status\n')

    def test_clean_export_and_export_again(self):
        skills = self.workspace / 'MyOS/_meta/global-skills'
        self.assertEqual(sorted(p.name for p in skills.iterdir()), ['devkernel-manager', 'security-audit', 'setup-agent'])
        for name in dk.SECURITY_FILES:
            self.assertEqual((skills / 'security-audit' / name).read_bytes(),
                             (ROOT / 'MyOS/_meta/global-skills/security-audit' / name).read_bytes())
        for rel in dk.DOC_FILES:
            self.assertTrue((self.workspace / dk.DOC_TEMPLATES / rel).is_file())
        self.assertFalse((self.workspace / '.git').exists())
        self.assertFalse((self.workspace / 'MyOS/graphify-out/graph.json').exists())
        self.assertEqual(list((self.workspace / 'MyOS/ObsidianVault/10 - Projects').iterdir()), [])
        self.assertFalse((self.workspace / '.devkernel').exists())
        for file in self.workspace.rglob('*'):
            if file.is_file():
                self.assertFalse(file.read_bytes().startswith(b'\xef\xbb\xbf'), str(file))
        result = subprocess.run([sys.executable, str(self.workspace / 'MyOS/_meta/devkernel.py'),
                                 'export', '--destination', str(self.root / 'second export')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with self.assertRaisesRegex(ValueError, 'must not exist'):
            dk.export_starter(self.workspace)

    def test_read_only_sync_keeps_missing_repository(self):
        self.register()
        before = (self.workspace / '.devkernel/local.json').read_bytes()
        self.repo.rename(self.root / 'moved')
        result = subprocess.run([sys.executable, str(self.workspace / 'MyOS/_meta/zentora_sync.py'), '--once'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('keeping its card', result.stdout)
        self.assertEqual(before, (self.workspace / '.devkernel/local.json').read_bytes())

    def test_invalid_repo(self):
        nested = self.repo / 'subdirectory'
        nested.mkdir()
        with self.assertRaisesRegex(ValueError, 'repository root'):
            dk.register(self.workspace, nested, 'codex')
        self.assertFalse((nested / 'AGENTS.md').exists())

    def test_documentation_preserves_authored_files_and_archify(self):
        originals = {
            '.docs/PRD.md': b'# Authored requirements\n',
            '.docs/architecture/system-architecture.html': b'<html>keep diagram</html>',
            '.docs/architecture/system-architecture.mmd': b'graph TD; A-->B',
            '.docs/decisions/001.md': b'# Existing decision\n',
            '.scratch/feature/issues/01-task.md': b'Status: ready-for-agent\n',
            'docs/old-plan.md': b'# Migrate only after review\n',
        }
        for rel, raw in originals.items():
            p = self.repo / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
        self.register()
        snapshots = {rel: (self.repo / rel).read_bytes() for rel in dk.DOC_FILES}
        for rel, raw in snapshots.items():
            self.assertNotIn(b'{{Project Name}}', raw)
            self.assertNotIn(b'{{project-slug}}', raw)
            self.assertFalse(raw.startswith(b'\xef\xbb\xbf'))
        self.assertIn('projects/external-project.md', (self.repo / '.docs/MEMORY.md').read_text())
        self.assertIn('10 - Projects/External project/', (self.repo / '.docs/MEMORY.md').read_text())
        self.register(reset=True)
        for rel, raw in {**snapshots, **originals}.items():
            self.assertEqual((self.repo / rel).read_bytes(), raw)
        self.assertEqual((self.repo / 'AGENTS.md').read_text().count('Follow `.docs/agents/documentation-onboarding.md`'), 1)
        self.assertFalse((self.repo / '.agents/skills/security-audit').exists())

    def test_exported_registration_uses_its_own_templates(self):
        result = subprocess.run([sys.executable, str(self.workspace / 'MyOS/_meta/devkernel.py'),
                                 'register', '--workspace', str(self.workspace), '--repo', str(self.repo),
                                 '--agent', 'codex'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('[NEXT]', result.stdout)
        for rel in dk.DOC_FILES:
            self.assertTrue((self.repo / rel).is_file())

    def test_read_only_sync_does_not_recreate_deleted_docs(self):
        self.register()
        doc = self.repo / '.docs/PRD.md'
        doc.unlink()
        result = subprocess.run([sys.executable, str(self.workspace / 'MyOS/_meta/zentora_sync.py'), '--once'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(doc.exists())
        self.register(dry_run=True)
        self.assertFalse(doc.exists())
        self.register()
        self.assertTrue(doc.exists())

    def test_documentation_directory_conflict_fails_before_writes(self):
        (self.repo / '.docs/PRD.md').mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, 'must be a file'):
            self.register()
        self.assertFalse((self.repo / 'AGENTS.md').exists())
        self.assertFalse((self.workspace / '.devkernel').exists())

    def test_fresh_setup_ignores_parent_workspace_environment(self):
        fresh = self.root / 'Fresh workspace'
        env = dict(os.environ, ZENTORA_ROOT=str(ROOT))
        result = subprocess.run([sys.executable, str(ROOT / 'MyOS/_meta/devkernel.py'), 'setup',
                                 '--workspace', str(fresh), '--repo', str(self.repo), '--agent', 'codex'],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((fresh / 'MyOS/projects/external-project.md').exists())
        result = subprocess.run([sys.executable, str(fresh / 'MyOS/_meta/graph_recall.py'), 'starter'],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('Graphify is optional', result.stderr)

    @unittest.skipUnless(os.name == 'nt', 'Windows junction test')
    def test_reset_rejects_junction_without_touching_target(self):
        shared = self.root / 'global-skills'
        shared.mkdir()
        sentinel = shared / 'SKILL.md'
        sentinel.write_text('Keep global skills\n')
        (self.repo / '.agents').mkdir()
        link = self.repo / '.agents/skills'
        script = "New-Item -ItemType Junction -Path '" + str(link) + "' -Target '" + str(shared) + "' | Out-Null"
        subprocess.run(['powershell', '-NoProfile', '-Command', script], check=True, capture_output=True)
        with self.assertRaisesRegex(ValueError, 'Reparse|Linked'):
            self.register(reset=True)
        self.assertEqual(sentinel.read_text(), 'Keep global skills\n')
        self.assertFalse((self.repo / 'AGENTS.md').exists())

    @unittest.skipUnless(os.name == 'nt', 'Windows junction test')
    def test_documentation_rejects_junction_before_writes(self):
        shared = self.root / 'external-docs'
        shared.mkdir()
        sentinel = shared / 'PRD.md'
        sentinel.write_text('Keep external docs\n')
        link = self.repo / '.docs'
        script = "New-Item -ItemType Junction -Path '" + str(link) + "' -Target '" + str(shared) + "' | Out-Null"
        subprocess.run(['powershell', '-NoProfile', '-Command', script], check=True, capture_output=True)
        with self.assertRaisesRegex(ValueError, 'Reparse|Linked|escapes repository'):
            self.register()
        self.assertEqual(sentinel.read_text(), 'Keep external docs\n')
        self.assertFalse((self.repo / 'AGENTS.md').exists())

    @unittest.skipUnless(shutil.which('powershell'), 'Windows PowerShell required')
    def test_powershell_entry_points(self):
        command = ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File']
        result = subprocess.run(command + [str(self.workspace / 'setup.ps1'),
                                '-WorkspacePath', str(self.workspace), '-RepoPath', str(self.repo),
                                '-Agent', 'chatgpt', '-NonInteractive'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for script, args in [('bootstrap_repo.ps1', ['-RepoPath', str(self.repo), '-Agent', 'cursor']),
                             ('setup_agent.ps1', ['-TargetRepo', str(self.repo), '-Agent', 'claude']),
                             ('bootstrap_machine.ps1', ['-WorkspacePath', str(self.workspace), '-RepoPath', str(self.repo),
                                                        '-Agent', 'copilot', '-NonInteractive'])]:
            result = subprocess.run(command + [str(self.workspace / 'MyOS/_meta' / script)] + args,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
