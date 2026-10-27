# Changelog

All notable changes to the **DevKernel** workspace, ICM project cards, Obsidian Vault knowledge base, and Graphify knowledge graph are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

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
