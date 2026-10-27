# ZentoraDev Architecture & Standards Documentation

This directory contains the authoritative system architecture, engineering protocols, and agent operational standards for the ZentoraDev Meta-Developer Operating System (MyOS).

---

## 1. System Architecture Specifications (`.docs/architecture/`)

Detailed design documents describing the components, data models, protocols, and workflows of ZentoraDev:

| Document | Scope & Contents |
| :--- | :--- |
| **[System Overview](architecture/system-overview.md)** | Executive architecture summary, high-level Mermaid system diagram, core invariants (One Home Per Fact, Zero Token Waste, Portable Paths), and orchestration model. |
| **[Knowledge Architecture (MyOS)](architecture/knowledge-layers.md)** | Deep-dive into the 3-Layer Knowledge Architecture: Layer 1 Memory (Obsidian Vault & Atomic Insights), Layer 2 Connections (Graphify AST graph & Context Capsule Generator), Layer 3 Direction (ICM Cards), and reconciliation engine (`zentora_sync.py`). |
| **[Backend Engineering Protocols (ZEP)](architecture/backend-engineering-protocols.md)** | Specification of the Two-Tier Simplicity Gate (Tier 1 CRUD vs Tier 2 High-Scale), the 10 Codified Backend Design Patterns, controller insulation, and progressive rule slicing. |
| **[Agent Lifecycle & Governance](architecture/agent-lifecycle.md)** | Autonomous AI pair programming lifecycle (AI Hero), mandatory verification gates (`verification-before-completion`), `/git-commit` production release pipeline, 16 pruned core skills, and repository bootstrapper. |

---

## 2. Agent Operational Standards (`.docs/agents/`)

Operational conventions and contracts used by agents across all child repositories:

| Document | Scope & Contents |
| :--- | :--- |
| **[Domain Documentation](agents/domain.md)** | Single-context layout standards for ubiquitous `GLOSSARY.md` and Architectural Decision Records (ADRs). |
| **[Issue Tracker](agents/issue-tracker.md)** | Local markdown issue tracking conventions inside `.scratch/<feature-slug>/` for autonomous tasks. |
| **[Triage Labels](agents/triage-labels.md)** | Canonical five triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). |
