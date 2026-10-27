# {{Project Name}} — Agent Entry

**Source of truth:** [`.agents/rules/`](.agents/rules/), [`package.json`](package.json), domain skills in [`.agents/skills/`](.agents/skills/), and global AI Hero / Zentora Dev skills in `~/.agents/skills/`.

## 1. Zentora Dev Delegation (One Home Per Fact)
Connected to the global **Zentora Dev** architecture ([`<ZENTORA_ROOT>/AGENTS.md`](file:///<ZENTORA_ROOT>/AGENTS.md)):
- **Live Status & Next Steps:** [`<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`](file:///<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md)
- **Long-Term Memory & Session Logs (NEVER write to Vault Root):** [`<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects\{{Project Name}}\`](file:///<ZENTORA_ROOT>/MyOS/ObsidianVault/10%20-%20Projects/{{Project%20Name}}/) (`{{Project Name}} Hub.md`, `{{Project Name}} Session YYYY-MM-DD.md`, `{{Project Name}} Changelog Archive.md`)
- **System Architecture Diagram:** [`.docs/architecture/system-architecture.html`](.docs/architecture/system-architecture.html) and [`.docs/architecture/system-architecture.mmd`](.docs/architecture/system-architecture.mmd)
- **Knowledge Graph & Recall:**
  - Fast 2-hop recall (no LLM): `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "{{english keywords}}" --hops 2`
  - Fast AST update (no LLM, no `--backend`/`--output`): `graphify update .` or `graphify update "<ZENTORA_ROOT>"`
  - Full DeepSeek extraction: `graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"` (NEVER use `graphify --update`)

## 2. AI Hero + Zentora Dev Development Workflow
1. **Clarify & Specify:** `/grill-me` (or `grill-with-docs`) -> `to-spec` -> `to-tickets`
2. **Design & Model:** `domain-modeling` / `codebase-design` / `archify`
3. **Build & Verify:** `tdd` -> `implement` -> `code-review`
4. **Commit & Version (`/git-commit`):** Atomic scoped commits that always update `## [Unreleased]` in `CHANGELOG.md`. Append or follow up with `major`, `minor`, or `patch` to promote `## [Unreleased]` and bump the project version.
5. **Persist Memory (`save progress`):** Record session note in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`, extract reusable gotchas to `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`, update `MyOS/projects/{{project-slug}}.md`, and run `graphify`.

## 3. Backend Engineering Protocols (ZEP) & Two-Tier Simplicity Gate
- **Boundary Insulation:** API route handlers and controllers must interact via injected services/repositories; direct database queries or raw external HTTP fetch calls in handlers are strictly forbidden.
- **Two-Tier Simplicity Gate:**
  - **Tier 1 (CRUD):** Enforce direct Repository + Service. Reject CQRS, Event Buses, and custom Builders for simple entities (`[SIMPLICITY_GATE] Preserving Tier 1 simplicity: Direct Repository + Service model used.`).
  - **Tier 2 (High-Scale / External / Multi-Algorithm):** Strategy (>3 algorithm branches), Adapter (external/legacy payloads), Observer (asynchronous side effects), Circuit Breaker (external network dependencies).
- **Polyglot Stack:**
  - TypeScript: Interface abstractions, Prisma/Drizzle ORM, Zod/Builders.
  - Python: `typing.Protocol` / ABCs, Pydantic v2 schemas, SQLAlchemy session repositories.

## Agent skills

### Issue tracker

Local markdown files under `.scratch/{{feature-slug}}/`. See `.docs/agents/issue-tracker.md`.

### Triage labels

Default five canonical triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `.docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`GLOSSARY.md` at repo root and ADRs in `.docs/decisions/`). See `.docs/agents/domain.md`.
