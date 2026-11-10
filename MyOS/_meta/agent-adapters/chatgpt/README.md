# ChatGPT CLI & OpenAI Codex Configuration — DevKernel

ChatGPT CLI, OpenAI Operator, and Codex environments natively read `AGENTS.md` at the root of the repository.

## Recommended CLI Launch Flags
When starting a session using ChatGPT CLI or OpenAI CLI tools in DevKernel:

```bash
# Point session context to root AGENTS.md
chatgpt --system "Follow all architectural invariants and the 4-step surgical lookup defined in ./AGENTS.md."
```

## 4-Step Surgical Lookup
1. Read `AGENTS.md` to orient project routing and invariants.
2. Read `MyOS/projects/<slug>.md` for live `status:` and immediate `next:`.
3. Read `MyOS/ObsidianVault/10 - Projects/<Name>/` for Hub and latest session decisions/mistakes.
4. Recall dynamic context via `python MyOS/_meta/graph_recall.py "<query>" --hops 2` to read only the ~4 to 5 relevant files per prompt.

## System Protocol Invariants
- Enforce "One Home Per Fact" (Live status in `MyOS/projects/<slug>.md`, Session notes in `MyOS/ObsidianVault/10 - Projects/<Name>/`).
- Consult `.docs/RULES.md` on-demand for Two-Tier Simplicity Gate (Tier 1 CRUD: Repo + Service; Tier 2: Strategy, Adapter, Observer, Circuit Breaker).
- Enforce Windows PowerShell 5.1 guardrails (no bash `&&` or `||`).
- Save files as UTF-8 without BOM with ASCII punctuation.
