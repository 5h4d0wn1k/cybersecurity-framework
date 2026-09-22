# SCHEMA.md — Tool Tree Data Format (v2, recursive)

Every domain of the tool map lives in `tree/<domain-id>.json`. The site renders from the
merged `docs/data/tree.json`; markdown mirrors are auto-generated.

## Recursive nesting

A domain's `categories` is a **recursive tree**. A node is a *category folder* that can
contain:
- `tools` — leaf entries (optional)
- `subcategories` — deeper folders (optional, **infinite depth**)

```json
{
  "id": "web",
  "name": "Web Application Security",
  "emoji": "🌐",
  "tagline": "One-service-scoped attacks on the web apps you build or test.",
  "class": "offense",
  "categories": [
    {
      "id": "content-discovery",
      "name": "Content Discovery",
      "subcategories": [
        {
          "id": "fuzzing",
          "name": "Fuzzing (brute wordlists)",
          "tools": [
            {
              "name": "FFUF",
              "best": true,
              "rating": 5,
              "effort": "easy",
              "desc": "Fast web fuzzer for dirs, files, params, vhosts.",
              "when": "Any brute-force discovery of paths or parameters.",
              "install": "go install github.com/ffuf/ffuf/v2@latest",
              "url": "https://github.com/ffuf/ffuf",
              "alt": ["gobuster", "feroxbuster"]
            }
          ]
        },
        {
          "id": "wordlists",
          "name": "Wordlists & seeds",
          "tools": []
        }
      ]
    }
  ]
}
```

## Field rules (tools)

| Field | Rule |
|---|---|
| `id` | lowercase, no spaces |
| `name` | display name |
| `best` | `true` on the single best-in-category tool (≤1 per group of siblings) |
| `rating` | 1-5 curation confidence / significance |
| `effort` | `easy` \| `medium` \| `advanced` — honest setup+usage effort |
| `desc` | 1-2 factual sentences, verb-first, no hype |
| `when` | 1-2 sentences saying *exactly* when to reach for it |
| `install` | one real install line (apt/pip/go/brew/exe, or "preinstalled (web)") |
| `url` | official repo/site URL |
| `alt` | 1-4 genuine alternatives already listed nearby where possible |
| `by` | *optional* — GitHub username authoring this tool (own/first-party tools, e.g. `"by": "5h4d0wn1k"`). Tools with `by` render a violet ◆ badge in the tree, a "by <user>" chip in the details panel, and a GitHub link. `url` must point at that owner's repo. |

## Category node fields

| Field | Rule |
|---|---|
| `id` | lowercase, no spaces |
| `name` | display name |
| `tools` | optional array of tool leaves |
| `subcategories` | optional array of nested category nodes (recursive, any depth) |

## Class

`"class": "offense"` (red/attack) or `"class": "defense"` (blue/defend).

## Markdown mirror

`tree/<domain-id>.md` mirrors the JSON in readable markdown (## categories, ### tools,
indented `####` for deeper nesting).