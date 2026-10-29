# Claude Code Guidelines — Zentora Dev (MyOS)

You are operating inside Zentora Dev or a Zentora-managed client repository. All interactions must strictly follow the routing and architectural rules established in `AGENTS.md`.

## Master Routing & Invariants
- **Primary Routing Table:** Read `AGENTS.md` before taking architectural actions or answering system status questions.
- **One Home Per Fact:**
  - Live Status & Immediate Next Steps live **ONLY** in `MyOS/projects/<project-slug>.md`.
  - Full History & Session Notes live **ONLY** in `MyOS/ObsidianVault/10 - Projects/<Project Name>/`. Notes must NEVER live at the vault root.
  - Reusable Gotchas & Decisions live **ONLY** in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
  - Code & Concept Graph lives **ONLY** in `MyOS/graphify-out/graph.json`.

## Windows PowerShell 5.1 Terminal Execution
- Never use bash chaining (`&&`, `||`, or `cd "path" && command`).
- Use PowerShell sequencing: `command1; if ($?) { command2 }` or set the target directory directly.
- All files must be saved as **UTF-8 without BOM** using ASCII-safe punctuation.

## Zero-Token Context Recall
Before reading full directory structures or unindexed notes:
```powershell
python MyOS/_meta/graph_recall.py "<query>" --hops 2
```
This extracts a targeted, <350 token Context Capsule containing project status, AST symbols, recent session decisions, and atomic gotchas.

## Core Workflows
1. **Save Progress (`save progress`):**
   - Update today's single consolidated session note: `MyOS/ObsidianVault/10 - Projects/<Project>/[<CODE>] YYYY-MM-DD - <Focus Title>.md`.
   - Extract atomic reusable insights to `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Update `status`, `next`, and `updated` in `MyOS/projects/<project-slug>.md`.
   - Run fast AST update: `graphify update "MyOS"`.
2. **Git Commit & Versioning (`/git-commit [patch|minor|major]`):**
   - Updates `## [Unreleased]` in `CHANGELOG.md` and creates an atomic conventional commit.
   - For `patch|minor|major`: promotes unreleased notes, updates `production` branch, creates annotated tag `vX.Y.Z`, and creates GitHub Release ONLY on `major`.
3. **Backend Engineering Protocols (ZEP):**
   - Enforce controller insulation (no raw queries/fetch in handlers).
   - Enforce Two-Tier Simplicity Gate: Tier 1 (Direct Repo + Service; strictly reject CQRS/Event Bus); Tier 2 (Strategy for >3 calculation branches, Adapter for dirty external schemas, Observer for async side effects, Circuit Breaker for external APIs).
4. **Strict Pre-Coding Modernity & Anti-Hallucination Gate (ZEP-03):**
   - **Inspect Version First:** Check `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt` before generating code for modern libraries (Next.js, Tailwind, Pydantic, Prisma, Supabase, FastAPI).
   - **Context7 Live Snippets:** Invoke `context7` MCP tool to pull current official API signatures and live documentation before writing code.
   - **Zero Deprecated Syntax:** Never use obsolete patterns (e.g., Next.js `pages/` in App Router, Pydantic v1 `.dict()`, unvetted CJS `require()`).
   - **Issue Diagnostics (Fetch Protocol):** When hitting package build or dependency errors, invoke `fetch` MCP tool to consult official GitHub issues/releases rather than inventing speculative flags.
