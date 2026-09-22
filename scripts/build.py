#!/usr/bin/env python3
"""Build the cybersecurity-framework site data & markdown mirrors.

- tree/*.json          -> docs/data/tree.json (merged, recursive)
- tree/*.json          -> tree/*.md (auto markdown mirror for Obsidian/reading)

Usage: python3 scripts/build.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREE = ROOT / "tree"
DOCS = ROOT / "docs" / "data"

CLASS_ORDER = ["offense", "defense"]


def sort_key(d):
    clz = d.get("class", "offense")
    return (
        CLASS_ORDER.index(clz) if clz in CLASS_ORDER else 9,
        d["id"],
    )


def read_structure(domains_by_id):
    """Load tree/_structure.json and expand domain refs into embedded domain objects."""
    sp = TREE / "_structure.json"
    if not sp.exists():
        return []
    struct = json.loads(sp.read_text())
    pillars = []
    for pillar in struct.get("pillars", []):
        groups = []
        for g in pillar.get("groups", []):
            doms = []
            for did in g.get("domains", []):
                if did in domains_by_id:
                    doms.append(domains_by_id[did])
            groups.append({"id": g["id"], "name": g["name"], "domains": doms})
        cls = pillar.get("class")
        pillars.append({"id": pillar["id"], "name": pillar["name"], "emoji": pillar.get("emoji", ""),
                        "class": cls, "cls": cls, "tagline": pillar.get("tagline", "")} | {"groups": groups})
    return pillars


def normalize_effort(node):
    for t in node.get("tools", []):
        if t.get("effort") == "beginner":
            t["effort"] = "easy"
    for sub in node.get("subcategories", []):
        normalize_effort(sub)


def index_refs(node, dom_id, refs, stack):
    stack = stack + [node.get("id", "")]
    for t in node.get("tools", []):
        refs.setdefault(t["name"].lower(), []).append((dom_id, "/".join(x for x in stack if x)))
    for sub in node.get("subcategories", []):
        index_refs(sub, dom_id, refs, stack)


def count_cats(node):
    return 1 + sum(count_cats(s) for s in node.get("subcategories", []))


def count_tools(node):
    return len(node.get("tools", [])) + sum(count_tools(s) for s in node.get("subcategories", []))


def best_of(node):
    return next((t["name"] for t in node.get("tools", []) if t.get("best")), None)


def md_node(node, depth):
    """Render a category node recursively as markdown."""
    lines = []
    has = node.get("name", node.get("id", ""))
    for t in node.get("tools", []):
        star = " ⭐" if t.get("best") else ""
        by = " ◆ by " + t["by"] if t.get("by") else ""
        lines += [f"{'#' * min(depth + 2, 6)} {t['name']}{star}{by}", ""]
        lines += [t.get("desc", ""), ""]
        lines += [f"**When:** {t.get('when', '')}", ""]
        lines += [f"**Effort:** {t.get('effort', '')}  ·  **Rating:** {t.get('rating', '')}/5", ""]
        if t.get("install"):
            lines += [f"**Install:** `{t['install']}`", ""]
        if t.get("url"):
            lines += [f"**URL:** {t['url']}", ""]
        if t.get("alt"):
            lines += [f"**Alternatives:** {', '.join(t['alt'])}", ""]
        lines.append("")
    for sub in node.get("subcategories", []):
        header = f"{'#' * min(depth + 2, 6)} {sub.get('name', sub.get('id', ''))}"
        lines += [header, ""]
        lines += ["", ""]
        lines += md_node(sub, depth + 1)
    return lines


def build():
    DOCS.mkdir(parents=True, exist_ok=True)
    domains, refs = [], {}

    for p in sorted(TREE.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = json.loads(p.read_text())
        domains.append(d)
        for cat in d.get("categories", []):
            index_refs(cat, d["id"], refs, [d["id"]])

    refs = {k: list(dict.fromkeys(v)) for k, v in refs.items()}

    for d in domains:
        for cat in d.get("categories", []):
            normalize_effort(cat)

    domains.sort(key=sort_key)

    for d in domains:
        d["cls"] = d.get("class")

    domains_by_id = {d["id"]: d for d in domains}
    pillars = read_structure(domains_by_id)

    total_cats = sum(sum(count_cats(c) for c in d.get("categories", [])) for d in domains)
    total_tools = sum(sum(count_tools(c) for c in d.get("categories", [])) for d in domains)

    merged = {
        "domains": domains,
        "pillars": pillars,
        "refs": refs,
        "stats": {"domains": len(domains), "categories": total_cats, "tools": total_tools},
    }

    DOCS.mkdir(parents=True, exist_ok=True)
    for name in ("README.md", "ETHICS.md", "SCOPE.md", "SCHEMA.md", "VISION.md",
                 "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "LICENSE"):
        src = ROOT / name
        if src.exists():
            (DOCS / name).write_text(src.read_text())

    (DOCS / "tree.json").write_text(json.dumps(merged, indent=2))

    for d in domains:
        lines = [f"# {d.get('emoji', '')} {d['name']}", "", d.get("tagline", ""), ""]
        for cat in d.get("categories", []):
            rl = ["", "", "", ""]
            h = f"## {cat.get('name', cat.get('id', ''))}"
            lines += [h, ""]
            b = best_of(cat)
            lines += [f"{b} ⭐" if b else ""]
            lines += ["", ""]
            lines += md_node(cat, 2)
            lines += rl
        (TREE / f"{d['id']}.md").write_text("\n".join(lines))

    print(f"OK: {len(domains)} domains, {total_cats} categories (nested incl.), {total_tools} tools -> docs/data/tree.json")
    return 0


if __name__ == "__main__":
    sys.exit(build())