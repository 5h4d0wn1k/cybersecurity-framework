# 🕸️ Web Application Security

The full web assessment stack: intercepting proxies, deep content discovery, injection testing, XSS & clickjacking, API security, and OWASP-class bypass tooling — nested by technique.

## Intercepting Proxies




#### Full-Feature Suites



##### Burp Suite ⭐

The de-facto intercepting proxy for manual testing: intercept/edit requests, inspect responses, map the app, and extend via a huge BApp marketplace.

**When:** Every authorized manual web engagement; the default scratchpad for inspecting and shaping requests to an app in scope.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `brew install --cask burp-suite`

**URL:** https://portswigger.net/burp

**Alternatives:** OWASP ZAP, Caido


##### OWASP ZAP

Free and open-source OWASP proxy with automated scanning, fuzzing, DOM spelunking, and a REST API for CI-driven baseline scans.

**When:** When you need a fully open, scriptable proxy with built-in automation you can drive from a pipeline against a staging app you own.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo snap install zaproxy --classic`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** Burp Suite, Caido


##### Caido

Lightweight, modern intercepting proxy with a clean UI, fast request replay, and a built-in graph of your target's flow.

**When:** When you want a slim, single-binary proxy for interception and replay without a heavyweight install footprint.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew tap caido/caido && brew install caido`

**URL:** https://github.com/caido/caido

**Alternatives:** Burp Suite, OWASP ZAP


#### Standalone Desktop Proxies



##### Charles Proxy ⭐

Commercial desktop proxy with SSL browsing, bandwidth throttling, and rewrite tools for debugging web traffic.

**When:** When you want a polished GUI focus on mobile app and local HTTPS traffic you are authorized to inspect.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask charles`

**URL:** https://www.charlesproxy.com

**Alternatives:** Proxyman, OWASP ZAP


##### Proxyman

Native macOS proxy with elegant UI, SSL pinning bypass for testing, and script-driven scenarios.

**When:** When you work primarily on macOS and want a fast proxy with iOS/Android companion apps for your own traffic.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew install --cask proxyman`

**URL:** https://proxyman.io

**Alternatives:** Charles Proxy, mitmproxy






## Content Discovery & Fuzzing




#### Directory & File Discovery



##### Fast Fuzzers



###### ffuf ⭐

Extremely fast Go web fuzzer for directories, files, parameters, and vhosts with matchers, filters, and recursion.

**When:** Anytime you need fast brute-force discovery of paths or parameters against a target you are authorized to test.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/ffuf/ffuf/v2@latest`

**URL:** https://github.com/ffuf/ffuf

**Alternatives:** gobuster, feroxbuster


###### gobuster

Simple multi-purpose fuzzer for directories, DNS subdomains, and virtual hosts using wordlists.

**When:** When you want a lightweight, easy-to-script brute forcer for your scoped discovery phase.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/OJ/gobuster/v3@latest`

**URL:** https://github.com/OJ/gobuster

**Alternatives:** ffuf, feroxbuster


###### feroxbuster

Fast recursive content discovery fuzzer in Rust that automatically scans directories it finds.

**When:** When you want recursion plus auto-rescanning of discovered directories out of the box.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install feroxbuster`

**URL:** https://github.com/epi052/feroxbuster

**Alternatives:** ffuf, gobuster


##### Scriptable Python Scanners



###### dirsearch ⭐

Mature Python path scanner with threading, proxy support, and rich status-code filters.

**When:** When a straightforward, cross-platform Python scanner with many wordlist and output options is all you need.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install dirsearch`

**URL:** https://github.com/maurosoria/dirsearch

**Alternatives:** wfuzz, feroxbuster


###### wfuzz

Flexible Python fuzzer for web content and parameters with rich payload/encoding options and multi-position iteration.

**When:** When you need fine-grained iteration over multiple payload positions and encoding filters in your tests.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install wfuzz`

**URL:** https://github.com/xmendez/wfuzz

**Alternatives:** ffuf, dirsearch


#### Parameter Discovery



##### Hidden Parameter Miners



###### Arjun ⭐

Finds hidden HTTP parameters in URLs and header values using a large wordlist and heuristics.

**When:** When you want to discover undocumented parameters an API or page accepts on a target in scope.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install arjun`

**URL:** https://github.com/s0md3v/Arjun

