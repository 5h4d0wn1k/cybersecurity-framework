# 🕵️ Reconnaissance & OSINT

Passive + active discovery: subdomains, DNS, historical data, people, leaks, and exposed assets.

## Subdomain Enumeration




#### grainrecon ◆ by 5h4d0wn1k

Automated recon / attack-surface mapper — subdomains, DNS, port/service, tech-detect, CIDR inventory, OSINT, dir fuzzing.

**When:** Building a full attack-surface map of assets you are authorized to test.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/grainrecon`

**URL:** https://github.com/5h4d0wn1k/grainrecon

**Alternatives:** Own tool — lab/authorized use only


#### Passive Sources



##### Certificate Transparency



###### crt.sh ⭐

Search engine over public Certificate Transparency logs; finds every subdomain that ever appeared in an issued TLS certificate.

**When:** Zero-setup first pass: instant historical subdomain list from issued certificates, no API keys required.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://crt.sh

**Alternatives:** subfinder, certspotter


###### Cert Spotter

SSLMate's certificate-transparency monitor with a JSON API; returns certificate-linked subdomains plus issuance history.

**When:** Watch a domain for newly issued certificates over time and script the subdomain results.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://github.com/sslmate/certspotter

**Alternatives:** crt.sh


##### Data Provider APIs



###### Subfinder ⭐

Fast passive subdomain discovery from 25+ sources (certificates, DNS, archives, APIs); runs well keyless and better with free API keys.

**When:** The daily driver for breadth: batch-enumerate subdomains from many passive sources in seconds.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`

**URL:** https://github.com/projectdiscovery/subfinder

**Alternatives:** amass, crt.sh


###### Chaos

ProjectDiscovery's continuously updated subdomain dataset fed by bug-bounty programs, queried through the chaos-client CLI.

**When:** Pull an up-to-date subdomain dataset for a listed asset instead of brute-forcing from scratch.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest`

**URL:** https://github.com/projectdiscovery/chaos-client

**Alternatives:** subfinder


###### VirusTotal

Huge passive-DNS and resolution graph; the domain 'Relations' tab exposes related hosts, resolutions, and SSL-cert domains.

**When:** Correlate a domain's infrastructure graph and pull historical resolutions when an API key is at hand.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.virustotal.com

**Alternatives:** crt.sh, chaos


#### Active Enumeration



##### Dictionary Brute Force



###### Resolver-verified Candidates



###### Puredns ⭐

Pipeline-focused brute-forcer that mass-resolves candidates through validated public resolvers and filters wildcard responses automatically.

**When:** Run a strong wordlist through trusted resolvers when you only want real, wildcard-free hits as pipeline output.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `go install -v github.com/d3mondev/puredns/v2@latest`

**URL:** https://github.com/d3mondev/puredns

**Alternatives:** gobuster, massdns


###### Gobuster

Multi-mode brute-forcer whose DNS mode guesses subdomains from a wordlist and resolves each candidate.

**When:** Quick DNS wordlist run when full resolver management is overkill for the scope.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `go install -v github.com/OJ/gobuster/v3@latest`

**URL:** https://github.com/OJ/gobuster

**Alternatives:** puredns


##### Permutation & Alteration



###### altdns ⭐

Generates wordlist-based permutations of known subdomains (prefixes, suffixes, number swaps) to rediscover forgotten hosts.

**When:** Expand an existing host list into thousands of plausible neighbor names before resolving.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/infosec-au/altdns && cd altdns && pip3 install -r requirements.txt`

**URL:** https://github.com/infosec-au/altdns

**Alternatives:** dnsgen, dnstwist


###### dnsgen

Pipes known domains through smart permutation rules (word insertion, affixing, number manipulation) to produce candidate subdomains.

**When:** Compose with massdns (cat list | dnsgen - | massdns) for a fast generate-then-resolve enumerator.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install dnsgen`

**URL:** https://github.com/AlephNullSK/dnsgen

**Alternatives:** altdns


##### Graph & API Aggregation



###### Amass ⭐

OWASP's one-stop subdomain engine: passive source scraping plus active brute forcing woven into an asset relationship graph.

**When:** Long-running, full-scope enumeration where breadth and cross-asset correlation matter most.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install -v github.com/owasp-amass/amass/v4/...@master`

