# DevKernel - Architecture

## Runtime and entrypoints

Windows PowerShell 5.1+ and Python 3.9+ standard library; Git for Windows is required. There is no root application package manifest or web backend. `setup.ps1` gathers inputs and delegates to [devkernel.py](../MyOS/_meta/devkernel.py). Compatibility wrappers for bootstrap and agent setup use the same registration path.

## Registration flow

Validate the workspace, existing Git repo root, supported agent, slug collisions, instruction markers, and linked configuration paths before writes. Merge one selected agent adapter. Render missing six-file planning templates and onboarding guidance from `MyOS/ObsidianVault/Templates/repo-agents-starter/.docs/`. Preserve existing documents. Dry runs validate and print a plan without writing. Successful registration prints the developer-interview next step.

Create ignored `.devkernel` registry and workspace pointers, plus missing project cards and hubs. Workspace identity comes from the local pointer rather than a parent directory or a fixed name. Optional engineering policies remain opt-in. Read-only reconciliation checks registered paths and does not scaffold docs, launch interviews, install hooks, or archive missing repos.

## Export boundary

An explicit allowlist includes runtime tools, core profiles, DevKernel-owned skills, planning templates, tests, and the complete pinned Cloudflare security-audit exception. Exclude personal history, graphs, generated diagrams, registrations, and other historical third-party bundles. Exported workspaces can register projects and export themselves independently.

## Architecture artifacts

Preserve the [interactive Archify diagram](architecture/system-architecture.html), [Mermaid source](architecture/system-architecture.mmd), and [source overview](architecture/system-overview.md) in place. These diagrams are pinned to an earlier implementation revision; this document describes the new documentation and security additions. Do not interpret the earlier export model as excluding the newly approved security exception.

Source diagrams and maintainer planning documents are not clean-export content. Reusable templates link a project's own architecture artifacts after verifying they exist. See [memory routing](MEMORY.md) and [rules](RULES.md).