**Alternatives:** x8, Param Miner


###### x8

Fast Go-based hidden parameter fuzzer with configurable detection heuristics and concurrency.

**When:** When you need a fast single-binary parameter miner that integrates into shell pipelines.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/Sh1Yo/x8@latest`

**URL:** https://github.com/Sh1Yo/x8

**Alternatives:** Arjun, Param Minner


###### Param Miner

Burp Suite extension that guesses hidden parameters, headers, and cookies on both base requests and reflected points.

**When:** When you are already in Burp and want passive parameter guessing while you manually explore in scope.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Install 'Param Miner' from the Burp BApp Store`

**URL:** https://github.com/portswigger/param-miner

**Alternatives:** Arjun, x8


##### Parameter Source Scrapers



###### ParamSpider ⭐

Scrapes parameters from Wayback, Common Crawl, and more to compile endpoint lists for later fuzzing.

**When:** When you want to bulk-collect parameter-bearing URLs from archives to feed subsequent testing.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pipx install paramspider`

**URL:** https://github.com/devanshbatham/ParamSpider

**Alternatives:** Arjun


#### Virtual Host Discovery



##### VHost Fuzzers



###### ffuf ⭐

Can brute-force virtual hosts by fuzzing the Host header and matching on distinct response sizes.

**When:** When you want to enumerate in-scope virtual hosts behind a shared IP or reverse proxy.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/ffuf/ffuf/v2@latest`

**URL:** https://github.com/ffuf/ffuf

**Alternatives:** gobuster


###### gobuster

Supports a dedicated vhost mode that fuzzes the Host header against a known target.

**When:** When you prefer a single simple binary for a quick virtual-host sweep on authorized targets.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `go install github.com/OJ/gobuster/v3@latest`

**URL:** https://github.com/OJ/gobuster

**Alternatives:** ffuf


#### Wordlists



##### General-Purpose Lists



###### SecLists ⭐

The community standard collection of wordlists for discovery, fuzzing, injection, usernames, passwords, and more.

**When:** When you need a broad, trustworthy baseline wordlist for any scoped fuzzing activity.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/danielmiessler/SecLists`

**URL:** https://github.com/danielmiessler/SecLists

**Alternatives:** Assetnote Wordlists, PayloadsAllTheThings


###### PayloadsAllTheThings

Categorized payloads and cheat sheets for every injection class, from RCE to SSTI to SSRF.

**When:** When you need a quick, in-context payload reference while crafting manual tests.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/swisskyrepo/PayloadsAllTheThings`

**URL:** https://github.com/swisskyrepo/PayloadsAllTheThings

**Alternatives:** SecLists


##### Curated & Scoped Lists



###### Assetnote Wordlists ⭐

Industry-derived wordlists built from massive real-world indexed datasets, including API parameter lists.

**When:** When baseline wordlists miss and you need high-quality lists for API and content discovery.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/assetnote/wordlists`

**URL:** https://wordlists.assetnote.io

**Alternatives:** SecLists, raft


###### raft (Rapid Fire Threads)

Classic raft wordlists (small/medium/large) for directories and files, maintained inside SecLists.

**When:** When you want quick, proven-size wordlists tuned to file and directory names without noise.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `curl -O https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/raft-large-files.txt`

**URL:** https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content

**Alternatives:** SecLists, Assetnote Wordlists






## Injection & Data-Plane Testing




#### Database Injection



##### SQL Injection



###### sqlmap ⭐

The reference automated SQLi tool: detects and exploits injection in GET/POST/headers, enumerates DBMSes, and dumps data on authorized targets.

**When:** When a parameter looks injectable and you want thorough detection, DB fingerprinting, safe limits, and batch modes.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install sqlmap`

**URL:** https://github.com/sqlmapproject/sqlmap

**Alternatives:** jSQL Injection


###### jSQL Injection

Java GUI tool for automated SQLi detection and exploitation with SQLi and NoSQL/path-style payloads.

**When:** When you want a desktop GUI over automated SQLi rather than a CLI-only flow on your scoped targets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ron190/jsql-injection`

**URL:** https://github.com/ron190/jsql-injection

**Alternatives:** sqlmap


##### NoSQL Injection



###### NoSQLMap ⭐

Automated testing tool for NoSQL databases (MongoDB, CouchDB) injection and misconfiguration.

**When:** When the backend is NoSQL and you need injection-point discovery against an app in scope.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/codingo/NoSQLMap && pip install -r NoSQLMap/requirements.txt`

