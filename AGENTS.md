# DevKernel — Global Workspace Routing Table (ICM)

You are operating inside `<ZENTORA_ROOT>` (the folder that contains this file; it can live on any drive or path -- resolve it at runtime or via the `ZENTORA_ROOT` env var, never hardcode a drive letter). Follow the "One Home Per Fact" principle:
- **Live Status & Next Steps** live ONLY in `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md`.
- **Full History & Session Notes** live ONLY in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/`.
- **Connections & Communities** live ONLY in `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json` and child repo `<Repo>/graphify-out/graph.json`.

## Where Everything Lives
| Area | Path | Purpose |
| :--- | :--- | :--- |
| Project Cards | `<ZENTORA_ROOT>/MyOS/projects/` | One short card per project (status, next step, links) |
| Long-term Memory | `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/` | Project Hub notes and dated session logs |
| Atomic Knowledge | `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/` | Reusable gotchas, decisions, and architecture facts |
| PARA Structure | `<ZENTORA_ROOT>/MyOS/ObsidianVault/` | `00 - Inbox`, `10 - Projects`, `20 - Areas`, `30 - Resources`, `40 - Archive` |
| Templates | `<ZENTORA_ROOT>/MyOS/ObsidianVault/Templates/` | Standard templates for Cards, Hubs, Sessions, Zettelkasten, Archify, and `repo-agents-starter/` |
| Global Graph | `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json` | Graphify knowledge graph & `GRAPH_REPORT.md` |
| Graph Env File | `<ZENTORA_ROOT>/MyOS/.env.graphify` | Local environment file for `DEEPSEEK_API_KEY` |
| Recall Script | `<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py` | Dynamic 1-to-2 hop score-dropoff & confidence-weighted recall (2-8 files) |
| Lifecycle Hook | `<ZENTORA_ROOT>/MyOS/_meta/agy_memory_hook.py` | Antigravity `SessionStart` & `PreInvocation` auto-memory/graph injector (`.agents/hooks.json`) |
| Repo Bootstrapper | `<ZENTORA_ROOT>/MyOS/_meta/bootstrap_repo.ps1` | Automated setup & skill deduplicator for any new or existing repo |
| Dev Tools Installer | `<ZENTORA_ROOT>/MyOS/_meta/install_devtools.ps1` | Installs Ponytail (pinned skill, merged into `surgical-coding`) and OmniRoute (`-Only ponytail|omniroute|all`, `-DryRun`) |
| Multi-Agent Setup | `<ZENTORA_ROOT>/MyOS/_meta/setup_agent.ps1` | Automated adapter & environment provisioner for Claude, Cursor, Antigravity, Copilot, ChatGPT |
| Global Skills | `~/.agents/skills/` | AI Hero (`aihero.dev`), `surgical-coding`, `archify`, `git-commit`, `verification-before-completion`, `design-taste-frontend`, `monorepo-architect`, `selfhost-devops`, `setup-agent`, `devkernel-manager` |
| Codebases | `<ZENTORA_ROOT>/Repos/` | Project source code repositories |

## Universal Engineering & Terminal Guardrails
1. **Windows PowerShell 5.1 Terminal Execution:**
   - Never use bash-style `&&`, `||`, or `cd "path" && command`.
   - Always pass the target directory via `Cwd` / `working_directory`, or use `command1; if ($?) { command2 }`.
2. **ASCII-Safe Punctuation & UTF-8 Without BOM:**
   - Save all project code, markdown, and config files as **UTF-8 without BOM**.
   - Prefer ASCII punctuation (`-`, `--`, `->`, `...`, `Section N`) over Unicode dashes/arrows to prevent PowerShell encoding corruption.
3. **Mandatory Verification Gate (`verification-before-completion`):**
   - Never claim a task is complete or commit code without fresh verification evidence (`npm run lint:fix` / `lint` and `npm run build` + affected tests exiting with code `0`).
4. **Universal Behavioral Guardrails (`surgical-coding` / Karpathy Guidelines):**
   - **Think Before Coding:** Never assume silently. If uncertain or facing ambiguity, stop immediately and ask. Surface tradeoffs explicitly rather than choosing unilaterally.
   - **Simplicity First:** Write the absolute minimum code that solves the requested problem. Zero speculative abstractions, zero unrequested configurability, and zero premature generalizations. If 50 lines suffice, never write 200. Follow the Two-Tier Simplicity Gate.
   - **Surgical Changes:** Touch only what you must. Zero collateral damage to adjacent code, comments, or formatting. Clean up only your own orphans. Every changed line in your diff must trace directly to the user's request.
   - **Goal-Driven Execution:** Establish verifiable success criteria upfront. State brief multi-step plans with verification checkpoints. Loop and test until verified before claiming completion (enforcing Gate 3: `verification-before-completion`).
5. **Strict Pre-Coding Modernity Gate (Context7 & Dependency Verification - ZEP-03):**
   - **Mandatory Library Inspection:** Always inspect `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt` to confirm the exact installed version before generating code for modern libraries.
   - **Context7 Live Documentation:** Always invoke the `context7` MCP tool to retrieve official, version-specific API signatures and syntax snippets for libraries prone to major version breaking changes (e.g. Next.js App Router, Tailwind v4, Pydantic v2, Prisma v5+, Supabase v2, FastAPI).
   - **Zero Deprecated Syntax Invariant:** Strictly forbid obsolete syntax patterns (no `pages/` routing in App Router, no Pydantic v1 `.dict()`, no unvetted CJS `require()`).
   - **Issue Diagnostics Gate (Fetch Protocol):** When encountering build errors or dependency bugs, inspect official GitHub issues/changelogs via `fetch` MCP instead of speculating.

## Exact Graphify CLI Syntax (Zero-Token-Waste Rule)
> **CRITICAL — NEVER run `graphify --update`!** `update` and `extract` are subcommands, NOT `--flags`. Do not run `graphify --help` to guess syntax:
- **1. Fast Code AST Re-Index (No LLM / No API Key):**
  - If repo has `scripts/graphify.ps1`: `.\scripts\graphify.ps1 update`
  - Otherwise: `graphify update "<ZENTORA_ROOT>/MyOS"` (accepts ONLY `[--force]` and `[--no-cluster]`, NEVER `--backend` or `--output`).
- **2. Full Semantic + AST Extraction with DeepSeek (Updates `<ZENTORA_ROOT>/MyOS/graphify-out/graph.json`):**
  ```powershell
  graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"
  ```

## The 4-Step Surgical Lookup (BrewedOps 3-Layer Architecture)
Instead of dumping full repositories or notes into chat, execute this deterministic 4-step surgical lookup on every task to read only ~4 to 5 highly relevant files:
1. **Master Routing Table (`AGENTS.md`):** Orient repository scope, skills, and directory layout.
2. **ICM Project Card (`MyOS/projects/<slug>.md`):** Read live `status:`, immediate `next:`, and exact paths.
3. **Obsidian Hub & Session (`MyOS/ObsidianVault/10 - Projects/<Name>/`):** Read the Project Hub note and latest dated session note for recent decisions, features built, and mistakes.
4. **Dynamic Context Recall (2–8 files):** Read the `## Dynamic Files to Read` manifest auto-injected by `.agents/hooks.json` in `[ZENTORA CONTEXT CAPSULE]` (or via `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<prompt keywords>" --repo "<RepoPath>" --hops 2`). Read **only those ~4 to 5 highly relevant files** per prompt.

