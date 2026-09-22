# 🔍 Vulnerability Scanning & Assessment

Automated detection of known CVEs and misconfigurations at scale, plus manual triage.

## Network & Host Scanning




#### Port & Service Scanning



##### Nmap & Friends



###### Nmap ⭐

The de-facto open-source network scanner: host discovery, port scanning, OS and service fingerprinting, and NSE scripts for scripted vulnerability checks.

**When:** Baseline port and service enumeration across your own servers before deeper targeted testing.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install nmap`

**URL:** https://github.com/nmap/nmap

**Alternatives:** masscan, rustscan


###### nmap-vulners NSE

An Nmap script pair (vulners.nse / vulscan.nse) that queries the Vulners API with each scanned software version and prints matching CVEs next to the banner.

**When:** Turning a routine nmap scan of services you operate into an instant CVE snapshot with no extra tooling.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/vulnersCom/nmap-vulners && sudo cp nmap-vulners/*.nse /usr/share/nmap/scripts/`

**URL:** https://github.com/vulnersCom/nmap-vulners

**Alternatives:** vulners, nvd


##### High-Speed Port Scanners



###### Masscan ⭐

Robert Graham's asynchronous parallel scanner that can sweep all 65k ports of an address range in minutes using raw SYN packets.

**When:** Large authorized perimeter sweeps where nmap's serialized timing would take too long, followed by nmap for detail.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install masscan`

**URL:** https://github.com/robertdavidgraham/masscan

**Alternatives:** nmap, rustscan


###### RustScan

Rust-based port scanner that finds open ports in seconds, then pipes them straight into nmap for full service discovery.

**When:** Fast first-pass open-port identification when running a full nmap -p- on your hosts is too slow.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install rustscan`

**URL:** https://github.com/bee-san/RustScan

**Alternatives:** masscan, nmap


#### Host Discovery



##### Layer-2/LAN Discovery



###### arp-scan ⭐

ARP-based discovery that maps every live host and MAC vendor on the local segment you operate, including those ignoring ping.

**When:** Inventorying the devices on a LAN you administer before running port scans against them.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install arp-scan`

**URL:** https://github.com/royhills/arp-scan

**Alternatives:** netdiscover, nmap


###### netdiscover

Active (ARP request) and passive (sniff-and-log) network discovery with a lightweight interactive frame view of the subnet.

**When:** Live host discovery on switched networks you manage without agents.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install netdiscover`

**URL:** https://github.com/netdiscover-scanner/netdiscover

**Alternatives:** arp-scan, nmap


##### Internet-Scale Discovery



###### ZMap ⭐

High-performance network scanner built for internet-wide research on services you own; the engine behind the ZMap project ('there are no secrets on the internet').

**When:** Measuring the exposed surface of your own public address space in collaboration with your network ops team.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install zmap`

**URL:** https://github.com/zmap/zmap

**Alternatives:** masscan, nmap


#### Automated Recon Pipelines



##### Multi-phase Recon & Correlation



###### AutoRecon ⭐

Tib3rius's recon orchestrator that runs nmap, service enumeration, web scans, and vulnerability checks in parallel and writes per-host reports you can review.

**When:** Structured, repeatable external assessment of an IP range you are authorized to test.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/Tib3rius/AutoRecon && cd AutoRecon && pip3 install -r requirements.txt`

**URL:** https://github.com/Tib3rius/AutoRecon

**Alternatives:** nettacker, nuclei


###### Nettacker

OWASP scanner framework that scans layers of your network (ports, services, subdomains), correlates results, then runs follow-up module checks.

**When:** One-pass automated network discovery plus vulnerability probing across the infrastructure you own.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install nettacker`

**URL:** https://github.com/OWASP/Nettacker

**Alternatives:** autorecon, nuclei






## Web Application Scanning




#### Server & Edge Fingerprinting



##### Server Fingerprinting



###### WhatWeb ⭐

Ruby web fingerprinting tool identifying the platform, CMS, JavaScript libraries, and headers behind over 1,800 technology signatures.

**When:** Telling what stack a web property you own runs before picking follow-up scanners.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo gem install whatweb`

**URL:** https://github.com/urbanadventurer/WhatWeb

**Alternatives:** wappalyzer, nikto


###### Nikto

Perl web server scanner running 7,000+ checks for known files, outdated software, and misconfigurations on your own sites.

**When:** Fast baseline sweep of a web server's exposed surface before deeper application testing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install nikto`

**URL:** https://github.com/sullo/nikto

