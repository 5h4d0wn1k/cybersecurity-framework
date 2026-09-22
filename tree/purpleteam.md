# 🟣 Purple Team, BAS & Adversary Emulation

Validate your detections by emulating real adversaries, running atomic TTPs, and mapping coverage against MITRE ATT&CK.

## Adversary Emulation & ATT&CK Operations




#### Emulation Platforms & Playbooks



##### MITRE Caldera ⭐

Automated adversary emulation platform (now an Apache project) built on ATT&CK: deploy agents, craft adversary profiles from techniques, and run them against your estate.

**When:** Build a repeatable adversary operation once and re-run it after every detection change or control rollout.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone --recursive https://github.com/apache/caldera.git`

**URL:** https://github.com/apache/caldera

**Alternatives:** atomic-red-team, adversary-emulation-library


##### Adversary Emulation Library

MITRE Center for Threat-Informed Defense's full (APT29, FIN6, Turla) and micro (webshells, process injection) emulation plans in human-readable plus machine-readable YAML for Caldera.

**When:** Execute a threat-intel-grounded scenario as a ready-made purple-team script instead of writing one from scratch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/center-for-threat-informed-defense/adversary_emulation_library.git`

**URL:** https://github.com/center-for-threat-informed-defense/adversary_emulation_library

**Alternatives:** mitre-caldera, ptef


##### PurpleSharp

C# adversary simulation tool that executes ATT&CK-mapped TTPs purely from Windows endpoints (process execution, scheduled tasks, WMI, Kerberos abuse) without needing a C2.

**When:** Run in-host purple exercises fast: trigger technique sequences and immediately check which SIEM/EDR detections fired.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/mvelazc0/PurpleSharp.git`

**URL:** https://github.com/mvelazc0/PurpleSharp

**Alternatives:** atomic-red-team, caldera


#### Atomic TTP Tests



##### Atomic Red Team ⭐

MITRE-aligned library of small, portable detection tests; each atomic test documents a technique's exact procedure plus the logs and telemetry a defender should see if the detection works.

**When:** Prove a specific detection fires by running the precise TTP procedure it was built to catch.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Install-Module -Name invoke-atomicredteam -Scope CurrentUser -Force`

**URL:** https://github.com/redcanaryco/atomic-red-team

**Alternatives:** atomictestharnesses, caldera


##### AtomicTestHarnesses

Red Canary's PowerShell module (Python for macOS/Linux) that executes many variations of a single technique and validates the telemetry each variation generates.

**When:** Check your detections hold up across technique variants, not just the single canonical procedure.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force`

**URL:** https://github.com/redcanaryco/AtomicTestHarnesses

**Alternatives:** atomic-red-team


#### Cloud Adversary Emulation



##### Stratus Red Team ⭐

Datadog's granular cloud emulation library — 'Atomic Red Team for the cloud' — detonating AWS, Azure, GCP, Entra ID, and K8s techniques mapped to ATT&CK with automatic warmup and cleanup.

**When:** Validate cloud SIEM detections against real TTPs in a dedicated sandbox cloud account, never production.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install stratus-red-team`

**URL:** https://github.com/DataDog/stratus-red-team

**Alternatives:** cloudgoat, infection-monkey


##### CloudGoat 2

Rhino Security Labs' 'Vulnerable by Design' AWS/Azure deployment tool that builds intentionally vulnerable, CTF-style scenarios for practicing cloud attack paths.

**When:** Stand up an authorized practice range in a throwaway cloud account to rehearse TTPs before running real emulation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install cloudgoat`

**URL:** https://github.com/RhinoSecurityLabs/cloudgoat

**Alternatives:** stratus-red-team


#### ATT&CK Reference for Emulation



##### MITRE ATT&CK Navigator ⭐

Web app for annotating and exploring ATT&CK matrices via shareable layer files; load emulation-plan technique lists to plan what you are about to run.

**When:** Scope an emulation exercise by marking the techniques on the matrix before touching any platform.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://github.com/mitre-attack/attack-navigator

**Alternatives:** mitre-attack, dettect


##### MITRE ATT&CK

The authoritative knowledge base: adversary tactics, techniques, sub-techniques, threat groups, and the data sources needed to detect them.

**When:** Resolve technique IDs and read detection guidance before any scoring, emulation, or rule building.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://attack.mitre.org

**Alternatives:** attack-navigator






## Breach & Attack Simulation




#### Open-source BAS



##### Infection Monkey ⭐

Open-source BAS platform (Guardicore/Akamai) whose agent self-propagates across a network via real exploiters and misconfiguration checks, reporting findings to the Monkey Island console.

