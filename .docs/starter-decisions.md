# Windows starter decisions

Accepted scope for the shareable starter:

- Windows PowerShell 5.1 and Python 3.9+, standard library only.
- Clone and run one interactive PowerShell command.
- Check Git and Python; guide installation rather than installing prerequisites.
- Any workspace name and path. Register Git repositories under Repos or elsewhere.
- Configure one chosen agent: Codex, Claude Code, Cursor, Copilot, or Antigravity.
- Preserve existing instructions, insert a marked DevKernel block, and flag potential policy conflicts for review.
- Explicit reset backs up all known repository agent instructions and local skills before clearing them.
- Global skills, Git hooks, MCP configuration, source files, and CI workflows remain untouched.
- Core routing and memory rules are standard. Engineering policies are opt-in.
- Obsidian, Graphify, semantic extraction, and API keys are optional.
- Include DevKernel-owned skills and the complete pinned Cloudflare `security-audit` as an explicit third-party exception, with MIT attribution and source revision. Agent installation remains separate; setup never changes global skills.
- Registration creates missing six-file `.docs` templates and interview guidance. Existing content is preserved. The coding agent drafts from evidence and interviews the developer; consolidation is reviewed and leaves redirects. Sync remains read-only.
- Produce a clean distribution through an explicit file allowlist; preserve maintainer history in this source checkout.
- Local changes only; no commit, push, release, or deployment.

Success means setup works without optional tools, preserves existing content on reruns,
can reset and recover configuration, supports external repositories, and exports no
maintainer history, generated graphs, machine paths, credentials, or unapproved external skill bundles.
