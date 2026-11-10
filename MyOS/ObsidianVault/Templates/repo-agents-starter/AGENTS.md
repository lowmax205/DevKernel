# {{Project Name}} — Agent Entry

**Master Routing Table:** Read before taking architectural actions or answering system status questions. Follow the **4-Step Surgical Lookup** and **One Home Per Fact** to eliminate prompt bloat and token waste.

## 1. 4-Step Surgical Lookup (BrewedOps 3-Layer Architecture)
Instead of scanning the whole repo or unindexed notes, execute this deterministic 4-step surgical lookup on every task:
1. **Master Routing:** Read this file (`AGENTS.md`) to orient repository scope, skills, and rules.
2. **ICM Project Card:** Read [`<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`](file:///<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md) for live `status:`, immediate `next:`, and exact paths.
3. **Obsidian Hub & Latest Session:** Read [`<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`](file:///<ZENTORA_ROOT>/MyOS/ObsidianVault/10%20-%20Projects/{{Project%20Name}}/) (`{{Project Name}} Hub.md` and latest dated session note) for recent decisions, what was built, and mistakes.
4. **Dynamic Context Recall (2–8 files):** Ingest the `## Dynamic Files to Read` manifest auto-injected by `.agents/hooks.json` in `[ZENTORA CONTEXT CAPSULE]` (or run `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<prompt keywords>" --repo . --hops 2`). Read **only those ~4 to 5 highly relevant files** per prompt.

## 2. One Home Per Fact (Canonical Boundaries)
- **Live Status & Next Steps:** Lives ONLY in [`<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md`](file:///<ZENTORA_ROOT>/MyOS/projects/{{project-slug}}.md).
- **Long-Term Memory & Session Logs (NEVER write to Vault Root):** Lives ONLY in [`<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`](file:///<ZENTORA_ROOT>/MyOS/ObsidianVault/10%20-%20Projects/{{Project%20Name}}/).
- **Reusable Gotchas & Architecture Rules:** Lives ONLY in [`<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`](file:///<ZENTORA_ROOT>/MyOS/ObsidianVault/30%20-%20Resources/Atomic%20Insights/).
- **Code & Concept Dependencies:** Lives in [`<ZENTORA_ROOT>/MyOS/graphify-out/graph.json`](file:///<ZENTORA_ROOT>/MyOS/graphify-out/graph.json) and repo-local `graphify-out/graph.json`.
- **System Architecture Diagram:** Stored in `.docs/architecture/system-architecture.html` and `.docs/architecture/system-architecture.mmd`.

## 3. Core Operating Invariants & On-Demand Docs
- **Windows PowerShell 5.1 & Encoding:** Never use bash `&&` or `||`. Save all files as **UTF-8 without BOM** using ASCII-safe punctuation.
- **Mandatory Verification Gate (`verification-before-completion`):** Run fresh native verification (`npm run lint:fix` / `lint` and `npm run build` + tests exiting with code `0`) before claiming completion or committing.
- **On-Demand Engineering Protocols (ZEP & Modernity Gate):**
  - **Backend Standards & Simplicity Gate:** Consult [`.docs/RULES.md`](.docs/RULES.md) or Atomic Insights before writing services (Tier 1 CRUD: Repository + Service; Tier 2: Strategy, Adapter, Observer, Circuit Breaker). Controllers never execute raw queries or direct HTTP fetch.
  - **Modernity & Context7 Gate:** Inspect `package.json` / `pyproject.toml` first; use `context7` MCP for live API signatures on breaking-change-prone libraries; use `fetch` MCP for issue diagnosis.
- **AI Hero Lifecycle:** `/grill-me` -> `to-spec` -> `to-tickets` -> `tdd` -> `implement` -> `verification-before-completion` -> `/git-commit [patch|minor|major]`.
- **Save Progress (`save progress`):** Consolidate today's session note in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`, extract reusable gotchas to `Atomic Insights/`, update `MyOS/projects/{{project-slug}}.md`, and run fast AST update `.\scripts\graphify.ps1 update` (zero LLM tokens).

## Agent skills

### Issue tracker
Local markdown files under `.scratch/{{feature-slug}}/`. See `.docs/agents/issue-tracker.md`.

### Triage labels
Default five canonical triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `.docs/agents/triage-labels.md`.

### Domain docs
Single-context layout (`GLOSSARY.md` at repo root and ADRs in `.docs/decisions/`). See `.docs/agents/domain.md`.

<!-- devkernel-documentation-onboarding -->
## Project documentation onboarding
Before planned feature work, follow [.docs/agents/documentation-onboarding.md](.docs/agents/documentation-onboarding.md).
Inspect existing project evidence, draft the six canonical .docs files, and interview the developer.
Resolve gaps relevant to the feature; diagnosis, urgent fixes, and documentation work may proceed with gaps recorded.
Security audits are on demand: use the global `security-audit` skill (`security audit this codebase`).
