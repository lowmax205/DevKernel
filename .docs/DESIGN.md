# ZentoraDev - Design

Review: repository-grounded draft; pending developer review.

## Applicability

ZentoraDev is a developer tooling and knowledge workspace. A product web or mobile UI, component library, responsive layout system, and application color tokens are not applicable to this root update. Client-repo UI systems belong to those repositories.

## Documentation and terminal experience

Use concise Markdown, navigable relative links, descriptive headings, and copyable PowerShell commands. Use ASCII punctuation and UTF-8 without BOM as required by [AGENTS.md](../AGENTS.md).

Keep machine-specific absolute paths out of committed docs. Use relative links within the repository and the `<ZENTORA_ROOT>` placeholder for workspace routing. Mark missing artifacts as pending instead of creating broken links.

Manual bootstrap prints the next-step interview prompt. Background sync does not prompt, launch agents, or run audits. Existing authored documents remain intact until reviewed consolidation.

## Architecture visualization

Follow the existing Archify workflow for future diagrams. Keep generated HTML and Mermaid sources in `.docs/architecture/`, linked through [ARCHITECTURE.md](ARCHITECTURE.md). This update does not create or redesign diagrams.

## Open questions

If a root dashboard or interactive product UI becomes a feature, interview the developer about users, interactions, and visual requirements before defining a design system.
