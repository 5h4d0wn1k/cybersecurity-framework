# 🧪 Application Security (SAST, DAST, Secrets & SCA)

Product-security gates for the code and recipes you ship: SAST, DAST, secrets detection, dependency (SCA), fuzzing, and threat modeling — nested by technique for dev and DevProd teams.

## Static Analysis (SAST)



#### viperstrike ◆ by 5h4d0wn1k

MCP (Model Context Protocol) server vulnerability auditor — AST/whitebox SAST for agentic AI tool handlers, SARIF-capable, optional oracle runtime mode.

**When:** Auditing MCP servers and AI tool endpoints for handler-level vulnerabilities.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/viperstrike`

**URL:** https://github.com/5h4d0wn1k/viperstrike

**Alternatives:** Own tool — lab/authorized use only


#### Multi-Language Engines


##### Semgrep ⭐

Lightweight app-sec static analyzer for 30+ languages: YAML rules that read like the code they match, bundled security packs (p/security-audit, p/owasp-top-ten), and pre-commit/CI/IDE hooks.

**When:** The default SAST layer for any dev team: run it per-PR in CI or in the editor to catch injection, dangerous-API misuse, and hardcoded secrets before merge.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install semgrep`

**URL:** https://github.com/semgrep/semgrep

**Alternatives:** codeql, bandit, gosec


##### CodeQL

GitHub's query-based analysis engine that databases your code and runs QL queries to find vulnerability classes; the CLI is free and the strongest maintained rule sets ship through GitHub code scanning.

**When:** High-signal coverage on GitHub-hosted repos: enable code scanning on schedules and PRs, then drop into the CodeQL CLI to run or author bespoke queries on a local database.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the CodeQL CLI bundle from github.com/github/codeql-action/releases`

**URL:** https://github.com/github/codeql

**Alternatives:** semgrep, sonarqube


##### SonarQube

Self-hosted code-quality and security platform: the Community Edition runs hundreds of static rules over 30+ languages with dashboards, quality gates, and trended security reports.

**When:** When an org needs a shared, dashboard-visible quality gate and SAST history instead of per-commit CLI output.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community`

**URL:** https://github.com/SonarSource/sonarqube

**Alternatives:** semgrep, codeql


#### Language-Specific Scanners


##### Python


###### Bandit ⭐

PyCQA's AST-based Python analyzer flags common first-party mistakes — SQLi, shell injection, pickles, eval, weak crypto, and path permissions — with a low-noise report you can tune.

**When:** A no-config SAST pass for Python services: pip-install, point it at the package directory, and wire into CI.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install bandit`

**URL:** https://github.com/PyCQA/bandit

**Alternatives:** semgrep, ruff


##### Go


###### gosec ⭐

SecureGo's Go static analyzer walking ASTs and data flow to find hardcoded creds, weak TLS configs, unsafe sql/exec sinks, and integer-overflow risk in first-party Go code.

**When:** The quick Go-specific SAST gate in CI, alongside or before a language-agnostic scanner like Semgrep.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/securego/gosec/v2/cmd/gosec@latest`

**URL:** https://github.com/securego/gosec

**Alternatives:** semgrep, govulncheck


##### Ruby


###### Brakeman ⭐

The reference Ruby on Rails scanner: static analysis tuned to Rails patterns (SQL injection, XSS, mass assignment, unsafe deserialization) with actionable remediation notes.

**When:** Any Rails/Ruby codebase in CI: one command and the framework-aware findings are worth more than generic engines.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `gem install brakeman`

**URL:** https://github.com/presidentbeef/brakeman

**Alternatives:** semgrep, codeql


##### Java & .NET


###### SpotBugs + FindSecBugs ⭐

SpotBugs is the Java bytecode static analyzer; the FindSecBugs plugin adds 120+ security patterns (path traversal, XXE, weak crypto, injection sinks) to its findings.

