#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
graph_recall.py - Federated High-Efficiency Context Capsule Generator for Zentora Dev.
Zero-LLM token, pure Python AST 1-to-2 hop traversal over Graphify's graph.json
across both MyOS (Obsidian Vault memory + Atomic Insights) and child repositories (code AST).
Emits a structured Context Capsule for pair-programming agents and lifecycle hooks.
"""

import argparse
import json
import os
import re
import sys
from collections import deque
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set

ENGLISH_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can", "can't", "cannot", "could",
    "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
    "during", "each", "few", "for", "from", "further", "had", "hadn't", "has",
    "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her",
    "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's",
    "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it",
    "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't",
    "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
    "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
    "they've", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
    "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
    "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves", "status", "current", "project", "code", "file",
    "please", "make", "sure", "use", "using", "check", "find", "search", "look",
    "fix", "update", "add", "create", "delete", "remove", "run", "test", "yes", "no"
}

GENERIC_MD_HEADINGS = {
    "decisions", "focus", "mistakes", "what was built", "wins", "overview",
    "session history", "architecture & key decisions", "context & connections",
    "problem solved", "applied in", "zentora standard", "home", "architecture",
    "notes", "summary", "next steps"
}

SCRIPT_DIR = Path(__file__).resolve().parent
MYOS_DIR = SCRIPT_DIR.parent
ZENTORA_ROOT = Path(os.environ.get("ZENTORA_ROOT") or SCRIPT_DIR.parents[1]).resolve()
DEFAULT_GRAPH_PATH = MYOS_DIR / "graphify-out" / "graph.json"
PROJECTS_DIR = MYOS_DIR / "projects"
REPOS_DIR = ZENTORA_ROOT / "Repos"


def tokenize_identifier(text: str) -> Set[str]:
    """Split camelCase, PascalCase, snake_case, and path segments into lowercase tokens."""
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    return set(re.findall(r"[a-z0-9]{2,}", spaced.lower()))


def extract_keywords(query: str) -> List[str]:
    raw_words = re.findall(r"[a-zA-Z0-9_-]+", query)
    expanded: List[str] = []
    seen: Set[str] = set()
    for rw in raw_words:
        low = rw.lower()
        if len(low) >= 2 and low not in ENGLISH_STOPWORDS and low not in seen:
            expanded.append(low)
            seen.add(low)
        camel_parts = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", rw).lower().split()
        for cp in camel_parts:
            for sub in re.split(r"[_-]+", cp):
                if len(sub) >= 3 and sub not in ENGLISH_STOPWORDS and sub not in seen:
                    expanded.append(sub)
                    seen.add(sub)
    return expanded


def _node_source_file(node: Dict[str, Any]) -> str:
    return str(node.get("source_file") or node.get("path") or node.get("file") or "").replace("\\", "/")


def _node_location(node: Dict[str, Any]) -> str:
    return str(node.get("source_location") or node.get("location") or "")


def load_graph(graph_path: Path, required: bool = False) -> Optional[Dict[str, Any]]:
    if not graph_path.exists():
        if required:
            print(f"[graphify capsule] Graph not found at {graph_path}. Graphify is optional; generate a graph or pass --graph explicitly.", file=sys.stderr)
            sys.exit(1)
        return None
    try:
        with open(graph_path, "r", encoding="utf-8", errors="replace") as f:
            return json.load(f)
    except Exception:
        if required:
            print(f"[graphify capsule] Graph not found at {graph_path}. Graphify is optional; generate a graph or pass --graph explicitly.", file=sys.stderr)
            sys.exit(1)
        return None


def discover_repo_graphs(target_repo: Optional[Path] = None, keywords: Optional[List[str]] = None) -> List[Tuple[str, Path]]:
    """
    Return list of (repo_name, graph_json_path) to search for code AST nodes.
    If target_repo is given (or CWD is inside a child repo), prioritize that repo.
    Otherwise, check if keywords mention a specific repo, or search all available child repo graphs.
    """
    if target_repo:
        cand = target_repo / "graphify-out" / "graph.json"
        if cand.exists():
            return [(target_repo.name, cand)]

    try:
        cwd = Path.cwd().resolve()
        for parent in [cwd] + list(cwd.parents):
            if (parent / "graphify-out" / "graph.json").exists() and parent != MYOS_DIR and parent != ZENTORA_ROOT:
                return [(parent.name, parent / "graphify-out" / "graph.json")]
    except Exception:
        pass

    all_repo_graphs: List[Tuple[str, Path]] = []
    if REPOS_DIR.exists():
        for level1 in sorted(REPOS_DIR.iterdir()):
            if not level1.is_dir() or level1.name.lower() in {"node_modules", ".git", "devkernel"}:
                continue
            g1 = level1 / "graphify-out" / "graph.json"
            if g1.exists():
                all_repo_graphs.append((level1.name, g1))
            else:
                for level2 in sorted(level1.iterdir()):
                    if not level2.is_dir() or level2.name.lower() in {"node_modules", ".git", "devkernel"}:
                        continue
                    g2 = level2 / "graphify-out" / "graph.json"
                    if g2.exists():
                        all_repo_graphs.append((level2.name, g2))

    if keywords and all_repo_graphs:
        kw_set = set(keywords)
        matched_repos = []
        for r_name, g_path in all_repo_graphs:
            slug_parts = set(re.findall(r"[a-z0-9]+", r_name.lower()))
            if r_name.lower() in kw_set or (slug_parts and slug_parts.intersection(kw_set)):
                matched_repos.append((r_name, g_path))
        if matched_repos:
            return matched_repos

    return all_repo_graphs


def search_and_walk(
    graph: Dict[str, Any],
    keywords: List[str],
    max_hops: int = 2,
    max_results: int = 12,
    repo_prefix: str = "",
    exclude_meta_code: bool = False
) -> List[Dict[str, Any]]:
    nodes = graph.get("nodes", [])
    links = graph.get("links", graph.get("edges", []))

    node_map = {str(n.get("id", "")): n for n in nodes if n.get("id")}
    adj: Dict[str, List[Any]] = {nid: [] for nid in node_map}

    for link in links:
        src, tgt = str(link.get("source", "")), str(link.get("target", ""))
        rel = link.get("relation", link.get("label", "related_to"))
        conf = link.get("confidence", "EXTRACTED")
        if src in adj and tgt in node_map:
            adj[src].append((tgt, rel, conf))
        if tgt in adj and src in node_map:
            adj[tgt].append((src, rel, conf))

    seed_scores: Dict[str, float] = {}
    for nid, n in node_map.items():
        label = str(n.get("label") or n.get("title") or "").strip()
        if label.lower() in GENERIC_MD_HEADINGS:
            continue
        sf = _node_source_file(n)
        if exclude_meta_code and sf.startswith("_meta/"):
            continue
        comm = str(n.get("community_name") or "")
        summary = str(n.get("summary") or "")
        norm_label = str(n.get("norm_label") or label).lower().rstrip("()")

        label_tokens = tokenize_identifier(label)
        sf_tokens = tokenize_identifier(sf)
        all_tokens = label_tokens | sf_tokens | tokenize_identifier(comm) | tokenize_identifier(summary)
        text_all = f"{nid} {label} {sf} {comm} {summary}".lower()

        score = 0.0
        for kw in keywords:
            if kw == norm_label or kw == label.lower().rstrip("()"):
                score += 5.0
            elif kw in label_tokens:
                score += 3.5
            elif len(kw) >= 4 and kw in label.lower():
                score += 2.5
            elif kw in sf_tokens:
                score += 2.0
            elif len(kw) >= 4 and kw in sf.lower():
                score += 1.5
            elif kw in all_tokens or (len(kw) >= 5 and kw in text_all):
                score += 1.0
        if score > 0:
            seed_scores[nid] = score

    sorted_seeds = sorted(seed_scores.keys(), key=lambda k: seed_scores[k], reverse=True)[:6]

    visited: Dict[str, Tuple[int, str, str, float]] = {}
    queue = deque()
    for seed in sorted_seeds:
        visited[seed] = (0, "seed match", "EXTRACTED", seed_scores[seed])
        queue.append((seed, 0, seed_scores[seed]))

    while queue:
        curr, hop, parent_score = queue.popleft()
        if hop >= max_hops:
            continue
        for neighbor, rel, conf in adj.get(curr, []):
            nb_node = node_map.get(neighbor, {})
            nb_label = str(nb_node.get("label") or "").strip().lower()
            nb_sf = _node_source_file(nb_node)
            if nb_label in GENERIC_MD_HEADINGS:
                continue
            if exclude_meta_code and nb_sf.startswith("_meta/"):
                continue
            if neighbor not in visited:
                visited[neighbor] = (hop + 1, rel, conf, parent_score * 0.5)
                queue.append((neighbor, hop + 1, parent_score * 0.5))

    results = []
    for nid, (hop, rel, conf, score) in visited.items():
        node = node_map[nid]
        sf = _node_source_file(node)
        if repo_prefix and sf and not sf.startswith(repo_prefix):
            sf_display = f"{repo_prefix}/{sf}"
        else:
            sf_display = sf
        results.append({
            "id": nid,
            "label": node.get("label") or node.get("title") or nid,
            "path": sf_display,
            "raw_path": sf,
            "location": _node_location(node),
            "community": str(node.get("community_name") or ""),
            "file_type": str(node.get("file_type") or ""),
            "summary": node.get("summary") or "",
            "hop": hop,
            "relation": rel,
            "confidence": conf,
            "score": score,
            "repo": repo_prefix,
            "is_repo_code": bool(repo_prefix or node.get("file_type") == "code"),
        })

    results.sort(key=lambda x: (x["hop"], -x["score"], 0 if x["confidence"] == "EXTRACTED" else 1))
    return results[:max_results]


def read_project_card_info(slug_or_name: str) -> Optional[Dict[str, str]]:
    """Read status and next step from MyOS/projects/<slug>.md."""
    if not PROJECTS_DIR.exists():
        return None
    target_norm = re.sub(r"[^a-z0-9]+", "-", slug_or_name.lower()).strip("-")
    for card in PROJECTS_DIR.glob("*.md"):
        card_norm = re.sub(r"[^a-z0-9]+", "-", card.stem.lower()).strip("-")
        if card_norm == target_norm or card_norm in target_norm or target_norm in card_norm:
            try:
                text = card.read_text(encoding="utf-8", errors="replace")
                status = "active"
                next_task = "Continue planned work"
                m_stat = re.search(r"^status:\s*([A-Za-z0-9_-]+)", text, re.MULTILINE)
                m_next = re.search(r"^next:\s*(.+)$", text, re.MULTILINE)
                if m_stat:
                    status = m_stat.group(1).strip()
                if m_next:
                    next_task = m_next.group(1).strip()
                return {"name": card.stem, "status": status, "next": next_task}
            except Exception:
                pass
    return None


def detect_project_context(
    results: List[Dict[str, Any]],
    keywords: List[str],
    target_repo: Optional[Path] = None
) -> Optional[Dict[str, str]]:
    """Infer active project context from target_repo, CWD, query keywords, or matched node paths."""
    if target_repo:
        info = read_project_card_info(target_repo.name)
        if info:
            return info

    try:
        cwd = Path.cwd().resolve()
        for parent in [cwd] + list(cwd.parents):
            if parent.parent == REPOS_DIR or parent.parent.parent == REPOS_DIR:
                info = read_project_card_info(parent.name)
                if info:
                    return info
    except Exception:
        pass

    for kw in keywords:
        if len(kw) >= 4:
            info = read_project_card_info(kw)
            if info:
                return info

    for r in results:
        p = (r.get("path", "") + " " + r.get("repo", "")).lower()
        if PROJECTS_DIR.exists():
            for card in PROJECTS_DIR.glob("*.md"):
                slug = card.stem.lower()
                if slug in p:
                    info = read_project_card_info(slug)
                    if info:
                        return info
    return None


def format_capsule(
    query: str,
    keywords: List[str],
    results: List[Dict[str, Any]],
    proj_ctx: Optional[Dict[str, str]]
) -> str:
    lines = [
        f'# [ZENTORA CONTEXT CAPSULE] Query: "{query}"',
        f"- Keywords: `{', '.join(keywords[:10])}`"
    ]
    if proj_ctx:
        lines.append(f"- Active Project: `{proj_ctx['name']}` | Status: `{proj_ctx['status']}` | Next: {proj_ctx['next']}")
    else:
        lines.append("- Active Project: `Meta-System` (Workspace Wide)")

    atomic_insights: List[Tuple[str, str, str]] = []
    sessions: List[Tuple[str, str]] = []
    code_nodes: List[Dict[str, Any]] = []
    seen_labels: Set[str] = set()

    for r in results:
        path = r.get("path", "")
        label = str(r.get("label", "")).strip()
        summary = str(r.get("summary", "")).strip()
        dedup_key = f"{label.lower()}::{path.lower()}"
        if dedup_key in seen_labels:
            continue
        seen_labels.add(dedup_key)

        if "Atomic Insights" in path or "Zettelkasten" in path:
            clean_lbl = label[:-3] if label.endswith(".md") else label
            atomic_insights.append((clean_lbl, path, summary))
        elif "10 - Projects" in path or "Session" in label or "Hub" in label or re.search(r"\d{4}-\d{2}-\d{2}", label):
            clean_lbl = label[:-3] if label.endswith(".md") else label
            sessions.append((clean_lbl, path))
        elif path.startswith("projects/") or path.startswith("dashboards/"):
            continue
        else:
            code_nodes.append(r)

    if atomic_insights:
        lines.append("\n## 1. Atomic Insights (Gotchas & Architecture Rules)")
        for lbl, p, summ in atomic_insights[:4]:
            summ_str = f" - {summ}" if summ else f" (`{p}`)"
            lines.append(f"- [[{lbl}]]{summ_str}")

    if sessions:
        lines.append("\n## 2. Connected Session & Hub Context")
        for lbl, p in sessions[:4]:
            lines.append(f"- [[{lbl}]] (`{p}`)")

    if code_nodes:
        lines.append("\n## 3. AST & Code Symbol Hops (<350 toks)")
        for r in code_nodes[:8]:
            lbl = r["label"]
            p = r["path"]
            loc = r.get("location", "")
            comm = r.get("community", "")
            hop = r["hop"]
            rel = r["relation"]
            conf = r["confidence"]
            loc_suffix = f":{loc}" if loc else ""
            comm_suffix = f" [module: {comm}]" if comm else ""
            path_str = f" (`{p}{loc_suffix}`){comm_suffix}" if p else ""
            hop_str = "seed" if hop == 0 else f"{hop}-hop via {rel} [{conf}]"
            lines.append(f"- `{lbl}`{path_str} -> {hop_str}")

    return "\n".join(lines)


def run_federated_recall(
    query: str,
    graph_override: Optional[Path] = None,
    repo_override: Optional[Path] = None,
    max_hops: int = 2,
    max_results: int = 12
) -> str:
    keywords = extract_keywords(query)
    if not keywords:
        return f"[graphify capsule] No significant keywords found in '{query}'."

    combined_results: List[Dict[str, Any]] = []

    is_meta_query = any(k in {"zentora", "myos", "graphify", "sync", "bootstrap", "hook", "recall"} for k in keywords)

    # 1. Search central MyOS knowledge graph (Vault notes, Session logs, Atomic Insights)
    myos_graph_path = graph_override if graph_override else DEFAULT_GRAPH_PATH
    repo_graphs = [] if graph_override else discover_repo_graphs(target_repo=repo_override, keywords=keywords)
    require_central_graph = bool(graph_override or (not repo_graphs and not DEFAULT_GRAPH_PATH.exists()))
    myos_graph = load_graph(myos_graph_path, required=require_central_graph)
    if myos_graph:
        combined_results.extend(
            search_and_walk(
                myos_graph,
                keywords,
                max_hops=max_hops,
                max_results=max_results,
                exclude_meta_code=bool(repo_override and not is_meta_query)
            )
        )

    # 2. Search child repository AST graphs unless caller explicitly locked --graph to a single non-MyOS file
    if not graph_override or graph_override.resolve() == DEFAULT_GRAPH_PATH.resolve():
        repo_graphs = discover_repo_graphs(target_repo=repo_override, keywords=keywords)
        per_repo_limit = max_results if len(repo_graphs) <= 2 else 4
        code_matches: List[Dict[str, Any]] = []
        for repo_name, rg_path in repo_graphs:
            rg = load_graph(rg_path)
            if rg:
                prefix = "" if repo_override else repo_name
                code_matches.extend(
                    search_and_walk(rg, keywords, max_hops=max_hops, max_results=per_repo_limit, repo_prefix=prefix)
                )
        code_matches.sort(key=lambda x: (x["hop"], -x["score"], 0 if x["confidence"] == "EXTRACTED" else 1))
        # Prepend repo code matches so Section 3 prioritizes target repository symbols
        combined_results = code_matches[:max_results] + combined_results

    if not combined_results:
        return f"[graphify capsule] Zero graph matches for keywords: {', '.join(keywords)}"

    proj_ctx = detect_project_context(combined_results, keywords, target_repo=repo_override)
    return format_capsule(query, keywords, combined_results, proj_ctx)


def main():
    parser = argparse.ArgumentParser(description="Zentora Dev Federated Context Capsule Generator")
    parser.add_argument("query", type=str, help="Search query in English")
    parser.add_argument("--graph", type=str, default=None, help="Optional explicit path to graph.json")
    parser.add_argument("--repo", type=str, default=None, help="Optional path to active child repository")
    parser.add_argument("--hops", type=int, default=2, help="Max hops to traverse (default: 2)")
    parser.add_argument("--limit", type=int, default=12, help="Max results per layer to return")
    args = parser.parse_args()

    graph_path = Path(args.graph).resolve() if args.graph else None
    repo_path = Path(args.repo).resolve() if args.repo else None

    capsule = run_federated_recall(
        args.query,
        graph_override=graph_path,
        repo_override=repo_path,
        max_hops=args.hops,
        max_results=args.limit
    )
    print(capsule)


if __name__ == "__main__":
    main()