## Workflow Rules
0. **Strict Obsidian Project Folder Resolution (NEVER write to Vault Root):**
   - Dynamically detect `<Project Name>` from the repository's root folder name (`Split-Path -Leaf (git rev-parse --show-toplevel)`).
   - **Strict Vault Root Invariant:** <ZENTORA_ROOT>/ObsidianVault must NEVER exist on disk. All Obsidian Vault notes live exclusively in <ZENTORA_ROOT>/MyOS/ObsidianVault/. If an agent or rule references or creates an ObsidianVault folder directly under <ZENTORA_ROOT>, halt immediately and redirect to <ZENTORA_ROOT>/MyOS/ObsidianVault/.
   - **NEVER create any Markdown file directly in `<ZENTORA_ROOT>/MyOS/ObsidianVault/` (the vault root).**
   - All project Hub notes, Session notes (`<Project Name> Session YYYY-MM-DD.md`), and Changelog archives MUST be created inside `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/`.
   - Atomic insights and reusable gotchas live exclusively in <ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/.
1. **Pre-Flight & Mandatory Graph-First Search Rule (Before ANY code search, bug fix, feature work, or status/architecture query):**
   - **Never start with blind `grep` or directory scans.** Always consult the Graphify Knowledge Graph and Project Memory first:
   - **Automatic Hook Capsule:** Read the `[ZENTORA CONTEXT CAPSULE]` and `[ZENTORA MEMORY & GRAPHIFY ACTIVE]` steps auto-injected by `.agents/hooks.json` (`agy_memory_hook.py`) at the start of every turn.
   - **Native `graphify` MCP Server:** Use `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, or `god_nodes` (passing `project_path: "<ZENTORA_ROOT>/Repos/<RepoName>"` when querying a child repository).
   - **Federated CLI Recall (Vault + Child Repo AST):** Run `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<english keywords>" --repo "<RepoPath>" --hops 2` (or repo-local `.\scripts\graphify.ps1 query "<question>"`).
   - **Project Status & Memory:** Read `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md` and latest session notes in `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/`. Run `python "<ZENTORA_ROOT>/MyOS/_meta/zentora_sync.py" --once` when reconciling workspace state.