**When:** Java/JVM builds that need bytecode-level findings beyond a pattern scanner — wire the Maven/Gradle plugin into the build.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install spotbugs`

**URL:** https://github.com/spotbugs/spotbugs

**Alternatives:** semgrep, codeql


###### Security Code Scan (.NET)

An open-source Roslyn analyzer that adds taint-tracking security rules for C#: SQL injection, deserialization, path traversal, and cryptographically weak constructs.

**When:** .NET solutions in CI: install the NuGet analyzer and let it run inline with the build for zero extra infra.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `dotnet add package SecurityCodeScan.VS2019`

**URL:** https://github.com/security-code-scan/security-code-scan

**Alternatives:** semgrep


##### JavaScript & PHP


###### eslint-plugin-security ⭐

Node.js Security's ESLint plugin that flags hardcoded credentials, unsafe regex, non-literal require/child_process, and other JS security smells directly in lint output.

**When:** Node/JS repos already on ESLint: enable the security ruleset for the fastest in-editor security feedback.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `npm install --save-dev eslint-plugin-security`

**URL:** https://github.com/nodesecurity/eslint-plugin-security

**Alternatives:** semgrep, codeql


###### Psalm

PHP static analysis with a taint-check mode (`--taint-analysis`) that traces untrusted input to sinks for SQLi, XSS, file access, and more.

**When:** PHP projects wanting first-party vulnerability detection in CI without a managed SaaS.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `composer require --dev vimeo/psalm`

**URL:** https://github.com/vimeo/psalm

**Alternatives:** semgrep



## Dynamic Analysis (DAST)



#### CI & Pipeline Scanning


##### OWASP ZAP ⭐

Full web/API security scanner: intercepting proxy, spider, passive + active scanning, and a programmable REST API; ships zap-baseline.py and Docker images ready for automated CI DAST.

**When:** Stand up per-app DAST: run the baseline scan against a staging build nightly or per-PR, then use the proxy for manual testing of tricky auth flows.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run -t ghcr.io/zaproxy/zaproxy zap-baseline.py -t https://staging.example.com`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** nuclei, wapiti


##### Nuclei

ProjectDiscovery's template-driven vulnerability scanner with 8,000+ community YAML templates (CVEs, exposures, misconfigs) and fast protocol-level scanning.

**When:** Broad templated coverage across an app inventory — feed it URLs/HTTP inputs in CI and get CVE-check results without bespoke rules.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest`

**URL:** https://github.com/projectdiscovery/nuclei

**Alternatives:** OWASP ZAP, wapiti


##### Wapiti

Python black-box web scanner performing GET/POST parameter fuzzing for OWASP classes (SQLi, XSS, file inclusion, command injection) with a DAST REST API.

**When:** Scriptable scan of internal apps where you want a ZAP alternative with no Docker dependency and easy output automation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install wapiti3`

**URL:** https://github.com/wapiti-scanner/wapiti

**Alternatives:** OWASP ZAP, nuclei


#### Manual Testing Suites


##### Burp Suite ⭐

PortSwigger's leading web application testing platform: Community gives the intercepting proxy, history, and Repeater/Decoder manual tools free; the automated scanner is paid.

**When:** Manual pentest-style review of your own apps: drive the app through the proxy, then replay, tamper, and fuzz individual requests by hand.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install burpsuite`

**URL:** https://portswigger.net/burp

**Alternatives:** OWASP ZAP, Caido


##### Arachni

Ruby-based web scanner with a rich modular architecture and REST/WebSocket APIs; unmaintained for several years but deployable standalone or embedded.

**When:** Legacy stacks that ship its browser-based grid, or when you want its fingerprinting modules self-hosted — otherwise prefer ZAP or Nuclei.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `docker run -td --name arachni -p 9292:9292 aharbor/arachni`

**URL:** https://github.com/Arachni/arachni

**Alternatives:** OWASP ZAP, wapiti


#### API-Specific DAST


##### RESTler ⭐

Microsoft's stateful REST API fuzzer: ingests your OpenAPI spec, infers producer-consumer request dependencies, then fuzzes request sequences to surface 5xx crashes, resource leaks, and security-checker violations.

**When:** API-only DAST beyond the HTML UI: after a ZAP baseline, point RESTler at the schema to grind through every endpoint and parameter combination.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the RESTler release archive from github.com/microsoft/restler-fuzzer/releases`

