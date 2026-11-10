# DevKernel - Product requirements

Review: current starter contract plus the approved documentation/security additions; further product goals remain open.

## Audience and purpose

A portable Windows starter for developers using AI coding agents across independent Git repositories. A workspace can have any name and location; projects can live inside or outside it. Keep live direction, long-term memory, and optional graph connections in separate canonical homes.

## Supported capabilities

One interactive PowerShell entrypoint checks Git and Python, creates a clean workspace, and registers an existing repository for a selected agent. Preserve existing instructions, merge a marked routing block, and create missing project cards and hubs. Engineering policies are opt-in. Explicit reset backs up supported local agent configuration before clearing it.

Registration introduces six missing planning docs and an interview workflow. New projects use templates and interviews; existing projects use evidence-backed drafts and interviews. Consolidation is reviewed and leaves redirects. Full security audits are on demand, using the bundled pinned Cloudflare skill after separate agent installation.

## Success criteria and exclusions

Setup must work without Node.js, Obsidian, Graphify, API keys, or a security audit. Reruns preserve authored docs, architecture artifacts, status, and history. Dry runs write nothing. Exports are reproducible and contain no personal history, registrations, credentials, generated graphs, or unapproved external skills.

No automatic agent authentication, repository moves, Git initialization, commits, hooks, MCP installation, global skill mirroring, watcher, or release audit gate is introduced. See [accepted starter decisions](starter-decisions.md) and [setup instructions](../README.md).

## Open questions

No new feature roadmap or quantitative product metrics beyond the accepted starter behavior have been approved.
