# 🕸️ OSINT — People, Infrastructure & Metadata

Passive intelligence on people, exposed infrastructure, and document metadata — for authorized recon and for auditing your own digital footprint.

## People & Social Intelligence



#### Username Lookup


##### Sherlock ⭐

Checks a username across 400+ platforms using HTTP status/pattern heuristics and returns every profile that exists; the reference CLI for username enumeration, actively maintained.

**When:** Confirm which sites a username you own is registered on so you can harden or clean up your own footprint.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install sherlock-project`

**URL:** https://github.com/sherlock-project/sherlock

**Alternatives:** maigret, blackbird, whatsmyname


##### Maigret

Collects a username dossier across 3000+ sites with account-type tags (social, dating, code) and exports HTML/PDF/JSON reports; picks up a fresh site list on each run.

**When:** When Sherlock's pass/fail list is not enough and you want an exportable report of everywhere a handle you control appears.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install maigret`

**URL:** https://github.com/soxoj/maigret

**Alternatives:** sherlock, blackbird, whatsmyname


##### Blackbird

Blazing-fast username enumerator that checks 500+ services with thread pools and color-coded existence results; built as a speed-focused companion to Sherlock and Maigret.

**When:** Bulk-check many candidate usernames over a short window, limited to handles and accounts you are authorized to investigate.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/p1ngul1n0/blackbird@latest`

**URL:** https://github.com/p1ngul1n0/blackbird

**Alternatives:** sherlock, maigret, whatsmyname


##### WhatsMyName

A community-maintained dataset of 700+ sites with exact fingerprints (URI patterns and success/not-found heuristics); the data engine underlying most username checkers.

**When:** Audit a checker result or drive your own authorized username sweep against a curated, up-to-date site list.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/WebBreacher/WhatsMyName.git`

**URL:** https://github.com/WebBreacher/WhatsMyName

**Alternatives:** sherlock, maigret, blackbird


#### Email Addresses


##### Breach Checkers


###### HaveIBeenPwned ⭐

Definitive breach and password-exposure checker: search any email or domain across a huge corpus of leaked datasets; free web search plus a documented API, with Pwned Passwords openly downloadable.

**When:** Check whether addresses or domains you control appeared in known breaches, and enforce password-exposure checks on your own estate.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web + API)`

**URL:** https://haveibeenpwned.com

**Alternatives:** intelligencex, leakcheck


###### IntelligenceX

Dark-web and public-data search engine indexing leaks, paste sites, forums, and code over a 10-year retention window; free tier with API and Telegram bots.

**When:** Check if your emails, domains, or phone numbers surface in dark-web and paste archives you are authorized to monitor.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key)`

**URL:** https://intelx.io

**Alternatives:** haveibeenpwned, leakcheck, dehashed


###### LeakCheck

Commercial breach aggregator with billions of entries supporting email, username, phone, and live-keyword search; paid tiers unlock full records.

**When:** Correlate breach hits across emails and passwords, but only on credentials you hold or are authorized to test.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - paid)`

**URL:** https://leakcheck.io

**Alternatives:** intelligencex, haveibeenpwned


##### Registration Checkers


###### Holehe ⭐

Checks which 120+ sites an email is registered on by replaying password-recovery flows without mailing the target, so the address is never alerted.

**When:** Find which platforms a breached or owned email is tied to, so stale accounts you control can be closed or secured.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install holehe`

**URL:** https://github.com/megadose/holehe

**Alternatives:** emailrep.io, theharvester


###### emailrep.io

Hosted API that scores email reputation, flags breach exposure and disposable providers, and lists the mainstream profiles tied to an address; free tier needs no key.

**When:** Triage a suspicious inbound sender or audit your own addresses as part of a defensive OSINT review.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key optional)`

**URL:** https://emailrep.io

**Alternatives:** holehe, haveibeenpwned


##### Domain Harvesting


###### theHarvester ⭐

Passive harvester of emails, employee names, subdomains, and reported API keys for a domain across many open sources; the reference domain reconnaissance CLI.

**When:** Map every email and subdomain publicly linked to a domain you own before hardening mail and DNS.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install theharvester`

**URL:** https://github.com/laramies/theHarvester

**Alternatives:** holehe, intelligencex