**URL:** https://github.com/owasp-amass/amass

**Alternatives:** subfinder, chaos


#### Resolution & Verification



##### Bulk Resolving



###### dnsx ⭐

High-performance DNS toolkit that resolves thousands of candidates and returns A/AAAA/CNAME/TXT with wildcard filtering.

**When:** Filter a huge candidate list down to live hosts and fetch their records in a single pass.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest`

**URL:** https://github.com/projectdiscovery/dnsx

**Alternatives:** massdns


###### massdns

Extremely fast bulk resolver built to validate millions of candidates over UDP against a list of public resolvers.

**When:** Feed permutation output at internet scale when normal resolver throughput rate-limits you.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/blechschmidt/massdns && cd massdns && make`

**URL:** https://github.com/blechschmidt/massdns

**Alternatives:** dnsx






## DNS & WHOIS Interrogation




#### Active DNS Queries



##### Core Utilities



###### dig ⭐

BIND's universal DNS interrogation client: any record type, AXFR/IXFR zone transfer attempts, and scripting-friendly output.

**When:** Verify individual records and try authorized zone transfers on targets you are cleared to test.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install dnsutils`

**URL:** https://bind.isc.org

**Alternatives:** nslookup, host


##### Recon-focused Tools



###### DNSRecon ⭐

Python DNS recon kit: standard records, cache snooping, wildcard testing, brute force, and AXFR checks in one pass.

**When:** Automate the full DNS interrogation checklist on a scope where hand-rolled dig commands get tedious.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install dnsrecon`

**URL:** https://github.com/darkoperator/dnsrecon

**Alternatives:** dnsx, dnstwist


###### dnstwist

Permutation engine for typo-squatting and homograph lookalikes of a domain; resolves each variant to flag impersonation risk.

**When:** Authorized brand-protection reviews: find lookalike domains that could phish or impersonate your organization.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/elceef/dnstwist && cd dnstwist && make all`

**URL:** https://github.com/elceef/dnstwist

**Alternatives:** dnsgen


#### WHOIS & RDAP



##### Protocol Clients



###### WHOIS ⭐

Standard registrar/registry client returning registration, owner, and nameserver records for domains and IP blocks.

**When:** Pull registration dates and registrant metadata for a domain or range during authorized investigations.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install whois`

**URL:** https://www.iana.org/whois

**Alternatives:** rdap


###### RDAP

openrdap's Go client for the modern RDAP protocol: structured JSON instead of loose text, with paging and entity linking.

**When:** Script structured WHOIS-like lookups and follow registrant/registrar entities programmatically.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `go install github.com/openrdap/rdap/cmd/rdap@latest`

**URL:** https://github.com/openrdap/rdap

**Alternatives:** whois


##### Web Aggregators



###### ViewDNS.info ⭐

Free web aggregator for historical DNS, reverse IP, IP history, ASN/netblock maps, and WHOIS, with no API key.

**When:** Cross-check old IPs, nameservers, or reverse lookups without pulling out heavy tooling.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://viewdns.info

**Alternatives:** whois, dig






## Passive DNS & Historical Data




#### Passive DNS Databases



##### Record History



###### SecurityTrails ⭐

Full passive-DNS history plus subdomain and associated-domain APIs; the free tier works without keys.

**When:** Reconstruct a domain's historical IP infrastructure to find withdrawn dev or staging servers.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://securitytrails.com

**Alternatives:** virustotal, rapid7


###### DNSDumpster

Visual subdomain, MX, and hostname map with optional on-page screenshots of discovered hosts.

**When:** A graphical first look at a domain's DNS layout without signing up for anything.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://dnsdumpster.com

**Alternatives:** securitytrails, crt.sh


###### Rapid7 Open Data

Massive historical forward-DNS, reverse-DNS, and SSL scan datasets published as downloadable snapshots.

