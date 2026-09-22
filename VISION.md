# 🧭 VISION.md — The end-to-end cybersecurity education platform

> **Short version:** CyberOps Framework is becoming more than a tool tree. It will be the
> most complete, open, community-maintained map of **everything in cybersecurity** — every
> domain, every technique, every tool, both offensive and defensive — presented as an
> interactive, learnable, educational website, and kept alive by the community for the
> community. Always ethical, always in-scope, always legal.

---

## 1. Why we exist

Cybersecurity is vast, scattered, and intimidating. Questions like…

- "What tools do I use to enumerate an Active Directory domain?"
- "I want to become a malware analyst — where do I start?"
- "What's the best way to scan my own cloud account?"
- "I'm a SOC analyst — what detection tools should I know?"

…rarely have a single map. Knowledge lives in hundreds of GitHub repos, blog posts, courses,
and certification tracks. Newcomers drown in tool overload; practitioners lose hours hunting
for the right instrument; and defensive and offensive worlds stay siloed.

**CyberOps Framework is the atlas that fixes this.** One map, one tree, one search box that
connects every part of the discipline — organized, rated, and explained.

---

## 2. The mission

> **Map every meaningful thing in cybersecurity — offensive AND defensive — in detail,
> organized so anyone can find the right tool, understand why it's the right one, and learn
> the concepts behind it. Then open it to the world so the community completes it together,
> faster, and keeps it accurate forever.**

We are building the **end-to-end cybersecurity education website**:

```
┌────────────────────────────────────────────────────────────────────┐
│             THE CYBEROPS EDUCATION PLATFORM                         │
│                                                                    │
│  INTERACTIVE MAP   ──►   CONCEPT NOTES   ──►   LEARNING PATHS      │
│  (the tree we have)      (added)             (planned)             │
│       ▲                       ▲                    ▲               │
│       └───── tools, domains, categories    notes teach the "why"  │
│             connected to real URLs,        steps become careers    │
│             ratings, install, effort                                │
└────────────────────────────────────────────────────────────────────┘
```

---

## 3. What we map — EVERYTHING, offensive and defensive

We divide the discipline into two pillars, then map every domain, every sub-problem and
every tool down to the finest practical detail.

### ⚔️ Offensive Security — the attacker's journey

1. **Reconnaissance & OSINT** — people, infrastructure, metadata, documents
2. **Scanning & Assessment** — vulnerability scanning, network mapping
3. **Web & Mobile Apps** — web app security, mobile (Android/iOS) security
4. **Identity & Active Directory** — enumeration, kerberoasting, AD attacks
5. **Passwords & Crypto** — cracking, wordlists, crypto attacks & cryptoanalysis
6. **Exploitation & Payloads** — exploitation frameworks, binary exploitation, privesc
7. **C2 & Red Team Ops** — command & control, red team infrastructure
8. **Phishing & Social Engineering**
9. **Wireless, Embedded & IoT** — WiFi, Bluetooth, firmware, embedded

### 🛡️ Defensive Security — the defender's journey

1. **Detection & Monitoring** — blue team, threat intelligence, SIEM/EDR
2. **Application Assurance** — SAST, DAST, secrets & SCA
3. **Forensics & Incident Response** — disk/memory/network forensics, DFIR
4. **Malware & Threat Analysis** — reverse engineering, sandboxing
5. **Hardening & Compliance** — CIS baselines, secure config, compliance
6. **Cloud & Container Security** — AWS/Azure/GCP, K8s, containers
7. **Deception & Adversary Emulation** — honeypots, purple team, BAS

### 🗺️ What "complete" means

A domain is *complete* when **every practical task** inside it has:

- a **category** (so the map is navigable),
- a **best-in-class tool** (★) with honest alternatives,
- each tool carrying `effort`, `rating`, `when-to-use`, `install`, and `url`,
- and ideally a **concept note** (see §5).

Example — the **Web Application Security** domain becomes:

