# 🔍 Vulnerability Scanning & Assessment

Automated detection of known CVEs and misconfigurations at scale, plus manual triage.

## General Vulnerability Scanners

### Nuclei ⭐

Template-driven scanner (projectdiscovery) running thousands of YAML checks against your web, network, and infrastructure targets to confirm known CVEs and misconfigurations.

**When:** First-pass automated sweep across a whole asset list; fast and CI-friendly enough to run on every build.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest`

**URL:** https://github.com/projectdiscovery/nuclei

**Alternatives:** nessus, openvas, vuls


### Nessus

Tenable's market-standard commercial scanner with credentialed and remote checks across OSes, services, and web; the free Essentials tier covers a small lab.

**When:** Deep credentialed findings and compliance-style reports on the servers you operate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo dpkg -i Nessus-10.x-ubuntu.deb  (free Essentials .deb from tenable.com)`

**URL:** https://www.tenable.com/products/nessus

**Alternatives:** openvas, nuclei


### OpenVAS (GVM)

Greenbone's open-source stack forked from the old Nessus; schedules scans of thousands of network vulnerability tests (NVTs) with a web dashboard.

**When:** Self-hosted, ongoing internal-network scanning without commercial licensing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gvm && sudo gvm-setup`

**URL:** https://github.com/greenbone/openvas-scanner

**Alternatives:** nessus, nuclei


### Vuls

Agentless Go scanner that runs from one control host over SSH to inventory OS packages, middleware, and containers, then maps each server to applicable CVEs.

**When:** Fleet-level Linux vulnerability tracking when installing agents on every box is not an option.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `go install github.com/vulsio/vuls@latest`

**URL:** https://github.com/vulsio/vuls

**Alternatives:** nuclei, openvas


## Web Vulnerability Scanners

### Nikto ⭐

Perl web server scanner running 7,000+ checks for known files, outdated software, and misconfigurations on your own sites.

**When:** Fast baseline sweep of a web server's exposed surface before deeper application testing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install nikto`

**URL:** https://github.com/sullo/nikto

**Alternatives:** owasp zap, wapiti


### OWASP ZAP

Full-featured open-source web app scanner combining an intercepting proxy, spidering, and automated active and passive scanning behind a REST API.

**When:** DAST runs against the apps you build, or as the intercepting proxy for manual test sessions.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install zaproxy`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** nikto, wapiti, arachni


### Arachni

Feature-rich Ruby web app scanner with modular platform checks, a REST API, and distributed scanning of your own applications.

**When:** Headless or scripted scans that need to scale across many of your endpoints from one controller.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `Download and extract the arachni release archive from GitHub`

**URL:** https://github.com/Arachni/arachni

**Alternatives:** owasp zap, wapiti


### sqlmap

Long-standing automated SQL injection detector with database fingerprinting; validates whether a suspected injection point on your own app is genuinely exploitable.

**When:** Confirming and triaging reported SQLi findings on applications you own and operate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install sqlmap`

**URL:** https://github.com/sqlmapproject/sqlmap

**Alternatives:** wapiti, owasp zap


## Network & Service Scanners

### Nettacker ⭐

OWASP automation framework that scans your networks in layers (ports, services, subdomains), correlates the results, then runs follow-up module checks.

**When:** Automating broad network discovery plus vulnerability checks against your own infrastructure in one pass.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install nettacker`

**URL:** https://github.com/OWASP/Nettacker

**Alternatives:** nuclei, openvas


### Vulners

Aggregated vulnerability and exploit database offering a free API plus an Nmap script that matches your scanned services against millions of CVEs.

**When:** Enriching plain nmap service banners of your hosts with live CVE matches at no cost.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Copy vulners.nse into /usr/share/nmap/scripts/ (get it from vulners.com)`

**URL:** https://vulners.com

**Alternatives:** nuclei, nettacker, openvas


### OpenSCAP

NIST-certified scanner applying security-policy content (CIS, STIG) and OVAL CVE definitions to your Linux hosts for compliance and vulnerability posture.

**When:** Auditing your servers against published baselines and tracking CVE coverage across them.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install openscap-scanner`

**URL:** https://github.com/OpenSCAP/openscap

**Alternatives:** openvas, vuls


## CMS Scanners

### WPScan ⭐

WordPress scanner that fingerprints core, theme, and plugin versions against the WPScan vulnerability database and does user and weak-password checks.

**When:** Regularly auditing the WordPress sites you maintain for outdated plugins and known CVEs.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install wpscan`

**URL:** https://github.com/wpscanteam/wpscan

**Alternatives:** cmsmap, droopescan


### CMSmap

Python tool that scans WordPress, Joomla, and Drupal sites you own for known vulnerabilities and exposed file paths.

**When:** A single-command health check across mixed small-CMS estates without installing separate scanners.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/Dionach/CMSmap && cd CMSmap && python3 cmsmap.py`

**URL:** https://github.com/Dionach/CMSmap

**Alternatives:** wpscan, droopescan


### droopescan

Lightweight Perl scanner focused on Drupal, with partial WordPress and Bolt coverage; strong on plugin and module fingerprinting.

**When:** Targeted assessments of the Drupal sites in your fleet.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip install droopescan`

**URL:** https://github.com/droope/droopescan

**Alternatives:** wpscan, cmsmap


## Application & Dependency Scanners

### Trivy ⭐

Aqua's scanner that fingerprints vulnerable packages and CVEs in the container images, filesystems, IaC templates, and SBOMs you run.

**When:** Adding vuln gates to your image builds and scanning local containers for known CVEs before deployment.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** grype, osv-scanner


### Grype

Anchore's fast scanner pairing with Syft to map dependency CVEs across the containers and filesystems you build and ship.

**When:** Container and directory scans where you also want an SBOM generated in the same workflow.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/grype

**Alternatives:** trivy, osv-scanner


### osv-scanner

Google's scanner that matches your project lockfiles and SBOMs against the open-source-focused OSV.dev vulnerability database.

**When:** Quick CI check of dependency lockfiles in your own repos against a community-maintained vuln feed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/google/osv-scanner/cmd/osv-scanner@latest`

**URL:** https://github.com/google/osv-scanner

**Alternatives:** grype, trivy


### cve-bin-tool

Scans binary files and their strings to identify which known-vulnerable library and product components your software bundles.

**When:** Checking compiled products you distribute for embedded third-party components with published CVEs.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pip install cve-bin-tool`

**URL:** https://github.com/intel/cve-bin-tool

**Alternatives:** osv-scanner, trivy


## CVE & Exploit Lookup

### searchsploit / Exploit-DB ⭐

Offline grep over the ~40,000-entry Exploit-DB archive bundled with Kali, showing exploit scripts, Metasploit modules, and build instructions for your own lab.

**When:** Looking up local proof-of-concept code to reproduce and verify a CVE on systems you control.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install exploitdb`

**URL:** https://www.exploit-db.com

**Alternatives:** cve-search, nvd


### cve-search

Local MongoDB-backed engine that ingests NVD, CISA, and Exploit-DB feeds for fast bulk lookups across your whole inventory.

**When:** Correlating a large asset list against CVE data offline when you cannot rely on external APIs.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `docker run -d -p 5000:5000 cve-search/cve-search`

**URL:** https://github.com/cve-search/cve-search

**Alternatives:** nvd, searchsploit


### NVD (NIST)

Official NIST vulnerability feed and web UI; the reference source for CVE metadata, CPE mappings, and CVSS metrics.

**When:** Confirming identifiers, severity scores, and affected product lists for a CVE under review.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web/API)`

**URL:** https://nvd.nist.gov

**Alternatives:** cve-search, vulners