**When:** Power offline historical enumeration across full internet snapshots with your own tooling.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `free account + dataset download`

**URL:** https://opendata.rapid7.com

**Alternatives:** securitytrails


#### Web History



##### Page & Site Archives



###### Wayback Machine ⭐

Internet Archive's snapshot library exposing old pages, removed endpoints, and historical response bodies for any URL.

**When:** Recover deleted pages or inspect the evolution of login/config URLs during authorized historical research.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web); CLI: pip3 install waybackpy`

**URL:** https://web.archive.org

**Alternatives:** urlscan.io


###### urlscan.io

Renders and archives pages with full DOM, request log, and IP metadata; searchable by domain across every scan.

**When:** See what a page actually loaded (networks, frameworks, subresources) without touching the target yourself.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://urlscan.io

**Alternatives:** web.archive.org






## Port Discovery




#### Broad Discovery



##### High-speed Sweeps



###### naabu ⭐

ProjectDiscovery's fast SYN scanner sweeping the top-N ports and handing live hosts to httpx/nuclei.

**When:** Broad-but-quick port sweep across a large host list as pipeline input.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest`

**URL:** https://github.com/projectdiscovery/naabu

**Alternatives:** rustscan, nmap


###### masscan

Internet-scale SYN scanner (millions of packets/sec) that emits results in a format nmap can consume.

**When:** Full-CIDR or internet-range sweeps when naabu's port sets are too small.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install masscan`

**URL:** https://github.com/robertdavidgraham/masscan

**Alternatives:** nmap


###### RustScan

Sweeps all 65,535 ports in seconds and auto-pipes open ports into nmap service detection.

**When:** Complete all-port coverage with minimal effort, letting nmap take over the fine details.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install rustscan`

**URL:** https://github.com/bee-san/RustScan

**Alternatives:** naabu, masscan


#### Service & OS Analysis



##### Scriptable Detection



###### Nmap ⭐

The canonical suite: stealth/connect scans, OS and service fingerprinting, version detection, and the NSE scripting engine.

**When:** Deep service identification and low-rate version scans on a focused host set.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install nmap`

**URL:** https://nmap.org

**Alternatives:** naabu, masscan






## HTTP Probing & Fingerprinting




#### Live Host Probing



##### HTTP/S Availability



###### httpx ⭐

Probes host lists for live web services, returning status, title, tech, CDN, and TLS fingerprints in one pass.

**When:** Turn DNS/noise results into a clean inventory of live, web-facing hosts.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest`

**URL:** https://github.com/projectdiscovery/httpx

**Alternatives:** httprobe


#### Technology Fingerprinting



##### Signature Detection



###### WhatWeb ⭐

Signature-based fingerprint scanner matching headers, cookies, and HTML against 1,800+ technology definitions.

**When:** Per-URL technology attribution across a moderately sized authorized target list.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install whatweb`

**URL:** https://github.com/urbanadventurer/WhatWeb

**Alternatives:** builtwith


###### Retire.js

Scans page JavaScript for known-vulnerable library versions using DOM signatures.

**When:** Fingerprint front-end dependencies and their exact versions on pages you are authorized to review.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `npm install --global retire`

**URL:** https://github.com/retirejs/retire.js

**Alternatives:** whatweb


#### WAF Detection



##### WAF Identification



###### wafw00f ⭐

Sends harmless, identifiable probes to classify which WAF (if any) fronts a site, with vendor-specific signatures.

**When:** Understand a target's defensive layer before deeper authorized testing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install wafw00f`

**URL:** https://github.com/EnableSecurity/wafw00f

**Alternatives:** whatweb






## Web Content Discovery




#### Directory & Path Brute Force



##### Directory & Path Discovery



###### Feroxbuster ⭐

Rust-based recursive content discovery with smart filtering, auto-tuning, and server-config thesaurus support.

**When:** Recursive directory/file brute force that stays fast on large authorized targets.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `cargo install feroxbuster`

**URL:** https://github.com/epi052/feroxbuster