**URL:** https://github.com/codingo/NoSQLMap

**Alternatives:** sqlmap


#### Code Injection



##### Command Injection



###### Commix ⭐

Automated OS command injection detection and exploitation with support for many injection techniques and filter bypasses.

**When:** When you suspect command injection in a parameter or header and want an automated detector on authorized targets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/commixproject/commix && python3 commix.py -h`

**URL:** https://github.com/commixproject/commix

**Alternatives:** sqlmap (secondary use of shell filters)


##### Server-Side Template Injection (SSTI)



###### tplmap ⭐

Detects and exploits server-side template injection across engines (Jinja2, Twig, Freemarker, etc.).

**When:** When an app renders user input inside templates and you need to confirm SSTI on a scope-authorized target.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/epinna/tplmap && pip install -r tplmap/requirements.txt`

**URL:** https://github.com/epinna/tplmap

**Alternatives:** SSTImap


###### SSTImap

Actively maintained fork/rewrite of tplmap for SSTI detection and exploitation across web template engines.

**When:** When tplmap is unmaintained and you want current engine payload support for your authorized tests.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/vladko312/SSTImap && python3 sstimap.py -h`

**URL:** https://github.com/vladko312/SSTImap

**Alternatives:** tplmap






## Cross-Site Scripting & Clickjacking




#### XSS Scanning



##### Automated Scanners



###### Dalfox ⭐

Fast XSS scanner with parameter analysis, payload generation, detection of reflection points, and CI-friendly output.

**When:** When you want to automate XSS discovery against endpoint lists on authorized targets and pipeline results.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/hahwul/dalfox/v2@latest`

**URL:** https://github.com/hahwul/dalfox

**Alternatives:** XSStrike, xsser


###### XSStrike

XSS detection suite with payload crafting, bruteforce, and WAF/filter-detection heuristics.

**When:** When you need sophisticated payload crafting and WAF detection for manual XSS validation in your tests.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/s0md3v/XSStrike && pip install -r XSStrike/requirements.txt`

**URL:** https://github.com/s0md3v/XSStrike

**Alternatives:** Dalfox


###### xsser

Long-standing XSS scanner with encoding/obfuscation bypasses, DORCE, and crawler support.

**When:** When you want a classic CLI scanner with many encoding bypass options against in-scope pages.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install xsser`

**URL:** https://github.com/epsylon/xsser

**Alternatives:** Dalfox, XSStrike


##### Out-of-Band Callback Platforms



###### XSS Hunter Express ⭐

Self-hostable platform that proves XSS via injected payload probes sending interactive callback notifications.

**When:** When you need persistent, hosted OOB XSS payloads that report callbacks during a longer engagement.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/mandatoryprogrammer/xsshunter-express && docker compose up --build`

**URL:** https://github.com/mandatoryprogrammer/xsshunter-express

**Alternatives:** interactsh, Burp Collaborator


#### Clickjacking / UI Redressing



##### quickjack ⭐

Point-and-click PoC generator for advanced clickjacking and frame slicing attacks with generated HTML snippets.

**When:** When you found a frameable page without X-Frame-Options/CSP frame-ancestors and need a PoC to demonstrate it.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Open the hosted generator at https://samy.pl/quickjack/quickjack.html`

**URL:** https://github.com/samyk/quickjack

**Alternatives:** ClickjackPoc


##### ClickjackPoc

Minimal browser-extension/POC helper for generating HTML clickjacking proofs quickly.

**When:** When you want a fast, scriptable way to produce clickjacking PoC HTML for reports.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/Raiders0786/ClickjackPoc`

**URL:** https://github.com/Raiders0786/ClickjackPoc

**Alternatives:** quickjack






## API Security & Traffic Shaping




#### API Traffic Tooling



##### API Clients



###### Postman ⭐

API client and collection runner for crafting, saving, and automating HTTP requests against services under test.

**When:** When you need organized collections, environments, and simple automation to reason about an API's behavior.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask postman`

**URL:** https://www.postman.com

**Alternatives:** Bruno, HTTPie


###### Bruno

Open-source, offline-first API client using plain-text collections you can version in git.

