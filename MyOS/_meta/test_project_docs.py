"""Integration checks use temporary workspace roots, never registered child repos."""
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from scaffold_project_docs import DOC_NAMES, ENTRY_MARKER
import zentora_sync

META = Path(__file__).resolve().parent
STARTER = META.parent / "ObsidianVault/Templates/repo-agents-starter"


class DocumentationOnboardingTests(unittest.TestCase):
    def run_path(self, manual, existing):
        with tempfile.TemporaryDirectory(prefix="docs-fixture-", dir=META) as tmp:
            root = Path(tmp)
            meta = root / "MyOS/_meta"
            meta.mkdir(parents=True)
            templates = root / "MyOS/ObsidianVault/Templates"
            shutil.copytree(STARTER, templates / "repo-agents-starter")
            for name in ("icm-project-card.md", "project-hub-note.md"):
                shutil.copy2(STARTER.parent / name, templates / name)
            for name in ("bootstrap_repo.ps1", "scaffold_project_docs.py"):
                shutil.copy2(META / name, meta / name)
            (root / "MyOS/projects").mkdir()
            repo = root / "Repos/2026/Fixture Project"
            repo.mkdir(parents=True)
            preserved = {}
            if existing:
                preserved = {
                    "AGENTS.md": "# Custom instructions\nKeep my conventions.\n",
                    ".docs/PRD.md": "# Developer authored PRD\n",
                    ".docs/architecture/system-architecture.html": "<html>existing</html>",
                    ".docs/architecture/system-architecture.mmd": "graph TD; A-->B",
                    ".docs/decisions/001.md": "# Existing ADR\n",
                    ".scratch/feature/issues/01-task.md": "Status: ready-for-agent\n",
                    "docs/old-plan.md": "# Do not migrate automatically\n",
                }
                for rel, text in preserved.items():
                    target = repo / rel
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(text, encoding="utf-8")

            def onboard():
                if manual:
                    result = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(meta / "bootstrap_repo.ps1"), "-RepoPath", str(repo)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("[NEXT]", result.stdout)
                else:
                    zentora_sync.sync_repo_starter_files({"is_repo_backed": True, "repo_path": str(repo), "name": repo.name, "slug": "fixture-project"})

            onboard()
            snapshots = {p: p.read_bytes() for p in (repo / ".docs").rglob("*") if p.is_file()}
            onboard()
            for path, raw in snapshots.items():
                self.assertEqual(path.read_bytes(), raw)
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
            entry = (repo / "AGENTS.md").read_text(encoding="utf-8")
            self.assertEqual(entry.count(ENTRY_MARKER), 1)
            for rel, text in preserved.items():
                actual = (repo / rel).read_text(encoding="utf-8")
                if rel == "AGENTS.md":
                    self.assertTrue(actual.startswith(text.rstrip()))
                else:
                    self.assertEqual(actual, text)
            for name in DOC_NAMES:
                text = (repo / ".docs" / name).read_text(encoding="utf-8")
                self.assertNotIn("{{Project Name}}", text)
                self.assertNotIn("{{project-slug}}", text)
            memory = (repo / ".docs/MEMORY.md").read_text(encoding="utf-8")
            self.assertIn("projects/fixture-project.md", memory)
            self.assertIn("10 - Projects/Fixture Project/", memory)
            architecture = (repo / ".docs/ARCHITECTURE.md").read_text(encoding="utf-8")
            self.assertIn("architecture/system-architecture.html", architecture)
            self.assertFalse((repo / ".agents/skills/security-audit").exists())
            json.loads((repo / ".agents/skills.json").read_text(encoding="utf-8"))

    def test_both_paths_new_and_existing(self):
        for manual in (False, True):
            for existing in (False, True):
                with self.subTest(manual=manual, existing=existing):
                    self.run_path(manual, existing)

    def test_hook_and_scoped_graphify_preservation(self):
        import agy_memory_hook
        import graph_recall

        # 1. Verify SessionStart and PreInvocation hook contracts
        erp_repo = META.parents[1] / "Repos/2026/Custom-ERP-CacayanRoofing"
        if erp_repo.exists():
            target_path = str(erp_repo)
            expected_name = "Custom-ERP-CacayanRoofing"
            query_str = "Where is POS cutting checkout handled?"
        else:
            target_path = str(META.parents[1])
            expected_name = "devkernel"
            query_str = "What is the 3-layer architecture in DevKernel?"

        sess_out = agy_memory_hook.handle_hook(
            "SessionStart",
            {"workspacePaths": [target_path]}
        )
        self.assertIn("injectSteps", sess_out)
        self.assertIn(expected_name.lower(), sess_out["injectSteps"][0]["systemMessage"]["systemMessage"].lower())

        pre_out = agy_memory_hook.handle_hook(
            "PreInvocation",
            {
                "workspacePaths": [target_path],
                "lastUserInput": query_str
            }
        )
        self.assertIn("injectSteps", pre_out)
        ephemeral = pre_out["injectSteps"][0]["ephemeralMessage"]
        self.assertIn("[ZENTORA CONTEXT CAPSULE]", ephemeral)

        # Trivial input should return empty dict
        trivial_out = agy_memory_hook.handle_hook("PreInvocation", {"lastUserInput": "yes"})
        self.assertEqual(trivial_out, {})

        # 2. Verify federated recall includes file:line locations
        rento_repo = META.parents[1] / "Repos/2026/RentoPlace"
        if rento_repo.exists():
            capsule = graph_recall.run_federated_recall(
                "ChatGateway",
                repo_override=rento_repo
            )
            self.assertIn("apps/api/src/chat/chat.gateway.ts:L46", capsule)
        else:
            capsule = graph_recall.run_federated_recall(
                "graph_recall",
                repo_override=META.parents[1]
            )
            self.assertIn("graph_recall.py", capsule)


if __name__ == "__main__":
    unittest.main()
