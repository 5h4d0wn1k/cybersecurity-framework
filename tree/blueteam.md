# 🛡️ Blue Team — Defense & Detection

Tools defenders run to detect, hunt, and respond on their own estate: SIEM, endpoint and network telemetry, detection engineering, response automation, and hostile edge hardening.

## SIEM & SOC Platforms




#### Open-Source SOC Stacks



##### Elastic Stack (ELK) ⭐

Reference open-core free SIEM: ships logs via Elastic Agent/Beats into Elasticsearch, renders detections and dashboards in Kibana, and runs the detection engine on EQL/ES|QL, Sigma, and YARA rule content.

**When:** Your first-stop free SOC when you want one cluster for full-text log search plus security detections and can absorb Elasticsearch operations.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run -d -p 9200:9200 -e discovery.type=single-node docker.elastic.co/elasticsearch/elasticsearch:9.5.1 (then add Kibana + Elastic Agent via the docs)`

**URL:** https://www.elastic.co/security

**Alternatives:** wazuh, graylog, splunk


##### Wazuh

Open-source XDR/SIEM pairing an Elastic/OpenSearch backend with a unified agent delivering file-integrity monitoring, security configuration assessment, vulnerability detection, active response, and compliance dashboards.

**When:** When you want SIEM plus an endpoint agent in one cohesive open bundle with built-in compliance reporting (PCI-DSS/HIPAA/SOC 2) and less manual Elasticsearch plumbing.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a`

**URL:** https://wazuh.com

**Alternatives:** elastic stack (elk), security onion


##### Security Onion

Turnkey NSM distribution bundling Suricata (detection + full packet capture), Zeek metadata, Elastic/Kibana dashboards, osquery host visibility, and alert/case management into a single guided install.

**When:** Fastest way to stand up a whole detection-and-response platform on one box when you don't want to assemble SIEM, IDS, and ingestion yourself.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the ISO from https://securityonion.com, install, then run: sudo so-setup-network (guided wizard)`

**URL:** https://securityonion.com

**Alternatives:** elastic stack (elk), wazuh


##### Graylog

Open-source log management and SIEM on Elasticsearch/OpenSearch storage, with flexible extraction pipelines (streams + pipeline rules) for parsing, enrichment, GEOIP, and threat-intel tagging.

**When:** Log centralization when you want clean server-side pipelines to poll, enrich, and route messages — without running a fleet of endpoint agents or Wazuh-style XDR.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `curl -L -o graylog-repo.deb https://packages.graylog2.org/repo/packages/graylog-7.1-repository_latest.deb && sudo dpkg -i graylog-repo.deb && sudo apt-get install graylog-server`

**URL:** https://www.graylog.org

**Alternatives:** elastic stack (elk), wazuh


#### Endpoint-Native Hunt & Response



##### Velociraptor ⭐

Open-source DFIR + endpoint-monitoring framework (Rapid7): fleet-wide hunts over VQL, live evidence collection across thousands of hosts, and a monitoring engine running Sigma detections against ETW/eBPF events in real time.

**When:** Endpoint hunt and incident response at scale — triage every host, collect volatile evidence, then keep them watched with live detections; often the 'endpoint SIEM' half of a free SOC.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `curl -LO https://github.com/Velocidex/velociraptor/releases/download/v0.76.3/velociraptor-v0.76.3-linux-amd64 && chmod +x velociraptor-v0.76.3-linux-amd64 && ./velociraptor gui quickstart`

**URL:** https://github.com/Velocidex/velociraptor

**Alternatives:** osquery, limacharlie


#### Commercial SIEM — Free Tier



##### Splunk Free ⭐

Free perpetual tier of the commercial SIEM incumbent: SPL search over indexed events and mature dashboards/alerts, capped at 500 MB/day ingest; a full license scales past the cap.

**When:** When you want enterprise SIEM UX and Splunk's integration ecosystem at zero cost for a lab or small estate, or as the benchmark when evaluating an all-open stack.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `wget -O /tmp/splunk-9.4.0-amd64.deb https://download.splunk.com/products/splunk/releases/9.4.0/linux/splunk-9.4.0-amd64.deb && sudo dpkg -i /tmp/splunk-9.4.0-amd64.deb && sudo /opt/splunk/bin/splunk start --accept-license --answer-yes`

**URL:** https://www.splunk.com

**Alternatives:** elastic stack (elk), wazuh






## Endpoint Detection & XDR Hunting




#### Endpoint Agents



##### Self-Hosted Fleet Agents



###### Velociraptor ⭐

