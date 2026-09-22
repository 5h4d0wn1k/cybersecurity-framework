# 🕸️ OSINT — People, Infrastructure & Metadata

Passive intelligence on people, exposed infrastructure, and document metadata — for authorized recon and for auditing your own digital footprint.

## Username & People Discovery

Sherlock ⭐


#### Sherlock ⭐

Checks a username across 400+ social networks using HTTP status/pattern heuristics; the most widely maintained CLI for username existence.

**When:** Find every public profile tied to a username you own, or verify a handle before cleaning up your own exposure.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install sherlock-project`

**URL:** https://github.com/sherlock-project/sherlock

**Alternatives:** maigret, whatsmyname, namechk (web)


#### Maigret

Collects a username dossier across 3000+ sites, tagging each account by type (social, dating, code) and generating HTML/PDF/JSON reports; actively maintained with a frequently refreshed site database.

**When:** When Sherlock's pass/fail list is not enough and you want account tags, graph export, and a readable report of where a username appears.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install maigret`

**URL:** https://github.com/soxoj/maigret

**Alternatives:** sherlock, whatsmyname


#### WhatsMyName

A community-maintained JSON dataset covering 700+ sites with exact success/not-found detections; the data layer behind many username checkers and the whatsmyname.app web UI since the bundled checker scripts were removed in 2023.

**When:** When you want the raw detection data to audit a check result or drive your own checker against a curated site list.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/WebBreacher/WhatsMyName.git`

**URL:** https://github.com/WebBreacher/WhatsMyName

**Alternatives:** sherlock, maigret, namechk (web)


#### namechk

Free web service that checks a name across 100+ social platforms and 36 domain extensions in one view; a hosted service, not a self-hosted tool — no API and no bulk mode.

**When:** A quick browser-only triage of where a name is already taken before you invest in CLI pipelines.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web)`

**URL:** https://namechk.com

**Alternatives:** whatsmyname, sherlock, maigret






## Email & Phone OSINT

theHarvester ⭐


#### theHarvester ⭐

Passively harvests emails, employee names, subdomains, hosts, and API leaks for a domain from open sources; the reference OSINT email/subdomain harvester, actively maintained.

**When:** Map every email address and subdomain publicly linked to a domain you own before hardening mail and DNS.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install theharvester`

**URL:** https://github.com/laramies/theHarvester

**Alternatives:** holehe, emailrep.io (web)


#### Holehe

Checks whether an email is registered on 120+ sites by replaying their password-recovery flows without sending anything to the mailbox, so the target address is not alerted.

**When:** Find which platforms a leaked or owned email is tied to so you can spot stale accounts you control that still need securing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install holehe`

**URL:** https://github.com/megadose/holehe

**Alternatives:** theharvester, emailrep.io (web)


#### PhoneInfoga

Framework for phone OSINT: country, area, carrier, line type, and footprint lookups via configurable scanners; stable but no longer actively maintained, so expect scanners to drift over time.

**When:** Resolve a phone number you own or are authorized to analyze into provider/line-type facts before deeper carrier-level checks.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install phoneinfoga`

**URL:** https://github.com/sundowndev/phoneinfoga

**Alternatives:** holehe


#### emailrep.io

Hosted API/service that scores an email's reputation, flags breach exposure and disposable/spammy providers, and lists the online profiles tied to it; a service, not a tool — the free tier needs no key, higher limits need one.

**When:** Triage a suspicious inbound email or audit your own addresses for exposure as part of defensive OSINT.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web–API key)`

**URL:** https://emailrep.io

**Alternatives:** holehe, theharvester






## Social Media Scraping

Instaloader ⭐


#### Instaloader ⭐

Downloads Instagram profiles, posts, hashtags, highlight stories, and companion metadata (captions, likes, comments) via its own private API without an official key; actively maintained and scriptable.

**When:** Pull an archive of a public profile you own for media/evidence preservation, or collect hashtag and post metadata on your own accounts.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install instaloader`

**URL:** https://github.com/instaloader/instaloader

**Alternatives:** osintgram, snscrape


#### snscrape

Python CLI/library that scrapes public posts and profiles from several platforms with JSONL output; Twitter/X scrapers are dead behind the login wall and Reddit needs the closed Pushshift, but Telegram, Weibo, and some Mastodon instances still work.

**When:** Programmatic bulk retrieval and archiving of public posts from the platforms snscrape still supports, e.g. Telegram channels.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip3 install snscrape`

**URL:** https://github.com/JustAnotherArchivist/snscrape

**Alternatives:** instaloader, osintgram, twscrape (github), twint (archived 2023)


#### OSINTgram

Interactive shell that collects public Instagram data — profile info, captions, followers, tagged users, comments, and bio contact strings — using a scratch-account session or a free HikerAPI token; the project's own disclaimer limits use to educational/authorized targets.