**URL:** https://github.com/microsoft/restler-fuzzer

**Alternatives:** schemathesis


##### Schemathesis

Property-based API testing against OpenAPI/GraphQL schemas: generates edge-case and adversarial requests and can run its built-in security checks against each response.

**When:** Shift-left API testing in CI where you want schema-driven request generation plus explicit security assertions, with a GiHub Action.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `pipx install schemathesis`

**URL:** https://github.com/schemathesis/schemathesis

**Alternatives:** RESTler, OWASP ZAP



## Dependency Scanning (SCA)



#### Multi-Language Engines


##### OWASP Dependency-Check ⭐

OWASP's SCA utility that fingerprints declared dependencies (Java, .NET, Python, Node, Ruby, Go, Rust, and more) against NVD and other feeds, emitting CVSS-scored known-CVE reports.

**When:** The reference dependency gate for build output: run on release builds to block known-vulnerable libraries before they ship; the first run downloads the full NVD feed.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -v "$PWD":/src owasp/dependency-check --scan /src --out /report`

**URL:** https://github.com/dependency-check/DependencyCheck

**Alternatives:** osv-scanner, trivy


##### OSV-Scanner

Google's open-source vulnerability scanner (the engine behind GitHub Dependabot) that matches lockfiles and SBOMs against the OSV.dev database — fast, quiet, and free of NVD feed friction.

**When:** Snappy per-lockfile check in CI (package-lock.json, go.sum, requirements, poetry, etc.) when you want OSV-only coverage without a heavyweight feed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/google/osv-scanner/cmd/osv-scanner@latest`

**URL:** https://github.com/google/osv-scanner

**Alternatives:** OWASP Dependency-Check, pip-audit


#### Per-Ecosystem Lockfile Scanners


##### Python


###### pip-audit ⭐

Python Packaging Authority's scanner audits direct and transitive PyPI requirements against OSV/advisory feeds, and can auto-fix vulnerable packages installed locally (--fix).

**When:** Python-only repos: the smallest honest way to keep requirements.txt/pyproject dependency lists clean as part of pre-commit or CI.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install pip-audit`

**URL:** https://github.com/pypa/pip-audit

**Alternatives:** osv-scanner, OWASP Dependency-Check


##### Node.js


###### npm audit ⭐

Bundled npm command that checks the installed dependency tree against the npm advisory database and can auto-downgrade (`npm audit fix`) where a patched version exists.

**When:** Zero-setup Node dependency gate: run in CI after install and block on high/critical findings.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Bundled with npm — no install needed`

**URL:** https://docs.npmjs.com/cli/v10/commands/npm-audit

**Alternatives:** osv-scanner, OWASP Dependency-Check


##### Go


###### govulncheck ⭐

The Go team's vulnerability scanner: uses static analysis of function call graphs to report only findings that are actually reachable from your code, not every transitive dependency.

**When:** Go modules in CI: `govulncheck ./...` gives call-reachable CVEs with far less noise than generic SCA.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install golang.org/x/vuln/cmd/govulncheck@latest`

**URL:** https://github.com/golang/vuln

**Alternatives:** osv-scanner, gosec


##### Rust


###### cargo-audit ⭐

RustSec's lockfile auditor (cargo.lock) reporting known vulnerabilities from the RustSec Advisory Database, with `cargo audit fix` for auto-updates.

**When:** Rust projects in CI: run against the committed Cargo.lock every PR.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install cargo-audit`

