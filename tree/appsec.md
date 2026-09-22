# 🧪 Application Security (SAST, DAST, Secrets & SCA)

Product-security gates for the code and recipes you ship: SAST, DAST, secrets detection, dependency (SCA), and IaC scanning for dev and DevProd teams.

## Static Analysis (SAST)

### Semgrep ⭐

Lightweight app-sec static analyzer for 30+ languages: YAML rules that read like the code they match, bundled security packs (p/security-audit, p/owasp-top-ten), and pre-commit/CI/IDE hooks; the free CLI covers single-function/file patterns while the commercial AppSec Platform adds cross-function taint.

**When:** The default SAST layer for any dev team: run it per-PR in CI or in the editor to catch injection, dangerous-API misuse, and hardcoded secrets before merge.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install semgrep`

**URL:** https://github.com/semgrep/semgrep

**Alternatives:** codeql, bandit, gosec


### SonarQube

Self-hosted code-quality and security platform: the free LGPL Community Edition runs hundreds of static rules over 30+ languages with dashboards, quality gates, and trended security reports; paid tiers add branch analysis and deeper coverage.

**When:** When an org needs a shared, dashboard-visible quality gate and SAST history instead of per-commit CLI output.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community`

**URL:** https://github.com/SonarSource/sonarqube

**Alternatives:** semgrep, codeql


### CodeQL

GitHub's query-based analysis engine that databases your code and runs QL queries to find vulnerability classes; the CLI is free, and the strongest maintained rule sets ship through GitHub code scanning.

**When:** High-signal coverage on GitHub-hosted repos: enable code scanning on schedules and PRs, then drop into the CodeQL CLI to run or author bespoke queries on a local database.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the CodeQL CLI bundle from github.com/github/codeql-action/releases`

**URL:** https://github.com/github/codeql

**Alternatives:** semgrep, sonarqube


### Bandit

PyCQA's AST-based Python analyzer that flags common first-party security mistakes - SQLi, shell injection, pickles, eval, weak crypto, and path permissions - with a low-noise report of findings you can tune.

**When:** A no-config SAST pass for Python services: pip-install, point it at the package directory, and wire into CI.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install bandit`

**URL:** https://github.com/PyCQA/bandit

**Alternatives:** semgrep, gosec


### gosec

SecureGo's Go static analyzer walking ASTs and data flow to find hardcoded creds, weak TLS configs, unsafe sql/exec sinks, and integer-overflow risk in first-party Go code.

**When:** The quick Go-specific SAST gate in CI, alongside or before a language-agnostic scanner like Semgrep.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/securego/gosec/v2/cmd/gosec@latest`

**URL:** https://github.com/securego/gosec

**Alternatives:** semgrep, bandit


## Dynamic Analysis (DAST)

### OWASP ZAP ⭐

Full web/API security scanner: intercepting proxy, spider, passive + active scanning, and a programmable REST API; ships zap-baseline.py and Docker images ready for automated CI DAST against the apps you deploy.

**When:** Stand up per-app DAST: run the baseline scan against a staging build nightly or per-PR, then use the proxy for manual testing of tricky auth and authorization flows.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install zaproxy`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** burp suite community, restler


### Burp Suite Community

PortSwigger's leading web application testing platform: the free Community Edition gives you the intercepting proxy, a searchable request/response history, and Repeater/Decoder/Comparer manual tools; the automated scanner requires paid Pro or Enterprise editions.

**When:** Manual pentest-style review of your own apps: drive the app through the proxy, then replay, tamper, and fuzz individual requests by hand.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web) - free Community download from portswigger.net`

**URL:** https://portswigger.net/burp

**Alternatives:** owasp zap, restler


### RESTler

Microsoft's stateful REST API fuzzer: ingests your OpenAPI spec, infers producer-consumer request dependencies, then fuzzes request sequences against the live service to surface 5xx crashes, resource leaks, and security-checker violations.

**When:** API-only DAST beyond the HTML UI: after a ZAP baseline, point RESTler at the schema to grind through every endpoint and parameter combination.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the RESTler release archive from github.com/microsoft/restler-fuzzer/releases`

**URL:** https://github.com/microsoft/restler-fuzzer

**Alternatives:** owasp zap


## Secrets Detection

### Gitleaks ⭐

Fastest OSS secret scanner: a single Go binary that sweeps full git history or plain directories with 200+ regex rules for API keys, tokens, and passwords, exporting JSON/SARIF, with pre-commit and GitHub Action hooks.

