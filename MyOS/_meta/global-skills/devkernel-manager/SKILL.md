---
name: devkernel-manager
description: Manage the DevKernel 3-layer knowledge architecture (ICM Project Cards, Obsidian Vault Session/Zettelkasten Notes, Archify Architecture Diagrams, AI Hero + git-commit Lifecycle, Repo Bootstrapper, and Graphify + DeepSeek Knowledge Graph).
---
# DevKernel Manager Skill

Use this skill when checking project status, recalling cross-project architectural context, running `archify <Project Name>`, `bootstrap <RepoName>`, `/git-commit [major|minor|patch]`, or `save progress` in `<ZENTORA_ROOT>`.

## Exact Graphify CLI Syntax (NEVER use `--update`)
- **Fast AST-only code update (no LLM needed, no `--backend` or `--output` flags):**
  - If repo has `scripts/graphify.ps1`: `.\scripts\graphify.ps1 update`
  - Otherwise: `graphify update "<ZENTORA_ROOT>/MyOS"`
- **Full AST + DeepSeek Semantic Extraction (writes to `<ZENTORA_ROOT>/MyOS/graphify-out`):**
  ```powershell
  graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"
  ```
- **Gotchas to Avoid:**
  1. Never pass `--update` (causes `error: unknown command '--update'`).
  2. Never pass `--backend` or `--output` to `graphify update`.
  3. Never pass `.../graphify-out` to `--output` in `graphify extract` (`--output <DIR>` automatically appends `/graphify-out/`).

## Portability (no hardcoded drive letters)
The workspace may live on any drive or path. Paths shown in this skill are examples only.
- Never commit a literal drive letter or absolute root (`<ZENTORA_ROOT>`). Use workspace-relative paths or `<ZENTORA_ROOT>`.
- Scripts and hooks (`zentora_sync.py`, `agy_memory_hook.py`, `bootstrap_*.ps1`, `graph_recall.py`, `git-hooks/post-commit`) must resolve one `ROOT` from their own location (`Path(__file__).parents[2]`, `$PSScriptRoot`, `git rev-parse --show-toplevel`), overridable by `ZENTORA_ROOT`.
- Never run blanket search-and-replace for paths or single letters. Use anchored edits and review `git diff` on `.py/.ps1/.mjs`.
- Discover child repos by scanning `<ROOT>/Repos/**`. A missing repo must warn only; never auto-archive it or flip it to Vault-Only.
- Machine-specific absolute paths belong only in gitignored output.

## Core Workflows
1. **Recall & Routing (`One Home Per Fact`) & The 4-Step Surgical Lookup**:
   - Execute the 4-Step Surgical Lookup on every task to read only ~4 to 5 highly relevant files:
     1. Read Master Routing Table (`<ZENTORA_ROOT>/AGENTS.md`)
     2. Read ICM Project Card (`<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md`)
     3. Read Obsidian Hub & Latest Session Note (`<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/`)
     4. Ingest Dynamic Surgical Files from `[ZENTORA CONTEXT CAPSULE]` (`graph_recall.py` routes 2–8 files dynamically based on score dropoff & confidence weighting).
   - Before ANY file/function search, bug fix, feature implementation, or architecture question:
     - Inspect the auto-injected `[ZENTORA CONTEXT CAPSULE]` and `[ZENTORA MEMORY & GRAPHIFY ACTIVE]` steps from `.agents/hooks.json` (`MyOS/_meta/agy_memory_hook.py`).
     - Use the native `graphify` MCP tools (`query_graph`, `get_node`, `get_neighbors`, `shortest_path` with `project_path` set to the child repository).
     - Or run federated recall: `python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<english keywords>" --repo "<RepoPath>" --hops 2` (or `.\scripts\graphify.ps1 query "<question>"`).