Open-source endpoint visibility and collection platform: deploy lightweight agents, run prebuilt forensic artifacts and fleet-wide VQL hunts, push live Sigma/EQL detections, and pull processes, disk, and registry data to a central server.

**When:** Hunt across every host you own in one place: stand up the server, enroll agents, and answer 'what happened here' with fleet-wide queries and persistent monitoring.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `curl -LO https://github.com/Velocidex/velociraptor/releases/download/v0.76.3/velociraptor-v0.76.3-linux-amd64 && chmod +x velociraptor-v0.76.3-linux-amd64 && ./velociraptor gui quickstart`

**URL:** https://github.com/Velocidex/velociraptor

**Alternatives:** osquery, sysmon


###### osquery

SQL-powered agent exposing OS state — processes, sockets, files, users, listeners — as queryable tables; fire fleet-wide queries instantly and schedule packs, managed via Fleet (FleetDM).

**When:** Lightweight cross-platform telemetry when you want to 'SELECT' answers from every host and ship results to SIEM; the armchair-friendly complement to Velociraptor.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -L https://pkg.osquery.io/deb/osquery_5.23.1-1.linux_amd64.deb -o /tmp/osquery.deb && sudo dpkg -i /tmp/osquery.deb`

**URL:** https://osquery.io

**Alternatives:** velociraptor, limacharlie


###### Sysmon

Windows Sysinternals driver that logs high-fidelity process creation, network connections, and file writes beyond default auditing; pair with the SwiftOnSecurity or Modular config for a solid hunting baseline.

**When:** On every Windows host where you need attacker-action visibility and can ship its event log to your SIEM — no heavy agent required.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -LO https://download.sysinternals.com/files/Sysmon.zip && curl -LO https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml && sysmon64.exe -accepteula -i sysmonconfig-export.xml`

**URL:** https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

**Alternatives:** velociraptor, osquery


##### Cloud-Native EDR



###### LimaCharlie ⭐

Cloud-native SecOps platform: an EDR sensor streams verbose endpoint telemetry over TLS in real time, and a YAML-based Detection & Response engine runs the full open Sigma ruleset with automated response actions.

**When:** When you want EDR plus detection-as-code in the cloud without running a SIEM or agent server yourself; the free Community org covers small estates and labs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (cloud SaaS) — create a free Community org at limacharlie.io, run the per-OS sensor installer, and enable the Sigma ruleset`

**URL:** https://limacharlie.io

**Alternatives:** velociraptor, osquery


#### Zeek-Log Threat Hunting



##### RITA ⭐

Active Countermeasures' open-source network-traffic analysis framework that ingests Zeek logs and scores beaconing, long connections, DNS tunneling, and threat-intel hits for hunting C2.

**When:** Turn passive Zeek metadata into C2 hunting: run it against captured or rolling Zeek logs to surface beacons and suspicious external connections a normal SIEM query would miss.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the installer from https://github.com/activecm/rita/releases, then: tar -xf rita-<version>-installer.tar.gz && sudo ./rita-*/install_rita.sh`

**URL:** https://github.com/activecm/rita

**Alternatives:** zeek, bzar


##### Zeek

Passive network-analysis framework (formerly Bro) feeding rich protocol metadata, file hashes, and events to hunting and SIEM pipelines via 70+ log types — the data source RITA and BZAR consume.

**When:** The metadata layer for hunt stacks: deploy the sensor, let its conn/dns/http logs flow into Elastic or RITA, and never push raw packets for every question.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt-get install zeek (zeek.org apt repo) or docker pull zeek/zeek`

**URL:** https://zeek.org

**Alternatives:** rita, suricata






## Log, Packet & Network Detection




#### Network Sensors



##### Signature IDS/IPS Engines



###### Suricata ⭐

OISF's multi-threaded open-source IDS/IPS engine inspecting traffic with Snort-compatible rules at multi-Gbps speeds and emitting structured EVE JSON alerts (plus PCAP) straight into your SIEM.

**When:** High-throughput signature detection at your network edge or segmentation points; the default self-managed NIDS with an IPS fallback.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo add-apt-repository ppa:oisf/suricata-stable && sudo apt-get update && sudo apt-get install suricata && sudo suricata-update`

**URL:** https://suricata.io

**Alternatives:** snort 3, zeek


###### Snort 3

Cisco's next-generation open-source NIDS/IPS: multi-threaded, Lua-based policy language, faster pattern matching than 2.x, tuned with Talos rules.

**When:** When you prefer Cisco's Talos rule ecosystem, are migrating an existing Snort 2 deployment, or want SnortML-driven engine tuning.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt-get install snort3 (Ubuntu 22.04+; otherwise build from the source tarball on snort.org)`

