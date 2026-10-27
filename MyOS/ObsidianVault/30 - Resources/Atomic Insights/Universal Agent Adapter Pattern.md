---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/ai
created: 2026-10-27
summary: Abstracting tool-specific configurations behind modular adapters while keeping AGENTS.md as universal master prevents vendor lock-in and repository clutter.
---
# Universal agent adapters decouple tools from repo core

Committing tool-specific directories (`.cursor/`, `.agents/`, `.github/`, `CLAUDE.md`) directly into repository roots introduces tool bias, causes configuration collisions among developers using different AI assistants, and pollutes git history.

By treating `AGENTS.md` as the universal single source of truth and isolating editor-specific instructions into modular adapters (`MyOS/_meta/agent-adapters/`), the repository root remains completely tool-neutral. Local configurations are generated on demand via automated setup scripts (`setup_agent.ps1` or conversational `/setup <agent>` commands), ensuring seamless interoperability across Claude Code, Cursor, Antigravity, GitHub Copilot, and ChatGPT CLI.

## Context & Connections
- Discovered during: [[[DEV] 2026-10-27 - Multi-Agent Architecture and Knowledge Codification]]
- Applied in: [[DevKernel Hub]], [[One Home Per Fact]]
