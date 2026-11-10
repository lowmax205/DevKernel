# Claude Code Guidelines — {{Project Name}}

You are operating inside {{Project Name}}, a repository managed under the Zentora Dev Meta-Developer Operating System.

## 1. 4-Step Surgical Lookup (BrewedOps 3-Layer Architecture)
Execute this deterministic 4-step surgical lookup to avoid prompt amnesia and token waste:
1. **Master Routing Table:** Read `AGENTS.md` before taking architectural actions.
2. **ICM Project Card:** Read `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md` for live `status:` and immediate `next:`.
3. **Obsidian Hub & Session:** Read `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/{{Project Name}} Hub.md` and the latest session note for recent decisions, built features, and bug post-mortems.
4. **Dynamic Context Recall (2–8 files):** Run `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<prompt keywords>" --repo . --hops 2`. Read **only the ~4 to 5 highly relevant files** routed in the manifest.

## 2. One Home Per Fact (Canonical Boundaries)
- Live Status & Immediate Next Steps live **ONLY** in `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`.
- Chronological Session Notes & Decisions live **ONLY** in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`. Notes must NEVER live at the vault root.
- Reusable Gotchas & Decisions live **ONLY** in `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
- Code & Concept Graph lives in `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json` and local `graphify-out/graph.json`.

## 3. Terminal Guardrails & On-Demand Protocols
- Never use bash chaining (`&&` or `||`). Use PowerShell sequencing: `command1; if ($?) { command2 }`.
- Save all files as **UTF-8 without BOM** using ASCII-safe punctuation.
- Run fresh verification (`npm run lint:fix` / `lint` and `npm run build` exit `0`) before committing.
- Load backend protocols (`.docs/RULES.md` / ZEP) and modernity checks (`context7` MCP tool) on-demand when implementing services or breaking-change prone dependencies.
- Commit atomically via `/git-commit [patch|minor|major]`.
- Persist memory via `save progress`.
