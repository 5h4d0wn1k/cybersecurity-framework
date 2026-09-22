# 📡 Threat Intelligence, Sharing & Detection Engineering

Enrich your own defenses: share and consume intel, pivot on IOCs, and write portable detections against common frameworks.

## Threat Intelligence Sharing & Platforms

### MISP ⭐

The open-source intelligence sharing platform: community-synced events, TLP/orgs, feed syncing, and a REST API for exchanging malware and attack indicators with trusted partners at scale.

**When:** Run or sync a MISP instance when you need structured, governed intel sharing across your team, an ISAC-style community, or your own feed ingestion pipeline.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo bash INSTALL/INSTALL.sh from MISP codebase (Ubuntu/Kali): wget -O /tmp/INSTALL.sh https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/INSTALL.sh && sudo bash /tmp/INSTALL.sh`

**URL:** https://github.com/MISP/MISP

**Alternatives:** OpenCTI, TAXII 2


### OpenCTI

Filigran's open cyber-threat-intelligence platform: ingests from 100+ connectors into a STIX-based knowledge graph with worker-managed import, investigations, and STIX/TAXII 2 exchange.

**When:** Stand up a central intel drive when you want automated feed ingestion (MISP, MITRE, abuse.ch) correlated into entities, reports, and indicators rather than raw IOC lists.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/OpenCTI-Platform/docker.git && cp .env.sample .env && docker compose up -d`

**URL:** https://github.com/OpenCTI-Platform/OpenCTI

**Alternatives:** MISP, TAXII 2


### TAXII 2

The STIX/TAXII 2.x protocol (OASIS standard) feed providers and ISACs use to push/pull structured intelligence; consume collections or publish your own vetted IOCs to partners.

**When:** Connect your SIEM/intel stack to TAXII feed endpoints, or publish your own vetted indicators to partners without building custom transport.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (protocol); pip install stix2 for client ingestion`

**URL:** https://oasis-open.github.io/cti-documentation/

**Alternatives:** MISP, OpenCTI


## Detection Engineering

### Sigma ⭐

The generic, SIEM-agnostic detection format: YAML rules for log semantics; sigma-cli compiles them to Splunk, Elastic, Loki, QRadar, Sentinel, and dozens of other query languages.

**When:** Author detection once and ship it anywhere: port a SigmaHQ rule, run sigma convert --target <siem>, and validate the query against logs before tuning.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install sigma-cli && git clone https://github.com/SigmaHQ/sigma`

**URL:** https://github.com/SigmaHQ/sigma

**Alternatives:** Atomic Red Team, YARA


### Atomic Red Team

Red Canary's adversary-simulation library mapping 700+ ATT&CK techniques to executable test definitions, used to prove a detection fires — or stays silent.

**When:** Verify Sigma or SIEM rules against real technique behavior: run the matching atom, watch your alert pipeline, and tune the rule before deployment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone --recurse-submodules https://github.com/redcanaryco/atomic-red-team`

**URL:** https://github.com/redcanaryco/atomic-red-team

**Alternatives:** Sigma, MITRE ATT&CK


### YARA

Binary pattern-matching rule engine for malware families and byte-level IOCs; complements SIEM rules when the evidence is a file, not a log (fuller coverage in the malware domain).

**When:** Match dropped samples or artifacts against signature rules, or encode a family signature your feed team can't express in a log query.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install yara`

**URL:** https://github.com/VirusTotal/yara

**Alternatives:** Sigma


### MITRE ATT&CK

The common knowledge base of adversary tactics, techniques, and data sources that Sigma rules, atoms, defenders, and coverage reports all annotate against — a reference framework, not a tool.

