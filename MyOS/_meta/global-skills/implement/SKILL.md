---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

### Pre-Implementation Modernity Check (ZEP-03 / Context7)
- Before writing code for any modern framework or external library (e.g., Next.js App Router, Tailwind v4, Pydantic v2, Prisma v5+, Supabase v2, FastAPI), verify the exact installed version in `package.json`, `package-lock.json`, `pyproject.toml`, or `requirements.txt`.
- When introducing new dependencies or unfamiliar library APIs, invoke the `context7` MCP tool to retrieve live, official documentation and working syntax snippets before implementation.
- Strictly avoid deprecated patterns (e.g., `pages/` routing in App Router repos, Pydantic v1 `.dict()` in v2 projects, or unvetted CommonJS `require()` in ESM).

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.