**Alternatives:** dirsearch, gobuster


###### dirsearch

Python content scanner with a large bundled dictionary, recursion, and multiple filter options.

**When:** Quick wordlist-driven directory hunting with minimal setup.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/maurosoria/dirsearch && cd dirsearch && python3 dirsearch.py`

**URL:** https://github.com/maurosoria/dirsearch

**Alternatives:** feroxbuster, ffuf


#### Parameter & Payload Fuzzing



##### Parameter Fuzzing



###### ffuf ⭐

Blazing-fast Go fuzzer for directories, virtual hosts, parameters, and headers via FUZZ placeholders.

**When:** Flexible content, vhost, or parameter fuzzing where wordlists and matcher filters need fine control.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/ffuf/ffuf/v2@latest`

**URL:** https://github.com/ffuf/ffuf

**Alternatives:** feroxbuster, wfuzz






## Crawling & JS Analysis




#### Crawlers



##### In-scope Crawling



###### Katana ⭐

ProjectDiscovery's crawler with headless and standard modes, strict scope control, and JS-rendered page crawling.

**When:** Deep crawl restricted to in-scope hosts while capturing files, parameters, and tech hints.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install -v github.com/projectdiscovery/katana/cmd/katana@latest`

**URL:** https://github.com/projectdiscovery/katana

**Alternatives:** gospider, hakrawler


###### gospider

Crawler focused on discovering subdomains, paths, buckets, and endpoints across seed URLs, with optional JS scraping.

**When:** Link newly found subdomains to their content and gather link graphs across many seeds.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `go install -v github.com/jaeles-project/gospider@latest`

**URL:** https://github.com/jaeles-project/gospider

**Alternatives:** katana


###### hakrawler

Simple, fast link-crawler emitting unique URLs, forms, and script references from the pages it visits.

**When:** A lightweight URL harvest with zero configuration before heavier crawling kicks in.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/hakluke/hakrawler@latest`

**URL:** https://github.com/hakluke/hakrawler

**Alternatives:** katana, gospider


#### JavaScript Recon



##### Endpoint Extraction



###### LinkFinder ⭐

Regex and JS-parser-based endpoint miner that extracts URLs and hidden API paths from JavaScript bundles.

**When:** Map the API surface hidden inside a site's JavaScript bundles.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/GerbenJavado/LinkFinder && cd LinkFinder && pip3 install -r requirements.txt`

**URL:** https://github.com/GerbenJavado/LinkFinder

**Alternatives:** secretfinder


###### SecretFinder

Scans JS files for hardcoded keys, tokens, and credentials using cloud/API-specific signature patterns.

**When:** Authorized audits: surface API keys or credentials accidentally shipped in client-side bundles.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/m4ll0k/SecretFinder && cd SecretFinder && pip3 install -r requirements.txt`

**URL:** https://github.com/m4ll0k/SecretFinder

**Alternatives:** linkfinder






## Internet Search Engines




#### Internet-wide Scanners



##### Host & Service Indexes



###### Shodan ⭐

The canonical search engine for exposed services: banners, ports, TLS certs, and device fingerprints across the internet.

**When:** Find every internet-facing service an organization exposes, by banner, org, or certificate query.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API)`

**URL:** https://www.shodan.io

**Alternatives:** censys, fofa


###### Censys

Continuous internet-scan dataset with faceted search over hosts, certificates, and services, plus ASN/hosting attribution.