**URL:** https://www.snort.org

**Alternatives:** suricata, zeek


##### Protocol Metadata Engines



###### Zeek ⭐

Passive network-analysis framework (formerly Bro) that logs rich protocol metadata, file hashes, and events across 70+ log types for later forensics instead of blocking in real time.

**When:** Deep protocol visibility feeding a SIEM or full-packet archive — run it beside Suricata/Snort because Zeek answers 'what happened' while the IDS engine answers 'alert'.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt-get install zeek (zeek.org apt repo) or docker pull zeek/zeek`

**URL:** https://zeek.org

**Alternatives:** rita, suricata


#### Packet Capture & Decoding



##### tshark ⭐

Wireshark's terminal sibling: captures, decrypts, and prints live or offline traffic with the full dissector set and CSV/JSON/raw output for scripted analysis.

**When:** Get Wireshark-grade dissection piped into grep, jq, or detection pipelines without a GUI — the workhorse for carving answers out of PCAP on servers and sensors.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt-get install tshark`

**URL:** https://www.wireshark.org/docs/man-pages/tshark.html

**Alternatives:** tcpdump, wireshark


##### tcpdump

Command-line packet capture using Berkeley Packet Filter (BPF) expressions; the standard for headless logging and scripted sniffing on any host.

**When:** Rolling capture on a sensor, router, or lab box where no GUI exists, or when you need a quick BPF-filtered sniff to confirm what is on the wire.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt-get install tcpdump`

**URL:** https://www.tcpdump.org

**Alternatives:** tshark


#### Host Audit Logging



##### Auditd ⭐

Linux Audit framework userspace (auditd, auditctl, ausearch) recording privileged actions, file access, and security-relevant events to an immutable log across reboots.

**When:** Build the audit trail that CIS/STIG rules require on Linux hosts and answer 'who accessed what, when' during a response with ausearch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt-get install auditd`

**URL:** https://github.com/linux-audit/audit-userspace

**Alternatives:** osquery, sysmon


#### Ingest Parsing & Routing



##### Logstash ⭐

Data-shaping pipeline (the 'L' in ELK) that pulls logs and metrics, parses, enriches, filters, and routes them to Elasticsearch or any other output.

**When:** The parsing/enrichment middle layer when an agent's native handling is not enough for messy or appliance-shaped log sources heading into Elastic.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `curl -L -o logstash.deb https://artifacts.elastic.co/downloads/logstash/logstash-9.5.1-amd64.deb && sudo dpkg -i logstash.deb`

**URL:** https://www.elastic.co/logstash

**Alternatives:** graylog, vector






## Detection Engineering & Playbook Tuning




#### Rule Authoring & Content



##### Cross-SIEM Rule Formats



###### Sigma ⭐

The generic, SIEM-agnostic detection format: YAML rules describing log semantics; sigma-cli compiles them to Splunk, Elastic, Loki, MS Sentinel, and dozens of query languages from the SigmaHQ public rule set.

**When:** Author one detection and ship it everywhere: port a SigmaHQ rule, run sigma convert --target <siem>, and validate the query against live logs before tuning.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install sigma-cli && git clone https://github.com/SigmaHQ/sigma`

**URL:** https://github.com/SigmaHQ/sigma

**Alternatives:** car, atomic red team


###### CAR

MITRE's Cyber Analytics Repository: a knowledge base of validated analytics that pair each ATT&CK technique with a hypothesis, pseudocode, and concrete implementations (Splunk, EQL, Zeek).

**When:** Harvest battle-tested analytic ideas to port into Sigma or your SIEM — read the operating theory and data model before writing new rules from scratch.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/mitre-attack/car`

**URL:** https://car.mitre.org/

**Alternatives:** sigma, atomic red team


##### Detection Validation & Malware Rules



###### Atomic Red Team

Red Canary's adversary-simulation library mapping hundreds of ATT&CK techniques to executable test definitions; each atomic documents the exact procedure and the telemetry a detection should fire on.

**When:** Prove a Sigma/SIEM rule actually fires by running the matching atomic test and watching your alert pipeline — the purple-team workflow lives in the purpleteam domain.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Install-Module -Name invoke-atomicredteam -Scope CurrentUser -Force`

**URL:** https://github.com/redcanaryco/atomic-red-team

**Alternatives:** sigma, limacharlie


###### YARA ⭐

Binary pattern-matching rule engine for malware families and byte-level IOCs; complements SIEM rules when the evidence is a dropped file, not a log (fuller coverage in the malware domain).

**When:** Match captured samples or suspicious files against signature rules, or encode a family signature your log-query team can't express in Sigma.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt-get install yara`

