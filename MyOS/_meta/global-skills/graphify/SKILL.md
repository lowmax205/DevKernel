---
name: graphify
description: Fast AST code indexing, semantic knowledge graph extraction, and graph recall for repositories across Zentora Dev.
---

# Graphify Knowledge Graph & AST Skill

Use this skill when mapping codebases, indexing dependencies, extracting semantic knowledge graphs, querying architectural relationships, or running `/graphify`.

## Exact Graphify CLI Syntax (Zero-Token-Waste Rule)

> [!CAUTION]
> **NEVER run `graphify --update`!**
> `update` and `extract` are **subcommands**, NOT flags.
> - Never run `graphify --update` (causes `error: unknown command '--update'`).
> - Never pass `--backend` or `--output` to `graphify update`.
> - Never pass `.../graphify-out` to `--output` in `graphify extract` (`--output <DIR>` automatically creates `/graphify-out/`).

---

## 1. Fast Code AST Re-Index (Zero LLM Tokens / No API Key)

Use this for immediate code structure updates, file relationship graphs, and AST indexing:

- **Inside any Child Repository (with `scripts/graphify.ps1`):**
  ```powershell
  .\scripts\graphify.ps1 update
  ```
- **In MyOS or Root Workspace:**
  ```powershell
  graphify update "<ZENTORA_ROOT>/MyOS"
  ```
  *(Accepts ONLY optional `[--force]` and `[--no-cluster]`)*

---

## 2. Graph Recall & Querying (Token-Free English Traversal)

Before modifying complex cross-module code or answering architectural questions:

- **Repo-Local Query:**
  ```powershell
  .\scripts\graphify.ps1 query "<natural language query>"
  ```
- **Global Cross-Project Graph Recall (1-to-2 Hop Traversal):**
  ```powershell
  python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<english keywords>" --hops 2
  ```

---

## 3. Full Semantic Extraction with DeepSeek (Major Milestones Only)

Use this ONLY when instructed (`save progress --deep` or major releases) to build rich semantic nodes and summaries:

```powershell
graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"
```
*Requires `DEEPSEEK_API_KEY` set in `<ZENTORA_ROOT>/MyOS/.env.graphify` or environment variables.*

---

## 4. Child Repositories Architecture

Every child repository contains:
- `scripts/graphify.ps1`: The local runner for fast AST updates and local queries.
- `.graphifyignore`: Excludes heavy directories (`node_modules`, `dist`, `.next`, `build`, `coverage`, `.venv`).
- `graphify-out/`: The local AST knowledge graph (`graph.json`, `graph.html`).
- Central synchronization: Running `.\scripts\graphify.ps1 -SyncToMyOS` or `python MyOS/_meta/zentora_sync.py --once` links repo updates back into the master knowledge graph.