#### Phone Numbers


##### PhoneInfoga ⭐

Phone-number OSINT framework that attributes country, area, carrier, and line type and gathers scattered footprint data via configurable scanners; stable but slowly maintained.

**When:** Resolve a number you own or are authorized to analyze into provider facts before deeper carrier-level checks.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install phoneinfoga`

**URL:** https://github.com/sundowndev/phoneinfoga

**Alternatives:** holehe


#### Social Media Profiles


##### Instagram


###### Instaloader ⭐

Downloads Instagram profiles, posts, hashtags, highlight stories, and their metadata (captions, likes, comments) without an API key; scriptable and actively maintained.

**When:** Archive a public profile you own, or collect hashtag and post metadata for evidence preservation.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install instaloader`

**URL:** https://github.com/instaloader/instaloader

**Alternatives:** osintgram, snscrape


###### Osintgram

Interactive shell that pulls public Instagram profile info, captions, followers, tag lists, and bio-contact strings using a scratch session or a free Hiker API token (educational-use disclaimer included).

**When:** Relationship analysis on a public profile you operate — who tags, who comments, what contact strings appear in bios.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Datalux/Osintgram && pip3 install -r requirements.txt`

**URL:** https://github.com/Datalux/Osintgram

**Alternatives:** instaloader


##### Multi-Platform


###### snscrape ⭐

Python library/CLI that scrapes public posts and profiles to JSONL from several platforms; X/Twitter and Reddit backends are dead behind logins, but Telegram, Weibo, and some Mastodon instances still work.

**When:** Programmatic retrieval and archiving of public posts on platforms snscrape still supports, e.g. Telegram channels you monitor.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip3 install snscrape`

**URL:** https://github.com/JustAnotherArchivist/snscrape

**Alternatives:** instaloader, osintgram



## Metadata & File Forensics



#### Image & EXIF


##### ExifTool ⭐

Reads, writes, and edits EXIF/GPS/IPTC/XMP metadata across images, PDFs, and Office files; the metadata workhorse behind most document-forensics pipelines.

**When:** Forensic-grade tag extraction from local files — geolocation, author, generator, timestamps — before release or after acquisition.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install libimage-exiftool-perl`

**URL:** https://exiftool.org

**Alternatives:** fotoforensics, metagoofil


##### FotoForensics

Web tool that runs Error Level Analysis (ELA), panel scans, EXIF review, and JPEG quantization analysis to spot digital tampering in an uploaded image.

**When:** Check whether an image you own or are authorized to examine was edited, and inspect residual metadata block by block.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://fotoforensics.com

**Alternatives:** exiftool


#### Document Metadata


##### Metagoofil ⭐

Dork-driven harvester that finds indexed documents (.pdf, .docx, .xlsx) for a domain and downloads them for metadata stripping; the maintained opsdisk fork ships on Kali.

**When:** Collect every publicly indexed document on a domain you own so metadata and hidden information can be scrubbed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/opsdisk/metagoofil && pip3 install -r requirements.txt`

**URL:** https://github.com/opsdisk/metagoofil

**Alternatives:** exiftool, foca


##### FOCA

Windows GUI (C# with SQL Server backend) that fingerprints documents across search engines and extracts users, folders, and software into a browsable metadata project.

**When:** When you have a Windows workstation and want a point-and-click metadata project view for documents you control.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `installer from GitHub Releases (Windows GUI)`

**URL:** https://github.com/ElevenPaths/FOCA

**Alternatives:** metagoofil, exiftool


#### File Reputation


##### VirusTotal ⭐

Industry-standard crowdsourced engine for hashes, samples, URLs, and IP/domain reputation with 90+ AV engines, plus passive DNS and threat-signal context.

**When:** Check a file hash, URL, or IP you are investigating against years of crowdsourced detections during authorized analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key optional)`

**URL:** https://www.virustotal.com

**Alternatives:** spiderfoot



## Geolocation & Mapping



#### IP Location


##### ipinfo.io ⭐

IP address datasets and API for location, ISP, ASN, company, and privacy-risk signals; free lookup tier covers geolocation and network attribution.

**When:** Resolve an IP address you are investigating into location, provider, and ASN context.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install ipinfo`

**URL:** https://ipinfo.io

