# 📡 Threat Intelligence, Sharing & Detection Engineering

Enrich your own defenses: ingest STIX/TAXII feeds, aggregate and pivot on IOCs, correlate infrastructure, and write portable detections against standard frameworks.

## Intel Platforms & Frameworks



#### STIX/TAXII-native Platforms


##### OpenCTI ⭐

Open-source threat-intelligence platform built around the STIX 2.x data model: consumes and exports STIX/TAXII 2.0/2.1, correlates entities into a knowledge graph, and ingests from 100+ connectors.

**When:** Stand up a central intel drive when you want automated feed ingestion (MISP, MITRE, abuse.ch, TAXII collections) correlated into entities, reports, and indicators rather than raw IOC lists.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/OpenCTI-Platform/docker.git && cp .env.sample .env && docker compose up -d`

**URL:** https://github.com/OpenCTI-Platform/OpenCTI

**Alternatives:** MISP, TheHive


##### MISP

The open-source intelligence sharing platform that stores and exchanges events as STIX/TAXII-compatible objects, syncs with federated communities, and exposes a full REST API for feeding SIEMs and SOARs.

**When:** Run or sync a MISP instance when you need governed, TLP-aware intel sharing across your team, an ISAC-style community, or a feed-ingestion pipeline that speaks STIX/TAXII 2 out of the box.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `wget -O /tmp/INSTALL.sh https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/INSTALL.sh && sudo bash /tmp/INSTALL.sh`

**URL:** https://github.com/MISP/MISP

**Alternatives:** OpenCTI, IntelOwl


##### TAXII 2.0

The OASIS STIX/TAXII 2.x protocol that feed providers and ISACs use to push and pull structured intelligence over REST in API- and collection-based patterns.

**When:** Connect your SIEM or intel stack to vendor and community TAXII endpoints, or publish your own vetted indicators to partners without building custom transport.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (protocol spec); pip install stix2 for client ingestion`

**URL:** https://oasis-open.github.io/cti-documentation/

**Alternatives:** MISP, OpenCTI


##### stix2-client

The official OASIS Python library for creating, querying, and consuming STIX 2 objects and TAXII 2.x collections; pairs with cti-python-taxii2-client for polling remote servers.

**When:** Automate feed pulls in Python: subscribe to a TAXII collection, parse bundles into STIX objects, and hand cleaned indicators to MISP or OpenCTI.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip install stix2`

**URL:** https://github.com/oasis-open/cti-python-stix2

**Alternatives:** TAXII 2.0, PyMISP


##### TheHive

Collaborative case-management and incident-response platform that ingests MISP events, runs observables through Cortex analyzers, and can export findings back as STIX/TAXII objects (4.x AGPL archived; current 5.x is StrangeBee commercial).

**When:** Pairs with MISP and Cortex in the classic open-source IR stack when you need a shared investigation workspace with built-in observable workflows.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/StrangeBeeCorp/docker.git && cd docker && docker compose up -d`

**URL:** https://github.com/TheHive-Project/TheHive

**Alternatives:** DFIR-IRIS, MISP


##### Cortex

Observable analysis and active-response engine that runs 100+ analyzers (OTX, VirusTotal, AbuseIPDB, GreyNoise, etc.) against IPs, domains, files, and hashes, returning structured, exportable reports.

**When:** Give TheHive or MISP one shared enrichment backend so every platform calls the same analyzers instead of re-implementing vendor API calls.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run -d -p 9001:9001 --name cortex thehiveproject/cortex:latest`

**URL:** https://github.com/TheHive-Project/Cortex

**Alternatives:** IntelOwl, MISP


##### IntelOwl

Self-hosted aggregation engine that runs a file, IP, domain, or hash through 100+ analyzers and pushes structured results out via connectors to MISP, OpenCTI, and YETI.

**When:** Automate whole-vendor enrichment in one request and sink normalized findings into your STIX-based platforms via its connector layer.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/intelowlproject/IntelOwl && ./initialize.sh && ./start prod up`

**URL:** https://github.com/intelowlproject/IntelOwl

**Alternatives:** Cortex, Pulsedive


#### Open-Source Intel Frameworks


##### MISP ⭐

The foundational open threat-intelligence and sharing framework: event-driven IOC correlation, feed syncing, taxonomies, and TLP/org governance across trusted communities.

**When:** When you need a mature, community-proven place to store, correlate, and share intel with partners — it is the default first platform to stand up.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `wget -O /tmp/INSTALL.sh https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/INSTALL.sh && sudo bash /tmp/INSTALL.sh`

**URL:** https://github.com/MISP/MISP

**Alternatives:** OpenCTI, YETI


##### OpenCTI

