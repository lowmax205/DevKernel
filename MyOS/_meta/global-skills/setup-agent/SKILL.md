---
name: setup-agent
description: Provision and configure ZentoraDev or child repositories for specific AI agents (Claude Code, ChatGPT CLI, Cursor, Antigravity, GitHub Copilot).
---
# Setup Agent Skill

Use this skill when the user asks to set up, install, or configure ZentoraDev or a child repository for a specific AI agent (e.g. `/setup antigravity`, `/setup cursor`, `/setup claude`, `/setup copilot`, `/setup chatgpt`, or `/setup all`).

## Supported Agents
- `all` (Provisions adapters for all agents simultaneously)
- `claude` (Deploys `CLAUDE.md` referencing `AGENTS.md`)
- `cursor` (Deploys `.cursor/rules/zentora-dev.mdc` and `.cursor/rules/backend-patterns.mdc`)
- `antigravity` (Configures directory junctions to `~/.agents/skills`, `.agents/skills.json`, and manifests)
- `copilot` (Deploys `.github/copilot-instructions.md`)
- `chatgpt` (Verifies `AGENTS.md` and CLI context)

## Command Execution
Run the automated provisioner via PowerShell:

```powershell
# For the root ZentoraDev workspace:
powershell -ExecutionPolicy Bypass -File .\MyOS\_meta\setup_agent.ps1 -Agent <name>

# For a specific child repository:
powershell -ExecutionPolicy Bypass -File .\MyOS\_meta\setup_agent.ps1 -Agent <name> -TargetRepo "<RepoName>"
```

### Slash Command Usage
- `/setup all`
- `/setup claude`
- `/setup cursor`
- `/setup antigravity`
- `/setup copilot`
- `/setup chatgpt`