**When:** Correlate exposed services with certificates and hosting metadata at scale.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API)`

**URL:** https://censys.io

**Alternatives:** shodan


###### FOFA

Cyberspace search engine indexing services, assets, and applications with powerful expression-based queries.

**When:** Get an overlapping, independent view of your exposed asset surface from different data sources.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://fofa.info

**Alternatives:** shodan, censys


#### Web Research



##### Site & Source Search



###### BuiltWith ⭐

Maps the technology stack of any site and can reverse-search for other sites sharing the same tech footprint.

**When:** Per-URL tech attribution and finding related deployments through shared vendor footprints.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://builtwith.com

**Alternatives:** whatweb


###### PublicWWW

Source-code search engine matching any snippet (analytics IDs, tracking pixels, specific JS) across indexed sites.

**When:** Find other properties sharing the same tracking or CDN code to expand the authorized asset footprint.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://publicwww.com

**Alternatives:** builtwith






## People & Identity OSINT




#### Username Enumeration



##### Multi-platform Checkers



###### Sherlock ⭐

Checks 400+ sites for a username in seconds and maps social/forum presences back to one identity.

**When:** Correlate an individual's handle across platforms during authorized persona research.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install sherlock-project`

**URL:** https://github.com/sherlock-project/sherlock

**Alternatives:** whatsmyname


###### WhatsMyName

Open-source username-presence database with auditable per-service detection patterns.

**When:** When you need a maintained, inspectable detection database you can extend for niche platforms.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/WebBreacher/WhatsMyName`

**URL:** https://github.com/WebBreacher/WhatsMyName

**Alternatives:** sherlock


#### Email Discovery



##### Address Discovery



###### theHarvester ⭐

Multipurpose passive gatherer of emails, subdomains, hosts, and employee names from search engines, PGP, and GitHub.

**When:** First-pass sweep that combines the human and asset surface in a single command.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/laramies/theHarvester && cd theHarvester && pip3 install -r requirements.txt`

**URL:** https://github.com/laramies/theHarvester

**Alternatives:** hunter, subfinder


###### Hunter.io

Web and API domain email finder with address patterns, verification, and per-domain counts (rate-limited free tier).

**When:** Discover and verify an organization's email address pattern during authorized intel gathering.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://hunter.io

**Alternatives:** theharvester


###### holehe

Checks whether an email address is registered on hundreds of online services without sending any mail.

**When:** Map which platforms an address is active on during an authorized investigation, minding service rate limits.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip3 install holehe`

**URL:** https://github.com/megadose/holehe

**Alternatives:** sherlock






## Leaks & Breach Data




#### Breach Lookup



##### Account Exposure



###### Have I Been Pwned ⭐

Canonical breach-correlation service checking emails and password ranges against aggregated breached datasets.

**When:** Identify which breaches an address appears in via the authenticated API during incident response.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web/API)`

**URL:** https://haveibeenpwned.com

**Alternatives:** dehashed, intelx


###### DeHashed

Searchable breach database with rich filtering by username, email, IP, and password hash.

**When:** Structured correlation across breaches with exportable results for authorized investigations.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API; paid)`

**URL:** https://www.dehashed.com

**Alternatives:** have i been pwned


#### Searchable Archives



##### Data Indexes



###### Intelligence X ⭐

Search engine for documents, leaks, dark-web content, PGP keys, and historical web data, with a public API.

**When:** Broadly triangulate a domain, email, or identity across leaks and scraped datasets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://intelx.io

**Alternatives:** dehashed






## Network & ASN Context




#### ASN & BGP



##### ASN Mapping



###### asnmap ⭐

ProjectDiscovery CLI mapping domains/IPs to ASNs and returning organization plus CIDR blocks from multiple sources.

**When:** Expand scope correctly by pulling every org-owned netblock for a target.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/asnmap/cmd/asnmap@latest`

**URL:** https://github.com/projectdiscovery/asnmap

**Alternatives:** bgp.he.net


###### bgp.he.net

Hurricane Electric's BGP board showing ASN graphs, prefix announcements, and peering for any network.

**When:** Visualize an organization's routing footprint, upstreams, and IPv4/IPv6 prefixes.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://bgp.he.net

**Alternatives:** asnmap


#### IP Geolocation



##### IP Metadata



###### ipinfo.io ⭐

IP metadata API providing geolocation, ASN, organization, hosting/cloud detection, and per-range domain lists.

**When:** Attach location and hosting context to discovered IPs and enrich bulk results from the CLI.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl https://ipinfo.io/8.8.8.8`

**URL:** https://ipinfo.io

**Alternatives:** ip-api.com





