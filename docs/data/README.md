# 🧭 Cybersecurity Framework

**The open-source map of everything in cybersecurity** — every domain, every category, and
the **best tool for each job** (★), organized the way OSINT Framework organizes recon, but
for the *whole* of cyber: attack, defense, cloud, mobile, IoT, forensics, malware, and more.

> Built to answer one question in seconds: **“I need to do X. Which tool?”**

## What it is

- A **curated tool tree**: domains → categories → best-in-class tools with honest
  `when-to-use`, `effort`, rating, install line, and real alternatives. No hype.
- A **learning map**: each tool links to the concepts behind it, so you learn *why* the tool
  is the right one, not just its name.
- A **GitHub Pages site**: `https://5h4d0wn1k.github.io/cybersecurity-framework/`
- **MIT-licensed and open** — contribute categories, tools, improvements.

## Quickstart

```bash
git clone https://github.com/5h4d0wn1k/cybersecurity-framework
cd cybersecurity-framework
python3 scripts/build.py   # tree/*.json -> docs/data/tree.json + tree/*.md mirrors
# serve docs/ locally:  python3 -m http.server 8000 --directory docs
```

## Structure

```
tree/                 domain JSON (source of truth) + auto-generated .md mirrors
docs/                 the GitHub Pages site (index.html + data/tree.json)
scripts/build.py      merges tree/*.json into the site data + markdown mirrors
SCHEMA.md             the tool-tree data format
ETHICS.md             intent & scope foundation — read first
SCOPE.md              the authorized-testing checklist
```

## Domains (20)

recon · vuln-scan · exploit · binary · web · network · wireless · passwords · social ·
osint-people · malware · forensics · cloud · mobile · iot · c2 · blueteam · appsec ·
container-k8s · threatintel · crypto

## Ethical use

This map exists to help owners and defenders test **their own** systems. Authorized targets
only. Read [ETHICS.md](ETHICS.md) and [SCOPE.md](SCOPE.md). Unauthorized use of these tools
may violate the CFAA (18 U.S.C. §1030) and local law.

## Contributing

Open issues / PRs to add tools, fix a URL, or refine a `when-to-use`. Follow SCHEMA.md —
every addition must be real, curated, and safety-gated.

---
**MIT** · made like an atlas: education first, always in scope.