**When:** When you want API collections stored as data you can review and diff in code review.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask bruno`

**URL:** https://github.com/usebruno/bruno

**Alternatives:** Postman, HTTPie


###### HTTPie

User-friendly command-line HTTP client with readable, colorful output for quick manual requests.

**When:** For fast ad-hoc requests in a terminal during investigation without a heavyweight GUI.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew install httpie`

**URL:** https://httpie.io

**Alternatives:** Postman, Bruno


##### Scriptable Proxies



###### mitmproxy ⭐

Interactive man-in-the-middle proxy with a powerful scriptable (Python) add-on API for request shaping and inspection.

**When:** When you need programmatic control over intercepted API and app traffic (rewrite, capture, fuzz) in your tests.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** HTTP Toolkit


###### HTTP Toolkit

GUI proxy for intercepting, inspecting, and mocking HTTP(S) traffic from browsers, Android, and server processes.

**When:** When you want zero-config TLS interception and a friendly UI for debugging your own or in-scope traffic.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew install --cask http-toolkit`

**URL:** https://github.com/httptoolkit/httptoolkit

**Alternatives:** mitmproxy


#### API Endpoint Fuzzing



##### Schema-Based Fuzzers



###### schemathesis ⭐

Property-based testing for OpenAPI/GraphQL schemas that generates edge-case requests to uncover 5xx and contract violations.

**When:** When an API publishes an OpenAPI spec and you want automated schema-driven testing in CI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install schemathesis`

**URL:** https://github.com/schemathesis/schemathesis

**Alternatives:** kiterunner


##### Hidden Route Discovery



###### kiterunner ⭐

Assetnote's fast API endpoint and route discovery scanner optimized against massive route wordlists.

**When:** When you want to expose undocumented API routes and endpoints a spec won't tell you about.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/assetnote/kiterunner && make build`

**URL:** https://github.com/assetnote/kiterunner

**Alternatives:** ffuf, schemathesis


##### 403 / 40x Response Bypass



###### byp4xx ⭐

Rapid 403/40x bypasser that tries path normalization, header tricks, and encoding variations against protected endpoints.

**When:** When an API path returns 403 solely due to WAF/path rules and you want to test authorized bypass vectors.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/lobuhi/byp4xx && bash byp4xx.sh`

**URL:** https://github.com/lobuhi/byp4xx

**Alternatives:** nomore403


###### nomore403

Go tool that scans a list of 403 URLs and tries common bypass techniques to reveal hidden content.

**When:** When you have many blocked URLs from crawling and want an automated sweep across bypass techniques.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/devploit/nomore403 && sudo python3 nomore403.py -u https://target/`

**URL:** https://github.com/devploit/nomore403

**Alternatives:** byp4xx






## Bypass, Auth & Misconfiguration




#### Authentication & Sessions



##### JWT Testing



###### jwt_tool ⭐

Audits JSON Web Tokens: signature verification, algorithm confusion, known CVE checks, and secret brute-forcing.

**When:** When an app uses JWTs and you need to inspect claims, check alg:none/confusion, and validate signing secrets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ticarpi/jwt_tool && cd jwt_tool && pip install -r requirements.txt`

**URL:** https://github.com/ticarpi/jwt_tool

**Alternatives:** JWT Editor, JWT4B


###### JWT Editor

Official Burp extension to encode, decode, forge, and tamper with JWTs including alg confusion and kid injection.

**When:** When you are already inside Burp and want intercept-time JWT tampering on requests in scope.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Install 'JWT Editor' from the Burp BApp Store`

**URL:** https://github.com/PortSwigger/jwt-editor

**Alternatives:** jwt_tool, JWT4B


###### JWT4B

Burp Suite tab extension that decodes, validates, and brute-forces JWT signatures with attack templates.

**When:** When you prefer a dedicated Burp tab for JWT analysis and signature brute-forcing during a test.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/ozzi-/JWT4B`

**URL:** https://github.com/ozzi-/JWT4B

**Alternatives:** jwt_tool, JWT Editor


#### Server-Side Request Forgery (SSRF)



##### SSRF Exploitation



###### SSRFmap

Automates SSRF discovery and exploitation including file reads, port scans, and protocol-based attacks.

**When:** When a URL/parameter fetches remote content and you want to confirm and demo SSRF impact in scope.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/swisskyrepo/SSRFmap && pip install -r SSRFmap/requirements.txt`

