# Changelog

All notable changes to the **DevKernel** workspace, ICM project cards, Obsidian Vault knowledge base, and Graphify knowledge graph are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Preserve-first six-file project documentation scaffolding through registration, with repo-grounded drafts, developer interviews, reviewed consolidation, and Archify references.
- Complete pinned Cloudflare security-audit bundle, MIT attribution, and provenance in clean exports; agent installation remains separate and audits stay on demand.
- Starter-specific root planning docs and integration checks for docs, dry runs, preservation, exports, and linked paths. Read-only reconciliation is unchanged.

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
