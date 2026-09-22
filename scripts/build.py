#!/usr/bin/env python3
"""Build the cybersecurity-framework site data, markdown mirrors & sitemap.

- tree/*.json   -> docs/data/tree.json   (merged, recursive)
- tree/*.json   -> tree/*.md             (auto markdown mirror for Obsidian/reading)
- *.md root     -> docs/*.md             (served copies for GitHub Pages)
- docs/sitemap.xml                      (regenerated, lastmod from last commit)

Usage:
  python3 scripts/build.py             build + write
  python3 scripts/build.py --ci        validate + determinism check (exit 1 on any issue)
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREE = ROOT / "tree"
DOCS = ROOT / "docs"
DOCS_DATA = DOCS / "data"

CLASS_ORDER = ["offense", "defense"]
URL_URL = r"^https?://[^\s<>\"]+$"
CI = "--ci" in sys.argv or "--check" in sys.argv


def note(level, msg):
    print(f"  {level}: {msg}")


def errors_from(node):
    """Return a list of human-readable validation issues under a node."""
    out = []
    path = node.get("name") or node.get("id") or "?"
    for t in node.get("tools", []):
        name = t.get("name", "?")
        if not t.get("name"):
            out.append(f"{path}: tool missing name")
        if not t.get("url"):
            out.append(f"{path}: tool {name!r} missing url")
        elif not re.match(URL_URL, t["url"] or ""):
            out.append(f"{path}: tool {name!r} url is not http(s): {t['url']!r}")
        for f in ("desc", "when"):
            if not t.get(f):
                out.append(f"{path}: tool {name!r} missing {f}")
        if t.get("rating") is not None:
            try:
                if not (0 <= float(t["rating"]) <= 5):
                    out.append(f"{path}: tool {name!r} rating out of range")
            except (TypeError, ValueError):
                out.append(f"{path}: tool {name!r} rating not a number: {t['rating']!r}")
        if t.get("effort") not in (None, "easy", "medium", "advanced", "beginner"):
            out.append(f"{path}: tool {name!r} unknown effort {t['effort']!r}")
        for a in t.get("alt", []) or []:
            if not a:
                out.append(f"{path}: tool {name!r} has empty alternative")
    for sub in node.get("subcategories", []):
        out.extend(errors_from(sub))
    return out


def validate_tools(domains):
    """Collect tool/category validation issues across the whole tree."""
    issues = []
    for d in domains:
        for cat in d.get("categories", []):
            for e in errors_from(cat):
                issues.append(e)
    return issues


def structure_refs(raw):
    """Collect missing-domain references from the raw _structure.json."""
    bad = []
    for pillar in raw.get("pillars", []):
        for g in pillar.get("groups", []):
            for did in g.get("domains", []):
                if not isinstance(did, str):
                    bad.append(f"structure.json group {g.get('id')!r} has non-string domain ref {did!r}")
    return bad


def sort_key(d):
    clz = d.get("class") or d.get("cls") or "offense"
    return (
        CLASS_ORDER.index(clz) if clz in CLASS_ORDER else 9,
        d.get("id", ""),
    )


def normalize_effort(node):
    for t in node.get("tools", []):
        if t.get("effort") == "beginner":
            t["effort"] = "easy"
        elif t.get("effort") not in (None, "easy", "medium", "advanced"):
            t["effort"] = "medium"
    for sub in node.get("subcategories", []):
        normalize_effort(sub)


def index_refs(node, dom_id, refs, stack):
    stack = stack + [node.get("id") or node.get("name") or ""]
    for t in node.get("tools", []):
        refs.setdefault((t.get("name") or "").lower(), []).append((dom_id, "/".join(x for x in stack if x)))
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
    for t in node.get("tools", []):
        star = " ⭐" if t.get("best") else ""
        by = " ◆ by " + t["by"] if t.get("by") else ""
        lines += [f"{'#' * min(depth + 2, 6)} {t.get('name', '?')}{star}{by}", ""]
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
        lines += [header, "", ""]
        lines += md_node(sub, depth + 1)
    return lines


def read_json(path, label):
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        note("ERROR", f"{label} {path.name} is not valid JSON: {e}")
        sys.exit(1)


def read_structure(domains_by_id):
    """Load tree/_structure.json and expand domain refs into embedded domain objects."""
    sp = TREE / "_structure.json"
    if not sp.exists():
        return []
    struct = read_json(sp, "structure")
    pillars = []
    for pillar in struct.get("pillars", []):
        groups = []
        for g in pillar.get("groups", []):
            doms = [domains_by_id[did] for did in g.get("domains", []) if did in domains_by_id]
            groups.append({"id": g.get("id", ""), "name": g.get("name", ""), "domains": doms})
        cls = pillar.get("class") or pillar.get("id", "")
        pillars.append({"id": pillar.get("id", ""), "name": pillar.get("name", ""), "emoji": pillar.get("emoji", ""),
                        "class": cls, "cls": cls, "tagline": pillar.get("tagline", "")} | {"groups": groups})
    return pillars


def last_modified():
    """Best-effort date of the last commit touching docs/ (short ISO date)."""
    try:
        r = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", "docs/"],
            capture_output=True, text=True, cwd=str(ROOT), timeout=5,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return datetime.date.today().isoformat()


def render_sitemap(docs_url):
    """Sitemap for the files GH Pages exposes under /docs/ (index served at root)."""
    pages = [
        "README.md", "VISION.md", "SCOPE.md", "SCHEMA.md",
        "ETHICS.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "LICENSE", "SECURITY.md",
        "CHANGELOG.md",
    ]
    lm = last_modified()
    urls = "\n".join(
        f"  <url><loc>{docs_url}/{p}</loc><lastmod>{lm}</lastmod></url>"
        for p in pages if (DOCS / p).exists()
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "  <url><loc>" + docs_url.rstrip("/") + "/</loc>"
        f"<lastmod>{lm}</lastmod></url>\n"
        "</urlset>\n"
    )


MIRROR = ("README.md", "ETHICS.md", "SCOPE.md", "SCHEMA.md", "VISION.md",
          "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "LICENSE", "SECURITY.md",
          "CHANGELOG.md")


def outputs(domains):
    """Return ordered {relative_path: content} describing everything the build writes."""
    out = {}
    total_cats = sum(sum(count_cats(c) for c in d.get("categories", [])) for d in domains)
    total_tools = sum(sum(count_tools(c) for c in d.get("categories", [])) for d in domains)

    domains_by_id = {d["id"]: d for d in domains if d.get("id")}
    pillars = read_structure(domains_by_id)

    merged = {
        "pillars": pillars,
        "stats": {"domains": len(domains), "categories": total_cats, "tools": total_tools},
        "generated": "cybersecurity-framework build.py",
    }

    DOCS_DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    out["docs/data/tree.json"] = json.dumps(merged, indent=2) + "\n"

    for name in MIRROR:
        src = ROOT / name
        if src.exists():
            out[f"docs/{name}"] = src.read_text()

    out["docs/sitemap.xml"] = render_sitemap("https://5h4d0wn1k.github.io/cybersecurity-framework")

    for d in domains:
        lines = [f"# {d.get('emoji', '')} {d.get('name', d.get('id', ''))}", "", d.get("tagline", ""), ""]
        for cat in d.get("categories", []):
            h = f"## {cat.get('name', cat.get('id', ''))}"
            lines += [h, ""]
            b = best_of(cat)
            lines += [f"{b} ⭐" if b else ""]
            lines += [""]
            lines += md_node(cat, 2)
            lines += [""]
        out[f"tree/{d.get('id', 'unnamed')}.md"] = "\n".join(lines) + "\n"

    return out, len(domains), total_cats, total_tools


def build():
    domains, issues = [], []
    for p in sorted(TREE.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = read_json(p, "tree")
        if not d.get("id"):
            issues.append(f"{p.name}: missing top-level id")
        domains.append(d)

    domains.sort(key=sort_key)
    for d in domains:
        d["cls"] = d.get("class")

    sp = TREE / "_structure.json"
    if sp.exists():
        issues.extend(structure_refs(read_json(sp, "structure")))
    issues.extend(validate_tools(domains))

    for d in domains:
        for cat in d.get("categories", []):
            normalize_effort(cat)

    out, nd, nc, nt = outputs(domains)

    if CI:
        ok = True
        for msg in issues:
            note("ERROR", msg)
            ok = False
        if not ok:
            print(f"  ({len(issues)} issue(s) — fix in tree/*.json)")
        drift = []
        for rel, content in out.items():
            target = ROOT / rel
            if not target.exists() or target.read_text() != content:
                drift.append(str(target.relative_to(ROOT)))
        if drift:
            ok = False
            note("ERROR", f"output differs from committed files: {', '.join(drift)} (run scripts/build.py and commit)")
        if ok:
            print(f"CI OK: deterministic, {nd} domains / {nc} categories / {nt} tools, no issues")
        return 0 if ok else 1

    for rel, content in out.items():
        target = ROOT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    for msg in issues:
        note("WARN", msg)
    if issues:
        print(f"  ({len(issues)} validation warnings — fix in tree/*.json)")
    print(f"OK: {nd} domains, {nc} categories (nested incl.), {nt} tools -> docs/data/tree.json")
    return 0


if __name__ == "__main__":
    sys.exit(build())