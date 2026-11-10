---
date: 2026-11-02
tags: [architecture, documentation, onboarding, guardrails]
---

# Documentation Onboarding Flow

Scaffold canonical `.docs/` planning files (`ARCHITECTURE.md`, `DESIGN.md`, `MEMORY.md`, `PRD.md`, `RULES.md`, `TASKS.md`) by first inspecting repository evidence, drafting findings, and interviewing the human developer to resolve ambiguities before committing.

Preserve existing Archify diagrams in place and link them from `ARCHITECTURE.md`. Keep ADRs in `.docs/decisions/` and active task cards in their designated issue trackers. Security audits must be performed strictly on-demand via the global `security-audit` skill, never automated during repo scaffolding.