**Alternatives:** whatweb, owasp zap


##### WAF & Edge Detection



###### wafw00f ⭐

Identifies whether and which WAF (Cloudflare, ModSecurity, AWS WAF, etc.) fronts a web property, and fingerprints its version where detectable.

**When:** Checking what edge protection sits in front of your applications before sending scan traffic through it.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip3 install wafw00f`

**URL:** https://github.com/EnableSecurity/wafw00f

**Alternatives:** whatweb, nmap


#### Application-layer DAST



##### General-purpose DAST



###### OWASP ZAP ⭐

Full-featured open-source web app scanner combining an intercepting proxy, spidering, and automated active and passive scanning behind a REST API.

**When:** DAST runs against the apps you build, or as the intercepting proxy for manual test sessions.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install zaproxy`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** wapiti, nikto


###### Wapiti

Command-line web fuzzer performing black-box scans for SQLi, XSS, file inclusion, SSRF, and more, without needing a browser.

**When:** Scriptable, headless DAST batches over many of your endpoints in CI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install wapiti3`

**URL:** https://github.com/wapiti-scanner/wapiti

**Alternatives:** owasp zap, nuclei


##### Template-driven Scanning



###### Nuclei ⭐

ProjectDiscovery's template engine running thousands of YAML checks against web, network, and infrastructure targets to confirm known CVEs and misconfigurations.

**When:** First-pass automated sweep across a whole asset list; fast and CI-friendly enough to run on every build.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest`

**URL:** https://github.com/projectdiscovery/nuclei

**Alternatives:** owasp zap, openscap


#### Injection & XSS Testing



##### SQL Injection



###### sqlmap ⭐

Long-standing automated SQL injection detector with database fingerprinting; validates whether a suspected injection point on your own app is genuinely exploitable.

**When:** Confirming and triaging reported SQLi findings on applications you own and operate.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install sqlmap`

**URL:** https://github.com/sqlmapproject/sqlmap

**Alternatives:** wapiti, owasp zap


##### Cross-Site Scripting



###### dalfox ⭐

Fast Go-based XSS scanner that fuzzes parameters, builds payloads, and verifies reflected and stored vectors against the pages you maintain.

**When:** Payload-based validation of XSS candidates found by DAST tools on your own endpoints.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `go install github.com/hahwul/dalfox/v2@latest`

**URL:** https://github.com/hahwul/dalfox

**Alternatives:** owasp zap, sqlmap


#### CMS-Specific Scanners



##### WordPress



###### WPScan ⭐

WordPress scanner that fingerprints core, theme, and plugin versions against the WPScan vulnerability database and does user and weak-password checks.

**When:** Regularly auditing the WordPress sites you maintain for outdated plugins and known CVEs.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo gem install wpscan`

**URL:** https://github.com/wpscanteam/wpscan

**Alternatives:** cmsmap, whatweb


##### Multi-CMS (Joomla / Drupal)



###### CMSmap ⭐

Python tool that scans WordPress, Joomla, and Drupal sites you own for known vulnerabilities and exposed file paths.

**When:** A single-command health check across mixed small-CMS estates without installing separate scanners.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/Dionach/CMSmap && pip3 install -r CMSmap/requirements.txt`

**URL:** https://github.com/Dionach/CMSmap

**Alternatives:** wpscan, droopescan


###### droopescan

Lightweight Perl scanner focused on Drupal, with partial WordPress and Bolt coverage; strong on plugin and module fingerprinting.

**When:** Targeted assessments of the Drupal sites in your fleet.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip3 install droopescan`

**URL:** https://github.com/droope/droopescan

**Alternatives:** wpscan, cmsmap






## Vulnerability Management Platforms




#### Full VM Platforms



##### Commercial VM



###### Nessus ⭐

Tenable's market-standard commercial scanner with credentialed and remote checks across OSes, services, and web; the free Essentials tier covers a small lab.

**When:** Deep credentialed findings and compliance-style reports on the servers you operate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download Nessus *.deb from tenable.com and run: sudo dpkg -i Nessus-*.deb`

**URL:** https://www.tenable.com/products/nessus

**Alternatives:** openscap, nuclei


##### Open-Source VM



###### OpenVAS (GVM) ⭐

Greenbone's open-source stack forked from the old Nessus; schedules scans of thousands of network vulnerability tests (NVTs) with a web dashboard.

**When:** Self-hosted, ongoing internal-network scanning without commercial licensing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gvm && sudo gvm-setup`

