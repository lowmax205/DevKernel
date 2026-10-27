---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/ai
created: 2026-10-18
summary: Storing live status in ICM project cards while keeping session history in Obsidian prevents context bloat and conflicting state.
---
# One home per fact keeps routing and history separate

In a multi-project AI knowledge architecture, mixing live task status with historical session logs causes agents to read outdated priorities or scan entire vaults unnecessarily. By enforcing the "One Home Per Fact" principle, each type of knowledge has a single canonical location.

Live status and immediate next steps live exclusively in `MyOS/projects/[project-slug].md`, full chronological session history lives in `ObsidianVault/10 - Projects/[Project Name]/`, reusable atomic insights live in `ObsidianVault/30 - Resources/Atomic Insights/`, and cross-note relationships live in `graphify-out/graph.json`.

## Context & Connections
- Discovered during: [[[TEST] 2026-10-18 - Initial Knowledge Sandbox Setup]]
- Applied in: [[DevKernel Hub]]