2. **AI Hero (`aihero.dev`) + DevKernel Development Lifecycle:**
   - Do NOT duplicate global skills (`~/.agents/skills/`) inside individual repository `.agents/skills/` folders; keep only project-specific domain skills locally.
   - **Clarify & Specify:** `/grill-me` (or `grill-with-docs`) -> `to-spec` -> `to-tickets`
   - **Design & Model:** `domain-modeling` / `codebase-design` / `archify`
   - **Build & Verify:** `tdd` -> `implement` -> `verification-before-completion` (`lint:fix` + `build` exit `0`) -> `code-review`
   - **Commit & Release (`/git-commit [patch|minor|major]`):**
     - **Without `patch|minor|major`:** Creates/updates `## [Unreleased]` in `CHANGELOG.md` (matching the repo's existing format) and commits atomically.
     - **With `patch|minor|major`:** Updates `## [Unreleased]`, promotes it to `## [X.Y.Z] - YYYY-MM-DD`, ensures/updates the `production` branch from `main`, creates an annotated git tag `vX.Y.Z` with the latest `CHANGELOG.md` notes, and triggers a **GitHub Release (`gh release create`) ONLY on `major` updates**.
3. **When told `save progress`:**
   - Detect `<Project Name>` and `<CODE>` from the git repository root (`Split-Path -Leaf (git rev-parse --show-toplevel)`), active editor file, or CLI parameter `-Project <CODE>`.
   - Locate or update today's single consolidated session note: `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/[<CODE>] YYYY-MM-DD - <Focus Title>.md`. If called multiple times in one day, append new work under `## What was built` and update the `# H1` and YAML `summary:` rather than creating multiple session notes.
   - Extract reusable architectural decisions or bugs ("gotchas") into `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Update `status`, `next`, and `updated` in `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md`.
   - Run fast AST update by default: `graphify update "<ZENTORA_ROOT>/MyOS"` (zero DeepSeek tokens). Run DeepSeek extraction `graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"` ONLY on major milestone releases or when told `save progress --deep`.
4. **When told `archify <Project Name>`:**
   - Output `.docs/architecture/system-architecture.html` and `.docs/architecture/system-architecture.mmd` inside the repository and link in `<Project Name> Hub.md` and `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md`.
5. **When told `bootstrap <RepoName>`:**
   - Run `powershell -ExecutionPolicy Bypass -File "<ZENTORA_ROOT>/MyOS/_meta/bootstrap_repo.ps1" -RepoPath "<RepoName-or-Path>"`.
6. **Backend Engineering Protocols (ZEP) & Two-Tier Simplicity Gate:**
   - Inspect backend code against the 10 Backend Design Patterns (`Repository`, `Factory`, `Singleton`, `Strategy`, `Observer`, `Builder`, `Adapter`, `Decorator`, `CQRS`, `Circuit Breaker`).
   - Enforce controller insulation: handlers never run raw SQL or direct third-party fetch calls.
   - Enforce Two-Tier Simplicity Gate: Tier 1 CRUD (Repo + Service; reject CQRS/Event Bus/Builders); Tier 2 (Strategy for >3 branches, Adapter for schemas, Observer for side effects, Breaker for external APIs).
   - Polyglot enforcement: TypeScript (interface/Prisma/Zod) vs Python (typing.Protocol/Pydantic v2/SQLAlchemy).
7. **Strict Pre-Coding Modernity & Anti-Hallucination Gate (ZEP-03):**
   - **Mandatory Library Verification Before Generation:**
     - Before writing code for any modern external library or framework feature prone to major version breaking changes (e.g., Next.js App Router, Tailwind v4, Pydantic v2, Prisma v5+, Supabase v2, LangChain, FastAPI):
     - The agent **MUST** inspect the target repo's `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt` to confirm the exact installed version.
     - The agent **MUST** invoke the `context7` MCP tool to retrieve live, official documentation and working syntax snippets before generating code.
   - **Zero Deprecated Syntax Invariant:**
     - Strictly forbid deprecated patterns (e.g., Next.js `pages/` routing in App Router repos, Pydantic v1 `.dict()` on Pydantic v2 codebases, or unvetted CommonJS `require()` in modern TypeScript/ESM projects).
   - **Issue Diagnostics Gate (Fetch Protocol):**
     - When encountering a package compiler bug or third-party dependency error, the agent must use the `fetch` MCP tool to inspect the official GitHub issue, changelog, or release notes instead of inventing hypothetical flags or configs.
8. **When told `/setup <agent>` or `setup <agent>`:**
   - Run `powershell -ExecutionPolicy Bypass -File "<ZENTORA_ROOT>/MyOS/_meta/setup_agent.ps1" -Agent <agent>` (supports `all`, `claude`, `cursor`, `antigravity`, `copilot`, `chatgpt`).

## Active Projects Registry

| Project | Type | Repo Path | Vault Folder | Status |
| :--- | :--- | :--- | :--- | :--- |
| `Starter-Project` | Repo | `<ZENTORA_ROOT>/Repos/Starter-Project` | `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/Starter-Project` | Active |

## Agent skills

### Issue tracker

Local markdown files under `.scratch/<feature-slug>/`. See `.docs/agents/issue-tracker.md`.

### Triage labels

Default five canonical triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `.docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`GLOSSARY.md` at repo root and ADRs in `.docs/decisions/`). See `.docs/agents/domain.md`.

<!-- devkernel-documentation-onboarding -->
## Root and child repository documentation and security

Manual bootstrap and automatic sync scaffold six canonical `.docs` planning files. Follow the shared workflow in `MyOS/ObsidianVault/Templates/repo-agents-starter/.docs/agents/documentation-onboarding.md`: inspect repo evidence, draft, interview the developer, and consolidate only after review. Preserve Archify artifacts in place and link them from `.docs/ARCHITECTURE.md`. Keep status, history, ADRs, and tickets in their canonical homes.

For work on DevKernel itself, start at [the root documentation index](.docs/README.md) and follow [root documentation onboarding](.docs/agents/documentation-onboarding.md). The six root `.docs` files describe this workspace; the starter templates remain the source for child-repo scaffolding.

Before planned feature work, resolve relevant documentation gaps. Diagnosis, urgent fixes, and documentation work may proceed with gaps recorded. Use the global `security-audit` skill on demand (`security audit this codebase`); bootstrap never runs audits or copies this skill into child repositories.