**Alternatives:** ipapi.co, shodan


##### ipapi.co

Free IP geolocation API returning country, city, ISP, timezone, and currency for any address; also offers bulk and commercial JSON/CSV plans.

**When:** Script location lookups for lists of IPs appearing in your own logs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API)`

**URL:** https://ipapi.co

**Alternatives:** ipinfo.io


#### Map & Geo Search


##### Google Maps ⭐

Global mapping, Street View, and satellite imagery search; the core visual geolocation and place-lookup surface for OSINT.

**When:** Correlate landmarks, signage, or geotagged imagery against the physical world during authorized investigations.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.google.com/maps

**Alternatives:** yandex maps


##### Yandex Maps

Alternative globe with strong coverage of Eastern Europe, Russia, and CIS regions plus street-level panoramas; a useful cross-check for place and imagery comparison.

**When:** Cross-check locations and side-by-side imagery with Google Maps when coverage hints at CIS or Eurasian regions.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://yandex.com/maps

**Alternatives:** google maps



## Domain & IP Infrastructure



#### IP & Attack Surface


##### Shodan ⭐

The reference internet device and service search engine indexing banners, ports, vulnerabilities, and exposure history for any IP or domain; also exposes free InternetDB lookups.

**When:** See exactly which ports and services your public IP ranges expose right now — and how long that exposure has existed — before closing them.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install shodan`

**URL:** https://www.shodan.io

**Alternatives:** censys, netlas


##### Censys

Internet-wide scan platform over hosts, services, and certificates with structured query language and host/cert/web-property APIs; free tier includes search and lookups.

**When:** Certificate-centric inventory and pivots — find every host presenting a given cert — or query structured service data beyond free Shodan limits.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install censys`

**URL:** https://search.censys.io

**Alternatives:** shodan, netlas


##### Netlas

Scanning platform over billions of indexed hosts supporting IPv4/IPv6, full response-body regex, DNS, WHOIS, and certificate search with a REST API; free tier capped near 50 requests/day.

**When:** Lucene/regex search across full HTTP response bodies when Shodan banners are too shallow for your authorized query.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install netlas`

**URL:** https://netlas.io

**Alternatives:** shodan, censys


#### DNS & Subdomains


##### DNSDumpster ⭐

One-page passive DNS mapping tool that enumerates subdomains, MX/TXT/SPF records, and hosts onto an interactive network map for a domain.

**When:** Fast visual pass over the subdomain and mail infrastructure of a domain you own before deeper enumeration.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://dnsdumpster.com

**Alternatives:** securitytrails, crt.sh


##### SecurityTrails

Commercial passive DNS and subdomain intelligence with historical DNS records, certificate timelines, and connected-domain data via REST API.

**When:** Retrieve DNS history and subdomain changes over time for a domain you operate, straight into scripts.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key)`

**URL:** https://securitytrails.com

**Alternatives:** dnsdumpster, crt.sh


#### Certificate Transparency


##### crt.sh ⭐

Open certificate-transparency log search; returns every issued certificate — and therefore every hostname — for a domain, sorted by issue date.

**When:** Enumerate all hostnames that ever had a public certificate for domains you own, including retired staging hosts.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://crt.sh

**Alternatives:** securitytrails, censys


#### WHOIS & Routing


##### Hurricane Electric BGP ⭐

Global BGP, IPv6, and routing intelligence: AS numbers, prefixes, IXP membership, route announcements, and peer relationships in a browsable web database.

**When:** Attribute an IP or prefix to its ASN and understand routing relationships for infrastructure you analyze.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://bgp.he.net

**Alternatives:** ripestat


##### RIPEstat

RIPE NCC's data API for IP/ASN attribution, route history, geolocation, and abuse contacts; queryable over REST with ready-made widgets.

**When:** Programmatic WHOIS/ASN and routing lookups for lists of IPs or prefixes you are researching.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API)`

**URL:** https://stat.ripe.net

**Alternatives:** hurricane electric bgp


#### Domain History


##### DomainTools ⭐

Commercial WHOIS and domain-intel suite (WhoIs, reverse whois, registration history, DNSHistory, Iris) maintained for 20+ years; priced via API/subscription tiers.

