# Claude Code Guidelines — DevKernel (MyOS)

You are operating inside DevKernel or a DevKernel-managed repository. All interactions must strictly follow the routing and architectural rules established in `AGENTS.md`.

## 1. 4-Step Surgical Lookup (BrewedOps 3-Layer Architecture)
Execute this deterministic 4-step surgical lookup on every task:
1. **Master Routing Table:** Read `AGENTS.md` before taking architectural actions or answering system status questions.
2. **ICM Project Card:** Read `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md` for live `status:` and immediate `next:`.
3. **Obsidian Hub & Session:** Read `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/` (`<Project Name> Hub.md` and latest dated session note) for recent decisions, what was built, and mistakes.
4. **Dynamic Context Recall (2–8 files):** Run `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<prompt keywords>" --repo . --hops 2`. Read **only the ~4 to 5 highly relevant files** routed in the manifest.

## 2. One Home Per Fact (Canonical Boundaries)
- Live Status & Immediate Next Steps live **ONLY** in `MyOS/projects/<project-slug>.md`.
- Full History & Session Notes live **ONLY** in `MyOS/ObsidianVault/10 - Projects/<Project Name>/`. Notes must NEVER live at the vault root.
- Reusable Gotchas & Decisions live **ONLY** in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
- Code & Concept Graph lives in `MyOS/graphify-out/graph.json` and repo-local `graphify-out/graph.json`.

## 3. Terminal Guardrails & Engineering Invariants
- Never use bash chaining (`&&`, `||`, or `cd "path" && command`). Use PowerShell sequencing: `command1; if ($?) { command2 }` or set target directory directly.
- All files must be saved as **UTF-8 without BOM** using ASCII-safe punctuation.
- Run fresh verification (`npm run lint:fix` / `lint` and `npm run build` exit code `0`) before completing tasks or committing.
- Consult `.docs/RULES.md` on-demand for backend design patterns (Tier 1 CRUD: Repo + Service; Tier 2: Strategy, Adapter, Observer, Breaker).
- Consult `context7` MCP tool on-demand for breaking-change-prone library syntax before writing code.
- Commit atomically via `/git-commit [patch|minor|major]`.
- Persist memory via `save progress`.
