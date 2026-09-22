#!/usr/bin/env python3
"""Build the cybersecurity-framework site data & markdown mirrors.

- tree/*.json  -> docs/data/tree.json   (merged, JSON the site renders)
- tree/*.json  -> tree/*.md             (auto markdown mirror for Obsidian/reading)

Usage: python3 scripts/build.py
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREE = ROOT / "tree"
DOCS = ROOT / "docs" / "data"

fields = {"x": None}  # keys are examples; "best" etc are standard

CLASS_ORDER = ["offense", "defense"]  # offense first, then defense


def sort_key(d):
    return (CLASS_ORDER.index(d.get("class", "offense")) if d.get("class", "offense") in CLASS_ORDER else 9,
            d["id"])


def build():
    DOCS.mkdir(parents=True, exist_ok=True)
    domains, refs = [], {}

    for p in sorted(TREE.glob("*.json")):
        d = json.loads(p.read_text())
        if d.get("id") in ("_schema",):
            continue
        domains.append(d)
        for cat in d.get("categories", []):
            for t in cat.get("tools", []):
                refs.setdefault(t["name"].lower(), []).append((d["id"], cat["id"]))

    # dedupe refs by (id,cat)
    refs = {k: list(dict.fromkeys(v)) for k, v in refs.items()}

    domains.sort(key=sort_key)

    # normalize effort vocabulary to easy/medium/advanced
    for d in domains:
        for cat in d.get("categories", []):
            for t in cat.get("tools", []):
                if t.get("effort") == "beginner":
                    t["effort"] = "easy"

    total_cats = sum(len(d.get("categories", [])) for d in domains)
    total_tools = sum(len(c.get("tools", [])) for d in domains for c in d.get("categories", []))

    merged = {"domains": domains, "refs": refs, "stats": {
        "domains": len(domains), "categories": total_cats, "tools": total_tools}}

    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "tree.json").write_text(json.dumps(merged, indent=2))

    # markdown mirrors
    for d in domains:
        lines = [f"# {d['emoji']} {d['name']}", "", d.get("tagline", ""), ""]
        for cat in d.get("categories", []):
            lines += [f"## {cat['name']}", ""]
            for t in cat.get("tools", []):
                star = " ⭐" if t.get("best") else ""
                lines += [f"### {t['name']}{star}", ""]
                lines += [t["desc"], "", f"**When:** {t.get('when','')}", ""]
                lines += [f"**Effort:** {t.get('effort','')}  ·  **Rating:** {t.get('rating','')}/5", ""]
                if t.get("install"):
                    lines += [f"**Install:** `{t['install']}`", ""]
                if t.get("url"):
                    lines += [f"**URL:** {t['url']}", ""]
                if t.get("alt"):
                    lines += [f"**Alternatives:** {', '.join(t['alt'])}", ""]
                lines.append("")
        (TREE / f"{d['id']}.md").write_text("\n".join(lines))

    print(f"OK: {len(domains)} domains, {total_cats} categories, {total_tools} tools -> docs/data/tree.json")
    return 0


if __name__ == "__main__":
    sys.exit(build())