Graph-based intel framework that treats actors, campaigns, malware, and infrastructure as interconnected entities, ingesting from MISP and dozens of connectors into a STIX-native store.

**When:** When your team reasons about campaigns and infrastructure relationships rather than flat IOC lists, so a knowledge-graph backend is worth the heavier deploy.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/OpenCTI-Platform/docker.git && cp .env.sample .env && docker compose up -d`

**URL:** https://github.com/OpenCTI-Platform/OpenCTI

**Alternatives:** MISP, YETI


#### Case Management & Analyzer Orchestration


##### TheHive ⭐

Collaborative incident case management that links alerts, observables, tasks, and Cortex responses in one shared workspace the whole IR team works from.

**When:** When multiple analysts investigate simultaneous incidents and you need tasking, observables, and audit history in a single pane with MISP/Cortex integration.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/StrangeBeeCorp/docker.git && cd docker && docker compose up -d`

**URL:** https://github.com/TheHive-Project/TheHive

**Alternatives:** DFIR-IRIS, MISP


##### Cortex

The analysis orchestrator behind TheHive: schedules observables through analyzers and responders, caches results, and exposes them via REST to any calling platform.

**When:** Attach a single Cortex to MISP and TheHive so enrichment and active-response is centralized, measured, and repeatable across tools.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run -d -p 9001:9001 --name cortex thehiveproject/cortex:latest`

**URL:** https://github.com/TheHive-Project/Cortex

**Alternatives:** IntelOwl, TheHive


##### DFIR-IRIS

Open-source incident-response platform with modern case management, timeline pivoting, IOC enumeration, malware-hash handling, and third-party CTI enrichment via resolvers.

**When:** Prefer a lighter, actively-developed OSS case manager that still publishes to MISP and pulls enrichment, without TheHive's legacy-or-commercial story.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker compose -f docker/default/docker-compose.yml up -d (from github.com/dfir-iris/dfir-iris)`

**URL:** https://github.com/dfir-iris/iris-web

**Alternatives:** TheHive, MISP



## IOC Aggregation & Feeds



#### IOC Aggregation & Enrichment


##### Reputation & Enrichment APIs


###### AlienVault OTX ⭐

Free open threat exchange (AT&T/LevelBlue): subscribe to community pulses, enrich indicators, and sync IOCs via the OTXv2 SDK into MISP, Splunk, or your SIEM.

**When:** Commercial-grade feeds with zero platform setup: register, grab an API key, and start aggregating community pulses within the hour.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API); pip install OTXv2`

**URL:** https://otx.alienvault.com

**Alternatives:** Pulsedive, ThreatFox


###### VirusTotal

Multivendor malware-scanning and reputation platform: submit files and URLs, query IP/domain/hash reputation, and pivot via its extensive relationships API.

**When:** Enrich any observable with detection-ratio context and passive-DNS relationships when you already hold an API key.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.virustotal.com

**Alternatives:** AlienVault OTX, GreyNoise


###### AbuseIPDB

Community-sourced IP-reputation database backed by user reports and abuse reports, exposed through a simple REST API and check endpoints.

**When:** Quickly score a suspicious source or destination IP before blocking, and let your SIEM auto-check IPs against its report feed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.abuseipdb.com

**Alternatives:** GreyNoise, AlienVault OTX


###### ThreatMiner

Free threat-intelligence portal and API aggregating passive DNS, WHOIS, hashes, SSL certs, URIs, and APT report tags for a single-indicator research view.

**When:** Pivot an IOC across WHOIS, passive DNS, and sample relationships in one free lookup with a documented v2 API for scripts.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web/API)`

**URL:** https://intelx.io

**Alternatives:** AlienVault OTX, Pulsedive


###### GreyNoise

Classifies internet-scan and background-noise traffic so analysts can tell routine scanning from targeted activity, with a free community API.

**When:** Filter out opportunistic scanners from your alerts: ask 'is this IP just noise?' before burning analyst time on it.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free community tier)`

**URL:** https://www.greynoise.io

**Alternatives:** AbuseIPDB, AlienVault OTX


##### Malware & URL Feeds (abuse.ch)


###### URLhaus ⭐

abuse.ch's malicious-URL feed: a plain-text URL list plus RPZ, hostfile, and Suricata/Snort rule packs for proxy, firewall, and log matching.

**When:** Block or hunt URLs in proxy and DNS logs — the plain-text daily list catches malware distribution paths with low false positives.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API)`

**URL:** https://urlhaus.abuse.ch

**Alternatives:** ThreatFox, MalwareBazaar


###### MalwareBazaar

