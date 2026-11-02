---
name: graphify
description: Fast AST code indexing, semantic knowledge graph extraction, and graph recall for repositories across Zentora Dev.
---

# Graphify Knowledge Graph & AST Skill

Use this skill when searching for files/functions, mapping codebases, indexing dependencies, extracting semantic knowledge graphs, querying architectural relationships, or running `/graphify`.

## Exact Graphify CLI Syntax (Zero-Token-Waste Rule)

> [!CAUTION]
> **NEVER run `graphify --update`!**
> `update` and `extract` are **subcommands**, NOT flags.
> - Never run `graphify --update` (causes `error: unknown command '--update'`).
> - Never pass `--backend` or `--output` to `graphify update`.
> - Never pass `.../graphify-out` to `--output` in `graphify extract` (`--output <DIR>` automatically creates `/graphify-out/`).

---

## 1. Automatic Lifecycle Hook & Native MCP Server

1. **Antigravity Lifecycle Hook (`.agents/hooks.json` -> `MyOS/_meta/agy_memory_hook.py`):**
   - `SessionStart`: Automatically injects the active project's ICM Card (`MyOS/projects/<slug>.md`) and latest Obsidian Session summary.
   - `PreInvocation`: Automatically injects a transient `[ZENTORA CONTEXT CAPSULE]` matching `lastUserInput` across both `MyOS` Vault memory and the active repo's AST `graphify-out/graph.json`.
2. **Native `graphify` MCP Server (`python -m graphify.serve`):**
   - Exposes `query_graph`, `get_node`, `get_neighbors`, `get_community`, `god_nodes`, `graph_stats`, and `shortest_path`.
   - Always pass `project_path: "<ZENTORA_ROOT>/Repos/2026/<RepoName>"` when querying a specific child repository's `graphify-out/graph.json`.

---

## 2. Fast Code AST Re-Index (Zero LLM Tokens / No API Key)

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

## 3. Federated Graph Recall & Querying (Token-Free English Traversal)

Before searching for files/functions, modifying cross-module code, or answering architectural questions:

- **Repo-Local Federated Query (Vault + Repo AST):**
  ```powershell
  .\scripts\graphify.ps1 query "<natural language query>"
  ```
- **Direct Federated Recall Script (1-to-2 Hop Traversal across MyOS + Repo AST):**
  ```powershell
  python "<ZENTORA_ROOT>/MyOS/_meta/graph_recall.py" "<english keywords>" --repo "<RepoPath>" --hops 2
  ```

---

## 4. Full Semantic Extraction with DeepSeek (Major Milestones Only)

Use this ONLY when instructed (`save progress --deep` or major releases) to build rich semantic nodes and summaries:

```powershell
graphify extract "<ZENTORA_ROOT>/MyOS" --backend deepseek --output "<ZENTORA_ROOT>/MyOS"
```
*Requires `DEEPSEEK_API_KEY` set in `<ZENTORA_ROOT>/MyOS/.env.graphify` or environment variables.*

---

## 5. Child Repositories Architecture

Every child repository contains:
- `.agents/hooks.json`: Automatic `SessionStart` + `PreInvocation` memory & graph capsule injector.
- `scripts/graphify.ps1`: The local runner for fast AST updates and federated queries.
- `.graphifyignore`: Excludes heavy directories (`node_modules`, `dist`, `.next`, `build`, `coverage`, `.venv`).
- `graphify-out/`: The local AST knowledge graph (`graph.json`, `graph.html`, `GRAPH_REPORT.md`).