```
web
├── Content Discovery ────── fuzzing (FFUF ★, gobuster, feroxbuster) · wordlists
├── Recon (in-app) ───────── js-analysis, api-enum, subdomain
├── Injection ────────────── SQLi (sqlmap ★) · NoSQL · SSTI · command injection
├── Authentication ───────── session attacks · JWT · OAuth
├── XSS / Client-side ────── XSS testing (XSStrike ★, Nuclei) · CSP auditing
├── SSRF & access ────────── SSRF · file uploads · path traversal
├── API Security ─────────── API testing (Postman, mitmproxy) · GraphQL
└── Infrastructure ───────── proxies (Burp ★, OWASP ZAP) · certs · waf evasions
```

That level of granularity is the goal **for every domain**, so the map is genuinely useful
for real work — not a shallow list of famous tools.

---

## 4. The three layers of the platform

### Layer 1 — The Interactive Map (built 🟢)
The tree site: `docs/index.html`. Pillars → categories → domains → subcategories → tools.
Search, jump-to-domain, expand/collapse with bloom animations, effort ratings, install
copies, direct tool URLs, offense/defense theming.

### Layer 2 — Concept Notes (next 🟡)
A short "learn this first" paragraph per **category** — the *why* behind the tools, embedded
as `notes` in the JSON tree (or a companion knowledge file). Teaches the idea behind the
tools, so the site becomes a study map, not just a tool list.

### Layer 3 — Learning Paths (planned 🟠)
Curated journey presets that string categories into career tracks:

- **Web App Pentester** — HTTP basics → content discovery → injection → auth → API → reporting
- **SOC / Blue Team Analyst** — event theory → detection engineering → threat intel → IR workflows
- **Malware Analyst** — PE/ELF basics → static → dynamic → sandboxing → report writing
- **Cloud Security Engineer** — IAM → network → data → container → CSPM
- **Red Team Operator** — C2 infra → phishing → lateral movement → persistence

Each path reuses the same tree data — just filtered and ordered. **No separate syllabus to
maintain; the tree IS the syllabus.**

---

## 5. Completeness — how we finish "everything in detail"

Everything is data: `tree/*.json`. Nothing is hard-coded. That means the project can be
completed incrementally, measured, and community-split like a wiki.

### Definition of "map complete"

Roadmap gates toward full coverage:

| Gate | Meaning | Status |
|---|---|---|
| G0 · **Tool coverage** | every practical task has best-in-class + alternatives | 🟢 27/27 domains scaffolded |
| G1 · **Domain completeness** | no missing practical sub-problem inside each domain | 🟡 in progress |
| G2 · **Concept notes** | every category node has an educational `notes` paragraph | 🔴 planned |
| G3 · **Frameworks alignment** | categories tagged to MITRE ATT&CK / NIST CSF / OWASP / CAPEC | 🔴 planned |
| G4 · **Learning paths** | curated career tracks navigate the tree | 🔴 planned |
| G5 · **Community live** | contributors + review flow keep everything current | 🔴 starting |

### Missing domains on the roadmap (to add next, G1)

- 🤖 **AI & LLM Security** — prompt injection, model extraction, OWASP LLM Top 10, evals
- 🏛️ **GRC / Governance, Risk & Compliance** — ISO 27001, NIST CSF, SOC 2, risk frameworks
- 🔗 **Supply-chain & DevSecOps** — SBOM, sigstore, dependency confusion, CI/CD abuse
- 🏭 **OT / ICS / SCADA** — Purdue model, industrial protocols, PLC attacks/defenses
- 🐞 **Bug Bounty & Responsible Disclosure** — platforms, scope reading, disclosure practice
- ⛓️ **Web3 / Blockchain Security** — smart contracts, wallets, DeFi attacks
- 🚀 **Hardware & 5G Security** — JTAG, side-channels, SIM, 5G core
- 📱 **OSINT beyond people** — geospatial, vehicle, datasets (OSINT framework parity)

### How the community completes it

Each domain is a single JSON file. An issue template asks for: tool name, why it's the best,
tags, install line, URL. A PR adds the file. Maintainers review against **SCHEMA.md** and
**ETHICS.md**. Because it's plain JSON + markdown, contribution friction is near zero — you
don't need to touch HTML, JS, or build systems.

