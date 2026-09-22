# SCHEMA.md — Tool Tree Data Format

Every domain of the tool map lives in `tree/<domain-id>.json` plus a human-readable
`tree/<domain-id>.md`. The site renders from the merged JSON; the markdown mirrors it
for Obsidian/reading.

## Domain file (JSON)

```json
{
  "id": "recon",
  "name": "Reconnaissance & OSINT",
  "emoji": "🕵️",
  "tagline": "Everything about subdomains, DNS, historical data, people, leaks.",
  "class": "offense",
  "categories": [
    {
      "id": "subdomains",
      "name": "Subdomain Enumeration",
      "tools": [
        {
          "name": "Amass",
          "best": true,
          "rating": 5,
          "effort": "medium",
          "desc": "OWASP-recommended active/passive subdomain enumeration with API integration and graph output.",
          "when": "Large scope discovery, or when you have a handful of recon API keys; the reference tool.",
          "install": "go install -v github.com/owasp-amass/amass/v4/...@master",
          "url": "https://github.com/owasp-amass/amass",
          "alt": ["subfinder", "crt.sh", "dnsx"]
        }
      ]
    }
  ]
}
```

## Field rules

| Field | Rule |
|---|---|
| `id` | lowercase, no spaces |
| `best` | `true` on the single best-in-category tool (≤1 per category) |
| `rating` | 1-5 curation confidence / significance |
| `effort` | `beginner` \| `medium` \| `advanced` — honest setup+usage effort |
| `when` | 1-2 sentences saying *exactly* when to reach for it |
| `desc` | 1-2 sentences. No hype, no marketing-speak. Verb-first. |
| `install` | one real install line (package, go install, pip, brew, or "preinstalled") |
| `url` | official repo/site URL only |
| `alt` | 1-4 genuine alternatives *already listed in the same category* where possible |

ToC-ish best-tools additions (commercial/SaaS) are allowed with `"class":"commercial"`.

## Markdown mirror

`tree/<domain-id>.md` mirrors the JSON in readable markdown (## categories, ### tools).