**When:** Full WHOIS history and reverse-ownership pivots on domains involved in authorized investigations.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - paid)`

**URL:** https://www.domaintools.com

**Alternatives:** securitytrails



## Business & Corporate OSINT



#### Company Registries


##### OpenCorporates ⭐

Open database of millions of companies worldwide extracted from public registries; unique API for entities, officers, and filings across many jurisdictions.

**When:** Discover corporate structure, officers, and cross-jurisdiction registrations behind a company you are authorized to research.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web - API key)`

**URL:** https://opencorporates.com

**Alternatives:** companies house (uk), sec edgar


##### Companies House (UK)

UK government registry of companies, officers, people with significant control (PSC), and filings, exposed through a free public API.

**When:** Company, director, and beneficial-owner lookups for UK-registered entities.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - free API key)`

**URL:** https://find-and-update.company-information.service.gov.uk

**Alternatives:** opencorporates


##### SEC EDGAR

US SEC's full-text filings database (10-K, 8-K, S-1, proxies) exposing financials, executives, and subsidiaries; free API with fair-use limits.

**When:** Pull US-listed company filings for financial and personnel intelligence.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API)`

**URL:** https://www.sec.gov/edgar

**Alternatives:** opencorporates


#### Company Profiles


##### Crunchbase ⭐

Venture and funding profile database with financing rounds, acquisitions, growth-stage signals, and key-people digests for startups and private companies.

**When:** Sketch the funding trajectory, investors, and key people of a private company you analyze.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key)`

**URL:** https://www.crunchbase.com

**Alternatives:** opencorporates



## Code & Developer OSINT



#### Code Search Engines


##### GitHub Code Search ⭐

GitHub's built-in search over the public code index with operators for language, path, and extension; also surfaces users, commits, and leaked-token suspects.

**When:** Find public code, configs, and secrets that mention an identifier you own, and review your own repositories' exposure.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://github.com/search

**Alternatives:** sourcegraph, gitdorker


##### Sourcegraph

Public-code search engine with regex, literal, and symbol-aware queries across open repositories; good for finding leaked patterns and re-used infrastructure.

**When:** Regex-wide sweep of public code for a credential prefix, domain, or package name you are attributing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://sourcegraph.com

**Alternatives:** github code search, gitdorker


#### Secret & Dork Hunting


##### GitDorker ⭐

Automates GitHub 'dork' queries from a 3000+-entry dork list through the search APIs to surface exposed files, keys, and configs in public repositories.

**When:** Glob for suspicious files and secrets across public repos related to your own organization or authorized targets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/obheda12/GitDorker && pip3 install -r requirements.txt`

**URL:** https://github.com/obheda12/GitDorker

**Alternatives:** github code search, nosey parker


##### Nosey Parker

Fast secret-scanner that extracts API tokens and credentials from git histories with high-precision regex and entropy rules; written in Rust for large corpora.

**When:** Scan cloned public repositories (e.g., ones you own) for historic secrets before they are abused.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/praetorian-inc/noseyparker && cargo build --release`

**URL:** https://github.com/praetorian-inc/noseyparker

**Alternatives:** gitdorker



## Crypto & Blockchain



#### Block Explorers


##### Blockchain.com Explorer ⭐

Bitcoin block explorer with address, transaction, and pending-mempool views plus webhooks and an authenticated explorer API.

**When:** Trace bitcoin addresses and transaction flows connected to a case you are authorized to investigate.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.blockchain.com/explorer

**Alternatives:** etherscan, walletexplorer


##### Etherscan

Reference Ethereum block explorer with address, token, contract-code, and event-log analysis and a free API; covers other EVM chains via sibling explorers.

**When:** Analyze EVM addresses, token transfers, and smart-contract interactions you are investigating.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API key)`

**URL:** https://etherscan.io

**Alternatives:** blockchain.com explorer


#### Wallet & Abuse Databases


##### WalletExplorer ⭐

Clusters bitcoin addresses into services where possible, letting you see a wallet's whole activity — including market aggregation endpoints.

**When:** View a bitcoin address in service context and reveal associated addresses during authorized tracing work.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.walletexplorer.com

**Alternatives:** blockchain.com explorer, bitcoinabuse


##### BitcoinAbuse

