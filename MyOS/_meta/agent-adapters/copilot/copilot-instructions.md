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

3. **Strict Pre-Coding Modernity & Anti-Hallucination Gate (ZEP-03):**
   - **Mandatory Package Version Verification:** Always inspect `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt` to confirm installed library versions before writing code.
   - **Live API Documentation:** Verify modern syntax and official API signatures via Context7 before writing code for breaking-change prone frameworks (Next.js App Router, Tailwind v4, Pydantic v2, Prisma v5+, Supabase v2, FastAPI).
   - **Zero Deprecated Syntax:** Strictly reject deprecated patterns (no `pages/` routing in Next.js App Router, no Pydantic v1 `.dict()`, no unvetted CommonJS `require()` in modern TypeScript/ESM).
   - **Issue Diagnostics (Fetch Protocol):** When hitting package build or dependency errors, inspect official GitHub issues/release notes via Fetch instead of speculating.

4. **Terminal & File Conventions:**
   - Use PowerShell 5.1 safe syntax on Windows (avoid bash `&&` or `||`).
   - Save all files as UTF-8 without BOM with ASCII punctuation.
   - Run verification (`lint:fix` and `build`) with exit code 0 before completing tasks.
