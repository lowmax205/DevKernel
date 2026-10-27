---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/ai
  - topic/graphify
created: 2026-10-17
summary: Graphify uses 'graphify update <path>' for AST-only updates and 'graphify extract <path> --backend deepseek --output <root>' for LLM semantic extraction; '--update' is not a valid flag.
---
# Graphify CLI

Uses update and extract subcommands instead of an update flag

Running `graphify --update <path> --backend deepseek --output <dir>` fails with `error: unknown command '--update'`, forcing AI agents to waste tokens running `graphify --help` and retrying commands.

In Graphify (`graphifyy` v0.9.x+):
1. **AST-only code update (no LLM, no `--backend` or `--output` flags):**
   `graphify update "<ZENTORA_ROOT>"` (or `graphify update .` inside a repository).
2. **Full AST + Semantic LLM extraction (DeepSeek):**
   `graphify extract "<ZENTORA_ROOT>" --backend deepseek --output "<ZENTORA_ROOT>"`
   *(Note: `--output <DIR>` automatically writes into `<DIR>/graphify-out/`, so always pass the workspace root `"<ZENTORA_ROOT>"`, never `"<ZENTORA_ROOT>/graphify-out"`.)*

## Context & Connections
- Discovered during: [[[REN] 2026-10-17 - Auth Resilience and Android SDK]]
- Applied in: [[Starter-Project Hub]], [[DevKernel Hub]]
