# SCOPE.md — Scope-checker for authorized testing

Before you run *anything* on a live target, answer these four questions. Write the answers
down. If you cannot answer "YES" to all four, **stop** — build a lab instead.

| # | Question | Acceptable answer |
|---|---|---|
| 1 | **Who owns the target?** Is it your hardware, your network, your cloud account, your code? | YES — I control it |
| 2 | **Do you have written permission?** Signed scope doc, bug-bounty program rules, employer authorization? | YES — written, current, bounded |
| 3 | **What is the blast radius?** What breaks if a scan or exploit goes wrong? Production? Client data? | YES — I've identified it and accepted it |
| 4 | **When does it end?** Time-boxed? Can you fully undo/clean up your testing? | YES — start/end defined |

## No-lab fork

If any answer is NO or unknown, use the **lab path** instead:

- Own router/AP → wireless & network testing (change the password after)
- Your laptop/VM → OS, malware, forensics
- `localhost` services, disposable containers → web/app/network
- A second radio you own → wireless
- HIPAA/PII/systems you don't control → **out of scope, always**

## Reporting an accidental hit

If you find a real vuln on a third party during authorized testing of a parent engagement:
1. Stop the specific test.
2. Report to the system owner privately, with timestamps and no PoC code reuse.
3. Follow the engagement's disclosure rules (usually coordinated disclosure).
4. Never publish without permission.

---

This checklist is the *operational* half of [ETHICS.md](ETHICS.md). The map stays legal and
useful because the user stays scoped. See [VISION.md](VISION.md) §7 for the permanent scope
boundaries of the project — including what will never be added to the map.