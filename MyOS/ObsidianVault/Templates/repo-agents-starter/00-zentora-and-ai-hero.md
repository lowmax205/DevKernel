---
description: Zentora Dev Global Architecture (ICM, Obsidian, Graphify), Engineering Guardrails & AI Hero Workflow
alwaysApply: true
---

# Zentora Dev & AI Hero Workflow Invariants ({{Project Name}})

## 1. 4-Step Surgical Lookup (BrewedOps 3-Layer Architecture)
Before scanning directories or modifying files, follow the 4-step surgical lookup to eliminate prompt bloat:
1. **Master Routing Table:** Read `AGENTS.md` (and `CLAUDE.md` / `.cursorrules` where applicable).
2. **ICM Project Card:** Read `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md` for live `status:` and immediate `next:`.
3. **Obsidian Hub & Session:** Read `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/{{Project Name}} Hub.md` and today's/latest session note for recent decisions, wins, and bug post-mortems.
4. **Dynamic Context Recall (2–8 files):** Ingest the `## Dynamic Files to Read` manifest auto-injected by `.agents/hooks.json` in `[ZENTORA CONTEXT CAPSULE]` (or run `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<prompt keywords>" --repo . --hops 2`). Read **only those ~4 to 5 highly relevant files**.

## 2. One Home Per Fact (Routing Integrity)
- **Live Status & Next Steps:** Lives ONLY in `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`.
- **Obsidian Project Folder (NEVER write to Vault Root):** All notes for {{Project Name}} live strictly in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`.
- **Reusable Gotchas & Architecture Rules:** Lives ONLY in `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
- **Dependencies & Relationships:** Lives in `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json` and local `graphify-out/graph.json`.
- **Architecture Diagrams:** Stored strictly in `.docs/architecture/system-architecture.html` and `.docs/architecture/system-architecture.mmd`.

## 3. Engineering Guardrails & Terminal Execution
- **Windows PowerShell 5.1:** Never use bash chaining (`&&` or `||`). Save all files as **UTF-8 without BOM** with ASCII-safe punctuation.
- **Mandatory Verification Gate (`verification-before-completion`):** Dynamically adapt to native toolchain (`npm`, `pnpm`, `python`) and verify lint, build, and affected test commands exit with code `0` before claiming completion or committing.
- **On-Demand Engineering Protocols (ZEP & Modernity Gate):**
  - **Backend Standards & Simplicity Gate:** Consult [`.docs/RULES.md`](.docs/RULES.md) or Atomic Insights for Tier 1 CRUD (Repo + Service) vs Tier 2 (Strategy, Adapter, Observer, Breaker). Controllers never execute raw queries or direct HTTP fetch.
  - **Modernity & Context7 Gate:** Inspect package manifests before code generation; use `context7` MCP for version-specific signatures; use `fetch` MCP for issue diagnosis.
- **AI Hero Lifecycle:** `/grill-me` -> `to-spec` -> `to-tickets` -> `tdd` -> `implement` -> `verification-before-completion` -> `/git-commit [patch|minor|major]`.
- **Save Progress (`save progress`):** Update today's single consolidated session note in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/[<CODE>] YYYY-MM-DD - <Focus Title>.md`, extract reusable gotchas to `Atomic Insights/`, update `MyOS/projects/{{project-slug}}.md`, and run fast AST update `.\scripts\graphify.ps1 update` (zero LLM tokens).
