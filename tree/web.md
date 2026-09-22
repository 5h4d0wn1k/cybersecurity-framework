# 🕸️ Web Application Security

Intercepting proxies, content discovery, injection testing, and API tooling for authorized web assessments.

## Intercepting Proxies

### Burp Suite ⭐

The de-facto intercepting proxy: intercept and edit requests, inspect responses, map the app, and extend workflows with a large marketplace.

**When:** When you need to manually inspect and shape every request against an app you're authorized to test, or want Professional-grade scanning and macro-based session handling.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install --cask burp-suite`

**URL:** https://portswigger.net/burp

**Alternatives:** OWASP ZAP, Caido


### OWASP ZAP

Free and open-source OWASP proxy with automated scanning, a baseline API for CI, fuzzing, and a REST API for integration.

**When:** When Burp is not an option due to licensing or budget, or you want scriptable scanning you can drive from a pipeline against a staging app you own.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo snap install zaproxy --classic`

**URL:** https://github.com/zaproxy/zaproxy

**Alternatives:** Burp Suite, Caido


### Caido

Lightweight, modern intercepting proxy with a clean UI and fast request replay, built as a slim alternative to the heavyweight suites.

**When:** When you want a quick, single-file proxy for interception and replay without a large install footprint.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `brew tap caido/caido && brew install caido`

**URL:** https://github.com/caido/caido

**Alternatives:** OWASP ZAP, Burp Suite


## Content Discovery & Fuzzing

### ffuf ⭐

High-speed Go web fuzzer handling directory, virtual-host, parameter, and header fuzzing over reusable wordlists and encoders.

**When:** Your default content-discovery engine on an authorized target: large wordlists, vhost fuzzing, and parameter guessing.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install github.com/ffuf/ffuf/v2@latest`

**URL:** https://github.com/ffuf/ffuf

**Alternatives:** gobuster, feroxbuster, wfuzz


### gobuster

Lightweight Go brute-forcer for directories/files, DNS subdomains, and virtual hosts using custom wordlists.

**When:** When you need a single-binary directory scan with zero dependencies, or a quick DNS or vhost brute force.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/OJ/gobuster/v3@latest`

**URL:** https://github.com/OJ/gobuster

**Alternatives:** ffuf, feroxbuster, dirsearch


### feroxbuster

Rust-based recursive content scanner that follows discovered paths automatically and color-codes results by status.

**When:** When recursive crawling of your own app's content tree matters more than raw wordlist throughput.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install feroxbuster --locked`

**URL:** https://github.com/epi052/feroxbuster

**Alternatives:** ffuf, gobuster


### dirsearch

Python directory brute-forcer with a built-in wordlist, recursive mode, and extension/status filters to cut noise.

**When:** When you want a battery-included scanner with sane defaults against a single host.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone --depth 1 https://github.com/maurosoria/dirsearch.git`

**URL:** https://github.com/maurosoria/dirsearch

**Alternatives:** gobuster, feroxbuster


### wfuzz

Flexible Python web fuzzer built on curl backends; supports multiple payload injection points and fine-grained response matching.

**When:** When you need to fuzz several positions (headers, cookies, parameters) in one request with precise match filters.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo pip3 install wfuzz`

**URL:** https://github.com/xmendez/wfuzz

**Alternatives:** ffuf, feroxbuster


## SQL Injection Testing

### sqlmap ⭐

Automated SQL injection engine supporting boolean, time-based, error, union, and stacked techniques plus database fingerprinting.

**When:** After a parameter in an app you're authorized to test looks injectable — it automates detection and database fingerprinting in one pass.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git`

**URL:** https://github.com/sqlmapproject/sqlmap

**Alternatives:** NoSQLMap, manual payload probes via Burp Repeater


### NoSQLMap

Automated NoSQL database testing (MongoDB, CouchDB) focused on enumeration, injection, and blind testing of document-store backends.

**When:** When the API you're testing is backed by a document store and classic SQL payloads don't apply.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone --depth 1 https://github.com/codingo/NoSQLMap.git && cd NoSQLMap && python3 setup.py install`

**URL:** https://github.com/codingo/NoSQLMap

**Alternatives:** sqlmap, manual query fuzzing via mitmproxy


## Cross-Site Scripting (XSS) Testing

### Dalfox ⭐

Go-based XSS scanner that runs a fast analysis pass, sends crafted payloads, and confirms findings with headless-browser verification.

**When:** When you want automated, verifiable XSS coverage across many endpoints in a target you're authorized to test.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/hahwul/dalfox/v2@latest`

**URL:** https://github.com/hahwul/dalfox

**Alternatives:** XSStrike, manual encoding checks via Burp Proxy


### XSStrike

Python XSS test suite with context-aware payload crafting, filter-detection heuristics, and a small built-in fuzzing engine.

**When:** When straight payloads fail and you need context-aware payload generation to understand why a filter rejected them.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone --depth 1 https://github.com/s0md3v/XSStrike.git`

**URL:** https://github.com/s0md3v/XSStrike

**Alternatives:** Dalfox, manual testing via OWASP ZAP


## API Testing

### mitmproxy ⭐

Interactive HTTPS proxy with a Python addon API for scripting request transformations, plus replay and mock flows for API traffic.

**When:** When you need scriptable request manipulation, or want to log, inspect, and replay API traffic headlessly.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** Burp Suite, Postman


### Postman

API client for organizing requests into collections, environment variables, and automated test runners; surfaces contract and auth issues early.

**When:** During development of your own service for functional API exploration, regression checks, and documenting expected behavior.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo snap install postman`

**URL:** https://www.postman.com

**Alternatives:** httpie, mitmproxy


### httpie

Human-friendly HTTP client with readable colored output, JSON-first rewriting, and simple chaining of requests in the shell.

**When:** When you want a quick one-liner API check without opening an app or writing verbose curl flags.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install httpie`

**URL:** https://httpie.io

**Alternatives:** curl, Postman


## Other Web Vulnerability Classes

### Commix ⭐

Automates detection of command injection flaws in arbitrary request fields using time- and output-based techniques plus filter-bypass payloads.

**When:** When a parameter in an authorized target appears to reach a shell (ping, logs, filename inputs) and you want automated confirmation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone --depth 1 https://github.com/commixproject/commix.git`

**URL:** https://github.com/commixproject/commix

**Alternatives:** manual output/time-based probes via Burp Repeater, ffuf for payload fuzzing at the field


### jwt_tool

JWT audit toolkit that checks common misconfigurations: algorithm confusion, weak signing keys, and expired/mis-set claims.

**When:** When the app under test uses JWTs and you want to audit key handling, which algorithms it accepts, and token lifetime settings.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone --depth 1 https://github.com/ticarpi/jwt_tool.git`

**URL:** https://github.com/ticarpi/jwt_tool

**Alternatives:** jwt.io decoder, manual token mutation in Burp


### smuggler

HTTP request-smuggling detector that fuzzes CL/TE header combinations against a host and reports which parsing behavior won.

**When:** When you control the web server stack and want to verify front/back-end header-parsing consistency on permitted infrastructure.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone --depth 1 https://github.com/defparam/smuggler.git`

**URL:** https://github.com/defparam/smuggler

**Alternatives:** manual CL/TE shaping in Burp Repeater, mitmproxy for crafted message injection

