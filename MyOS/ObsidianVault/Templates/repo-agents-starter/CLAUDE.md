# Claude Code Guidelines — {{Project Name}}

You are operating inside {{Project Name}}, a repository managed under the Zentora Dev Meta-Developer Operating System.

## Master Routing & Invariants
- **Primary Routing Table:** Always consult `AGENTS.md` before taking architectural actions or modifying project structures.
- **One Home Per Fact:**
  - Live Status & Immediate Next Steps live **ONLY** in `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`.
  - Chronological Session Notes & Decisions live **ONLY** in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`. Notes must NEVER live at the vault root.
  - Reusable Gotchas & Decisions live **ONLY** in `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
  - Code & Concept Graph lives **ONLY** in `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json`.

## Windows PowerShell 5.1 Terminal Execution
- Never use bash chaining (`&&`, `||`, or `cd "path" && command`).
- Use PowerShell sequencing: `command1; if ($?) { command2 }` or set the target directory directly.
- Save all files as **UTF-8 without BOM** using ASCII-safe punctuation.

## Fast Context Recall
```powershell
python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "{{english keywords}}" --hops 2
```

## Core Workflows
1. **Save Progress (`save progress`):**
   - Update today's single consolidated session note: `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/[<CODE>] YYYY-MM-DD - <Focus Title>.md`.
   - Extract atomic reusable insights to `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Update `status`, `next`, and `updated` in `MyOS/projects/{{project-slug}}.md`.
   - Run fast AST update: `graphify update "<ZENTORA_ROOT>/MyOS"`.
2. **Git Commit & Versioning (`/git-commit [patch|minor|major]`):**
   - Updates `## [Unreleased]` in `CHANGELOG.md` and commits atomically.
   - For `patch|minor|major`: promotes notes, updates `production`, creates annotated tag `vX.Y.Z`.
3. **Backend Engineering Protocols (ZEP):**
   - Enforce controller insulation (no raw SQL/fetch in route handlers).
   - Enforce Two-Tier Simplicity Gate (Tier 1 CRUD: Direct Repo + Service; Tier 2: Strategy, Adapter, Observer, Circuit Breaker).
