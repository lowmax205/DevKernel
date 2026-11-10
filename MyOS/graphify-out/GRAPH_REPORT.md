# Graph Report - MyOS  (2026-11-10)

## Corpus Check
- 34 files · ~15,676 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: (none) 4)

## Summary
- 230 nodes · 376 edges · 18 communities (12 shown, 6 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `207d4811`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- graph_recall.py
- test_project_docs.py
- agy_memory_hook.py
- check_portable_paths.py
- [DEV] 2026-11-10 - BrewedOps 3-Layer Architecture and System Diagrams
- install_devtools.ps1
- zentora_sync.py
- DevKernel Hub.md
- Singleton Pattern controls expensive lifecycle resources
- Starter-Project Hub.md
- setup_agent.ps1
- Adapter Pattern insulates domain models from external schemas
- Strategy Pattern isolates interchangeable calculation algorithms
- DevKernel Tracker
- DevKernel
- Starter-Project

## God Nodes (most connected - your core abstractions)
1. `reconcile_all()` - 16 edges
2. `run_federated_recall()` - 11 edges
3. `handle_hook()` - 9 edges
4. `sync_repo_starter_files()` - 9 edges
5. `search_and_walk()` - 8 edges
6. `detect_project_context()` - 8 edges
7. `main()` - 8 edges
8. `load_graph()` - 7 edges
9. `_detect_active_repo()` - 6 edges
10. `extract_keywords()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `onboard()` --calls--> `sync_repo_starter_files()`  [EXTRACTED]
  _meta/test_project_docs.py → _meta/zentora_sync.py
- `handle_hook()` --calls--> `extract_keywords()`  [EXTRACTED]
  _meta/agy_memory_hook.py → _meta/graph_recall.py
- `handle_hook()` --calls--> `run_federated_recall()`  [EXTRACTED]
  _meta/agy_memory_hook.py → _meta/graph_recall.py
- `sync_repo_starter_files()` --calls--> `scaffold()`  [EXTRACTED]
  _meta/zentora_sync.py → _meta/scaffold_project_docs.py

## Import Cycles
- None detected.

## Communities (18 total, 6 thin omitted)

### Community 0 - "graph_recall.py"
Cohesion: 0.18
Nodes (14): detect_project_context(), discover_repo_graphs(), extract_keywords(), _find_latest_project_session(), format_capsule(), load_graph(), main(), _node_location() (+6 more)

### Community 1 - "test_project_docs.py"
Cohesion: 0.13
Nodes (6): main(), scaffold(), DocumentationOnboardingTests, onboard(), check_links(), get_vault_stems_and_names()

### Community 2 - "agy_memory_hook.py"
Cohesion: 0.27
Nodes (9): _build_session_start_message(), _clean_user_input(), _detect_active_repo(), _extract_section_bullets(), _find_child_repo_by_name(), _find_child_repo_from_path(), _get_latest_session_summary(), handle_hook() (+1 more)

### Community 3 - "check_portable_paths.py"
Cohesion: 0.43
Nodes (3): main(), scan(), tracked_files()

### Community 4 - "[DEV] 2026-11-10 - BrewedOps 3-Layer Architecture and System Diagrams"
Cohesion: 0.29
Nodes (6): Decisions, [DEV] 2026-11-10 - BrewedOps 3-Layer Architecture and System Diagrams, Focus, Mistakes / Gotchas, What was built, Wins

### Community 5 - "install_devtools.ps1"
Cohesion: 0.80
Nodes (4): Act(), Install-OmniRoute(), Install-Ponytail(), Step()

### Community 6 - "zentora_sync.py"
Cohesion: 0.08
Nodes (19): audit_vault_integrity(), discover_projects(), generate_registry_table(), get_filesystem_snapshot(), get_post_commit_hook_script(), load_env_graphify(), load_state_manifest(), main() (+11 more)

### Community 49 - "DevKernel Hub.md"
Cohesion: 0.06
Nodes (25): Decisions, [DEV] 2026-10-27 - Multi-Agent Architecture and Knowledge Codification, Focus, What was built, Wins, Architecture & Key Decisions, Architecture Patterns, DevKernel Hub (+17 more)

### Community 92 - "Singleton Pattern controls expensive lifecycle resources"
Cohesion: 0.33
Nodes (5): Anti-Pattern Warning, Applied In, Problem Solved, Singleton Pattern controls expensive lifecycle resources, Zentora Standard

### Community 94 - "Starter-Project Hub.md"
Cohesion: 0.05
Nodes (30): Architecture & Key Decisions, Architecture Patterns, Overview, Session History, Starter-Project Hub, Applied In, Builder Pattern simplifies complex multi-field object construction, Problem Solved (+22 more)

### Community 102 - "Adapter Pattern insulates domain models from external schemas"
Cohesion: 0.40
Nodes (4): Adapter Pattern insulates domain models from external schemas, Applied In, Problem Solved, Zentora Standard

### Community 107 - "Strategy Pattern isolates interchangeable calculation algorithms"
Cohesion: 0.40
Nodes (4): Applied In, Problem Solved, Strategy Pattern isolates interchangeable calculation algorithms, Zentora Standard

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `reconcile_all()` connect `zentora_sync.py` to `graph_recall.py`, `check_portable_paths.py`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Should `test_project_docs.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13450292397660818 - nodes in this community are weakly interconnected._
- **Should `zentora_sync.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07536231884057971 - nodes in this community are weakly interconnected._
- **Should `DevKernel Hub.md` be split into smaller, more focused modules?**
  _Cohesion score 0.06439393939393939 - nodes in this community are weakly interconnected._
- **Should `Starter-Project Hub.md` be split into smaller, more focused modules?**
  _Cohesion score 0.05263157894736842 - nodes in this community are weakly interconnected._