abuse.ch's sample-sharing database: search by hash, signature, or imphash, download binaries, and pull hourly or daily batch hashes for YARA hunts and sandbox feeds.

**When:** Grab up-to-date reference samples and hashes by tag or malware family to train detections or validate sandbox coverage.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API: https://mb-api.abuse.ch/api/v1/)`

**URL:** https://bazaar.abuse.ch

**Alternatives:** ThreatFox, URLhaus


###### ThreatFox

abuse.ch's malware-IOC feed: query and submit IPs, domains, URLs, and hashes tagged to malware families, with CSV/JSON dumps and MISP event exports.

**When:** Pull current malware IOCs into your SIEM or pivot a domain/IP to its associated family — the fastest 'what is this IOC attached to' lookup.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free auth key)`

**URL:** https://threatfox.abuse.ch

**Alternatives:** URLhaus, MalwareBazaar


##### Multi-vendor Aggregators


###### IntelOwl ⭐

Self-hosted analyzer aggregation: one request runs a file, IP, domain, or hash through 100+ free and commercial analyzers (OTX, ThreatFox, MalwareBazaar, VirusTotal, GreyNoise, YARA) and chains pivots.

**When:** Pivot every incoming IOC across your whole vendor stack automatically, or plug it into MISP, OpenCTI, and TheHive for repeatable centralized enrichment.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/intelowlproject/IntelOwl && ./initialize.sh && ./start prod up`

**URL:** https://github.com/intelowlproject/IntelOwl

**Alternatives:** Pulsedive, Cortex


###### Pulsedive

Free IOC portal combining passive and active scans, risk scores, ATT&CK tags, and a pivot 'Explore' query language, plus a browser extension for on-page enrichment.

**When:** Enrich an indicator with risk scores and relationship pivots without standing up a platform — free account, pivot graphs, and exports for fast triage.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; free account)`

**URL:** https://pulsedive.com

**Alternatives:** AlienVault OTX, ThreatFox



## Pivoting & Passive DNS



#### Passive DNS & Historical Infrastructure


##### SecurityTrails ⭐

Passive DNS history and subdomain API with a no-key free tier: see every hostname an IP ever resolved and every IP a domain has used.

**When:** Spot old dev/staging infrastructure or infrastructure churn by replaying DNS history that no longer resolves via live queries.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://securitytrails.com

**Alternatives:** DNSDumpster, PassiveTotal


##### PassiveTotal

RiskIQ's passive-DNS and infrastructure-pivoting workbench whose legacy portal is retiring into Microsoft Defender Threat Intelligence (retired 2026); its DNS-history datasets live on in MDTI.

**When:** Only as a historical reference or for old integrations — use Microsoft Defender Threat Intelligence for RiskIQ-class passive-DNS pivot data going forward.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web) - retired; successor requires M365 Defender TI license`

**URL:** https://www.riskiq.com/products/passivetotal

**Alternatives:** Microsoft Defender TI, SecurityTrails


##### Microsoft Defender Threat Intelligence

Microsoft's defender intel platform (successor to RiskIQ/PassiveTotal): passive DNS, certificate/SOAR artifacts, infrastructure-chaining pivots on IPs, domains, and hosts, with a free community tier.

**When:** When you want RiskIQ-class passive-DNS and infrastructure-chaining datasets and already operate in Defender XDR, Sentinel, or the Microsoft security portal.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `preinstalled (portal/API; premium licensed, community tier available)`

**URL:** https://www.microsoft.com/en-us/security/business/intelligence

**Alternatives:** SecurityTrails, Censys


##### DNSDumpster

Free one-click DNS mapping service: resolves a domain to its subdomains, A/NS/MX records, and IPs with a visual map and TXT records.

**When:** A zero-signup first pass at a domain's DNS surface when you want a quick map before heavier enumeration.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://dnsdumpster.com

**Alternatives:** SecurityTrails, crt.sh


#### Internet-wide Search & Service Pivoting


##### Censys ⭐

Internet-wide scanning platform searchable by protocol, certificate, banner, and ASN — ideal for TLS-certificate pivoting back to hosts and exposure discovery.

**When:** Pivot a certificate, hostname, or service banner to every public-facing asset that matches, and monitor your own attack surface over time.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API; free account with query quota)`

**URL:** https://censys.com

**Alternatives:** Shodan, Netlas


##### Shodan

The classic internet-exposure search engine: filters by port, product, vulnerability, ASN, and even CVEs, with API and banner-to-host pivoting.

**When:** Find every internet-facing instance running a vulnerable service, or check whether an observed IP hosts additional exposed ports and software.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API; free tier, paid for API)`

**URL:** https://www.shodan.io

**Alternatives:** Censys, ZoomEye


##### ZoomEye