**When:** Automated lateral-movement and control-gap testing on a lab segment or isolated data-center island.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker pull guardicore/monkey-island:latest`

**URL:** https://github.com/guardicore/monkey

**Alternatives:** openbas, stratus-red-team


##### OpenBAS

Filigran's open-source breach-and-attack simulation platform (now evolving into OpenAEV) for planning, scheduling, and running adversary-simulation campaigns and crisis exercises.

**When:** When you need a free multi-team BAS platform that couples technical simulations with exercise tracking, integrated with OpenCTI threat intel.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/OpenBAS-Platform/openbas.git`

**URL:** https://github.com/OpenBAS-Platform/openbas

**Alternatives:** infection-monkey, vectr


#### Commercial BAS



##### SafeBreach Validate ⭐

Commercial BAS pioneer: lightweight simulators on endpoints, network, and cloud run 30,000+ attack methods from its Hacker's Playbook to continuously validate controls.

**When:** Continuous, enterprise-scale security-control validation when you have budget for a licensed BAS product.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial (trial via safebreach.com)`

**URL:** https://www.safebreach.com/validate-breach-and-attack-simulation/

**Alternatives:** attackiq, cymulate


##### AttackIQ

MITRE ATT&CK-aligned BAS platform with a free AttackIQ Flex tier and a large scenario library that continuously exercises prevention, detection, and response controls.

**When:** Continuous control validation with ATT&CK coverage reporting baked into the vendor platform.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial (freemium via attackiq.com)`

**URL:** https://www.attackiq.com/

**Alternatives:** safebreach-validate, cymulate


##### Cymulate

BAS platform that deploys lightweight agents to simulate the full kill chain plus exposure management, scoring security posture with prioritized remediation guidance.

**When:** Benchmark your controls against sector peers and get prioritized gap remediation from one dashboard.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial (trial via cymulate.com)`

**URL:** https://www.cymulate.com/

**Alternatives:** safebreach-validate, attackiq






## Detection Test Harnesses & Labs




#### Detection Lab Environments



##### DetectionLab ⭐

Chris Long's Packer/Vagrant suite that builds a Windows domain pre-loaded with Sysmon, WEF, osquery, and Splunk plus hardened logging defaults (no longer actively maintained since 2023, but still widely used).

**When:** Spin up a known-good instrumented AD lab to test detections against realistic Windows telemetry.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/clong/DetectionLab.git`

**URL:** https://github.com/clong/DetectionLab

**Alternatives:** splunk-attack-range, detectionlab-primer


##### DetectionLab Primer

The official DetectionLab documentation/introduction: architecture, deployment guides for VirtualBox, AWS, Azure, and Hyper-V, and walkthroughs of each pre-installed tool.

**When:** Read before first build so you pick the right provider and understand what logging you are getting.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://detectionlab.network/introduction/

**Alternatives:** detectionlab


##### Splunk Attack Range

Splunk Threat Research Team's Terraform/Ansible range that deploys instrumented AWS/Azure/GCP labs, runs Atomic Red Team and PurpleSharp simulations, and forwards telemetry into Splunk.

**When:** Develop and CI-test Splunk detections against reproducible attack data in an isolated cloud range.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker compose -f docker/docker-compose.yml up`

**URL:** https://github.com/splunk/attack_range

**Alternatives:** detectionlab, atomic-red-team


#### Purple Team Exercise Frameworks



##### Purple Team Exercise Framework (PTEF) ⭐

SCYTHE's industry-standard methodology (v4) for designing purple-team exercises: planning templates, TTP mapping spreadsheets, emulation-plan formats, and a maturity model.

**When:** Structure your first (or fiftieth) purple exercise so CTI, red, and blue roles, evidence collection, and lessons-learned are all defined up front.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/scythe-io/purple-team-exercise-framework.git`

**URL:** https://github.com/scythe-io/purple-team-exercise-framework

**Alternatives:** owasp-purpleteam, vectr


##### OWASP PurpleTeam

OWASP's open purpleteam tooling: an orchestrator with TLS and application scanning components that run coordinated security tests and report results for CI use.

**When:** Add repeatable purpleteam-style scanning checks to an application/TLS hardening pipeline.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/purpleteam-labs/purpleteam-orchestrator.git`

**URL:** https://owasp.org/www-project-purpleteam/

**Alternatives:** ptef






## Detection Coverage Mapping




#### ATT&CK Coverage Scoring



##### DeTT&CT ⭐

Rabobank's framework to administer and score data-source quality, visibility, and detection per ATT&CK technique, then export the resulting coverage as ATT&CK Navigator layers.

**When:** Build a scored, evidence-based map of detection and visibility coverage and prioritize blue-team effort on the gaps.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/rabobank-cdc/DeTTECT.git`

**URL:** https://github.com/rabobank-cdc/DeTTECT

**Alternatives:** attack-navigator, mitre-car


##### MITRE ATT&CK Navigator

Web app for annotating and exploring ATT&CK matrices via shareable layer files; load DeTT&CT or VECTR output to render coverage heatmaps.

**When:** Visualize and communicate detection coverage across the matrix during and after purple exercises.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://github.com/mitre-attack/attack-navigator

