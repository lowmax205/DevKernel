### One Home Per Fact
- Live status and next steps belong only in `MyOS/projects/<slug>.md` in the workspace.
- History belongs in `MyOS/ObsidianVault/10 - Projects/<Repository Name>/`.
- Reusable insights belong in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
- Never create notes at the vault root or a second vault outside `MyOS`.
- On `save progress`, update one consolidated daily session note and the project card.
- Graph connections belong in `MyOS/graphify-out/graph.json`, when Graphify is enabled.
- Read the project card before answering project status questions. Use graph recall only when a graph exists.

### Safe engineering
- Preserve existing repository standards. Flag conflicting rules for the developer to resolve.
- Make minimal changes tied to the request; clarify material ambiguity before implementation.
- Verify changes with the repository's applicable checks before claiming completion.
- Use PowerShell 5.1-compatible commands and UTF-8 without BOM.
- Keep machine paths, credentials, backups, and local registration under ignored configuration.
- Global skills are installed separately. Never delete or mirror the developer's global skill directories.
- Optional tools must not block core workspace use. Never install hooks or MCP servers implicitly.

### Project documentation and security
- Follow `.docs/agents/documentation-onboarding.md` for the six canonical planning files under `.docs/`.
- Inspect repo evidence and interview the developer; new projects use templates, existing projects use evidence-backed drafts. Resolve feature-relevant gaps before planned features; diagnosis, urgent fixes, and docs work may proceed with gaps recorded.
- Consolidate only after developer review, leaving redirects. Preserve setup guidance, Archify artifacts, ADRs, tickets, and central memory in place.
- Use bundled Cloudflare `security-audit` on demand after separate agent installation. Setup does not install global skills or run audits. Check its UPSTREAM.md for native Windows validator limitations.