Public API and searchable database of bitcoin addresses reported for scams and fraud, with user-submitted evidence and descriptions.

**When:** Check whether an address you are investigating carries attached abuse reports.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web - API)`

**URL:** https://www.bitcoinabuse.com

**Alternatives:** walletexplorer



## Historical & Archived Content



#### Web Archives


##### Wayback Machine ⭐

The Internet Archive's store of hundreds of billions of web snapshots; view any URL as it existed historically, with CDX listings and full-text site search.

**When:** Recover removed pages, track historical site changes, and capture evidence before content disappears.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://web.archive.org

**Alternatives:** waybackpy, archive.today, common crawl


##### waybackpy

Python client for the Wayback and CDX APIs: save snapshots, query availability, and stream archive listings programmatically.

**When:** Scripted archival and CDX queries to build change-history timelines for URLs you monitor.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install waybackpy`

**URL:** https://github.com/akamhy/waybackpy

**Alternatives:** wayback machine


##### Archive.today

Independent web snapshot service that mirrors pages on demand and blocks most crawlers; a useful second capture layer parallel to the Wayback Machine.

**When:** Save a live page as evidence through an independent archive when you want redundancy across capture providers.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://archive.ph

**Alternatives:** wayback machine


#### Web Corpora


##### Common Crawl ⭐

Petabyte-scale open crawl corpus refreshed monthly (WARC/WAT/WET files) with a URL index API; reconstruct what a site published even without per-page snapshots.

**When:** Pull historical page versions or URL-level index data for content you have permission to analyze.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `preinstalled (web - S3/CLI)`

**URL:** https://commoncrawl.org

**Alternatives:** wayback machine



## Dark Web & Breach Intelligence



#### Onion Search & Directories


##### Ahmia ⭐

Ethical search engine for the Tor network with support for .onion and I2P; continuously indexes dark-web pages and filters illegal content.

**When:** Index and discover .onion pages relevant to a monitoring program you are authorized to run.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://ahmia.fi

**Alternatives:** dark.fail


##### Dark.fail

Trusted, hand-verified directory of live .onion marketplaces and services with uptime status; a safe entry index rather than an in-depth search engine.

**When:** Locate legitimate .onion services and verify their current uptime during authorized dark-web research.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://dark.fail

**Alternatives:** ahmia


#### Breach Data Aggregators


##### DeHashed ⭐

Commercial breach database covering email, username, phone, IP, and password hashes with fuzzy search and cross-referencing across billions of records; subscription required for full records.

**When:** Correlate leaked credentials and keys across datasets — only for accounts you own or are contracted to test.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web - paid)`

**URL:** https://dehashed.com

**Alternatives:** intelligencex, leakcheck


#### Paste Search & Monitoring


##### Pastebin Search ⭐

Pastebin's own search across public pastes, combinable with search engines via site: dorks; useful for monitoring dropped credentials and dumps.

**When:** Monitor public paste dumps that mention an organization or domain you are authorized to defend.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://www.pastebin.com

**Alternatives:** intelligencex



## Automation & Platforms



#### Correlation & Automation


##### SpiderFoot ⭐

Automated OSINT correlation engine with 200+ modules and a YAML correlation engine, surfaced through a web UI, CLI, and API; built to map an attack surface and connect entities.

**When:** A broad sweep of a domain, IP, or email you own to correlate entities across many free data sources in a single scan.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/smicallef/spiderfoot && pip3 install -r requirements.txt`

**URL:** https://github.com/smicallef/spiderfoot

**Alternatives:** maltego


##### Maltego

Commercial graph-based link-analysis platform (desktop and browser) whose transforms reach identity, breach, and infrastructure datasets; free Community Edition exists with result limits.

**When:** Investigative link analysis where a visual graph of who connects to whom beats raw JSON output.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/desktop - free CE)`

**URL:** https://www.maltego.com

**Alternatives:** spiderfoot


#### Search Dork Reference


##### Google Hacking Database (GHDB) ⭐

Canonical reference catalog of search-engine operators and example queries that surface exposed files, login panels, and misconfigurations in public indexes.

**When:** Compose and reuse proven dorks to audit what public indexes expose about domains you own.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.exploit-db.com/google-hacking-database

**Alternatives:** gitdorker