**URL:** https://github.com/rustsec/cargo-audit

**Alternatives:** osv-scanner


#### Container Images & SBOMs


##### Grype + Syft ⭐

Anchore's pair: Syft generates SPDX/CycloneDX SBOMs from images and filesystems, Grype matches them against multiple vulnerability feeds with reachability-aware reporting in some modes.

**When:** Container-first SCA inside the build: generate the SBOM, scan it with Grype, and attach it as a build attestation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install anchore/grype/grype anchore/syft/syft`

**URL:** https://github.com/anchore/grype

**Alternatives:** trivy, OWASP Dependency-Check



## Secrets Detection



#### Git History & Repo Sweeps


##### Gitleaks ⭐

Fastest OSS secret scanner: a single Go binary that sweeps full git history or plain directories with 200+ regex rules for API keys, tokens, and passwords, exporting JSON/SARIF with pre-commit and GitHub Action hooks.

**When:** Gate every repo and pipeline: full-history sweep when onboarding, then pre-commit/PR scans from then on; the default before anything heavier.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/gitleaks/gitleaks/v8@latest`

**URL:** https://github.com/gitleaks/gitleaks

**Alternatives:** TruffleHog, detect-secrets


##### TruffleHog

Secret scanner with 600+ credential detectors that actively verify matches against vendor APIs to separate live credentials from noise; scans git, GitHub/GitLab orgs, S3, Docker, and filesystems.

**When:** Org-wide sweeps where knowing which leaked credentials still work matters more than raw match counts.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin`

**URL:** https://github.com/trufflesecurity/trufflehog

**Alternatives:** gitleaks, detect-secrets


#### Baseline & Diff-Based


##### detect-secrets ⭐

Yelp's Python scanner that audits a repo once into a .secrets.baseline then diffs only new lines in pre-commit/CI, so only genuinely new secrets get flagged instead of the same approved ones on every run.

**When:** Teams worn out by re-flagged false positives: do the one-time audit + baseline review, then let it police new commits.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install detect-secrets`

**URL:** https://github.com/Yelp/detect-secrets

**Alternatives:** gitleaks, git-secrets


#### Pipeline & Simple Mode


##### ggshield ⭐

GitGuardian's open-source CLI that scans commits, PRs, and CI output for secrets with pre-commit hooks and does live-verification checks; the hosted dashboard beyond it is commercial.

**When:** Pre-commit + CI hook coverage when you already use GitGuardian's engine conventions and want its detectors locally.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pipx install ggshield`

**URL:** https://github.com/GitGuardian/ggshield

**Alternatives:** gitleaks, TruffleHog



## Coverage-Guided Fuzzing



#### toxindb ◆ by 5h4d0wn1k

RAG retrieval-time poisoning detector — demand-recency discrimination, canary injection, provenance attestation; fully offline, SARIF+MD reports.

**When:** Checking your own RAG/vector knowledge bases for poisoned or injected content.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/toxindb`

**URL:** https://github.com/5h4d0wn1k/toxindb

**Alternatives:** Own tool — lab/authorized use only


#### Native / Binary Fuzzing


##### AFL++ ⭐

The maintained successor of American Fuzzy Lop: coverage-guided in-process fuzzing with QEMU and Frida modes, custom mutators, and calibration for both source and pure-binary targets.

**When:** Fuzz any C/C++ parser or binary you own: compile with afl-clang-fast, seed a corpus, and let parallel instances grind for crashes and hangs.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install afl++`

**URL:** https://github.com/AFLplusplus/AFLplusplus

**Alternatives:** honggfuzz, libFuzzer


##### libFuzzer

Clang's in-process, coverage-guided fuzzing library: link a fuzz target function, enable -fsanitize=fuzzer,address, and get corpus minimization plus sanitizer-detected crashes for free.

