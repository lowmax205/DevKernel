# ChatGPT CLI & OpenAI Codex Configuration — Zentora Dev

ChatGPT CLI, OpenAI Operator, and Codex environments natively read `AGENTS.md` at the root of the repository.

## Recommended CLI Launch Flags
When starting a session using ChatGPT CLI or OpenAI CLI tools in ZentoraDev:

```bash
# Point session context to root AGENTS.md
chatgpt --system "Follow all architectural invariants and routing rules defined in ./AGENTS.md."
```

## System Protocol Invariants
- Enforce "One Home Per Fact" (Live status in `MyOS/projects/<slug>.md`, Session notes in `MyOS/ObsidianVault/10 - Projects/<Name>/`).
- Recall knowledge via `python MyOS/_meta/graph_recall.py "<query>" --hops 2`.
- Apply the Two-Tier Simplicity Gate for backend services (Tier 1 CRUD: Repo + Service; Tier 2: Strategy, Adapter, Observer, Circuit Breaker).
- Enforce Windows PowerShell 5.1 guardrails (no bash `&&` or `||`).