**When:** Gate every repo and pipeline: full-history sweep when onboarding, then pre-commit/PR scans from then on; the default before anything heavier.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/gitleaks/gitleaks/v8@latest`

**URL:** https://github.com/gitleaks/gitleaks

**Alternatives:** trufflehog, detect-secrets, ggshield


### TruffleHog

Secret scanner (trufflesecurity) with 600+ credential detectors that actively verify matches against vendor APIs to separate live credentials from noise; scans git, GitHub/GitLab orgs, S3, Docker, and filesystems.

**When:** Org-wide and history-hardening sweeps where knowing which leaked credentials still work matters more than raw match counts.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin`

**URL:** https://github.com/trufflesecurity/trufflehog

**Alternatives:** gitleaks, detect-secrets, ggshield


### detect-secrets

Yelp's Python scanner that audits a repo once into a .secrets.baseline then diffs only new lines in pre-commit/CI, so only genuinely new secrets get flagged instead of the same approved ones on every run.

**When:** Teams worn out by re-flagged false positives: do the one-time audit + baseline review, then let it police new commits.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install detect-secrets`

**URL:** https://github.com/Yelp/detect-secrets

**Alternatives:** gitleaks, git-secrets


### git-secrets

AWS Labs' original git-hook guard that registers grep patterns (including a ready AWS credential set) as client-side commit hooks so secrets never land in history; legacy and effectively unmaintained.

**When:** Last-resort hook-only protection on old, isolated repos - otherwise reach for Gitleaks or TruffleHog.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/awslabs/git-secrets && cd git-secrets && make install`

**URL:** https://github.com/awslabs/git-secrets

**Alternatives:** gitleaks, detect-secrets


## Dependency Scanning (SCA)

### OWASP Dependency-Check ⭐

OWASP's SCA utility that fingerprints declared dependencies (Java, .NET, Python, Node, Ruby, Go, Rust, and more) against NVD and other feeds, emitting HTML/XML reports of CVSS-scored known-CVE matches; ships CLI, Gradle/Maven plugins, and a GitHub Action.

**When:** The reference dependency gate for build output: run on release builds to block known-vulnerable libraries before they ship; the first run downloads the full NVD feed, so schedule it early.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -v "$PWD":/src owasp/dependency-check --scan /src --out /report`

**URL:** https://github.com/dependency-check/DependencyCheck

**Alternatives:** osv-scanner, pip-audit, trivy (container & SBOM scans)


### osv-scanner

Google's open-source vulnerability scanner (the engine behind GitHub Dependabot) that matches your lockfiles and SBOMs against the OSV.dev database - fast, quiet, and free of NVD feed friction.

**When:** Snappy per-lockfile check in CI (package-lock.json, go.sum, requirements, poetry, etc.) when you want OSV-only coverage without a heavyweight feed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/google/osv-scanner/cmd/osv-scanner@latest`

**URL:** https://github.com/google/osv-scanner

**Alternatives:** pip-audit, owasp dependency-check


### pip-audit

Python Packaging Authority's scanner that audits direct and transitive PyPI requirements against OSV/advisory feeds, and can even auto-fix vulnerable packages installed locally (--fix).

**When:** Python-only repos: the smallest honest way to keep requirements.txt/pyproject dependency lists clean as part of pre-commit or CI.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install pip-audit`

**URL:** https://github.com/pypa/pip-audit

**Alternatives:** osv-scanner, owasp dependency-check


## Infrastructure-as-Code Security

### Checkov ⭐

Prisma Cloud-maintained IaC static analyzer with 1,000+ built-in policies for Terraform (incl. plan output), CloudFormation, Kubernetes, Helm, Dockerfile, Bicep, ARM, and Serverless; graph-based and multi-resource aware, with Python/YAML custom policies.

**When:** The default IaC gate: scan Terraform/K8s/Dockerfile in CI and on terraform plan to catch exposed resources, weak IAM, and missing encryption before apply.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install checkov`

**URL:** https://github.com/bridgecrewio/checkov

**Alternatives:** kics, terrascan (archived Nov 2025), trivy (also scans IaC via tfsec)


### KICS

Checkmarx's open-source IaC scanner (Keeping Infrastructure as Code Secure) running thousands of queries across 20+ platforms - Terraform, Kubernetes, Docker, Helm, CloudFormation, Ansible - with SARIF/SonarQube output and custom queries via OPA/Rego.

**When:** A complementary cross-check on IaC after Checkov, or the pick when you want OPA/Rego policy authoring (the slot that archived Terrascan used to fill).

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -t -v "$PWD":/path checkmarx/kics:latest scan -p /path -o /path`

**URL:** https://github.com/Checkmarx/kics

**Alternatives:** checkov, terrascan (archived Nov 2025)