**URL:** https://github.com/greenbone/openvas-scanner

**Alternatives:** nessus, nuclei


##### Agentless Fleet Scanning



###### Vuls ⭐

Agentless Go scanner that runs from one control host over SSH to inventory OS packages, middleware, and containers, then maps each server to applicable CVEs.

**When:** Fleet-level Linux vulnerability tracking when installing agents on every box is not an option.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `go install github.com/future-architect/vuls/cmd/vuls@latest`

**URL:** https://github.com/future-architect/vuls

**Alternatives:** openscap, openscap






## Infrastructure & Compliance Audit




#### Host Hardening Audit



##### Linux Security Audit



###### Lynis ⭐

Security auditing tool that runs 300+ tests on Unix systems to score hardening posture and flag misconfigurations, missing patches, and weak settings.

**When:** Whole-box hardening reviews of the Linux servers you run, on demand or scheduled.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install lynis`

**URL:** https://github.com/CISOfy/lynis

**Alternatives:** openscap, chkrootkit


##### SCAP/STIG Baselines



###### OpenSCAP ⭐

NIST-certified scanner applying security-policy content (CIS, STIG) and OVAL CVE definitions to your Linux hosts for compliance and vulnerability posture.

**When:** Auditing your servers against published baselines and tracking CVE coverage across them.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install openscap-scanner`

**URL:** https://github.com/OpenSCAP/openscap

**Alternatives:** lynis, openvas


#### Cloud Posture Assessments



##### AWS Attack & Posture



###### Pacu ⭐

Rhino Security Labs' AWS exploitation framework with modules for privilege escalation, lateral movement, and misconfiguration chaining against accounts you own.

**When:** Testing the blast radius of an IAM misconfiguration in your own AWS account during a red-team exercise.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/RhinoSecurityLabs/pacu && cd pacu && bash install.sh`

**URL:** https://github.com/RhinoSecurityLabs/pacu

**Alternatives:** scoutsuite, prowler


###### Prowler

Cloud security tooling applying 200+ AWS (and Azure/GCP) checks aligned to CIS, NIST, and ISO to surface misconfigurations in accounts you operate.

**When:** Automated compliance sweeps of your cloud accounts before audits.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install prowler`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** scoutsuite, pacu


##### AWS / Azure / GCP



###### ScoutSuite ⭐

Security audit tool from NCC Group that uses cloud APIs to enumerate resources and generate an HTML report of weaknesses across AWS, Azure, and GCP.

**When:** Read-only posture reviews of your cloud subscriptions summarized into one report.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip3 install scoutsuite`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** prowler, pacu






## Container & Image Scanning




#### Image & Filesystem Scanning



##### CLI & CI Scanners



###### Trivy ⭐

Aqua's scanner that fingerprints vulnerable packages and CVEs in the container images, filesystems, IaC templates, and SBOMs you run.

**When:** Adding vuln gates to your image builds and scanning local containers for known CVEs before deployment.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** grype, syft


###### Grype

Anchore's fast scanner pairing with Syft to map dependency CVEs across the containers and filesystems you build and ship.

**When:** Container and directory scans where you also want an SBOM generated in the same workflow.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/grype

**Alternatives:** trivy, clair


##### SBOM Generation



###### Syft ⭐

Generates an inventory/SBOM of the packages, libraries, and metadata inside container images and directory trees, feeding downstream scanners.

**When:** Getting a machine-readable software bill of materials for the images you build, then diffing against CVE feeds.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/syft

**Alternatives:** trivy, grype


#### Registry & Fleet Scanning



##### Registry Scanning



###### Clair ⭐

Quay's open-source static analyzer that watches container registries and reports vulnerabilities in each image's layers via a JSON API.

**When:** Continuous scanning of the container registry you operate so images are screened before and after push.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run -d -p 6060:6060 -p 6061:6061 quay.io/projectquay/clair`

**URL:** https://github.com/quay/clair

**Alternatives:** trivy, grype






## Dependency & SCA Scanning




#### Lockfile & Package Scanners



##### Multi-language



###### Snyk ⭐

Developer-focused SCA platform with a free CLI that maps your manifest and lockfiles to known vulnerabilities and suggests upgrades.

**When:** Fast triage of dependency findings in your repos with remediation hints.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `npm install -g snyk && snyk auth`

**URL:** https://github.com/snyk/cli

**Alternatives:** osv-scanner, pip-audit


###### osv-scanner

