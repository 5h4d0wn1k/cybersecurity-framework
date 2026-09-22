# 🧭 CyberOps Framework — The Interactive Map of Everything in Cybersecurity

> **An open-source, living atlas of the entire cybersecurity landscape** — every domain,
> every category, and the **best tool for each job** (★), mapped the way OSINT Framework
> maps recon — but for the *whole* of cyber: offense, defense, cloud, mobile, IoT,
> forensics, malware, hardening and more.

🌐 **Live site:** <https://5h4d0wn1k.github.io/cybersecurity-framework/>

📚 **Read the vision first:** [VISION.md](VISION.md) — how this becomes a full end-to-end
cybersecurity education platform.

---

## What this is

| | |
|---|---|
| **A curated tool tree** | domains → categories → best-in-class tools with honest `when-to-use`, `effort`, rating, install line, and real alternatives. No hype. |
| **A learning map** | every tool links to the concepts behind it — you learn *why* it's the right instrument, not just its name. |
| **An education platform** | offensive + defensive, organized into two pillars and 27 domains covering the full attack/defense lifecycle. |
| **A community project** | MIT-licensed. Anyone can add categories, tools, or fixes. Contributions reviewed against SCHEMA.md and ETHICS.md. |

**One question it answers in seconds:** *“I need to do X. Which tool?”*

---

## Built to answer that question

- ⚔️ **Offensive Security pillar** — Reconnaissance & OSINT → Scanning → Web & Mobile Apps →
  Identity & AD → Passwords & Crypto → Exploitation → C2 & Red Team → Phishing →
  Wireless/IoT/Embedded
- 🛡️ **Defensive Security pillar** — Detection & Monitoring → Application Assurance →
  Forensics & IR → Malware Analysis → Hardening & Compliance → Cloud & Container →
  Deception & Adversary Emulation
- ★ **Best-in-class picks** — 517 of the best tools flagged, so beginners aren't thrown into
  decision paralysis.
- 🎚️ **Honest effort ratings** — 524 easy · 416 medium · 127 advanced, so you can pick a sane
  entry path and grow.
- 🔗 **Install line + URL for every tool** — copy-paste real install commands directly from
  the site.
- 🔎 **Instant search** across 1067 tools.
- 🧩 **Recursive depth** — categories nest arbitrarily deep (subcategories → sub-subcategories → tools).

---

## Current coverage

| Metric | Value |
|---|---|
| **Domains** | 27 |
| **Categories** (nested incl.) | 776 |
| **Tools** | 1067 |
| **Best-in-class picks (★)** | 517 |
| **Tools by first-party authors (◆)** | 30 |
| **Effort split** | easy 524 · medium 416 · advanced 127 |
| **License** | MIT |

The 27 domains: Active Directory Security, Application Security, Binary Exploitation,
Blue Team, C2 Frameworks, Cloud Security, Container & K8s, Cryptography, Exploitation,
Digital Forensics & IR, Hardening & Compliance, Honeypots, IoT & Embedded, Malware
Analysis, Mobile Security, Network Attacks, OSINT, Password Attacks, Phishing & Social
Engineering, Privilege Escalation, Purple Team, Reconnaissance, Red Team, Threat
Intelligence, Vulnerability Scanning, Web App Security, Wireless & Bluetooth.

---

## 🚀 The Vision — from tool tree to full education platform

This is **V1**. The endgame is documented in [VISION.md](VISION.md) — a complete,
community-built, end-to-end cybersecurity education website where every concept, tool,
attack technique, and defense control in the field is mapped, explained, and connected.

**Near-term roadmap:**

- [ ] **AI & LLM Security** domain (prompt injection, model extraction, OWASP LLM Top 10)
- [ ] **GRC / Governance, Risk & Compliance** domain (ISO 27001, NIST CSF, SOC 2)
- [ ] **Supply-chain & DevSecOps** domain (SBOM, sigstore, CI/CD abuse)
- [ ] **OT/ICS/SCADA** domain
- [ ] **Bug-bounty & Responsible Disclosure** resources
- [ ] **Web3 / Blockchain security** domain
- [ ] **Concept notes** on every category — a short "learn this first" paragraph per node
- [ ] **Learning paths** — preset journeys: *Web App Pentester*, *SOC Analyst*, *Malware
      Analyst*, *Cloud Security Engineer*, *Red Team Operator*, *DFIR*
- [ ] **Alignment with MITRE ATT&CK, NIST CSF, OWASP** so the map is also a study map
- [ ] **Community features** — issues template-driven additions, badge for contributors

See the full plan, scope boundaries, and non-goals in [VISION.md](VISION.md).

---

## Quickstart

```bash
git clone https://github.com/5h4d0wn1k/cybersecurity-framework
cd cybersecurity-framework
python3 scripts/build.py          # tree/*.json -> docs/data/tree.json + tree/*.md mirrors
python3 -m http.server 8000 --directory docs   # serve locally
# open http://localhost:8000
```

No build step, no npm, no framework — the site is a single vanilla-JS `docs/index.html`
pushed to GitHub Pages.

## Repository structure

```
tree/                  domain JSON (source of truth) + auto-generated .md mirrors
tree/_structure.json   pillar → main-category → domain grouping
docs/                  the GitHub Pages site (index.html + data/tree.json + robots + sitemap)
scripts/build.py       merges tree/*.json into the site data + markdown mirrors
SCHEMA.md              the tool-tree data format (v2, recursive)
ETHICS.md              intent & scope foundation — read first
SCOPE.md               the authorized-testing checklist
VISION.md              the education-platform roadmap
CONTRIBUTING.md        how to add tools / categories / fixes
```

---

## 🛡️ Ethics, legal & scope — read before using

This map exists to help owners and defenders test **their own** systems. Every tool here
must be used only on systems you own or for which you hold **explicit written
authorization**. Unauthorized access may violate the **CFAA (18 U.S.C. §1030)**,
the Wiretap Act, EU Directive 2013/40/EU, and local law.

- Read [ETHICS.md](ETHICS.md) — the four non-negotiable rules.
- Run the [SCOPE.md](SCOPE.md) four-question checklist before any live testing.
- This is an **atlas**, not a weapon. Categories are written from the defender/tester
  perspective: *never a how-to break into a third party; always a how-to check your own.*

---

## Contributing

We want the community to help complete the map. Open an issue or PR to add a tool, fix a
dead URL, or refine a `when-to-use`. 

- Read [CONTRIBUTING.md](CONTRIBUTING.md) first.
- Every addition must follow [SCHEMA.md](SCHEMA.md) — real, curated, safety-gated, no hype.

## License

**MIT** — free to use, remix, and redistribute with attribution. See [LICENSE](LICENSE).

---

**· an atlas of cyber education — always in scope, always educational. ·**