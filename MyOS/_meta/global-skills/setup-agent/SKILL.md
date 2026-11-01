---
name: setup-agent
description: Configure a supported AI agent for a DevKernel-registered Git repository.
---
# Setup Agent

Use `MyOS/_meta/setup_agent.ps1 -Agent <agent> -TargetRepo <existing-git-root>`
from the workspace. Agents: codex (chatgpt alias), claude, cursor, copilot,
antigravity. Configure one agent per invocation. Use `-DryRun` for a preview.

Existing instructions and skills are preserved by default. Only pass
`-ResetAgentConfig` when explicitly requested; this backs up and clears the
supported repository instruction and local skill paths for all agents.
Never change global skills, credentials, MCP configuration, or Git hooks.
`-EngineeringProfile` is optional. Missing tools require installation guidance,
not automatic installation. Report conflicts for manual review.