**When:** Map and measure detection coverage: tag rules with technique IDs, standardize on its vocabulary for alerts and reports, or browse technique details before writing a rule.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web reference; API at attack.mitre.org)`

**URL:** https://attack.mitre.org

**Alternatives:** Atomic Red Team, Sigma


## Analytics & IOC Marketplaces

### AlienVault OTX ⭐

Free open threat exchange (AT&T/LevelBlue): subscribe to community pulses, query indicator enrichment, and sync IOCs via the OTXv2 SDK or DirectConnect agents.

**When:** Commercial-grade feeds with zero setup: register, grab an API key, and enrich or ingest IOCs within the hour — the broadest free pulse ecosystem.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API); pip install OTXv2`

**URL:** https://otx.alienvault.com

**Alternatives:** ThreatFox, MalwareBazaar, URLhaus


### ThreatFox

abuse.ch's malware-IOC feed: submit and query malpedia-labeled IOCs (IPs, domains, URLs, hashes), with CSV/JSON dumps, Suricata ruleset, and MISP event exports.

**When:** Pull current malware IOCs into your SIEM or blocklist, or pivot a domain/IP to its associated malware family (also covered in ioc-pivoting).

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free auth key)`

**URL:** https://threatfox.abuse.ch

**Alternatives:** MalwareBazaar, URLhaus


### MalwareBazaar

abuse.ch's sample-sharing database: search by hash, signature, or imphash, download malware samples, and pull hourly/daily batch feeds.

**When:** Grab reference samples or up-to-date hashes by tag or signature for your sandbox, YARA hunting, or detection validation.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API: https://mb-api.abuse.ch/api/v1/)`

**URL:** https://bazaar.abuse.ch

**Alternatives:** ThreatFox, URLhaus


### URLhaus

abuse.ch's malicious-URL feed complementing ThreatFox: a plain-text URL list plus RPZ, hostfile, and Suricata/Snort rulesets for proxy and log matching.

**When:** Blocklist or hunt URLs in proxy/DNS logs; the plain-text URL list catches malware download paths with low false positives.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://urlhaus.abuse.ch

**Alternatives:** ThreatFox, MalwareBazaar


## IOC Pivoting & Correlation

### IntelOwl ⭐

Self-hosted aggregation and analysis platform: one request runs a file/IP/domain/hash through 100+ analyzers (OTX, ThreatFox, MalwareBazaar, VirusTotal, GreyNoise, YARA) and chains them with pivots.

**When:** Pivot every incoming IOC across your whole free-vendor stack automatically, or plug it into SOAR/MISP/OpenCTI for repeatable, centralized enrichment.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/intelowlproject/IntelOwl && ./initialize.sh && ./start prod up`

**URL:** https://github.com/intelowlproject/IntelOwl

**Alternatives:** MISP, ThreatFox, Pulsedive


### MISP

(Also in threat-sharing): its correlation engine links identical and high-fidelity-cluster attributes across every event in your instance and its federated communities, surfacing related infrastructure from others' incidents.

**When:** Correlate a suspicious attribute against your event history to find linked campaigns, reused C2, or related infrastructure while investigating an alert.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `see threat-sharing category`

**URL:** https://github.com/MISP/MISP

**Alternatives:** IntelOwl, ThreatFox


### ThreatFox

(Also in analytics-marketplaces): excels at pivoting a file hash to the hosts and IPs that served it plus its family label — the fastest 'what is this IOC attached to' lookup.

**When:** Instant pivoting with zero infrastructure: paste a hash, domain, or IP and get malware family, threat type, and related IOCs from the community dataset.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free auth key)`

**URL:** https://threatfox.abuse.ch

**Alternatives:** Pulsedive, IntelOwl


### Pulsedive

Free IOC portal combining passive/active scans, risk scores, ATT&CK tags, and a pivot/Explore query language across its indicator database, with a browser extension for on-page enrichment.

**When:** Enrich an indicator with risk scores and relationship pivots without standing up a platform: free account, pivot graphs, and exports for quick triage.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free account)`

**URL:** https://pulsedive.com

**Alternatives:** ThreatFox, MISP

