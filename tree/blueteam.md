# 🛡️ Blue Team — Defense & Detection

Tools defenders run to detect, monitor, and protect their own estate: SIEM, endpoint telemetry, network monitoring, and hostile-HTTP defense.

## SIEM & SOC Analytics

Elastic Stack (ELK) ⭐


#### Elastic Stack (ELK) ⭐

Reference open-core SIEM: ingests logs via Beats/Elastic Agent into Elasticsearch (Kibana for UI), and runs the detection engine with EQL/ES|QL/Sigma rules, dashboards, and built-in threat hunting.

**When:** Your first-stop SIEM when you want one cluster for security detections plus powerful full-text log search and can absorb Elasticsearch operations.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run -d -p 9200:9200 -e discovery.type=single-node docker.elastic.co/elasticsearch/elasticsearch:9.5.1 (then add Kibana + Elastic Agent per the docs)`

**URL:** https://www.elastic.co/security

**Alternatives:** wazuh, graylog, splunk


#### Wazuh

Open-source XDR/SIEM pairing an Elastic/OpenSearch backend with a unified agent delivering file-integrity monitoring, security configuration assessment, vulnerability detection, active response, and compliance dashboards.

**When:** When you want SIEM plus endpoint agent in one cohesive open bundle with built-in compliance reporting (PCI-DSS/HIPAA/SOC 2) and less manual Elasticsearch plumbing.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a`

**URL:** https://wazuh.com

**Alternatives:** elastic, graylog


#### Splunk

Commercial SIEM incumbent (Cisco-owned): SPL search over indexed events, mature dashboards/alerts, and the largest third-party integration ecosystem; licensed per GB/day.

**When:** When budget exists and you need enterprise SIEM tooling, best-in-class search UX, and vendor support — or as the benchmark when evaluating an all-open stack.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `wget -O /tmp/splunk-<VERSION>-amd64.deb https://download.splunk.com/products/splunk/releases/<VERSION>/linux/splunk-<VERSION>-amd64.deb && sudo dpkg -i /tmp/splunk-<VERSION>-amd64.deb`

**URL:** https://www.splunk.com

**Alternatives:** elastic, wazuh


#### Graylog

Open-source log management and SIEM on Elasticsearch/OpenSearch storage, with flexible extraction pipelines (streams + pipeline rules) for parsing, routing, GEOIP, and threat-intel enrichment.

**When:** Log centralization when you want clean server-side pipelines to poll, enrich, and route messages into destinations like Splunk or Elastic — without running agent fleets or Wazuh-style XDR.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `curl -L -o graylog-repo.deb https://packages.graylog2.org/repo/packages/graylog-7.1-repository_latest.deb && sudo dpkg -i graylog-repo.deb && sudo apt-get install graylog-server`

**URL:** https://www.graylog.org

**Alternatives:** elastic, wazuh


#### Logstash

Data-shaping pipeline (the 'L' in ELK) that pulls logs and metrics, transforms them — parse, enrich, filter, route — and ships them to Elasticsearch or any other output.

**When:** The standalone parsing/enrichment middle layer when an agent's native handling or a Beats module isn't enough for messy or appliance-shaped log sources.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `curl -L -o logstash.deb https://artifacts.elastic.co/downloads/logstash/logstash-9.5.1-amd64.deb && sudo dpkg -i logstash.deb`

**URL:** https://www.elastic.co/logstash

**Alternatives:** vector, fluentd






## Endpoint Detection & Response

Velociraptor ⭐


#### Velociraptor ⭐

Open-source DFIR + endpoint-monitoring framework (Rapid7): the Velociraptor Query Language hunts the entire fleet for forensic artifacts, collects live evidence at scale, and the monitoring engine runs Sigma detections against ETW/eBPF events in real time.

**When:** Endpoint hunting and incident response at scale — triage thousands of hosts, collect volatile evidence, then keep them monitored with live detections.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `curl -LO https://github.com/Velocidex/velociraptor/releases/download/v0.76.3/velociraptor-v0.76.3-linux-amd64 && chmod +x velociraptor-v0.76.3-linux-amd64 && ./velociraptor gui quickstart`

**URL:** https://github.com/Velocidex/velociraptor

**Alternatives:** osquery, sysmon, limacharlie


#### osquery

SQL-powered agent that exposes OS state — processes, sockets, files, users, listeners — as queryable tables; defenders fire fleet-wide queries instantly and schedule packs for continuous inspection, managed via Fleet.

**When:** Lightweight cross-platform endpoint telemetry when you want to 'SELECT' answers from every host and ship the results to a SIEM; pair with Fleet (fleetdm) for enroll/query management.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -L https://pkg.osquery.io/deb/osquery_5.23.1-1.linux_amd64.deb -o /tmp/osquery.deb && sudo dpkg -i /tmp/osquery.deb`

**URL:** https://osquery.io

**Alternatives:** velociraptor, limacharlie


#### Sysmon

Windows Sysinternals driver that logs high-fidelity process creation, network connections, and file writes beyond default auditing; pair with the SwiftOnSecurity (or Modular) config for a solid threat-hunting baseline.

**When:** On every Windows host where you need attacker-action visibility and can ship its event log to your SIEM — no heavy agent required.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -LO https://download.sysinternals.com/files/Sysmon.zip && curl -LO https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml && sysmon64.exe -accepteula -i sysmonconfig-export.xml`