**URL:** https://github.com/VirusTotal/yara

**Alternatives:** sigma, atomic red team






## Response Automation, SOAR & Playbooks




#### SOAR / Workflow Automation



##### Shuffle ⭐

Open-source SOAR platform: drag-and-drop workflow builder wiring apps, triggers, and actions to automate alert triage, enrichment calls, and response playbooks against your SIEM and intel tools.

**When:** Automate repeatable analyst actions (enrich an IOC, quarantine a host, open a ticket) with a free self-hosted SOAR instead of hand-scripted glue.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/shuffle/shuffle && cd shuffle && docker compose up -d`

**URL:** https://shuffler.io

**Alternatives:** n8n, thehive


##### n8n

Fair-code workflow automation platform with 400+ integrations and a visual editor; a flexible general engine for chaining webhooks, email, HTTP APIs, and internal tools.

**When:** Lighter-weight automation when Shuffle feels security-specific but you still want playbooks, schedules, and HTTP-triggered workflows in one self-hosted box.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `docker run -d --name n8n -p 5678:5678 docker.n8n.io/n8nio/n8n`

**URL:** https://n8n.io

**Alternatives:** shuffle


#### Case Management & Enrichment



##### TheHive ⭐

Open-source security incident-response platform (TheHive 5) for collecting, sharing, and analyzing alerts as collaborative cases with tasks, observables, and full audit history.

**When:** Track active incidents and alerts with structured cases, then close the loop by pushing findings back into detection tuning.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d --name thehive -p 9000:9000 thehiveproject/thehive:5`

**URL:** https://thehive-project.org

**Alternatives:** shuffle, cortex


##### Cortex

Open-source analyzer engine (TheHive companion): responders and analyzers run one-shot enrichments — DNS, hash lookups, intel feeds, quarantines — from TheHive, MISP, or its REST API.

**When:** Standardized IOC enrichment as analyzers you can call from TheHive cases, MISP, or your SOAR playbooks without wiring each vendor API yourself.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d --name cortex -p 9001:9001 thehiveproject/cortex`

**URL:** https://github.com/TheHive-Project/Cortex

**Alternatives:** thehive, intelowl


#### Guidance & Incident Playbooks



##### CISA Incident Response Playbooks ⭐

CISA's Federal Government Cybersecurity Incident and Vulnerability Response Playbooks: role-by-role, phase-by-phase response guidance with ready-to-copy templates for incident handling.

**When:** Start with these when writing your own playbooks — lift the phases, roles, and communications plan, then adapt the details to your estate.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — PDF downloads from cisa.gov`

**URL:** https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks

**Alternatives:** nist sp 800-61


##### NIST SP 800-61r3

NIST Special Publication 800-61 revision 3: incident-response recommendations and considerations for cybersecurity risk management — organizing IR, handling evidence, and coordination guidance.

**When:** A defensible framework for how response teams should be structured and measured, whether you are building a small SOC or a whole CSIRT.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — PDF from csrc.nist.gov`

**URL:** https://csrc.nist.gov/pubs/sp/800/61/r3/final

**Alternatives:** cisa incident response playbooks






## Deception & Tripwires




#### Tripwires & Canaries



##### Canarytokens ⭐

Thinkst's free hosted (or self-hosted Docker) tripwire factory generating DNS, URL, document (PDF/Word), AWS-key, QR-code, and Slack tokens that alert instantly when touched.

**When:** When a full honeypot is overkill: sprinkle fake DNS names, URLs, or documents across AD, share drives, and public infra for cheap, near-instant detection of unauthorized access.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (canarytokens.org) — self-host: git clone https://github.com/thinkst/canarytokens-docker && cd canarytokens-docker && docker compose up`

**URL:** https://github.com/thinkst/canarytokens

**Alternatives:** opencanary


##### OpenCanary

Thinkst's open-source multi-protocol honeypot daemon (SSH, telnet, HTTP, FTP, SNMP, SMB, RDP, MySQL) firing syslog, email, Slack, and webhook alerts on any probe; the OSS sibling of commercial Thinkst Canary.

**When:** Drop a near-zero-footprint daemon on a jump host, file server, or DMZ for alerting on unexpected interaction — richer coverage lives in the honeypots domain.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install opencanary && opencanaryd --copyconfig`

**URL:** https://github.com/thinkst/opencanary

**Alternatives:** canarytokens






## Mail, Edge & Web Hardening




#### Mail Authentication & Filtering



##### rspamd ⭐

Fast open-source mail filter scoring incoming message content with Bayesian/spamassassin rules, and signing outbound mail with DKIM plus DMARC/SRS support via its own Milter interface.

**When:** Harden your own postfix/exim MTA: filter inbound spam and authenticate outbound with DKIM signing and SPF/DMARC alignment in one service.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo add-apt-repository ppa:rspamd/rspamd && sudo apt-get update && sudo apt-get install rspamd`

