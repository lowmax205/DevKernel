---
name: context7-docs
description: Retrieve live, up-to-date, version-specific library and framework documentation using Context7 MCP.
---

# Context7 Documentation Skill

Use this skill when you need fresh, accurate, version-specific documentation, APIs, and code examples for modern frameworks and libraries (e.g., Next.js 15, Tailwind v4, React 19, Vite, Prisma, Supabase, TanStack Query, Expo, etc.).

## Why Context7
Static training data frequently hallucinates deprecated APIs, wrong parameters, or missing configuration fields for fast-evolving packages. Context7 fetches real-time source documentation straight into the conversation.

## Workflow

### 1. Identify Library & Version
Check the project's `package.json`, `pyproject.toml`, or configuration files to determine the exact version in use.

### 2. Resolve Library ID
If the Context7 MCP server is available, invoke the library resolver tool:
- Call `resolve-library-id` with the package name (e.g. `next`, `tailwind`, `prisma`, `lucide-react`).
- This returns the canonical library path identifier (e.g., `/vercel/next.js`).

### 3. Fetch Targeted Documentation
- Call `get-library-docs` with the resolved library ID and the specific topic or component query (e.g., `Server Actions`, `app router middleware`, `zod validation schema`).
- Read the official guidelines and syntax before writing implementation code.

## Best Practices
- Never guess breaking changes between major versions.
- If Context7 is temporarily unavailable or unauthenticated, fall back to searching repository types (`.d.ts`), inline docstrings, or local configuration files.

