# ADR 001: Local OmniRoute Gateway & Ponytail Skill for Free-Tier Research and Anti-Bloat

- **Status:** Accepted
- **Date:** 2026-11-03
- **Deciders:** User & Antigravity

## Context
When performing exploratory codebase indexing, dependency lookups, and graph recall queries (via Graphify and Context7), running top-tier proprietary models for every minor question can accumulate unnecessary token costs. Additionally, coding agents can easily introduce premature abstractions or unneeded boilerplate when given broad tasks.

## Decisions

1. **OmniRoute Gateway for Free-Tier Research:**
   - Install `omniroute` globally on the local machine (`http://127.0.0.1:20128`).
   - Restrict OmniRoute host to local loopback (`127.0.0.1`) with `REQUIRE_API_KEY=true` to ensure inference is inaccessible from the external network.
   - Restrict OmniRoute use to **read-only research and indexing**. Code generation and edits remain strictly governed by Antigravity under mandatory verification gates.
   - Sensitive keys reside in the git-ignored `MyOS/.env.omniroute` loaded on demand via `launch_research_omni.ps1`.

2. **Ponytail Skill as Global Restraint Policy:**
   - Install `ponytail` globally in `~/.agents/skills/ponytail/SKILL.md` (no duplication in child repositories).
   - Serves alongside `surgical-coding` as a 7-rung decision ladder (YAGNI, platform-native over custom code, minimal diffs) to eliminate code bloat during implementation tasks.

## Consequences
- **Positive:** Reduces token consumption for routine file and concept research; reinforces minimalist diff discipline across all Zentora child repositories.
- **Negative / Risks:** Free-tier models have limited reasoning and tool-calling reliability; must remain strictly constrained to read-only queries without file write access.

