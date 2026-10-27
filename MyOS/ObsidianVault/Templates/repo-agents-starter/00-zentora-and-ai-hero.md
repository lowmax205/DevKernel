---
description: Zentora Dev Global Architecture (ICM, Obsidian, Graphify), Engineering Guardrails & AI Hero Workflow
alwaysApply: true
---

# Zentora Dev & AI Hero Workflow Invariants ({{Project Name}})

## 1. One Home Per Fact (Zentora Dev Routing)
- **Live Status & Next Steps:** Read/update `<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md` before starting work and when saving progress.
- **Obsidian Project Folder (NEVER write to Vault Root):**
  - All `{{Project Name}}` notes live strictly in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects\{{Project Name}}\`.
  - Hub Note: `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects\{{Project Name}}\{{Project Name}} Hub.md`
  - Session Notes: `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects\{{Project Name}}\{{Project Name}} Session YYYY-MM-DD.md`
  - Changelog Archive: `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects\{{Project Name}}\{{Project Name}} Changelog Archive.md`
  - Atomic Gotchas/Decisions: `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`
- **System Architecture Diagrams:** Stored strictly in `.docs/architecture/system-architecture.html` and `.docs/architecture/system-architecture.mmd` (never `docs/`).

## 2. Universal Terminal, Encoding & Verification Guardrails
- **Windows PowerShell 5.1 Execution:** Never use bash `&&`, `||`, or `cd "path" && command`. Set `Cwd` / `working_directory` directly, or use `cmd1; if ($?) { cmd2 }`.
- **ASCII-Safe Punctuation & UTF-8 Without BOM:** Save all project files as UTF-8 without BOM. Prefer ASCII `-`, `--`, `->`, `...`, `Section N` to prevent PowerShell encoding corruption.
- **Mandatory Verification Gate (`verification-before-completion`):** After code changes and before claiming completion or committing, dynamically adapt to the repo's native toolchain (`npm`, `pnpm`, `python`, etc.) and confirm lint, build, and affected test commands exit with code `0`.

## 3. Graphify Knowledge Graph & Zero-Token-Waste CLI
- **Consult Graph Before Raw Grep/Read:**
  - Global 2-hop recall (no LLM): `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "{{english keywords}}" --hops 2`
  - Scoped subgraph CLI: if `scripts/graphify.ps1` exists, use `.\scripts\graphify.ps1 query|path|explain "{{arg}}"`; otherwise use `graphify query|path|explain "{{arg}}"`.
- **Exact CLI Syntax (CRITICAL -- NEVER run `graphify --update` or `--help`):**
  - **Fast AST-only code update (no LLM):** `.\scripts\graphify.ps1 update` (if present) or `graphify update "<ZENTORA_ROOT>/MyOS"`.
  - **Full AST + DeepSeek Semantic Extraction:** `graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"`.

## 4. AI Hero (`aihero.dev`) + Zentora Dev Development Lifecycle
Use globally installed skills (`~/.agents/skills/`) rather than duplicating generic skills into `.agents/skills/`:
1. **Clarify & Specify:** `/grill-me` (or `grill-with-docs`) -> `to-spec` -> `to-tickets` (tracked in `.scratch/<feature-slug>/` and committed to Git).
2. **Design & Model:** `domain-modeling` / `codebase-design` / `archify` (`archify {{Project Name}}` creates interactive `.docs/architecture/system-architecture.html`).
3. **Build & Verify:** `tdd` -> `implement` -> `verification-before-completion` (native lint + build exit `0`) -> `code-review`.
4. **Commit & Release (`/git-commit [patch|minor|major]`):**
   - **No version keyword:** Appends technical bullets under `## [Unreleased]` in `CHANGELOG.md` (matching existing format) and commits atomically.
   - **With `patch`, `minor`, or `major`:** Updates `## [Unreleased]`, promotes it to `## [X.Y.Z] - YYYY-MM-DD`, ensures/updates `production` branch from `main` (or tags directly on `main` for single-branch repos), creates an annotated git tag `vX.Y.Z`, and triggers a **GitHub Release (`gh release create`) ONLY on `major` updates**.
5. **Persist Memory (`save progress`):**
   - Update today's session note in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/[{{project-code}}] YYYY-MM-DD - <Focus Title>.md` (synthesizing Decisions, Mistakes, and Wins).
   - Extract strictly reusable, cross-project gotchas and patterns to `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Update `MyOS/projects/{{project-slug}}.md` `next:` task.
   - Run fast `graphify update "<ZENTORA_ROOT>/MyOS"` (or `graphify extract --backend deepseek` on explicit `save progress --deep` / major releases).

## 5. Backend Engineering Protocols (ZEP) & Two-Tier Simplicity Gate
When developing backend services, route handlers, or persistence layers:
- **Two-Tier Simplicity Gate:**
  - **Tier 1 (Simple CRUD):** Enforce direct Repository + Service. Strictly **reject** CQRS, Event Buses, and custom Builders for straightforward entities. Output: `[SIMPLICITY_GATE] Preserving Tier 1 simplicity: Direct Repository + Service model used.`
  - **Tier 2 (High-Scale / Multi-Algorithm / Integrations):** Mandate Strategy for variant business logic (>3 branches), Adapter for third-party schemas, Observer for multi-step side effects, and Circuit Breaker for external network APIs.
- **Polyglot Adherence:**
  - TypeScript: Interface contracts, Prisma/Drizzle repositories, Zod validation.
  - Python: `typing.Protocol` / ABCs, Pydantic v2 schemas, SQLAlchemy session repositories.
- **Controller Boundary:** Never run direct database queries or raw HTTP fetch in route handlers or controllers.