**Alternatives:** dettect, mitre-attack


#### MITRE Analytic & Defense Ontologies



##### MITRE CAR ⭐

MITRE Cyber Analytics Repository: a curated set of analytics, each tied to ATT&CK techniques with data requirements, pseudocode, and reference implementations for validating detections.

**When:** Find analytics worth implementing when you know which ATT&CK technique you need coverage for.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://car.mitre.org

**Alternatives:** d3fend, shield


##### MITRE D3FEND

Counter-adversary engineering knowledge graph of digital artifacts, tactics, and hardening techniques — the defensive counterpart to ATT&CK for describing how countermeasures work.

**When:** Name and structure defensive countermeasures precisely when documenting what each control actually prevents.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://d3fend.mitre.org

**Alternatives:** mitre-car, shield


##### MITRE SHIELD

Active defense knowledge base of techniques defenders can use to engage adversaries (deception, hunting, hardening), mapped to ATT&CK for planning proactive defense operations.

**When:** Plan proactive or deception-based defenses that complement your detection coverage map.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://shield.mitre.org

**Alternatives:** d3fend, mitre-car


#### Detection Content Testing



##### YARA Rule Testers



###### yara-x ⭐

VirusTotal's Rust rewrite of YARA with a strict compiler that surfaces syntax errors and warnings early, plus a fast CLI for scanning samples with your rules.

**When:** Compile and regression-test YARA rules in CI — stricter diagnostics catch broken rules before deployment.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install yara-x --bins`

**URL:** https://github.com/VirusTotal/yara-x

**Alternatives:** yara, yara-validator


###### YARA

The de-facto pattern-matching engine for malware rules; `yara -w` compiles rule sets and flags syntax problems before you scan anything.

**When:** The baseline check: compile your rules locally and run them against known samples to confirm hits and false positives.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install yara`

**URL:** https://github.com/VirusTotal/yara

**Alternatives:** yara-x, yara-validator


###### CIRCL yara-validator

CIRCL's Python validator that compiles batches of YARA rules, reports which are broken, and attempts automatic repairs on include-related breakage.

**When:** Bulk-validate a shared rule repository before merging changes.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip3 install yara_validator`

**URL:** https://github.com/CIRCL/yara-validator

**Alternatives:** yara-x, cccs-yara


###### YaraValidator online

Free web validator that compiles rules against current YARA and YARA-X versions to catch compatibility issues without any local install.

**When:** Instant one-off compatibility check of a rule paste across engine versions.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://yaravalidator.manalyzer.org/

**Alternatives:** yara-x, yara


##### Sigma Detection Rule Pipeline



###### Sigma ⭐

Vendor-agnostic detection rule format with a converter ecosystem that turns portable Sigma rules into Splunk, Elastic, QRadar, Sentinel, and dozens of other query languages.

**When:** Write detection content once and compile it to every SIEM you run; the shared syntax is also easy to unit-test.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install sigma-cli`

**URL:** https://github.com/SigmaHQ/sigma

**Alternatives:** sigma-cli, elastic-detection-rules


###### Sigma CLI

Official SigmaHQ CLI (sigma-cli) that converts, validates, and tests Sigma rules against backend plugins, catching broken syntax and unsupported constructs.

**When:** Automate rule conversion and linting in CI so bad Sigma never reaches a SIEM.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install sigma-cli`

**URL:** https://github.com/SigmaHQ/sigma-cli

**Alternatives:** sigma, elastic-detection-rules


###### Elastic detection-rules

Elastic's production rule repository with prebuilt and custom Sigma-style rules, plus tooling (detection-rules CLI) to unit-test, version, and package rules for the Elastic Stack.

**When:** Benchmark your own rule quality against vendor-maintained content and test rules before shipping to Elastic.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install -r requirements.txt`

**URL:** https://github.com/elastic/detection-rules

**Alternatives:** sigma






## Exercise Tracking & Metrics




#### Result & Campaign Tracking



##### VECTR ⭐

Free purple-team platform (Security Risk Advisors) that tracks red/blue test cases, campaigns, and per-tool detection/prevention outcomes measured against MITRE ATT&CK over time.

**When:** Record exercise results and trend detection coverage over months so purple-team improvements are measurable.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/SecurityRiskAdvisors/VECTR.git`

**URL:** https://github.com/SecurityRiskAdvisors/VECTR

**Alternatives:** dettect, attack-flow


##### MITRE Attack Flow

Center for Threat-Informed Defense's STIX-based format and tooling for modeling how adversary behaviors chain together within an operation or campaign.

**When:** Document the full flow of an emulated campaign — not just isolated techniques — for reporting and ATT&CK mapping.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/center-for-threat-informed-defense/attack-flow.git`

**URL:** https://github.com/center-for-threat-informed-defense/attack-flow

**Alternatives:** vectr, dettect





