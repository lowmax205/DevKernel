---
name: devkernel-manager
description: Route DevKernel project cards, local Markdown memory, and optional graph recall.
---
# DevKernel Manager

Resolve the workspace using the repository's ignored `.devkernel/workspace.json`.
Paths are relative to the project repository when possible; across drives they
are machine-local absolute paths. Never infer the workspace from its folder name.

Read the project card in `MyOS/projects/` before answering status questions.
Keep live status and next steps only there. Keep history under
`MyOS/ObsidianVault/10 - Projects/<Repository Name>/` and reusable insights under
`MyOS/ObsidianVault/30 - Resources/Atomic Insights/`. Never write notes at vault root.

On `save progress`, update one daily session and the card. Graphify is optional:
use `graphify update "MyOS"` only when installed and requested by the workflow.
Use semantic extraction only when explicitly requested. No automatic API calls.

Register projects using `bootstrap_repo.ps1 -RepoPath <existing-root> -Agent <agent>`.
Preserve local and global instructions and skills. Reset requires an explicit
user request and uses `-ResetAgentConfig`, which backs up supported repository
instructions and local skills. Never reset global skills or overwrite hooks.