**When:** C/C++ libraries in LLVM builds where in-process fuzzing with ASan/UBSan finds more per second than fork-based engines.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Built into clang — compile with -fsanitize=fuzzer,address`

**URL:** https://llvm.org/docs/LibFuzzer.html

**Alternatives:** AFL++, honggfuzz


##### Honggfuzz

Google's coverage-guided fuzzer with hardware-based performance counters (Intel PT), persistent mode, and simple configuration; strong on Linux for network and file-parsing targets.

**When:** When you want hardware-assisted coverage on Linux or a fast standalone alternative to AFL++ for your parsers.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/google/honggfuzz.git && cd honggfuzz && make`

**URL:** https://github.com/google/honggfuzz

**Alternatives:** AFL++, libFuzzer


#### Managed Runtimes (JVM)


##### Jazzer ⭐

CodeIntelligence's JVM coverage-guided fuzzer built on libFuzzer: fuzzes Java/Kotlin through a JNI agent with sanitizer-like detection of OOM, stack overflow, and exception-based failures.

**When:** Grab your @FuzzTest hooks and parse untrusted Java input (JSON, XML, protobuf) to find exceptions, hangs, and memory issues.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the Jazzer release archive from github.com/CodeIntelligenceTesting/jazzer/releases`

**URL:** https://github.com/CodeIntelligenceTesting/jazzer

**Alternatives:** AFL++, libFuzzer


#### Fuzzing Infrastructure


##### OSS-Fuzz ⭐

Google's open-source continuous fuzzing service for critical OSS: builds your project with sanitizers, runs libFuzzer/AFL++/Honggfuzz at scale, and files issues when new bugs are found.

**When:** You maintain a widely-used open-source library with a C/C++/Golang/Rust surface and want Google-scale fuzzing with zero infra of your own.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Follow google/oss-fuzz quickstart (Docker + build.sh) — no direct install`

**URL:** https://github.com/google/oss-fuzz

**Alternatives:** libFuzzer, AFL++


#### Research & Benchmarks


##### ProFuzzBench ⭐

TU Delft's highly-configurable benchmark for stateful protocol fuzzing: 8 real network protocols with reproducible AFLNet/AFL++/libFuzzer harnesses and Docker-based campaigns.

**When:** Evaluate or compare protocol fuzzers, or learn stateful fuzzing against realistic targets before applying it to your own servers.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/profuzzbench/profuzzbench.git`

**URL:** https://github.com/profuzzbench/profuzzbench

**Alternatives:** OSS-Fuzz



## Threat Modeling



#### Visual & Diagram-First


##### OWASP Threat Dragon ⭐

OWASP's open-source threat-model tooling for STRIDE/LINDDUN workflows with a browser-based or desktop diagram UI that exports models to JSON for CI review automation.

**When:** Teams that want a shared, reviewable threat model per service without forcing every engineer to learn a coding DSL.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d -p 3000:3000 owasp/threat-dragon`

**URL:** https://github.com/OWASP/threat-dragon

**Alternatives:** pytm, Threagile


#### Threat Models as Code


##### pytm ⭐

OWASP's Pythonic framework: define your system as Python objects and generate data-flow diagrams, STRIDE threat lists, and mitigations — diffs cleanly in git and runs in CI.

**When:** When the threat model must live in the repo and be code-reviewed like any other artifact, or is derived from your IaC definitions.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install pytm`

**URL:** https://github.com/OWASP/pytm

**Alternatives:** Threat Dragon, Threagile


##### Threagile

Agile threat-modeling toolkit driven by a YAML architecture description: auto-generates STRIDE-based risks, diagrams, and reports via CLI or Kubernetes operator, with a rules engine.

**When:** Organizations that standardize on YAML-first threat modeling and want automated risk catalogs from the same source of truth.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run --rm -v "$PWD":/app threagile/threagile`

**URL:** https://github.com/threagile/threagile

**Alternatives:** pytm, Threat Dragon



