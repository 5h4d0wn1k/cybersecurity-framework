# 🕵️ Reconnaissance & OSINT

Passive + active discovery: subdomains, DNS, historical data, people, leaks, and exposed assets.

## Subdomain Enumeration

### Amass ⭐

OWASP-recommended, querying dozens of sources for active/passive subdomains; builds graph and flagship-level relationships between discovered assets.

**When:** Full-scope startup: let it run long against a big target while you work other recon.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install -v github.com/owasp-amass/amass/v4/...@master`

**URL:** https://github.com/owasp-amass/amass

**Alternatives:** subfinder, crt.sh, dnsx


### Subfinder

Fast passive-only subdomain discovery from 30+ sources (APIs optional, works well without them).

**When:** The daily driver when you want speed over depth, or when API keys are scarce.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`

**URL:** https://github.com/projectdiscovery/subfinder

**Alternatives:** amass, crt.sh


### crt.sh

Transparency-log search over issued TLS certificates; zero-install, browser or curl.

**When:** Instant no-setup check; great for history not visible via simple DNS queries.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://crt.sh

**Alternatives:** subfinder, certsh


### dnsx

Fast multi-threaded DNS resolver built to verify a big list of candidate subdomains (A/AAAA/CNAME/TXT).

**When:** After enumeration: confirm which hosts resolve and grab their records in one pass.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest`

**URL:** https://github.com/projectdiscovery/dnsx

**Alternatives:** massdns


## HTTP Probing & Titles

### httpx ⭐

Probes a list of hosts and returns live status codes, technologies, titles, and fingerprints.

**When:** Convert hundreds of DNS names into a live-but-quiet target list before tooling takes over.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest`

**URL:** https://github.com/projectdiscovery/httpx

**Alternatives:** naabu (port scan), masscan


## Passive DNS & History

### SecurityTrails ⭐

Passive DNS history and subdomain API; free tier without keys.

**When:** See records that no longer resolve but reveal old infrastructure (staging, dev).

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://securitytrails.com

**Alternatives:** crt.sh, dnsdumpster


### VirusTotal DNS

Relations/passive-dns endpoints to map infrastructure and finding subdomains via historical resolution.

**When:** Correlate IP→domains and flag anomalies when you already have an API key.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.virustotal.com

**Alternatives:** crt.sh


## Port Discovery

### naabu ⭐

Fast SYN port scanner (projectdiscovery) focused on top 100/1000 ports; integrates cleanly with httpx/nuclei.

**When:** Quick-but-broad port discovery feeding the rest of the pipeline.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest`

**URL:** https://github.com/projectdiscovery/naabu

**Alternatives:** masscan, nmap, rustscan


### Masscan

Most-port-fastest scanner; emits results in a format easily piped into nmap or naabu.

**When:** Scan the entire internet range of your target (or very large CIDRs) quickly.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install masscan`

**URL:** https://github.com/robertdavidgraham/masscan

**Alternatives:** naabu, nmap


### nmap

The classic suite: port scan, OS/service detection, and scripting engine (NSE).

**When:** Deep service identification and vulnerability scripts on a small, targeted set of hosts.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install nmap`

**URL:** https://nmap.org

**Alternatives:** naabu, masscan, rustscan


### RustScan

Rust-based scanner that sweeps all ports in seconds then hands specifics to nmap.

**When:** When you want all-ports coverage faster than nmap's default and the pipeline output into nmap.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install rustscan`

**URL:** https://github.com/RustScan/RustScan

**Alternatives:** naabu, masscan

