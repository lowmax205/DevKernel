# GitHub Copilot Custom Instructions — {{Project Name}}

When authoring, reviewing, or generating code in {{Project Name}}:

1. **4-Step Surgical Lookup & Canonical Routing:**
   - Follow the 4-step surgical lookup in `AGENTS.md` (Master Routing -> ICM Card in `MyOS/projects/{{project-slug}}.md` -> Obsidian Hub/Session in `MyOS/ObsidianVault/10 - Projects/{{Project Name}}/` -> Dynamic recall via `graph_recall.py`).
   - Reusable gotchas and architecture decisions belong strictly in `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
   - Never create project or session markdown notes in the Obsidian Vault root.

2. **On-Demand Backend Protocols & Simplicity Gate:**
   - Consult `.docs/RULES.md` before designing domain modules:
     - Route handlers must not make direct database queries or raw external HTTP fetch calls.
     - Enforce Tier 1 Simplicity (Repository + Service) for standard CRUD; reserve Tier 2 patterns (Strategy, Adapter, Observer, Circuit Breaker) for complex multi-branch integrations.

3. **Strict Modernity Gate & Anti-Hallucination:**
   - Always inspect `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt` to confirm installed versions before generating code.
   - For breaking-change prone libraries, consult `context7` MCP tool or official docs. Reject deprecated syntax patterns.

4. **Terminal, Encoding & Verification:**
   - Use PowerShell 5.1 safe syntax on Windows (no bash `&&` or `||`).
   - Save all files as UTF-8 without BOM with ASCII punctuation.
   - Run native verification (`npm run lint:fix` / `lint` and `npm run build` exit code 0) before completing tasks or committing.
