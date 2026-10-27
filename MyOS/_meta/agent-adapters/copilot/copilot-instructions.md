# GitHub Copilot Custom Instructions — Zentora Dev

When authoring, reviewing, or generating code in this repository:

1. **Routing & Knowledge Authority:**
   - Adhere strictly to the "One Home Per Fact" rules in `AGENTS.md`.
   - Never create project or session markdown notes in the Obsidian Vault root. Place notes in `MyOS/ObsidianVault/10 - Projects/<Project Name>/`.
   - Reusable gotchas and architecture decisions belong in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.

2. **Backend Engineering Protocols (ZEP):**
   - **Controller Insulation:** Controllers and route handlers must never make direct database queries, execute raw SQL, or trigger raw HTTP fetch calls. Delegate to domain services and repositories.
   - **Two-Tier Simplicity Gate:**
     - For standard CRUD (Tier 1): Use direct Repository + Service. Reject CQRS, event buses, and custom builders.
     - For complex operations (Tier 2): Use Strategy for >3 business variants, Adapter for third-party schemas, Observer for side effects, and Circuit Breaker for flaky external APIs.

3. **Terminal & File Conventions:**
   - Use PowerShell 5.1 safe syntax on Windows (avoid bash `&&` or `||`).
   - Save all files as UTF-8 without BOM with ASCII punctuation.
   - Run verification (`lint:fix` and `build`) with exit code 0 before completing tasks.
