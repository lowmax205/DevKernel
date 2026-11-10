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

Registration creates missing six-file `.docs` planning templates and references
`.docs/agents/documentation-onboarding.md` in the managed agent block. New projects
use templates plus interviews; existing projects use evidence-backed drafts plus
interviews. Resolve feature-relevant gaps before planned implementation. Preserve
Archify artifacts and canonical memory. Consolidate only after developer review,
leaving redirects. Read-only sync does not scaffold or launch interviews.

Cloudflare's pinned `security-audit` is bundled in clean exports with attribution.
Install it separately using the agent's supported mechanism; do not mirror global
skills. Use it on demand and read UPSTREAM.md for Windows validator limitations.
