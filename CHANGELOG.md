# Changelog

All notable changes to the **DevKernel** workspace, ICM project cards, Obsidian Vault knowledge base, and Graphify knowledge graph are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Preserve-first six-file project documentation scaffolding through registration, with repo-grounded drafts, developer interviews, reviewed consolidation, and Archify references.
- Complete pinned Cloudflare security-audit bundle, MIT attribution, and provenance in clean exports; agent installation remains separate and audits stay on demand.
- Starter-specific root planning docs and integration checks for docs, dry runs, preservation, exports, and linked paths. Read-only reconciliation is unchanged.
- **BrewedOps 3-Layer Knowledge Architecture & 4-Step Surgical Lookup**:
  - Implemented the deterministic 4-step surgical lookup in `AGENTS.md`, `CLAUDE.md`, `00-zentora-and-ai-hero.md`, `copilot-instructions.md`, `cursor/devkernel.mdc`, `chatgpt/README.md`, `devkernel-manager` skill, and `.docs/ARCHITECTURE.md`.
  - Added full PARA structure to `MyOS/ObsidianVault/` (`00 - Inbox/`, `10 - Projects/`, `20 - Areas/`, `30 - Resources/`, `40 - Archive/` with `.gitkeep`).
  - Added Antigravity lifecycle memory hook (`MyOS/_meta/agy_memory_hook.py`) supporting `SessionStart` and `PreInvocation` automated context injection.
  - Upgraded `MyOS/_meta/graph_recall.py` to dynamic score-dropoff (>= 35% cutoff) and confidence weighting (`EXTRACTED` 1.0, `INFERRED` 0.75, `AMBIGUOUS` 0.4), outputting the `## Dynamic Files to Read (Surgical Context)` manifest (2 to 8 files dynamically routed).
  - Enriched `icm-project-card.md` template and all `MyOS/projects/*.md` cards with `Repo AST Graph` and `On-Demand Docs` rows.
  - Standardized `MyOS/_meta/zentora_sync.py` to source the canonical post-commit hook script from `MyOS/_meta/git-hooks/post-commit` (`[<CODE>] YYYY-MM-DD - <Focus Title>.md`).
  - Slimmed down `repo-agents-starter` templates (`AGENTS.md`, `CLAUDE.md`, `00-zentora-and-ai-hero.md`, `copilot-instructions.md`) and adapter configs to eliminate prompt bloat and load `.docs/RULES.md` / `context7` on demand.
  - Added `scaffold_project_docs.py`, `test_project_docs.py`, and `install_devtools.ps1`.
- **System Architecture Diagrams (Archify)**:
  - Finalized standalone interactive HTML architecture diagram `.docs/architecture/system-architecture.html` with signal-flow animation, dark/light theme switching, and component detail drawers (passed all 4 showcase quality gates with 0 line crossings).
  - Generated companion Mermaid diagram `.docs/architecture/system-architecture.mmd` modeling Meta-Control Plane, MyOS 3-Layer Knowledge Architecture, and Client Repositories.
  - Fully wired all 17 components with 0 orphaned nodes and 0 unresolved crossings.
- **Canonical Documentation Suite**:
  - Scaffolding canonical six-file `.docs` structure (`README.md`, `ARCHITECTURE.md`, `DESIGN.md`, `MEMORY.md`, `PRD.md`, `RULES.md`, `TASKS.md`, `agents/documentation-onboarding.md`).
- **Atomic Insights Codification**:
  - Codified `Vault Path Resolution Invariant.md` and `Documentation Onboarding Flow.md` under `30 - Resources/Atomic Insights/`.
- **Curated Global Skills**:
  - Added `surgical-coding`, `ponytail`, `dead-code-audit`, `security-audit`, and `ui-motion-performance` to `MyOS/_meta/global-skills/`.