**URL:** https://rspamd.com

**Alternatives:** checkdmarc, swaks


##### checkdmarc

Python module/CLI validating SPF and DMARC DNS records end-to-end, including SPF lookup counts and void lookups, DMARC effectiveness warnings, MTA-STS, DANE/TLSA, and BIMI checks.

**When:** Audit your own domain's email authentication posture before or after publishing records — run it defensively to catch a policy an attacker or vendor broke.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install checkdmarc && checkdmarc example.com`

**URL:** https://github.com/domainaware/checkdmarc

**Alternatives:** rspamd, swaks


##### swaks

Swiss Army Knife for SMTP: crafts arbitrary test messages with full control over sender, headers, attachments, and TLS to verify mail relays and backend behavior on hosts you administer.

**When:** Verify an MTA or relay does what it should — test who can relay, check headers and SPF/DKIM passing, or reproduce a delivery issue from your own mail server.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt-get install swaks`

**URL:** https://jetmore.org/john/code/swaks/

**Alternatives:** checkdmarc, rspamd


#### Host & Edge Intrusion Prevention



##### CrowdSec ⭐

Open-source crowd-sourced IPS (Suricata-aware): watches logs and events locally, bans offending IPs via bouncers at the firewall/nginx/cloud level, and shares signals through the community blocklist.

**When:** Active response at the edge — replace dumb fail2ban-style blocking with attack-originated, shareable banishment backed by community signals.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -s https://install.crowdsec.net | sudo sh && sudo cscli collections install crowdsecurity/linux && sudo systemctl start crowdsec`

**URL:** https://www.crowdsec.net

**Alternatives:** fail2ban, suricata


##### Fail2ban

Classic log-scrape intrusion-prevention daemon that watches services (ssh, nginx, postfix) and bans repeat offenders through the host firewall or iptables backends.

**When:** Simple, well-understood scoring-based banning on a single host — perfect when CrowdSec's community-signal model is more than you need.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt-get install fail2ban`

**URL:** https://github.com/fail2ban/fail2ban

**Alternatives:** crowdsec


#### Web Application Firewalls



##### ModSecurity ⭐

The OWASP open-source WAF engine (an OWASP Production project) inspecting HTTP and enforcing SecRule policies on Apache/nginx; load the OWASP CRS on top for real attack coverage.

**When:** Inline HTTP-layer defense when you want the battle-tested rule ecosystem and can commit to tuning false positives against your own apps.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt-get install libapache2-mod-security2 (Apache; for nginx compile the module with --with-compat --add-dynamic-module=../ModSecurity-nginx)`

**URL:** https://modsecurity.org

**Alternatives:** coraza, owasp crs


##### Coraza

OWASP WAF written in Go with near-full ModSecurity compatibility — runs CRS v4 without the legacy C engine as a library or middleware for Caddy, Traefik, APISIX, and API gateways.

**When:** Cloud-native stacks (Go services, containers, Caddy/Traefik/APISIX) where ModSecurity's build model is awkward but you still want CRS protection.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `xcaddy build --with github.com/corazawaf/coraza-caddy/v2 (then add the coraza_waf block to the Caddyfile)`

**URL:** https://coraza.io

**Alternatives:** modsecurity, owasp crs


##### OWASP CRS

The OWASP flagship Core Rule Set — a community-maintained rule layer detecting SQLi, XSS, scanners, and OWASP Top 10 attacks that runs on both ModSecurity and Coraza engines; a ruleset, not a standalone tool.

**When:** The rule layer to load onto any WAF engine so a bare install actually detects web attacks; tune via the anomaly-scoring exclusions to cut false positives.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone --depth 1 https://github.com/coreruleset/coreruleset.git (then Include the CRS config in your WAF engine)`

**URL:** https://coreruleset.org

**Alternatives:** modsecurity, coraza


##### Cloudflare WAF

Commercial managed edge WAF (SaaS) filtering traffic on Cloudflare's CDN with managed rulesets (including OWASP CRS coverage) plus bot and rate controls — no servers to run.

**When:** When your apps already sit behind Cloudflare and you want managed rules, DDoS/bot defense, and zero self-hosting in one panel.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (SaaS) — enable in the dash.cloudflare.com Security panel, pick a managed ruleset, and tune via custom rules`

**URL:** https://developers.cloudflare.com/waf/

**Alternatives:** modsecurity, coraza





