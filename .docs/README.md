# ZentoraDev Architecture & Standards Documentation

This directory contains the authoritative system architecture, engineering protocols, and agent operational standards for the ZentoraDev Meta-Developer Operating System (MyOS).

## Root project planning

These documents apply the same six-file workflow used by child repositories to ZentoraDev itself. Their content is grounded in the existing workspace and marks product decisions pending developer review.

| Document | Purpose |
| :--- | :--- |
| [PRD.md](PRD.md) | Product baseline, audience, boundaries, and acceptance criteria. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Current tooling and data flow, with references to architecture artifacts kept in place. |
| [RULES.md](RULES.md) | Index of inherited rules and root verification commands. |
| [DESIGN.md](DESIGN.md) | Documentation and terminal conventions; application UI is not applicable. |
| [TASKS.md](TASKS.md) | Workflow phases and canonical ticket references, without duplicate live status. |
| [MEMORY.md](MEMORY.md) | Links to the project card, Vault, and other canonical memory homes. |

Follow [documentation onboarding](agents/documentation-onboarding.md) for repo-grounded drafts, developer interviews, and reviewed consolidation. Security audits use the global `security-audit` skill on demand; see [pinned provenance and Windows limitations](../MyOS/_meta/global-skills/security-audit/UPSTREAM.md).

---

## 1. Consolidated planning references

Detailed design documents describing the components, data models, protocols, and workflows of ZentoraDev:

| Document | Scope & Contents |
| :--- | :--- |
| **[System Overview](ARCHITECTURE.md)** | Executive architecture summary, high-level Mermaid system diagram, core invariants (One Home Per Fact, Zero Token Waste, Portable Paths), and orchestration model. |
| **[Knowledge Architecture (MyOS)](ARCHITECTURE.md)** | Deep-dive into the 3-Layer Knowledge Architecture: Layer 1 Memory (Obsidian Vault & Atomic Insights), Layer 2 Connections (Graphify AST graph & Context Capsule Generator), Layer 3 Direction (ICM Cards), and reconciliation engine (`zentora_sync.py`). |
| **[Backend Engineering Protocols (ZEP)](RULES.md)** | Specification of the Two-Tier Simplicity Gate (Tier 1 CRUD vs Tier 2 High-Scale), the 10 Codified Backend Design Patterns, controller insulation, and progressive rule slicing. |
| **[Agent Lifecycle & Governance](TASKS.md)** | Autonomous AI pair programming lifecycle (AI Hero), mandatory verification gates (`verification-before-completion`), `/git-commit` production release pipeline, curated global skills, and repository bootstrapper. |

---

## 2. Agent Operational Standards (`.docs/agents/`)

Operational conventions and contracts used by agents across all child repositories:

| Document | Scope & Contents |
| :--- | :--- |
| **[Domain Documentation](agents/domain.md)** | Single-context layout standards for ubiquitous `GLOSSARY.md` and Architectural Decision Records (ADRs). |
| **[Issue Tracker](agents/issue-tracker.md)** | Local markdown issue tracking conventions inside `.scratch/<feature-slug>/` for autonomous tasks. |
| **[Triage Labels](agents/triage-labels.md)** | Canonical five triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). |
| **[ADR 001: OmniRoute & Ponytail](decisions/001-omniroute-and-ponytail.md)** | Local AI gateway routing for research and global anti-bloat skill. |
