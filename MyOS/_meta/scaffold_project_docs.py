"""Shared, non-interactive documentation scaffolding for both onboarding paths."""
import argparse
from pathlib import Path

DOC_NAMES = ("PRD.md", "ARCHITECTURE.md", "RULES.md", "DESIGN.md", "TASKS.md", "MEMORY.md")
ENTRY_MARKER = "<!-- devkernel-documentation-onboarding -->"
ENTRY_BLOCK = """

<!-- devkernel-documentation-onboarding -->
## Project documentation onboarding

Before planned feature work, follow [.docs/agents/documentation-onboarding.md](.docs/agents/documentation-onboarding.md).
Inspect existing project evidence, draft the six canonical .docs files, and interview the developer.
Resolve gaps relevant to the feature; diagnosis, urgent fixes, and documentation work may proceed with gaps recorded.
Security audits are on demand: use the global `security-audit` skill (for example, `security audit this codebase`).
Bootstrap does not run audits or install repo-local copies.
"""


def scaffold(repo_path, project_name, project_slug, starter_dir=None):
    repo = Path(repo_path)
    starter = Path(starter_dir) if starter_dir else Path(__file__).resolve().parents[1] / "ObsidianVault/Templates/repo-agents-starter"
    for relative in [*(Path(".docs") / name for name in DOC_NAMES), Path(".docs/agents/documentation-onboarding.md")]:
        target = repo / relative
        if not target.exists():
            content = (starter / relative).read_text(encoding="utf-8")
            for token, value in (("{{Project Name}}", project_name), ("<Project Name>", project_name), ("{{project-slug}}", project_slug), ("<project-slug>", project_slug)):
                content = content.replace(token, value)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    entry = repo / "AGENTS.md"
    content = entry.read_text(encoding="utf-8") if entry.exists() else ""
    if ENTRY_MARKER not in content:
        entry.write_text(content.rstrip() + ENTRY_BLOCK, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--slug", required=True)
    args = parser.parse_args()
    scaffold(args.repo, args.name, args.slug)


if __name__ == "__main__":
    main()