**URL:** https://github.com/swisskyrepo/SSRFmap

**Alternatives:** Gopherus


###### Gopherus ⭐

Generates Gopher payloads to attack MySQL, Redis, SMTP, and more from SSRF-capable endpoints.

**When:** When you have an SSRF that reaches internal services and need gopher payload generation for exploitation.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/tarunkant/Gopherus && python3 Gopherus/gopherus.py --help`

**URL:** https://github.com/tarunkant/Gopherus

**Alternatives:** SSRFmap


##### OAST Callback Platforms



###### interactsh ⭐

Open-source Out-of-Band interaction server with client that catches DNS/HTTP/SMTP callbacks for SSRF and OAST.

**When:** When you want self-hosted or public OOB callbacks to confirm blind SSRF, XSS, or injection in authorized tests.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest`

**URL:** https://github.com/projectdiscovery/interactsh

**Alternatives:** XSS Hunter Express, Burp Collaborator


#### Desync & Request Smuggling



##### HTTP Request Smuggling



###### smuggler ⭐

Detects HTTP request smuggling variants (CL.TE, TE.CL, TE.TE obfuscation) against proxy/backend parsing mismatches.

**When:** When a stack splits differently between proxies and back-ends and you want to test smuggling scenarios in scope.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/defparam/smuggler && python3 smuggler.py regex.txt urls.txt`

**URL:** https://github.com/defparam/smuggler

**Alternatives:** HTTP Request Smuggler


###### HTTP Request Smuggler

Official PortSwigger extension automating CL.TE / TE.CL / TE.TE smuggling detection and exploit generation.

**When:** When you are inside Burp and want integrated smuggling detection with guided payload confirmation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Install 'HTTP Request Smuggler' from the Burp BApp Store`

**URL:** https://github.com/PortSwigger/http-request-smuggler

**Alternatives:** smuggler


#### Transport & mTLS Security



##### TLS / Certificate Auditing



###### testssl.sh ⭐

Free TLS/SSL audit CLI that checks ciphers, protocols, certificate chains, BEAST/POODLE/Heartbleed-family issues, and client-auth (mTLS) settings.

**When:** When you need a thorough, fork-friendly TLS configuration audit of an endpoint you are authorized to test.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone --depth 1 https://github.com/testssl/testssl.sh && ./testssl.sh example.com`

**URL:** https://github.com/testssl/testssl.sh

**Alternatives:** sslyze


###### sslyze

Fast Python TLS scanner analyzing SSL configs, supported ciphers, and certificate details, scriptable for CI.

**When:** When you need structured, machine-readable TLS scan output across many hosts in your own infrastructure.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install sslyze`

**URL:** https://github.com/nabla-c0d3/sslyze

**Alternatives:** testssl.sh


#### Security Headers & CSP



##### CSP Analysis



###### CSP Evaluator ⭐

Google's hosted query engine that flags weak Content-Security-Policy directives that allow XSS to slip through.

**When:** When the target sends a CSP and you want to quickly grade its effectiveness and find bypassable directives.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Open the hosted checker at https://csp-evaluator.withgoogle.com`

**URL:** https://github.com/google/csp-evaluator

**Alternatives:** SecurityHeaders.com


##### Response Header Auditing



###### SecurityHeaders.com ⭐

Scans a URL's response headers against the OWASP Secure Headers Project and scores the hardening state.

**When:** When you want an instant, shareable header hardening report for a site you own or administer.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -s 'https://securityheaders.com/?q=https://example.com&followRedirects=on'`

**URL:** https://securityheaders.com

**Alternatives:** headers.dev, httpx


###### headers.dev

Simple API/website that returns all response headers of a URL for quick inspection from the terminal.

**When:** When you want a fast, no-install way to pull and eyeball a target's response headers.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `curl -s https://headers.dev/example.com`

**URL:** https://headers.dev

**Alternatives:** SecurityHeaders.com, httpx


###### httpx

ProjectDiscovery's fast HTTP toolkit that fingerprints hosts, technologies, status codes, and response headers at scale.

**When:** When you need to bulk-collect status codes, headers, and tech fingerprints across hundreds of in-scope hosts.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest`

**URL:** https://github.com/projectdiscovery/httpx

**Alternatives:** headers.dev, SecurityHeaders.com