### Changed
- Consolidated ignore patterns into `MyOS/.graphifyignore` and eliminated redundant root `.graphifyignore`.
- **Dedicated Global Companion Skills**: Mirrored 4 new curated workflow skills in `MyOS/_meta/global-skills/`:
  - `context7-docs`: Real-time version-specific library and API documentation retrieval via Context7 MCP.
  - `playwright-browser`: Snapshot-first browser automation, DOM exploration, and screenshot capture via Playwright MCP.
  - `database-toolbox`: Two-tier database operations enforcing read-only inspection by default and explicit confirmation for mutations.
  - `graphify`: Dedicated Zentora Graphify AST re-indexing, graph recall, and semantic extraction skill.
- **Child Repository Graphify Runner & Ignore**: Deployed `scripts/graphify.ps1` and `.graphifyignore` to `MyOS/ObsidianVault/Templates/repo-agents-starter/`, root workspace, and automated deployment via `MyOS/_meta/bootstrap_repo.ps1`.
- **Automated MCP Server Configuration**: Updated `MyOS/_meta/setup_agent.ps1` to automatically write and maintain `~/.gemini/config/mcp_config.json` with stdio configurations for Context7, Playwright, SQLite, PostgreSQL, and GCP Database Toolbox.
- **Context7 & Fetch MCP Tooling Integration**: Configured modular MCP server templates for `@upstash/context7-mcp` and `mcp-fetch-server` across Cursor (`MyOS/_meta/agent-adapters/cursor/mcp.json`) and Antigravity/Gemini adapters.
- **Strict Pre-Coding Modernity & Anti-Hallucination Gate (ZEP-03)**: Added mandatory pre-coding library version inspection, live documentation retrieval via Context7, and strict prohibition of deprecated patterns across `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, and `.cursor/rules/modern-stack-guard.mdc`.
- **Engineering Skill Enhancements**: Upgraded `implement` skill with Context7 pre-implementation modernity checks, `code-review` with ZEP-03 deprecated framework syntax detection, and `diagnosing-bugs` with Fetch protocol for remote issue lookup.
- **MCP Adapter Provisioner**: Updated `MyOS/_meta/setup_agent.ps1` to detect host `npx` availability and dynamically provision global and repo-level MCP definitions.
- **Clean Neutral Root Invariant Protection**: Added on-demand agent folders (`.cursor/`, `.agents/`, `.github/`, `CLAUDE.md`) to `.gitignore`.
- **Universal Multi-Agent Adapter Architecture**: Decoupled DevKernel from single-agent lock-in by establishing modular adapter profiles in `MyOS/_meta/agent-adapters/` for Claude Code CLI (`CLAUDE.md`), Cursor (`.cursor/rules/*.mdc`), Google Antigravity (`.agents/skills/`, `.agents/rules/`, junctions), GitHub Copilot CLI/VS Code (`.github/copilot-instructions.md`), and ChatGPT CLI / OpenAI Codex (`AGENTS.md`).
- **Automated Multi-Agent Setup Engine (`MyOS/_meta/setup_agent.ps1`)**: Created one-command environment provisioner supporting `-Agent [antigravity|cursor|claude|chatgpt|copilot|all]` with `-TargetRepo` scoping for root workspace or child repositories.
- **Global `setup-agent` & `devkernel-manager` Skills**: Added `setup-agent` and moved `devkernel-manager` to `MyOS/_meta/global-skills/` to provide conversational slash commands (`/setup all`, `/setup claude`, `/setup cursor`, `/setup antigravity`, `/setup copilot`) across all AI assistants.
- **Child Repository Multi-Agent Bootstrapper**: Updated `MyOS/_meta/bootstrap_repo.ps1` and `MyOS/ObsidianVault/Templates/repo-agents-starter` to automatically scaffold `CLAUDE.md`, `.github/copilot-instructions.md`, and `.cursor/rules/` for any new or existing child repository in `Repos/`.
- **Machine Onboarding Refactoring (`MyOS/_meta/bootstrap_machine.ps1`)**: Refactored workstation bootstrapper with an `-Agent` parameter (defaulting to `all`), delegating adapter deployment to `setup_agent.ps1`.
- **Master README.md Overhaul**: Rewrote Sections 3 through 6 to feature the Universal Multi-Agent Ecosystem, Mermaid adapter flowcharts, quickstart commands, and updated directory maps.

## [0.1.1] - 2026-11-01

### Added
- Source-pinned Windows starter architecture in interactive HTML, Mermaid, and reusable Archify JSON, with automated browser verification.
- Refreshed maintainer AST graph and verified starter registration, export, reset, and safety symbols without LLM extraction.
- Windows starter setup for Codex, Claude Code, Cursor, GitHub Copilot, and Antigravity, with interactive and noninteractive entry points.
- Explicit backup-before-reset for all supported repository agent instruction and local skill paths, with junction protection and recovery guidance.
- Allowlisted clean starter export containing only DevKernel-owned skills, reusable templates, and verification tools.
- Integration coverage for setup, reruns, internal and external repositories, reset backups, profile opt-in, and workspace isolation.

### Changed
- Preserve existing repository instructions by default and keep engineering policies opt-in.
- Support arbitrary workspace names and existing Git repositories inside or outside Repos.
- Replace implicit global skill mirroring, tool installation, hooks, and watchers with local registration and read-only reconciliation checks.
- Keep optional graph recall scoped to the selected workspace rather than falling back to a parent workspace.

## [0.1.0] - 2026-10-27

### Added
- **DevKernel Meta-Developer OS (MyOS)**: Standalone 3-layer knowledge and engineering operating system core enabling disciplined AI pair programming across multi-repository workspaces.
- **Detailed System Architecture Documentation (`.docs/architecture/`)**: Modular architectural specifications (`system-overview.md`, `knowledge-layers.md`, `backend-engineering-protocols.md`, and `agent-lifecycle.md`) along with a top-level `.docs/README.md` index.
- **10 Backend Engineering Protocols (ZEP) in Atomic Insights**: Codified 10 concept-first notes in `ObsidianVault/30 - Resources/Atomic Insights/` (`Repository Pattern`, `Factory Pattern`, `Singleton Pattern`, `Strategy Pattern`, `Observer Pattern`, `Builder Pattern`, `Adapter Pattern`, `Decorator Pattern`, `CQRS Pattern`, `Circuit Breaker Pattern`) with core problems solved, polyglot standards (TypeScript/Node & Python/FastAPI), anti-pattern warnings, and cross-project hub links.
- **Two-Tier Simplicity Gate**: Embedded Tier 1 (Simple CRUD: direct Repository + Service) and Tier 2 (High-Scale: Strategy, Adapter, Observer, Circuit Breaker) simplicity gates across rules, documentation, and starter templates.
- **16 Core Bundled Global Skills (`MyOS/_meta/global-skills/`)**: Bundled engineering protocol suite covering Clarify & Specify (`grill-me`, `to-spec`, `to-tickets`), Design & Model (`archify`, `domain-modeling`, `codebase-design`, `design-taste-frontend`), Build & Verify (`implement`, `tdd`, `verification-before-completion`, `code-review`, `diagnosing-bugs`), and Release & Ops (`git-commit`, `selfhost-devops`, `monorepo-architect`, `setup-pre-commit`).
- **High-Efficiency Context Capsule Generator (`MyOS/_meta/graph_recall.py`)**: Zero-token-waste Context Capsule generator outputting strict <350 token summaries of active project status, relevant Atomic Insights, session context, and AST symbol dependencies.
- **Automated Workstation & Child Repo Bootstrapping**: Automated onboarding (`bootstrap_machine.ps1`) restoring global skills, creating symlinks, and installing Git hooks; and repository connector (`bootstrap_repo.ps1`) for child repo scaffolding and skill deduplication.
- **Pre-Commit Portability Guard (`MyOS/_meta/check_portable_paths.py`)**: Script blocking hardcoded drive letters (`C:`, `F:`) and UTF-8 BOM corruptions.
