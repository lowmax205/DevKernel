---
date: 2026-11-01
tags: [architecture, obsidian, routing, guardrails]
---

# Vault Path Resolution Invariant

The Obsidian Vault lives exclusively at `<ZENTORA_ROOT>/MyOS/ObsidianVault/`. Never reference or create an `ObsidianVault` folder directly at `<ZENTORA_ROOT>`.

Child repositories must route long-term history and atomic insights strictly via `MyOS/ObsidianVault/10 - Projects/<Project Name>/` and `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`. Stale rule files in child repos that omit `MyOS/` will cause agents to spawn rogue untracked vault folders at the root. Use `zentora_sync.py` drift audit to enforce synchronization.

