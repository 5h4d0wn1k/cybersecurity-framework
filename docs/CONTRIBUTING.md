# CONTRIBUTING.md — How to help complete the map

Thank you for wanting to contribute to **CyberOps Framework**. Everything is plain JSON and
Markdown — you never need to touch HTML or JS to add knowledge. This guide makes it
possible for anyone to help in a few minutes.

---

## Ways to contribute

| Contribution | Where | Difficulty |
|---|---|---|
| Add / fix a tool | `tree/<domain>.json` | easy |
| Add a whole missing category | `tree/<domain>.json` | easy–medium |
| Write a concept note | `notes` field on a category node | medium |
| Audit a domain (URLs alive? picks actually best?) | review issues | easy |
| Propose a new domain | issue + `tree/<domain>.json` | medium |
| Fix the site / animations / a11y | `docs/index.html` | medium |
| Design a learning path | issue discussion + notes | medium–hard |
| Translate the site or docs | copy / i18n | easy |

---

## The 3-minute "add a tool" recipe

1. **Pick the domain file** — e.g. `tree/web.json`. Open it.
2. **Find the category** where the tool belongs, or add a new one:

```json
{
  "id": "api-security",
  "name": "API Security",
  "tools": [
    {
      "name": "Mitmproxy2Swagger",
      "best": false,
      "rating": 4,
      "effort": "medium",
      "desc": "Automates OpenAPI generation from captured traffic.",
      "when": "When you need a readable API spec from a logged session.",
      "install": "pip install mitmproxy2swagger",
      "url": "https://github.com/alufers/mitmproxy2swagger",
      "alt": ["mitmproxy"]
    }
  ]
}
```

3. **Follow the schema rules** — see [SCHEMA.md](SCHEMA.md) for every field.
4. **Run the build** to verify and regenerate the site data:

```bash
python3 scripts/build.py
```

5. Open a **PR**. Done.

---

## Contribution rules (enforced at review)

- ✅ **Real, verifiable** — every tool has a working official `url` and an accurate `install`.
- ✅ **Curated, not loud** — `best: true` is earned by merit, reserved for the single
  best-in-class tool in its sibling group (≤1 per group). No marketing.
- ✅ **Honest effort** — `effort` = real setup+usage effort. Update it if you know better.
- ✅ **Defensive framing** — tools and `when` text are written from the tester/owner
  perspective: *never a how-to break into a third party; always a how-to check your own.*
- ❌ No dead URLs, placeholder tools, or "coming soon" entries.
- ❌ No listings whose primary purpose is harming others or evading law enforcement
  (see [ETHICS.md](ETHICS.md) and [VISION.md](VISION.md) §7).
- ❌ No duplicate tool names across the tree (`build.py` warns).

## Pull request workflow

1. Fork the repo, create a branch: `feat/add-<tool>` or `fix/<domain>-urls`.
2. Make small, focused PRs (one domain/topic per PR is ideal).
3. Run `python3 scripts/build.py` locally to confirm the build passes.
4. In the PR description, note: what you added, why it's the best pick (if marked ★),
   and any URLs you verified.
5. A maintainer reviews against SCHEMA + ETHICS and merges. Contributors are credited in
   git history and thanked in releases.

## Issue templates

Use the provided templates when opening issues:
- **Add a tool** — name, category, why best, install, URL.
- **Fix / dead link** — what's broken, suggested replacement.
- **Add a domain** — proposed domain, categories, key tools.
- **Question** — anything else.

## Reporting problems

- Spots in the site: open a bug issue with browser + steps.
- Security issue in this repository itself (not tooling): see [SECURITY.md](SECURITY.md).

---

**Community first, always in scope.** Read [ETHICS.md](ETHICS.md) and
[SCOPE.md](SCOPE.md) before contributing content.