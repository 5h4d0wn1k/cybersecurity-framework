# 🟣 Purple Team, BAS & Adversary Emulation

Validate your detections by emulating real adversaries, running atomic TTPs, and mapping coverage against MITRE ATT&CK.

## Adversary Emulation Platforms

### MITRE Caldera ⭐

Automated adversary emulation platform built on ATT&CK, now an Apache project: deploy agents, craft adversary profiles from ATT&CK techniques, and run them against your own estate for blue-team validation.

**When:** Build a repeatable adversary operation once and re-run it after every detection change or control rollout.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone --recursive https://github.com/apache/caldera.git`

**URL:** https://github.com/apache/caldera

**Alternatives:** adversary-emulation-library


### Adversary Emulation Library

MITRE Center for Threat-Informed Defense's library of full (APT29, FIN6, Turla) and micro (webshells, process injection) emulation plans in human-readable plus machine-readable YAML for Caldera.

**When:** Execute a threat-intel-grounded scenario as a ready-made purple-team script instead of writing one from scratch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/center-for-threat-informed-defense/adversary_emulation_library.git`

**URL:** https://github.com/center-for-threat-informed-defense/adversary_emulation_library

**Alternatives:** mitre-caldera


## Atomic Tests & Detection Validation

### Atomic Red Team ⭐

MITRE-aligned library of small, portable detection tests; each atomic test documents a technique's exact procedure plus the logs and telemetry a defender should see if their detection works.

**When:** Prove a specific detection fires by running the precise TTP procedure it was built to catch.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Install-Module -Name invoke-atomicredteam -Scope CurrentUser -Force`

**URL:** https://github.com/redcanaryco/atomic-red-team

**Alternatives:** atomictestharnesses


### AtomicTestHarnesses

Red Canary's PowerShell module (Python for macOS/Linux) that executes many variations of a single technique and validates the telemetry each variation generates.

**When:** Check your detections hold up across technique variants, not just the single canonical procedure.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force`

**URL:** https://github.com/redcanaryco/AtomicTestHarnesses

**Alternatives:** atomic-red-team


## Breach & Attack Simulation

### Infection Monkey ⭐

Open-source BAS/adversary emulation platform (Guardicore/Akamai) whose agent self-propagates across a network via real exploiters and reports to the Monkey Island console.

**When:** Automated lateral-movement and control-gap testing on a lab segment or isolated data-center island.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker pull guardicore/monkey-island:latest`

**URL:** https://github.com/guardicore/monkey

**Alternatives:** safebreach-validate, stratus-red-team


### SafeBreach Validate

Commercial BAS pioneer: lightweight simulators on endpoints, network, and cloud run 30,000+ attack methods from its Hacker's Playbook to continuously validate controls.

**When:** Continuous, enterprise-scale security-control validation when you have budget for a licensed BAS product.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial (trial via safebreach.com)`

**URL:** https://www.safebreach.com/validate-breach-and-attack-simulation/

**Alternatives:** infection-monkey


### Stratus Red Team

Cloud-oriented BAS: 'Atomic Red Team for the cloud', with granular AWS/Azure/GCP/Entra ID/K8s techniques that detonate then clean up after themselves; the star of the cloud-bas category.

**When:** When your attack surface is cloud-first — jump to the cloud-bas category where Stratus is the pick.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install stratus-red-team`

**URL:** https://github.com/DataDog/stratus-red-team

**Alternatives:** infection-monkey


## Detection Coverage Mapping

### DeTT&CT ⭐

Rabobank's framework to administer and score data-source quality, visibility, and detection per ATT&CK technique, then export the resulting coverage as ATT&CK Navigator layers.

**When:** Build a scored, evidence-based map of your detection and visibility coverage and prioritize blue-team effort on the gaps.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/rabobank-cdc/DeTTECT.git`

**URL:** https://github.com/rabobank-cdc/DeTTECT

**Alternatives:** attack-navigator


### MITRE ATT&CK (website)

The authoritative knowledge base: adversary tactics, techniques, sub-techniques, threat groups, and the data sources needed to detect them.

**When:** Resolve technique IDs and read detection guidance before any scoring, emulation, or rule building.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://attack.mitre.org

**Alternatives:** attack-navigator


### ATT&CK Navigator

Web app for annotating and exploring ATT&CK matrices via shareable layer files; load DeTT&CT or VECTR output to render coverage heatmaps.

**When:** Visualize and communicate detection coverage across the matrix during and after purple exercises.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://github.com/mitre-attack/attack-navigator

**Alternatives:** dettect


## Cloud Breach & Attack Simulation

### Stratus Red Team ⭐

Datadog's cloud BAS: a self-contained Go binary that detonates granular cloud attack techniques for AWS, Azure, GCP, Entra ID, and K8s, mapped to the ATT&CK cloud matrix, with automatic warmup and cleanup.

**When:** Validate your cloud SIEM detections against real TTPs on a dedicated sandbox cloud account, never production.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install stratus-red-team`

**URL:** https://github.com/DataDog/stratus-red-team

**Alternatives:** cloudgoat


### CloudGoat 2

Rhino Security Labs' 'Vulnerable by Design' AWS/Azure deployment tool that builds intentionally vulnerable, CTF-style scenarios for practicing cloud attack paths.

**When:** Stand up an authorized practice range in a throwaway cloud account to rehearse TTPs before running real emulation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install cloudgoat`

**URL:** https://github.com/RhinoSecurityLabs/cloudgoat

**Alternatives:** stratus-red-team


## Exercise Tracking & Metrics

### VECTR ⭐

Free purple-team platform (Security Risk Advisors) that tracks red/blue test cases, campaigns, and per-tool detection/prevention outcomes measured against MITRE ATT&CK over time.

**When:** Record exercise results and trend detection coverage over months so purple-team improvements are measurable.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/SecurityRiskAdvisors/VECTR.git`

**URL:** https://github.com/SecurityRiskAdvisors/VECTR

**Alternatives:** dettect

