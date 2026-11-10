---
name: dead-code-audit
description: Audit a repository for unused files, exports, dependencies, unreachable blocks, and retired paths. Use when asked to find dead or obsolete code and provide evidence for a separate cleanup.
---

# Dead-code audit

Default to a report. Keep source, manifests, lockfiles, and existing work intact. Record the Git revision and working-tree state before and after the scan.

1. Map entry points from workspace manifests, framework conventions, test configurations, build and deployment commands, and documentation. Use Graphify when available. Check workers, schedulers, migration and seed tooling, public routes, and assets referenced by strings or loaded from data. Review analyzer-loaded project configs before running them because they can execute code.
2. For JavaScript and TypeScript, use the project's Knip version or an exact published version via `npx knip@<version>` (`npx.cmd` in Windows PowerShell). Record the version and run from the workspace root. Run once with the default scope and once with `--production`. If needed, pass a temporary JSON config with `--config`. Use targeted entry patterns and keep tests and development tools out of production scope. Use `--debug` to verify discovered entries and plugins. Keep reports and configuration outside tracked files. Omit autofix flags.
3. Resolve missing entry points and unresolved imports before treating results as candidates. Check symbol references, string searches, deployment and test consumers, and Git history. For dead blocks within reachable files, use existing ESLint or TypeScript diagnostics without fixes or emit. For other languages, use the existing compiler or linter and state the coverage. Age and zero test coverage are weak signals by themselves.
4. Report commands, versions, scope, and coverage gaps. Group findings as **removal candidate** when checks found no known consumer, **still used** when you can cite one, or **needs confirmation** when runtime callers, deployment usage, or older data could still depend on it. Include file locations and evidence. Keep deletion and verification in a separate authorized task.

See [Knip configuration](https://knip.dev/guides/configuring-project-files) and [production mode](https://knip.dev/features/production-mode).