2. **AI Hero + DevKernel Development Lifecycle**:
   - Keep generic AI Hero & workflow skills globally in `~/.agents/skills/` (`grill-me`, `grill-with-docs`, `to-spec`, `to-tickets`, `domain-modeling`, `codebase-design`, `tdd`, `implement`, `code-review`, `git-commit`, `archify`, `surgical-coding`, `design-taste-frontend`, `monorepo-architect`, `selfhost-devops`, `setup-agent`, `devkernel-manager`). Keep only strictly domain-specific skills in `<Repo>/.agents/skills/`.
   - **Commit & Version (`/git-commit`)**: Invokes the global `git-commit` skill to create atomic conventional commits that always append technical bullets under `## [Unreleased]` in `CHANGELOG.md` (matching the repo's format), and supports inline or follow-up `major`, `minor`, or `patch` version bumping.
3. **Save Progress (`save progress`)**:
   - Dynamically resolve `<Project Name>` and `<CODE>` from git repository root, active editor file, or CLI parameter `-Project <CODE>`.
   - Ensure `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/` exists on demand. **NEVER create files at the root of `<ZENTORA_ROOT>/MyOS/ObsidianVault/`.**
   - Create or update today's single consolidated session note: `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/[<CODE>] YYYY-MM-DD - <Focus Title>.md`. If called multiple times in one day, append new work under `## What was built` and update the H1 / summary instead of spawning duplicate notes.
   - Extract atomic reusable insights to `<ZENTORA_ROOT>/MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Update `status`, `next`, and `updated` in `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md`.
   - Run fast AST update by default: `.\scripts\graphify.ps1 update` (in child repo) and `graphify update "<ZENTORA_ROOT>/MyOS"` (zero DeepSeek tokens). Run DeepSeek extraction `graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"` ONLY on major milestone releases or when told `save progress --deep`.
4. **Interactive System Architecture (`archify <Project Name>`)**:
   - Read the global `archify` skill and `<ZENTORA_ROOT>/MyOS/ObsidianVault/Templates/archify-architecture-workflow.md`.
   - Always output into `.docs/architecture/` (never `docs/architecture/`): produce `.docs/architecture/system-architecture.html` and `.docs/architecture/system-architecture.mmd` inside the repository.
   - Update `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/<Project Name>/<Project Name> Hub.md` (`## Architecture` section) and `<ZENTORA_ROOT>/MyOS/projects/<project-slug>.md` (`| Architecture Diagram | ... |` row).
5. **Bootstrap Repository (`bootstrap <RepoName>`)**:
   - Run:
     ```powershell
     powershell -ExecutionPolicy Bypass -File "<ZENTORA_ROOT>/MyOS/_meta/bootstrap_repo.ps1" -RepoPath "<RepoName-or-Path>"
     ```
   - This scaffolds multi-agent support (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.cursor/rules/`), `.agents/hooks.json`, `.agents/rules/00-zentora-and-ai-hero.md`, `CHANGELOG.md` (with `## [Unreleased]`), `MyOS/projects/<project-slug>.md`, `MyOS/ObsidianVault/10 - Projects/<Project Name>/<Project Name> Hub.md`, and initializes `graphify-out/graph.json`, while preserving custom scoped `scripts/graphify.ps1` runners and pruning duplicate global skills from `<Repo>/.agents/skills/`.
6. **Backend Engineering Protocols (ZEP) & Two-Tier Simplicity Gate**:
   - When scaffolding, reviewing, or refactoring backend code, inspect design against the 10 Backend Design Patterns codified in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`:
     - `Repository Pattern`: Controller insulation and data access abstraction.
     - `Factory Pattern`: Provider creation and dynamic driver resolution.
     - `Singleton Pattern`: Lifecycle and state safety without globals.
     - `Strategy Pattern`: Multi-algorithm isolation (>3 variations).
     - `Observer Pattern`: Event publication decoupling async side-effects.
     - `Builder Pattern`: Multi-step assembly (5+ parameters).
     - `Adapter Pattern`: External API schema translation.
     - `Decorator Pattern`: Cross-cutting transparent telemetry/caching.
     - `CQRS Pattern`: High-concurrency command and query separation.
     - `Circuit Breaker Pattern`: Remote fault tolerance and fallback degradation.
   - Enforce controller insulation: handlers never run raw SQL or direct third-party fetch calls.
   - Enforce Two-Tier Simplicity Gate: Tier 1 CRUD (Repo + Service; reject CQRS/Event Bus/Builders); Tier 2 (Strategy for >3 branches, Adapter for schemas, Observer for side effects, Breaker for external APIs).
   - Polyglot enforcement: TypeScript (interface/Prisma/Zod) vs Python (typing.Protocol/Pydantic v2/SQLAlchemy).
