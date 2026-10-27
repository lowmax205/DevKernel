#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
graph_recall.py - High-Efficiency Context Capsule Generator for Zentora Dev.
Zero-LLM token, pure Python AST 1-to-2 hop traversal over Graphify's graph.json.
Emits a structured <350 token Context Capsule for pair-programming agents.
"""

import argparse
import json
import os
import re
import sys
from collections import deque
from pathlib import Path
from typing import Dict, List, Any, Optional

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
    "yourself", "yourselves", "status", "current", "project", "code", "file"
}

SCRIPT_DIR = Path(__file__).resolve().parent
MYOS_DIR = SCRIPT_DIR.parent
ZENTORA_ROOT = Path(os.environ.get("ZENTORA_ROOT") or SCRIPT_DIR.parents[1]).resolve()
DEFAULT_GRAPH_PATH = MYOS_DIR / "graphify-out" / "graph.json"
PROJECTS_DIR = MYOS_DIR / "projects"


def extract_keywords(query: str) -> List[str]:
    words = re.findall(r"[a-zA-Z0-9_-]+", query.lower())
    return [w for w in words if len(w) > 2 and w not in ENGLISH_STOPWORDS]


def load_graph(graph_path: Path) -> Dict[str, Any]:
    if not graph_path.exists():
        # Fallback to relative search
        alt = ZENTORA_ROOT / "MyOS" / "graphify-out" / "graph.json"
        if alt.exists():
            graph_path = alt
        else:
            print(f"[graphify capsule] Error: Graph file not found at: {graph_path}", file=sys.stderr)
            sys.exit(1)
    with open(graph_path, "r", encoding="utf-8", errors="replace") as f:
        return json.load(f)


def search_and_walk(graph: Dict[str, Any], keywords: List[str], max_hops: int = 2, max_results: int = 10) -> List[Dict[str, Any]]:
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

    seed_scores = {}
    for nid, n in node_map.items():
        text = " ".join([
            str(n.get("id", "")), str(n.get("label", "")),
            str(n.get("title", "")), str(n.get("summary", "")), str(n.get("path", ""))
        ]).lower()
        hits = sum(1 for kw in keywords if kw in text)
        if hits > 0:
            seed_scores[nid] = hits

    sorted_seeds = sorted(seed_scores.keys(), key=lambda k: seed_scores[k], reverse=True)[:5]

    visited = {}
    queue = deque()
    for seed in sorted_seeds:
        visited[seed] = (0, "seed match", "EXTRACTED")
        queue.append((seed, 0))

    while queue:
        curr, hop = queue.popleft()
        if hop >= max_hops:
            continue
        for neighbor, rel, conf in adj.get(curr, []):
            if neighbor not in visited:
                visited[neighbor] = (hop + 1, rel, conf)
                queue.append((neighbor, hop + 1))

    results = []
    for nid, (hop, rel, conf) in visited.items():
        node = node_map[nid]
        results.append({
            "id": nid,
            "label": node.get("label") or node.get("title") or nid,
            "path": node.get("path") or node.get("file") or "",
            "summary": node.get("summary") or "",
            "hop": hop,
            "relation": rel,
            "confidence": conf
        })

    # Prioritize EXTRACTED over INFERRED, then sort by hop
    results.sort(key=lambda x: (x["hop"], 0 if x["confidence"] == "EXTRACTED" else 1))
    return results[:max_results]


def detect_project_context(results: List[Dict[str, Any]]) -> Optional[Dict[str, str]]:
    """Infer active project context from matched node paths or cards."""
    for r in results:
        p = r.get("path", "").lower()
        for card in PROJECTS_DIR.glob("*.md"):
            slug = card.stem.lower()
            if slug in p:
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


def format_capsule(query: str, keywords: List[str], results: List[Dict[str, Any]], proj_ctx: Optional[Dict[str, str]]) -> str:
    lines = [
        f'# [ZENTORA CONTEXT CAPSULE] Query: "{query}"',
        f"- Keywords: `{', '.join(keywords)}`"
    ]
    if proj_ctx:
        lines.append(f"- Active Project: `{proj_ctx['name']}` | Status: `{proj_ctx['status']}` | Next: {proj_ctx['next']}")
    else:
        lines.append("- Active Project: `Meta-System` (Workspace Wide)")

    atomic_insights = []
    sessions = []
    nodes = []

    for r in results:
        path = r.get("path", "")
        label = r.get("label", "")
        summary = r.get("summary", "")
        if "Atomic Insights" in path or "Zettelkasten" in path:
            atomic_insights.append((label, path, summary))
        elif "[" in label and "]" in label and ("Session" in label or re.search(r"\d{4}-\d{2}-\d{2}", label)):
            sessions.append((label, path))
        elif "Session" in label or "Session" in path:
            sessions.append((label, path))
        else:
            nodes.append((label, path, r["hop"], r["relation"], r["confidence"]))

    if atomic_insights:
        lines.append("\n## 1. Atomic Insights (Gotchas & Architecture Rules)")
        for lbl, p, summ in atomic_insights[:3]:
            summ_str = f" - {summ}" if summ else ""
            lines.append(f"- [[{lbl}]]{summ_str}")

    if sessions:
        lines.append("\n## 2. Connected Session Context")
        for lbl, p in sessions[:3]:
            lines.append(f"- [[{lbl}]]")

    if nodes:
        lines.append("\n## 3. AST & Code Symbol Hops (<350 toks)")
        for lbl, p, hop, rel, conf in nodes[:5]:
            path_str = f" ({p})" if p else ""
            hop_str = "seed" if hop == 0 else f"{hop}-hop via {rel} [{conf}]"
            lines.append(f"- `{lbl}`{path_str} -> {hop_str}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Zentora Dev High-Efficiency Context Capsule Generator")
    parser.add_argument("query", type=str, help="Search query in English")
    parser.add_argument("--graph", type=str, default=str(DEFAULT_GRAPH_PATH), help="Path to graph.json")
    parser.add_argument("--hops", type=int, default=2, help="Max hops to traverse (default: 2)")
    parser.add_argument("--limit", type=int, default=10, help="Max results to return")
    args = parser.parse_args()

    keywords = extract_keywords(args.query)
    if not keywords:
        print(f"[graphify capsule] No significant keywords found in '{args.query}'.")
        return

    graph = load_graph(Path(args.graph))
    results = search_and_walk(graph, keywords, max_hops=args.hops, max_results=args.limit)

    if not results:
        print(f"[graphify capsule] Zero graph matches for keywords: {', '.join(keywords)}")
        return

    proj_ctx = detect_project_context(results)
    capsule = format_capsule(args.query, keywords, results, proj_ctx)
    print(capsule)


if __name__ == "__main__":
    main()
