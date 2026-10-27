# GitHub Copilot Custom Instructions — {{Project Name}}

When authoring, reviewing, or generating code in {{Project Name}}:

1. **Routing & Authority:**
   - Adhere strictly to the "One Home Per Fact" rules in `AGENTS.md`.
   - Never create project or session markdown notes in the Obsidian Vault root. Notes belong in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/`.
   - Reusable gotchas and architecture decisions belong in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.

2. **Backend Engineering Protocols (ZEP):**
   - **Controller Insulation:** Route handlers must not make direct database queries or raw external HTTP fetch calls. Delegate to domain services and repositories.
   - **Two-Tier Simplicity Gate:**
     - For standard CRUD: Use direct Repository + Service. Reject CQRS, event buses, and custom builders.
     - For complex operations: Use Strategy (>3 variants), Adapter (third-party schemas), Observer (side effects), and Circuit Breaker (flaky external APIs).

3. **Terminal & File Conventions:**
   - Use PowerShell 5.1 safe syntax on Windows (no bash `&&` or `||`).
   - Save all files as UTF-8 without BOM with ASCII punctuation.
   - Run verification (`lint:fix` and `build`) with exit code 0 before completing tasks.
