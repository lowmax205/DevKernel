# DevKernel Windows Starter Architecture

[Interactive diagram](system-architecture.html) | [Mermaid source](system-architecture.mmd) | [Archify candidate](system-architecture.json)

The diagram is a system overview of the Windows starter, with source references
pinned to implementation commit `480ce99465d420b344077def60e4ecc7e9695045`.
It models runtime ownership and persistent outputs, rather than every helper.

`setup.ps1` checks prerequisites and collects the workspace, repository, agent,
and optional flags. The compatibility entry points delegate to the same setup.
The Python standard-library CLI validates the existing Git repository root and
rejects linked configuration, then merges marked instructions for one selected
agent. Core routing applies by default; engineering rules are opt-in.

Registration supports repositories inside or outside Repos without moving them.
It writes ignored machine-local registry and workspace pointers, creates a
project card and hub only when absent, and preserves existing status and history.
The optional reconciliation script reads registrations and warns about missing
paths without installing hooks, starting a watcher, or archiving projects.

Reset is a separate explicit flag. The CLI copies every supported repository
instruction and skill target into a timestamped backup before clearing any
of them, then writes only the chosen agent adapter. Global skills, source files,
CI workflows, credentials, Git hooks, and MCP configuration are outside its scope.

Export is a separate CLI action. An allowlist copies reusable tools, DevKernel
skills, core rules, and templates into a new workspace. It excludes personal
history, generated diagrams and graphs, credentials, registrations, Git history,
and external skill bundles. This source checkout retains legacy material.

Graphify is optional and invoked independently. AST updates do not call an LLM;
semantic extraction is a separate API-consuming action. Recall reads this
workspace's graph or an explicit --graph path, with no parent-workspace fallback.
Obsidian is optional: all memory remains ordinary Markdown.

The optional graph subsystem is deliberately separate from setup in the diagram.
The overview does not depict tool installation, authentication, runtime agent UI,
or a semantic-extraction service because none is part of starter setup.

Automated Archify validation, strict artifact checks, and real-browser checks
passed. No perceptual screenshot review was requested or performed. Machine-local
verification receipts remain ignored beside the artifact or under `.archify/`.