**When:** Relationship analysis of a public profile you own (who comments, who is tagged, contact strings in bios).

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/Datalux/Osintgram && pip3 install -r requirements.txt`

**URL:** https://github.com/Datalux/Osintgram

**Alternatives:** instaloader, snscrape






## Internet Infrastructure Search

Shodan ⭐


#### Shodan ⭐

The reference internet device/port search engine indexing exposed services, banners, vulnerabilities, and history for any IP or domain; a commercial service with a lasting free tier and a separate no-key InternetDB lookup endpoint.

**When:** See every port and service your public IP ranges expose right now, exactly as an attacker would, before closing them.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install shodan`

**URL:** https://www.shodan.io

**Alternatives:** censys, zoomeye, netlas


#### Censys

Internet-wide scan platform covering hosts, services, certificates, and web properties with structured query language; the free tier includes search plus host/cert/web-property lookup APIs.

**When:** Certificate-centric inventory and pivots — find every host presenting a given cert — or structured queries beyond Shodan's free tier.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install censys`

**URL:** https://search.censys.io

**Alternatives:** shodan, netlas


#### ZoomEye

Cyber-space search engine by KnownSec scanning IPv4/IPv6, services, and web layers via Xmap/Wmap; strongest on IoT/OT devices and Asian-region asset coverage, with roughly 10k free API queries/month.

**When:** Coverage of less-Shodanized regions or internet-of-things/embedded device hunting on ranges you own.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install zoomeye`

**URL:** https://www.zoomeye.ai

**Alternatives:** shodan, censys, netlas


#### Netlas

Internet scanning platform over 8B+ indexed hosts with response-body, DNS, WHOIS, and certificate search plus a full REST API and Python SDK; the free tier is key-limited at about 50 requests/day.

**When:** Regular-expression/Lucene search across full HTTP response bodies when Shodan's banners are too shallow.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install netlas`

**URL:** https://netlas.io

**Alternatives:** shodan, censys, zoomeye






## Document Metadata & Forensics

exiftool ⭐


#### exiftool ⭐

Reads, writes, and edits EXIF/GPS/IPTC/XMP and hundreds of tag formats across images, PDFs, Office files, and more; the metadata workhorse behind most doc-forensics pipelines.

**When:** Forensic-grade tag extraction from any local file — geolocation, author, generator, timestamps — before release or after acquisition.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install libimage-exiftool-perl`

**URL:** https://exiftool.org

**Alternatives:** metagoofil, foca


#### Metagoofil

Dork-driven document harvesting: finds indexed files (.pdf, .docx, .xlsx) on a domain and downloads them for stripping; the maintained opsdisk fork ships on Kali and deliberately defers metadata analysis to exiftool.

**When:** Collect every publicly indexed document on a domain you own so you can scrub metadata and accidental information leaks.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/opsdisk/metagoofil && pip3 install -r requirements.txt`

**URL:** https://github.com/opsdisk/metagoofil

**Alternatives:** exiftool, foca


#### FOCA

Windows GUI (C# with a SQL Server back end) that searches a domain via Google/Bing/DuckDuckGo, fingerprints documents, and extracts metadata — users, folders, software — into a browsable project; a Windows GUI, not a POSIX tool, with slow updates.

**When:** When you have a Windows box and want a point-and-click metadata project view instead of CLI pipelines.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `installer from GitHub Releases (Windows GUI)`

**URL:** https://github.com/ElevenPaths/FOCA

**Alternatives:** metagoofil, exiftool






## OSINT Automation Platforms

SpiderFoot ⭐


#### SpiderFoot ⭐

Automated OSINT correlation engine with 200+ modules and a YAML correlation engine, surfaced through a web UI and CLI; built to map an attack surface and connect entities automatically.

**When:** A broad sweep of a domain/IP/email you own to correlate entities across many free data sources in a single scan.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/smicallef/spiderfoot && pip3 install -r requirements.txt`

**URL:** https://github.com/smicallef/spiderfoot

**Alternatives:** maltego, recon-ng


#### Maltego

Commercial graph-based link-analysis and OSINT platform (desktop and browser) with transforms into 1B+ identities, breach data, and infrastructure datasets; a free Community Edition (Basic plan) exists but is result-limited. A commercial service, not open source.

**When:** Investigative link analysis where a visual graph of who/what connects to whom beats JSON output.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/desktop — free CE with Maltego ID)`

**URL:** https://www.maltego.com

**Alternatives:** spiderfoot, recon-ng


#### recon-ng

Metasploit-style modular reconnaissance framework for web OSINT, with a marketplace of modules, workspace isolation, and database-backed reporting; stable but leisurely maintained.

**When:** Scripted, repeatable recon workflows with structured output and API keys for your own estate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install recon-ng`

**URL:** https://github.com/lanmaster53/recon-ng

**Alternatives:** spiderfoot, maltego






## Search Dorks Reference

Google Hacking Database (GHDB) ⭐


#### Google Hacking Database (GHDB) ⭐

Reference catalog of search-engine operators ('dorks') and example queries that surface exposed files, login panels, admin pages, and misconfigurations in public indexes. A reference page, not a tool.

**When:** Compose and reuse proven search-engine queries to audit what public indexes expose about your own domains.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.exploit-db.com/google-hacking-database

**Alternatives:** netlas dorks (github)





