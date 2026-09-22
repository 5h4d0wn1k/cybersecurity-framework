# 🕸️ Web Application Security

The full web assessment stack: intercepting proxies, discovery, injection testing, API tooling, and OWASP-class vulnerability testing — nested by technique.

## Intercepting Proxies

Burp Suite ⭐


#### Burp Suite ⭐

The de-facto intercepting proxy for manual testing: intercept/edit requests, inspect responses, map the app, and extend via a large BApp marketplace.

**When:** Every manual web engagement; the default scratchpad for inspecting and shaping requests to an app you are authorized to test.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `brew install --cask burp-suite`

**URL:** https://portswigger.net/burp

**Alternatives:** OWASP ZAP, Caido


#### OWASP ZAP

Free and open-source OWASP proxy with automated scanning, fuzzing, and a REST API for CI-driven baseline scanning.

**When:** When you need a fully open, scriptable proxy with automated scanning you can drive from a pipeline against a staging app you own.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo snap install zaproxy --classic`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** Burp Suite, Caido


#### Caido

Lightweight, modern intercepting proxy with a clean UI and fast request replay, built as a slim alternative to the heavyweight suites.

**When:** When you want a quick, single-file proxy for interception and replay without a large install footprint.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew tap caido/caido && brew install caido`

**URL:** https://github.com/caido/caido

**Alternatives:** Burp Suite, OWASP ZAP






## Content Discovery & Fuzzing

ffuf ⭐


#### ffuf ⭐

Extremely fast web fuzzer written in Go for directories, files, parameters, vhosts, and more; supports filters, recursion, and matchers.

**When:** Anytime you need fast brute-force discovery of paths or parameters against a target you are authorized to test.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/ffuf/ffuf/v2@latest`

**URL:** https://github.com/ffuf/ffuf

**Alternatives:** gobuster, feroxbuster, dirsearch


#### gobuster

Simple multi-purpose fuzzer for directories, DNS subdomains, and virtual hosts using wordlists.

**When:** When you want a lightweight, easy-to-script brute forcer without a big learning curve.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/OJ/gobuster/v3@latest`

**URL:** https://github.com/OJ/gobuster

**Alternatives:** ffuf, feroxbuster


#### feroxbuster

Fast, recursive content discovery fuzzer built in Rust that automatically scans discovered directories.

**When:** When you want recursion and auto-re-scanning of found directories out of the box.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install feroxbuster`

**URL:** https://github.com/epi052/feroxbuster

**Alternatives:** ffuf, gobuster, dirsearch


#### dirsearch

Mature Python path scanner with threading, proxy support, and extensive filter/ignored-status options.

**When:** When a simple, cross-platform Python scanner with many wordlist and output options is all you need.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install dirsearch`

**URL:** https://github.com/maurosoria/dirsearch

**Alternatives:** ffuf, feroxbuster, gobuster


#### wfuzz

Flexible Python fuzzer for web content and parameter brute-forcing with rich payload/encoding options.

**When:** When you need fine-grained iteration over multiple payload positions and encoding filters.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install wfuzz`

**URL:** https://github.com/xmendez/wfuzz

**Alternatives:** ffuf, ffuf






## Injection & Data-Plane Testing




#### SQL Injection



##### sqlmap ⭐

The reference automated SQLi tool: detects and exploits injection in GET/POST/headers, enumerates DBMSes, and dumps data on targets you are authorized to test.

**When:** When a parameter looks injectable and you want thorough detection plus DB fingerprinting, safe limits, and batch modes.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install sqlmap`

**URL:** https://github.com/sqlmapproject/sqlmap

**Alternatives:** NoSQLMap


##### NoSQLMap

Automated pentesting tool for NoSQL databases (MongoDB, CouchDB) injection and misconfiguration.

**When:** When the backend is NoSQL and you need injection-point discovery against an app you own or have scope for.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/codingo/NoSQLMap && pip3 install -r NoSQLMap/requirements.txt`

**URL:** https://github.com/codingo/NoSQLMap

**Alternatives:** sqlmap


#### Command Injection



##### Commix ⭐

Automated OS command injection detection and exploitation with support for many injection techniques and filter bypasses.

**When:** When you suspect command injection in a parameter or header and want an automated detector on authorized targets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/commixproject/commix && cd commix && python3 commix.py -h`

**URL:** https://github.com/commixproject/commix

**Alternatives:** sqlmap (secondary)


#### Server-Side Template Injection (SSTI)



##### tplmap ⭐

Detects and exploits server-side template injection across engines (Jinja2, Twig, Freemarker, etc.).

**When:** When an app renders user input inside templates and you need to confirm SSTI on a scope-authorized target.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/epinna/tplmap && pip3 install -r tplmap/requirements.txt`

**URL:** https://github.com/epinna/tplmap






## Cross-Site Scripting (XSS) Testing

Dalfox ⭐


#### Dalfox ⭐

Fast, parameter-analysis XSS scanner written in Go with payload generation and Telegram/Discord notification support.

**When:** When you want to automate XSS discovery against a list of endpoints on authorized targets and pipeline results.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/hahwul/dalfox/v2@latest`

**URL:** https://github.com/hahwul/dalfox

**Alternatives:** XSStrike


#### XSStrike

XSS detection suite with payload crafting, bruteforce, and WAF/filter-detection heuristics.

**When:** When you need sophisticated payload crafting and WAF detection for manual XSS validation in your tests.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/s0md3v/XSStrike && pip3 install -r XSStrike/requirements.txt`

**URL:** https://github.com/s0md3v/XSStrike

**Alternatives:** Dalfox






## API Testing & Traffic Shaping

mitmproxy ⭐


#### mitmproxy ⭐

Interactive man-in-the-middle proxy with a powerful scriptable (Python) add-on API for request shaping and inspection.

**When:** When you need programmatic control over intercepted API traffic (rewrite, capture, fuzz) in your tests.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** Postman, httpie


#### Postman

API client and collection runner for crafting, saving, and automating HTTP requests against services under test.

**When:** When you need organized collections, environments, and simple automation to reason about an API's behavior.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask postman`

**URL:** https://www.postman.com

**Alternatives:** httpie, mitmproxy


#### HTTPie

User-friendly command-line HTTP client with readable, colorful output for quick manual requests.

**When:** For fast ad-hoc requests in a terminal during investigation without a heavyweight GUI.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew install httpie`

**URL:** https://httpie.io

**Alternatives:** Postman, mitmproxy






## Class & Variable-Specific Testing




#### JWT / Token Security



##### jwt_tool ⭐

Audits JSON Web Tokens: signature verification, algorithm confusion, and known CVE checks against tokens issued by apps you test.

**When:** When an application uses JWTs and you need to inspect claims, check alg:none/confusion, and validate signing secrets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ticarpi/jwt_tool && cd jwt_tool && python3 jwt_tool.py -h`

**URL:** https://github.com/ticarpi/jwt_tool


#### HTTP Request Smuggling



##### smuggler ⭐

Detects HTTP request smuggling variants (CL.TE, TE.CL, TE.TE obfuscation) against backend parsing mismatches.

**When:** When a stack splits differently between proxies/back-ends and you want to test smuggling scenarios on authorized targets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/defparam/smuggler && python3 smuggler.py regex.txt urls.txt`

**URL:** https://github.com/defparam/smuggler





