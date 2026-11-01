# DevKernel

A Windows starter workspace for developers using AI coding agents across repositories.
Keep live project direction in short cards, project history in a local vault, and
optional graph connections in Graphify. Your workspace can have any name.

## Start here

Requirements: Windows, PowerShell 5.1+, Git for Windows, and Python 3.9+ on PATH.
Install missing tools from [Git for Windows](https://gitforwindows.org/) and
[Python](https://www.python.org/downloads/windows/), enable PATH, then reopen PowerShell.
The selected AI agent must already be installed and signed in. Setup configures
repository instructions; it does not install or authenticate the agent.

Clone this repository, open PowerShell in the clone, and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
```

Choose a **new, empty destination path** for your workspace (the directory must not
yet exist), select an agent, and enter the root of an existing Git repository.
For later registrations, select the workspace previously created by setup.
Repositories may live anywhere, including inside the workspace's Repos folder.
Setup never moves, clones, initializes, or commits your project repositories.

The prompts also offer an optional engineering profile and a reset option; both
default to no. Use a noninteractive invocation for repeatable setup:

```powershell
.\setup.ps1 -WorkspacePath '..\MyWorkspace' -RepoPath '..\ExistingProject' -Agent codex -NonInteractive
```

Add `-DryRun` to preview without writes. Use `-EngineeringProfile` to opt into
version-aware library checks, simple backend patterns, and project verification
policies. Existing repository standards still require review for conflicts.

## Agent integrations

| Agent | Repository instructions |
| --- | --- |
| Codex (`codex`, also `chatgpt`) | AGENTS.md |
| Claude Code (`claude`) | CLAUDE.md pointing to AGENTS.md |
| Cursor (`cursor`) | .cursor/rules/devkernel.mdc pointing to AGENTS.md |
| GitHub Copilot (`copilot`) | .github/copilot-instructions.md pointing to AGENTS.md |
| Antigravity (`antigravity`) | GEMINI.md pointing to AGENTS.md |

Setup adds or updates a marked DevKernel block and preserves surrounding content.
It reports existing instructions for policy review; it cannot determine whether
natural-language instructions contradict each other. Malformed markers stop setup.
Choosing another agent adds that adapter without deleting previous adapters.

Native file conventions: [Claude memory](https://code.claude.com/docs/en/memory),
[Cursor rules](https://cursor.com/docs/context/rules),
[Copilot instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions),
and [Antigravity rules](https://antigravity.google/docs/rules/).
Agent UI behavior must be checked in your installed client; automated tests verify
the generated files and setup behavior, not authenticated agent sessions.

## Register another repository

From the generated workspace:

```powershell
.\MyOS\_meta\bootstrap_repo.ps1 -RepoPath '..\AnotherProject' -Agent claude
```

`setup_agent.ps1 -Agent cursor -TargetRepo <path>` is another entry point. Both use
the same preserve-first registration. Pass an existing Git repository root, not
a project name or a subdirectory. `all` is no longer a setup target: choose one
agent per invocation. No global settings, MCP servers, Git hooks, or tools are installed.

## Reset repository instructions and skills

Explicitly add `-ResetAgentConfig` to setup or registration. This backs up **all
known local instruction and skill paths for all five agents**, then configures
only the selected agent. The exact path list is `RESET_PATHS` in
`MyOS/_meta/devkernel.py`; it includes root AGENTS/CLAUDE/GEMINI instructions,
legacy Cursor rules, local rules, local skills, and Copilot instruction files.
Custom instructions stored elsewhere are outside this reset list.

Backups are under `<repository>/.devkernel/backups/<timestamp>/`, with a
`manifest.json` listing original relative paths. To restore, close the agent,
copy each listed path from the backup over its original repository location,
and keep the backup until you have checked the restored configuration. For a
complete rollback, remove newly generated adapter files that are not listed in
the backup manifest. Global skills, credentials, CI workflows, source files, and
MCP configuration are outside reset scope. Links and junctions are rejected.

## Workspace layout

- `MyOS/projects/<slug>.md`: live status and next steps.
- `MyOS/ObsidianVault/10 - Projects/<Repository Name>/`: hubs and daily sessions.
- `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`: reusable knowledge.
- `MyOS/ObsidianVault/Templates/`: session and insight templates.
- `MyOS/graphify-out/`: optional graph output, empty initially.
- `.devkernel/local.json`: ignored machine-local repository registry.
- `<repository>/.devkernel/workspace.json`: ignored workspace pointer.

Do not commit `.devkernel` files or backups. Copying a workspace to a different
machine requires registering its repositories again. Duplicate repository names
that produce the same slug are rejected to prevent card collisions.

The optional `zentora_sync.py --once` checks registered paths without changing
cards or archiving missing repositories. Registration is explicit; setup does
not enable a watcher or scan other workspaces.

## Optional tools and skills

Markdown memory works without Obsidian. To browse it visually, open the generated
`MyOS/ObsidianVault` folder as a vault. Do not create another vault at workspace root.

Graphify is optional and installed separately. From the workspace, use
`graphify update "MyOS"` for AST updates. Semantic extraction is an explicit,
API-consuming action: `graphify extract "MyOS" --backend deepseek --output "MyOS"`.
Store API keys in a local ignored environment file. Use
`python MyOS/_meta/graph_recall.py "keywords" --hops 2` only after generating a graph.

See [.docs/external-skills.md](.docs/external-skills.md) for separate skill
installation. Only DevKernel-owned skills are included in clean exports.

## Share a clean starter

The maintainer source checkout contains historical notes, generated diagrams,
graphs, and legacy skill bundles. **Use the clean export rather than sharing a
copy of that checkout.** Export uses an explicit allowlist and never copies them:

```powershell
python MyOS/_meta/devkernel.py export --destination '..\DevKernel-Starter'
```

The output has no Git history, credentials, machine registrations, personal notes,
generated graphs, or external skills. Review it, then distribute it or initialize
a separate Git repository when ready. Export refuses to overwrite a destination.

## Verify development changes

```powershell
python -m unittest discover -s tests -v
powershell -NoProfile -ExecutionPolicy Bypass -File tests\verify-powershell.ps1
python MyOS/_meta/check_portable_paths.py
git diff --check
```

Runtime uses only Python's standard library; there are no runtime package dependencies.
See [.docs/starter-decisions.md](.docs/starter-decisions.md) for the accepted scope.