Google's scanner that matches your project lockfiles and SBOMs against the open-source-focused OSV.dev vulnerability database.

**When:** Quick CI check of dependency lockfiles in your own repos against a community-maintained vuln feed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/google/osv-scanner/cmd/osv-scanner@latest`

**URL:** https://github.com/google/osv-scanner

**Alternatives:** snyk, osv.dev


##### Python



###### pip-audit ⭐

PyPA's scanner that audits installed Python packages and lockfiles against the OSV and PyPI advisory feeds, with a fix action.

**When:** Adding a pip dependency check to your Python projects' CI pipelines.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install pip-audit`

**URL:** https://github.com/pypa/pip-audit

**Alternatives:** osv-scanner, snyk


##### JavaScript / Node.js



###### npm audit ⭐

Built-in npm command that checks package-lock.json against the npm advisory database and proposes non-breaking or breaking upgrades.

**When:** Dependency health checks in JS projects you maintain, straight from your package manager.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `npm audit`

**URL:** https://docs.npmjs.com/cli/v10/commands/npm-audit

**Alternatives:** snyk, osv-scanner


#### Binary Component Scan



##### Compiled Artifacts



###### cve-bin-tool ⭐

Scans binary files and their strings to identify which known-vulnerable library and product components your software bundles.

**When:** Checking compiled products you distribute for embedded third-party components with published CVEs.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip3 install cve-bin-tool`

**URL:** https://github.com/intel/cve-bin-tool

**Alternatives:** osv-scanner, trivy






## Vulnerability Databases & Lookup




#### CVE & NVD Sources



##### NIST NVD



###### NVD ⭐

Official NIST vulnerability feed and web UI; the reference source for CVE metadata, CPE mappings, and CVSS metrics.

**When:** Confirming identifiers, severity scores, and affected product lists for a CVE under review.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web + free REST API, no install)`

**URL:** https://nvd.nist.gov

**Alternatives:** cve.org, vulners


##### CVE Authority (MITRE)



###### CVE.org ⭐

The CVE Program's own record search and API maintained by MITRE, giving canonical descriptions, references, and reservation workflows.

**When:** Reading the authoritative record and reference list for a given CVE-ID.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web + JSON 5.0 API, no install)`

**URL:** https://www.cve.org

**Alternatives:** nvd, osv.dev


##### Aggregators & Local Feeds



###### Vulners ⭐

Aggregated vulnerability and exploit database offering a free API plus the vulners.nse Nmap script that matches your scanned services against millions of CVEs.

**When:** Enriching plain nmap service banners of your hosts with live CVE matches at no cost.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install vulners  (or query the REST API)`

**URL:** https://vulners.com

**Alternatives:** nvd, nmap-vulners


###### cve-search

Local MongoDB-backed engine that ingests NVD, CISA, and Exploit-DB feeds for fast bulk lookups across your whole inventory.

**When:** Correlating a large asset list against CVE data offline when you cannot rely on external APIs.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run -d -p 5000:5000 cve-search/cve-search`

**URL:** https://github.com/cve-search/cve-search

**Alternatives:** nvd, vulners


#### OSV & Open-Source Feeds



##### OSV.dev



###### OSV.dev ⭐

Google's open-source-oriented vulnerability database with a query API keyed on affected package/ecosystem plus a public, continuous-export data feed.

**When:** Programmatic lookup of vulnerabilities for the exact package versions in your SBOM or lockfile.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web + REST/GraphQL API, no install)`

**URL:** https://osv.dev

**Alternatives:** nvd, osv-scanner


#### Exploit Intelligence



##### Exploit-DB & searchsploit



###### Exploit-DB / searchsploit ⭐

Offline grep over the ~40,000-entry Exploit-DB archive bundled with Kali, showing exploit scripts, Metasploit modules, and build instructions for your own lab.

**When:** Looking up local proof-of-concept code to reproduce and verify a CVE on systems you control.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install exploitdb`

**URL:** https://github.com/offensive-security/exploitdb

**Alternatives:** metasploit, cve-search


##### Metasploit & Modules



###### Metasploit Framework ⭐

Rapid7's exploit framework whose auxiliary and exploit modules double as scanners, with searchsploit-backed proof-of-concept modules for verified CVEs.

**When:** Reproducing a known CVE against your lab systems and deploying the matching exploit module in a controlled environment.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod +x msfinstall && sudo ./msfinstall`

**URL:** https://github.com/rapid7/metasploit-framework

**Alternatives:** exploit-db / searchsploit, cve-search