Chinese internet-wide asset-search engine (Knownsec) covering web applications, devices, and services with components, ports, and country filters.

**When:** Cross-check Censys/Shodan results against an independent fourth scanning corpus, especially for Asia-heavy infrastructure.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.zoomeye.ai

**Alternatives:** Shodan, Censys


##### FOFA

Internet asset-search platform with a rich query DSL (body, header, port, cert, icon hashes) and bulk API search for infrastructure mapping.

**When:** When you need expressive full-body searches and favicon based pivoting that cleanly link otherwise unrelated assets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://fofa.info

**Alternatives:** Censys, Shodan


##### Netlas

Internet-OSINT search engine with cert, DNS, IP, and response-body queries plus a Python SDK, letting you hunt by regex across a large scan index.

**When:** When you prefer scripting searches in Python or need regex-level body/header pivoting beyond Shodan's filter grammar.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; pip install netlas)`

**URL:** https://netlas.io

**Alternatives:** Censys, Shodan


##### Criminal IP

IP-intel and attack-surface search engine with malware, Geopolitics, and internet-scan pivots, plus free API access tiers for resolver lookups.

**When:** Aggregate IP reputation, exposed-service, and banner intel in one query when reviewing C2 or abuse infra candidates.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web/API; free tier)`

**URL:** https://www.criminalip.io

**Alternatives:** Shodan, AbuseIPDB


#### Graph & Campaign Correlation


##### MISP ⭐

MISP's correlation engine links identical and high-fidelity-cluster attributes across every event in your instance and its federated communities.

**When:** Correlate a suspicious attribute against your event history to find linked campaigns, reused C2, or related infrastructure while investigating an alert.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `see stix-taxii category install`

**URL:** https://github.com/MISP/MISP

**Alternatives:** OpenCTI, IntelOwl


##### OpenCTI

Uses its STIX knowledge graph to pivot from an indicator to the attack patterns, intrusion sets, and reports that reference it, revealing campaign context.

**When:** When an IOC is only a starting point and you need the surrounding actor, tooling, and TTP relationships a graph store preserves.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `see stix-taxii category install`

**URL:** https://github.com/OpenCTI-Platform/OpenCTI

**Alternatives:** MISP, ThreatFox



## Detection Engineering



#### Portable Rule Engines


##### Sigma ⭐

The SIEM-agnostic YAML rule format: sigma-cli compiles one generic rule to Splunk, Elastic, Loki, QRadar, Sentinel, and dozens of other query languages via conversion backends.

**When:** Author detection once and ship it anywhere: port a SigmaHQ rule, run sigma convert --target <siem>, and validate the query against logs before tuning.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install sigma-cli && git clone https://github.com/SigmaHQ/sigma`

**URL:** https://github.com/SigmaHQ/sigma

**Alternatives:** Atomic Red Team, YARA


##### YARA

Binary pattern-matching rule engine for malware families and byte-level IOCs; complements SIEM rules when the evidence is a file, not a log.

**When:** Match dropped samples or artifacts against signature rules, or encode a family signature your feed team cannot express in a log query.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install yara`

**URL:** https://github.com/VirusTotal/yara

**Alternatives:** Sigma


#### Validation & Adversary Emulation


##### Atomic Red Team ⭐

Red Canary's adversary-simulation library mapping 700+ ATT&CK techniques to executable test definitions used to prove a detection fires or stays silent.

**When:** Verify Sigma or SIEM rules against real technique behavior: run the matching atom, watch your alert pipeline, and tune the rule before deployment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone --recurse-submodules https://github.com/redcanaryco/atomic-red-team`

**URL:** https://github.com/redcanaryco/atomic-red-team

**Alternatives:** MITRE ATT&CK, Sigma


##### MITRE ATT&CK

The common knowledge base of adversary tactics, techniques, and data sources that Sigma rules, atoms, defenders, and coverage reports all annotate against.

**When:** Map and measure detection coverage: tag rules with technique IDs, standardize alert vocabulary, or browse technique data sources before writing a rule.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web reference; API at attack.mitre.org)`

**URL:** https://attack.mitre.org

**Alternatives:** Atomic Red Team, MITRE ATT&CK Navigator


##### MITRE ATT&CK Navigator

Web-based matrix viewer for layering technique coverage across your detections, with layers you can save as JSON and share between teams.

**When:** Visualize and report which techniques your Sigma/atomic coverage addresses and which gaps remain in a browsable, shareable matrix layer.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) - self-host: git clone https://github.com/mitre-attack/attack-navigator`

**URL:** https://github.com/mitre-attack/attack-navigator

**Alternatives:** MITRE ATT&CK, Atomic Red Team