---

## 6. Open source & community — why and how

The stated architecture (data-as-files) makes **open source the only correct model**: a map
of everything is impossible for one person to own accurately. Community brings coverage,
accuracy, and freshness.

- **License:** MIT — use it, remix it, teach from it.
- **Everything editable:** the tree, the notes, the paths, the site copy.
- **Transparent review:** every entry is a real URL with a real install line; nothing is
  marketed or paywalled. ★ marks are earned by merit, not sponsorship.
- **Attribution:** contributors are credited in commit history and the ◆ badge is reserved
  for first-party tools. See [CONTRIBUTING.md](CONTRIBUTING.md).

We want students to learn from it, SOC teams to use it, red teams to plan with it, and
researchers to fork it for their own curricula.

---

## 7. Ethics, legality & scope — the permanent boundaries

This map is an **atlas, not a weapon**. An atlas that explains locks is how locksmiths and
homeowners describe their job — it is not a burglary manual. The difference is **intent and
scope**, and both are encoded into the project *by design*.

### The four rules (full text in [ETHICS.md](ETHICS.md))

1. **Authorized targets only.** Use every tool exclusively on systems you own or have
   written permission to assess. Unauthorized use may violate the CFAA (18 U.S.C. §1030),
   the Wiretap Act (18 U.S.C. §2511), EU Directive 2013/40/EU, and local law.
2. **Teach and defend, don't enable.** Editorial policy: *never a how-to break into a third
   party; always a how-to check your own.*
3. **Safety by default.** Staged paths — start in a lab, understand the protocol, then move
   to authorized real scope.
4. **Responsible disclosure.** Real bugs found on real systems are reported privately with
   a fix window — never weaponized.

### The scope checklist (full text in [SCOPE.md](SCOPE.md))

Before running anything on a live target, all four must be **YES**:
owned target, written permission, known blast radius, defined end. If any is NO, use the
**lab path** (own router, VM, localhost, second-hand radio).

### What will NEVER be added here

To keep the map legal, ethical, and useful, we deliberately exclude or gate:

- ❌ Malware/tooling whose primary purpose is evading law enforcement or harming others
- ❌ Locked/paywalled "best" placements, or listings that market a commercial product
- ❌ Guides framed to break into third parties — including "capture the data of domain X"
- ❌ Any tool with no verifiable legitimate/authorized defense-and-testing use case
- ⚠️ Dual-use tooling is listed **defensively** (when/how to test your own estate), never
  framed as an intrusion recipe for others

These lines make the project safe to host, safe to learn from, and safe to keep open.

---

## 8. Near-term plan (next 3–6 months)

1. **Finish G0/G1** — add the 8 missing domains, then sweep every domain for empty or
   underspecified categories (fill real tools, kill dupes).
2. **Ship concept notes (Layer 2)** — a `notes` field on category nodes; render in the
   details panel.
3. **Frameworks alignment (G3)** — add `mitre-id` / `owasp-ref` tags; a secondary toggle on
   the site filters tools by technique/control.
4. **Learning paths (Layer 3)** — 5 starter career tracks rendered from filtered tree order.
5. **Community release** — issue/PR templates, contribution badges, a short "how to add a
   tool in 3 minutes" doc, and a public roadmap page.
6. **SEO & discoverability** — indexed Pages site, sitemap, rich Open Graph, structured
   data, and README/About metadata kept current (done in this release; maintained ongoing).

## 9. How you can help

- **Add or fix a tool** — one file, one PR. See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Write concept notes** — explain a category in a paragraph someone novice can grasp.
- **Design a learning path** — sequence tree categories into a credible career journey.
- **Audit a domain** — check every URL is alive and every pick is actually best-in-class.
- **Spread the word** — a GitHub star, a mention in your blog/course, a link on LinkedIn.

---

**The map belongs to the community. The boundaries never move.**
Read [ETHICS.md](ETHICS.md) → [SCOPE.md](SCOPE.md) → [CONTRIBUTING.md](CONTRIBUTING.md).