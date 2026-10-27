---
name: verification-before-completion
description: "Mandatory evidence gate before claiming work is complete, committing, or finishing a task. Requires running fresh lint, build, and test verification commands with exit code 0."
---

# Verification Before Completion (The Iron Law)

```text
NO COMPLETION CLAIMS OR COMMITS WITHOUT FRESH VERIFICATION EVIDENCE
```

Claiming work is complete without running verification in the current turn is dishonesty, not efficiency.

---

## 1. The 5-Step Gate Function

Before claiming any task is complete, expressing satisfaction ("Done!", "Fixed!", "All set!"), or invoking `/git-commit`:

1. **IDENTIFY**: Which lint, typecheck, build, and test commands prove this change works?
2. **RUN**: Execute the full commands in PowerShell using the proper `Cwd` / `working_directory` (never chain with bash `&&`).
3. **READ**: Inspect the complete output, exit code (`$LASTEXITCODE`), and warning/error counts.
4. **VERIFY**:
   - Did `lint:fix` / `lint`, `build`, and affected tests exit `0`?
   - If **NO**: Fix the root cause and re-run before claiming completion.
   - If **YES**: Report the result with concrete command evidence.
5. **CLAIM**: Only state completion after Step 4 passes.

---

## 2. Standard Repository Quality Gates

| Repository Type | Mandatory Verification Sequence |
| :--- | :--- |
| **Full-Stack / Monorepo (`frontend`, `backend`, `apps/*`, `packages/*`)** | Run `npm run lint:fix` (or `pnpm lint`) followed by `npm run build` (and `test:unit` / `test:smoke`) in every modified package. |
| **Database / Schema Changes (`Prisma` / `Drizzle`)** | Verify migration generation, migration application against local/shadow DB, and schema build compilation (`exit 0`). |
| **Scripts / Rules / Docs Only** | Verify file paths, JSON/YAML syntax, and run any affected PowerShell/Python scripts in `-DryRun` or `--help` mode. |

---

## 3. Prohibited Rationalizations

| Forbidden Excuse | Required Action |
| :--- | :--- |
| *"Should pass now" / "Looks right"* | Execute the test/build command and verify `exit 0`. |
| *"Linter passed, so build is fine"* | Linter does not check full TypeScript/bundler compilation; run `build`. |
| *"Subagent said it succeeded"* | Check `git status` / `git diff` and run verification independently. |
| *"Just a small one-line change"* | No exceptions; run the verification gate. |