**URL:** https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

**Alternatives:** velociraptor, osquery


#### LimaCharlie

Cloud-native SecOps platform: an EDR sensor streams verbose endpoint telemetry over TLS in real time, and a YAML-based Detection & Response engine runs the full open Sigma ruleset with automated response actions.

**When:** When you want EDR plus detection-as-code in the cloud without running a SIEM or agent server yourself; the free Community org covers small estates and labs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (SaaS) — create a free Community org at limacharlie.io, then run the per-OS sensor installer and enable the Sigma ruleset`

**URL:** https://limacharlie.io

**Alternatives:** velociraptor, osquery






## Intrusion Detection / Network Monitoring

Suricata ⭐


#### Suricata ⭐

OISF's multi-threaded open-source IDS/IPS engine that inspects traffic with Snort-compatible rules at multi-Gbps speeds and emits structured EVE JSON alerts (plus PCAP) straight into your SIEM.

**When:** High-throughput signature detection at your network edge or segmentation points; the default pick for a self-managed NIDS with IPS fallback.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo add-apt-repository ppa:oisf/suricata-stable && sudo apt-get update && sudo apt-get install suricata && sudo suricata-update`

**URL:** https://suricata.io

**Alternatives:** snort, zeek


#### Snort 3

Cisco's next-generation open-source NIDS/IPS: Snort 3 adds multi-threading, a Lua-based policy language, and faster pattern matching over the classic 2.x line, tuned via Talos rules.

**When:** When you prefer Cisco's Talos rules ecosystem, are migrating an existing Snort 2 deployment, or want SnortML-driven engine tuning.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt-get install snort3 (Ubuntu 22.04+; otherwise build from the source tarball on snort.org)`

**URL:** https://www.snort.org

**Alternatives:** suricata, zeek


#### Zeek

Passive network-analysis framework (formerly Bro) that logs rich protocol metadata, file hashes, and events across 70+ log types for later forensics instead of blocking in real time.

**When:** Deep protocol visibility feeding a SIEM or full-packet archive — run it beside Suricata/Snort because it answers 'what happened', while the engine answers 'alert'.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker pull zeek/zeek (or add the zeek.org apt repo: sudo apt-get install zeek)`

**URL:** https://zeek.org

**Alternatives:** suricata, snort


#### Security Onion

Turnkey NSM distribution that bundles Suricata (detection + full packet capture), Zeek metadata, Elasticsearch/Kibana dashboards, osquery host visibility, and alert/case management into a single install.

**When:** Fastest way to stand up a complete detection-and-response platform on one box or a small grid when you don't want to assemble the components yourself.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the ISO from https://securityonion.com, install, then run: sudo so-setup-network (guided wizard)`

**URL:** https://securityonion.com

**Alternatives:** suricata, zeek






## Web Application Firewall

ModSecurity ⭐


#### ModSecurity ⭐

The OWASP open-source WAF engine (an OWASP Production project) that inspects HTTP traffic and enforces SecRule policies on Apache/nginx; load the OWASP CRS on top for real attack coverage.

**When:** Inline HTTP-layer defense when you want the battle-tested rule ecosystem and can commit to tuning false positives against your apps.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt-get install libapache2-mod-security2 (Apache; for nginx compile the module with --with-compat --add-dynamic-module=../ModSecurity-nginx)`

**URL:** https://modsecurity.org

**Alternatives:** coraza, coreruleset (OWASP CRS)


#### Coraza

OWASP WAF written in Go with near-full ModSecurity compatibility — runs CRS v4 without the legacy C engine as a library or middleware for Caddy, Traefik, APISIX, and API gateways, ideal for detection-as-code.

**When:** Cloud-native stacks (Go services, containers, Caddy/Traefik/APISIX) where ModSecurity's build model is awkward but you still want CRS protection.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `xcaddy build --with github.com/corazawaf/coraza-caddy/v2 (then add the coraza_waf block to the Caddyfile)`

**URL:** https://coraza.io

**Alternatives:** modsecurity, coreruleset (OWASP CRS)


#### OWASP CRS

The OWASP flagship Core Rule Set — a community-maintained rule layer detecting SQLi, XSS, scanners, and other OWASP Top 10 attacks that runs on both ModSecurity and Coraza engines; a ruleset, not a standalone tool.

**When:** The rule layer to load onto any WAF engine so a bare install actually detects web attacks; tune via the anomaly-scoring exclusions to cut false positives.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone --depth 1 https://github.com/coreruleset/coreruleset.git (then Include the CRS config in your WAF engine)`

**URL:** https://coreruleset.org

**Alternatives:** modsecurity, coraza


#### Cloudflare WAF

Commercial managed edge WAF (SaaS) that filters traffic on Cloudflare's CDN using managed rulesets (including OWASP CRS coverage) plus bot and rate controls — no servers to run.

**When:** When your apps already sit behind Cloudflare and you want managed rules, DDoS/bot defense, and zero self-hosting in one panel.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (SaaS) — enable in the dash.cloudflare.com Security panel, pick a managed ruleset, and tune via custom rules`

**URL:** https://developers.cloudflare.com/waf/

**Alternatives:** modsecurity, coraza





