---
name: surgical-coding
description: Behavioral guidelines to eliminate common LLM coding pitfalls, derived from Andrej Karpathy's principles. Enforces thinking before coding, minimum speculative code, surgical modifications without collateral damage, and verifiable goal-driven execution loops.
license: MIT
---

# Surgical Coding (Karpathy Guidelines)

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on AI coding pitfalls.

**Tradeoff:** These guidelines bias toward caution, precision, and verification over speed. For trivial tasks, use pragmatic judgment.

---

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- **State assumptions explicitly**: If uncertain about requirements, contracts, or side effects, ask before coding.
- **Surface alternatives**: If multiple valid implementations or interpretations exist, present them clearly; do not pick one silently.
- **Push back when warranted**: If a simpler, more direct approach exists, explain why. Do not blindly adopt over-engineered proposals.
- **Stop on confusion**: If a codebase pattern, legacy structure, or requirement is unclear, stop immediately. Name the confusion and ask.

---

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- **No unrequested features**: Solve exactly what was requested; do not anticipate unasked requirements.
- **No speculative abstractions**: Never build generic frameworks, wrapper classes, or factory patterns for single-use code. Follow Zentora's Two-Tier Simplicity Gate.
- **No speculative configurability**: Avoid adding environment variables, configuration flags, or options that were not requested.
- **No defensive code for impossible scenarios**: Avoid wrapping well-defined local operations in layers of paranoid exception handling.
- **Conciseness rule**: If you write 200 lines and it could be cleanly expressed in 50 lines, rewrite and simplify.

*Self-check:* "Would a staff engineer say this is overcomplicated?" If yes, simplify.

---

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When modifying existing code:
- **Zero collateral damage**: Never touch or "reformat" adjacent code, unrelated comments, or preexisting formatting.
- **Preserve working logic**: Do not refactor code that is not broken or directly relevant to the current task.
- **Match existing conventions**: Adhere strictly to the repository's surrounding style, even if you would personally format it differently.
- **Do not delete unrelated dead code**: If you notice preexisting dead code, report it to the user; do not delete it unilaterally.
- **Clean up your own orphans**: Remove imports, variables, functions, or dependencies that your changes have made unused.

*The litmus test:* Every single changed line in your diff must trace directly to the user's request.

---

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform every task into verifiable, measurable criteria before coding:
- **Bug fixing**: Write or identify a reproduction check/test first, verify failure, make changes, verify success.
- **Feature implementation**: Establish the exact verification commands (`test`, `build`, `lint`) before claiming completion.
- **Refactoring**: Ensure all automated checks pass identically before and after changes.

For multi-step workflows, formulate a concise verification plan:
```
1. [Step A] -> verify: [command / test / evidence]
2. [Step B] -> verify: [command / test / evidence]
3. [Step C] -> verify: [command / test / evidence]
```

Pass through the mandatory **`verification-before-completion`** gate (`lint` and `build` exit code `0`) before marking any task complete or committing code.

---

<!-- ponytail:begin -->
## Ponytail Integration (managed by install_devtools.ps1 - do not edit)

Ponytail (skill `ponytail`, pinned upstream 96608e0) decides **how much** to write; this skill decides **how** to edit.
Before writing code, take the first option that fully works:
1. Skip it if nobody asked for it (name what you skipped in one line).
2. Reuse what already exists in the codebase.
3. Use the standard library or a platform feature.
4. Use an already-installed dependency (never add one for a few lines).
5. Otherwise write the minimum code that works.

Never cut validation, error handling, security, or accessibility. On conflict: Ponytail wins on size, surgical-coding wins on scope of edits.
<!-- ponytail:end -->
