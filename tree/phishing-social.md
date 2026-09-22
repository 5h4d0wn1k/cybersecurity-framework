# 🎣 Phishing & Social Engineering

Simulating the human factor: phishing campaigns, cloned logins, credential harvesting, and MFA-phishing proxies — all framed for authorized security-awareness testing.

## Phishing Simulation Platforms

GoPhish ⭐


#### GoPhish ⭐

Open-source, self-hosted campaign engine: compose email templates, landing pages, target groups, and SMTP profiles, then track opens, clicks, and submitted credentials per recipient via web UI and REST API.

**When:** The standard engine for authorized organizational awareness campaigns — schedule simulations against your own employees, export per-recipient results, and measure click-rate improvement over time.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install -v github.com/gophish/gophish@latest`

**URL:** https://github.com/gophish/gophish

**Alternatives:** king phisher, phishspark


#### King Phisher

Python client/server phishing toolkit (SecureState) with parallel campaigns, page cloning, credential-harvesting landing pages, geo-location of clickers, and SPF checks. Declared no longer maintained — treat as legacy.

**When:** Self-hosted client-plus-server workflows in legacy environments; otherwise prefer Gophish for new authorized programs.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `wget -q https://github.com/securestate/king-phisher/raw/master/tools/install.sh && sudo bash ./install.sh`

**URL:** https://github.com/securestate/king-phisher

**Alternatives:** gophish


#### PhishSpark

Commercial self-hostable phishing-simulation platform with SPF/DKIM/DMARC setup wizard, HMAC-signed tracking links, prebuilt templates (Microsoft 365, payroll portals), and per-department risk scoring. Sends only to your own users with written approval.

**When:** Teams that want a lighter-weight, guided simulation workflow with built-in authorization guardrails without standing up Gophish infrastructure.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Sign up at https://phishspark.com (free tier) or follow the Docker quick-start in /docs for self-host.`

**URL:** https://phishspark.com/

**Alternatives:** gophish, king phisher


#### Adversary-in-the-Middle Simulation



##### Evilginx2 ⭐

Go-based reverse-proxy that fronts a real site over a domain you control, captures post-login session cookies, and demonstrates why legacy 2FA alone does not protect a session. The reference tool for authorized MFA-phishing and passkey-migration exercises.

**When:** When authorized red-team scope includes proving session-token exposure or comparing legacy 2FA against phishing-resistant FIDO2/passkeys in your own environment.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/kgretzky/evilginx2 && cd evilginx2 && make`

**URL:** https://github.com/kgretzky/evilginx2

**Alternatives:** modlishka, evilgophish


##### Modlishka

Go reverse proxy that transparently proxies a whole multi-domain HTTPS site through one phishing domain and captures credentials and session tokens. Pioneered the modern AitM technique in research; author restricts use to authorized testing and defensive awareness.

**When:** Authorized engagements that need whole-domain transparent proxying without client-side certificates, or historical demos of the AitM technique.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `go install github.com/drk1wi/Modlishka@latest`

**URL:** https://github.com/drk1wi/Modlishka

**Alternatives:** evilginx2, evilgophish


##### EvilGophish

Combines the Gophish campaign engine with an evilginx2-class reverse proxy in one toolchain, letting an authorized red team schedule phishing emails and capture session tokens from a single console.

**When:** When you want token capture plus Gophish-style campaign scheduling and reporting in one self-hosted deployment.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/fin3ss3g0d/EvilGophish && cd EvilGophish && sudo bash setup.sh`

**URL:** https://github.com/fin3ss3g0d/EvilGophish

**Alternatives:** evilginx2, modlishka


#### Social Engineering Toolkits



##### Social-Engineer Toolkit (SET) ⭐

TrustedSec's menu-driven Python framework bundling page cloning, credential harvesters, email mass-mailers, and SMS vectors behind one guided interface. Preinstalled on Kali; built for running authorized awareness campaigns.

**When:** Guided multi-vector campaigns on a Kali box — a single menu covers credential-harvest, phishing, and SMS exercises entirely inside your own scoped environment.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install set`

**URL:** https://github.com/trustedsec/social-engineer-toolkit

**Alternatives:** gophish, beef


##### BeEF

Browser Exploitation Framework: serves a JavaScript hook that, once a consenting user's browser loads it, gives the operator a live inside view of that browser session with modules including fake login prompts and environment probing.

**When:** Training that shows employees the inside of a compromised browser session live, or to check whether your org notices browser-hook indicators.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install beef-xss`

**URL:** https://github.com/beefproject/beef

**Alternatives:** set


##### Wifiphisher

Rogue-access-point toolkit that drives nearby clients to a captive-portal page to collect Wi-Fi credentials — a physical testing and awareness tool for demonstrating lookalike Wi-Fi portals on scoped, consenting networks.

**When:** On-site authorized assessments where the goal is showing how easily a lookalike Wi-Fi portal harvests credentials; never on networks you do not own or lack written consent for.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install wifiphisher`

**URL:** https://github.com/wifiphisher/wifiphisher

**Alternatives:** set


##### Credential-Harvesting Labs (Authorized Only)



###### zphisher ⭐

Automated login-page cloning kit with 30+ ready templates, served over localhost/cloudflared/ngrok links with submissions logged locally. Widely used for building credential-phishing awareness demos — strictly in authorized labs or against your own organization.

**When:** Entry-level awareness demos or in-house training where a ready-made lookalike login page is enough and no full campaign engine is needed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone --depth=1 https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh`

**URL:** https://github.com/htr-tech/zphisher

**Alternatives:** credsniper


###### CredSniper

Flask/Jinja2 framework serving cloned multi-step login pages (username → password → 2FA token) with Let's Encrypt SSL and a results API. Unmaintained since 2020; use only in authorized test campaigns and labs.

**When:** Small scoped engagements that want a page-only collector with a results API; prefer the AitM proxes for session-level testing.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/ustayready/CredSniper && cd CredSniper && ./install.sh`

**URL:** https://github.com/ustayready/CredSniper

**Alternatives:** zphisher


#### Campaign Content & Email Generation



##### PhishMailer ⭐

Generates realistic HTML and plain-text email messages with attachments for in-house phishing simulations, including per-recipient personalization and SMTP sending. Fills the content-creation step of authorized awareness campaigns.

**When:** When you need convincing message and attachment content to feed into Gophish or your own SMTP as part of an approved simulation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/BiZken/PhishMailer && cd PhishMailer && pip install -r requirements.txt`

**URL:** https://github.com/BiZken/PhishMailer

**Alternatives:** gophish






## Email Spoofing & DMARC Testing

MXToolbox ⭐


#### MXToolbox ⭐

Suite of free web lookups covering SPF, DKIM, DMARC, BLACKLIST, and email header analysis plus spam-score checks — the de-facto starter kit for validating whether your own domain records are spoof-proof and readable by receivers.

**When:** First stop when you deploy or audit your org's email authentication; also useful pre-/post-campaign to confirm your simulation sender domain isn't bouncing.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Open https://mxtoolbox.com/ in a browser.`

**URL:** https://mxtoolbox.com/

**Alternatives:** dmarcian, easydmarc


#### Google Admin Toolbox Check MX

Google's lookup service that checks MX, SPF, and DMARC records for a domain and flags common misconfigurations from a Google-managed mail perspective.

**When:** Quick monthly self-checks of your domain's mail authentication plus loopbacks against Gmail's parser behavior.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Open https://toolbox.googleapps.com/apps/checkmx/ in a browser.`

**URL:** https://toolbox.googleapps.com/apps/checkmx/

**Alternatives:** mxtoolbox


#### Mail-Tester

Generates a test address and scores an actual emailed message against SPF, DKIM, DMARC, and content heuristics (0-10), including which records Gmail/Outlook see when your message arrives.

**When:** Verifying that a simulation or real marketing message passes authentication before you trust email-deliverability reports.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Send a test email to the address shown at https://www.mail-tester.com/.`

**URL:** https://www.mail-tester.com/

**Alternatives:** mxtoolbox


#### SPF/DKIM/DMARC Deployment Checkers



##### dmarcian ⭐

DMARC-focused platform with free record inspectors and DMARC aggregate-report parsing that shows which senders are failing authentication against your own domain. A core tool for the defense side of spoofing.

**When:** Parsing DMARC aggregate reports, planning policy progression (none → quarantine → reject), and proving to leadership that typosquatting mail is being rejected.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Open https://dmarcian.com/ (free DMARC record check).`

**URL:** https://dmarcian.com/

**Alternatives:** easydmarc


##### EasyDMARC

Free DNS records lookup for SPF, DKIM, DMARC, and BIMI with visual health reports; also offers continuous monitoring and report parsing on paid tiers.

**When:** Self-service DNS-stack validation and monthly health snapshots across many domains at once.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Open https://easydmarc.com/ (free lookup).`

**URL:** https://easydmarc.com/

**Alternatives:** dmarcian


##### DKIMValidator

Free web validator that checks a public DKIM record for a given domain and selector, verifying RFC 6376 correctness before rollout.

**When:** Confirming a specific DKIM selector publishes correct records during signing deployment.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Open https://www.dkimvalidator.com/ and enter the domain/selector.`

**URL:** https://www.dkimvalidator.com/

**Alternatives:** mxtoolbox


#### Header Analysis & Spoofed-Sender Behavior



##### Google Message Header Analyzer ⭐

Google's free raw-header decoder that maps each Received hop, SPF/DKIM/DMARC verdict, and authentication results into a consumable timeline — great for teaching how spoofed look-alikes get flagged (or slip through).

**When:** Post-campaign forensics and training walkthroughs where you show employees exactly which header tells a phish from a real sender.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Paste raw headers at https://toolbox.googleapps.com/apps/messageheader/.`

**URL:** https://toolbox.googleapps.com/apps/messageheader/

**Alternatives:** microsoft message header analyzer


##### Microsoft Message Header Analyzer

Free Microsoft header decoder that parses authentication results (SPF/DKIM/DMARC) and delivery path from raw outlook.com/Exchange messages, including spam-confidence and EOP verdict lines.

**When:** Investigating how a message behaved inside Microsoft 365, or inside table-top exercises where defenders trace a reported phish end to end.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Paste raw headers at https://mha.azurewebsites.net/.`

**URL:** https://mha.azurewebsites.net/

**Alternatives:** google message header analyzer






## Click Tracking & Phishing Forensics

Canarytokens ⭐


#### Canarytokens ⭐

Thinkst's free drop-in tokens — a unique URL, document, or credential cred that alerts your team the moment it is visited or submitted. Uses any arbitrary token in an email so a single interaction is logged and correlated.

**When:** Defensive phishing-awareness tracking: embed a custom URL token in an awareness email or lure-bearing document and get alerted when anyone (attacker or trainee) interacts with it.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Generate a token at https://canarytokens.org/generate (self-host via github.com/thinkst/canarytokens).`

**URL:** https://canarytokens.org/generate

**Alternatives:** gophish


#### PhishTool

Web-based phishing analysis workspace (with a Chrome extension) that decodes emails, auto-extracts headers, URLs, and indicators, and routes findings to case-management/email-security tools. Also offers click-through analytics for reporting.

**When:** Turning employee reports into vetted phishing cases, or running analytics on how reported phish relate to your authorized campaign metrics.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Sign up at https://www.phishtool.com/ (web app + Chrome extension).`

**URL:** https://www.phishtool.com/

**Alternatives:** gophish, microsoft message header analyzer


#### URL & Reputation Scanners



##### urlscan.io ⭐

Screenshots and inventories full page loads — every request, redirect, domain, script, and certificate — for a submitted URL. The reference tool for dissecting phishing landing pages and look-alike domains.

**When:** Analyzing a reported phish's full resource pattern, comparing a look-alike against the real login site, and sharing a sandboxed screenshot in incident write-ups.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Submit a URL at https://urlscan.io/.`

**URL:** https://urlscan.io/

**Alternatives:** virustotal, checkphish


##### VirusTotal

Aggregates dozens of antivirus and URL-blocker verdicts plus domain reputation for a submitted URL or file. Fast triage when deciding whether a link is attacker infrastructure.

**When:** Quick triage of a reported URL against multi-vendor verdicts before escalation to your SOC.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Submit a URL at https://www.virustotal.com/ (APIs via account).`

**URL:** https://www.virustotal.com/

**Alternatives:** urlscan, checkphish


##### CheckPhish

Bolster's AI URL scanner that renders pages in isolation and classifies phishing/brand-impersonation attempts with a screenshot and intelligence score, exposed as a web dashboard and REST API.

**When:** Automated triage of suspected brand-impersonation and look-alike domains inside awareness campaigns or hunt queues.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Submit a URL at https://checkphish.ai/ (API key required).`

**URL:** https://checkphish.ai/

**Alternatives:** urlscan, virustotal


#### Phishing Domain Detectors



##### PhishTank ⭐

Community-run phishing URL database (operated by Cisco Talos) you can query to see whether a domain/URL is already classified as phishing, and where defenders and vendors submit new sightings.

**When:** Defensive lookup of reported URLs against a maintained community blocklist, and submitting confirmed phish from your campaign analysis.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Query or submit at https://phishtank.org/.`

**URL:** https://phishtank.org/

**Alternatives:** openphish


##### OpenPhish

Automated phishing intelligence engine that curates active phishing URLs and feeds them through API and free/demo endpoints, with per-campaign and per-region details.

**When:** Feeding confirmed phishing URLs from your analysis into this feed to inform downstream detectors, and researching active campaigns your org may have been targeted by.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Browse or pull feeds at https://openphish.com/.`

**URL:** https://openphish.com/

**Alternatives:** phishtank


##### PhishDetect

Open-source service (client + self-hosted node) that clusters phishing pages by SHA-1 hash of page content and exposes an API for lookups, letting an org build its own look-alike detector.

**When:** Self-hosted phishing-pattern detection where you want clustering and a private lookup API for your own authorized-scope pages.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/phishdetect/phishdetect && cd phishdetect && docker-compose up -d`

**URL:** https://github.com/phishdetect/phishdetect

**Alternatives:** openphish, urlscan


##### Blocklists & Indicator Feeds



###### URLhaus ⭐

abuse.ch's malware-URL sharing platform that tracks URLs used for phishing, drive-by downloads, and C2, with free API and hourly CSV/JSON feeds for defensive enrichment.

**When:** Checking whether a reported URL is already tracked as malicious and pulling machine-readable feeds into your detection stack.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Query at https://urlhaus.abuse.ch/ (API: https://urlhaus-api.abuse.ch).`

**URL:** https://urlhaus.abuse.ch/

**Alternatives:** phishtank


###### PhishStats

Real-time database of active phishing domains with public dashboards, IP/URL/domain/RDNS queries, and an API — useful for validating whether host indicators are known-phishing infrastructure.

**When:** Enriching an I/O indicator from a reported phish against a live phishing-activity database.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `https://phishstats.info/ (web dashboards + API).`

**URL:** https://phishstats.info/

**Alternatives:** urlhaus


###### Google Safe Browsing Transparency

Google's Safe Browsing status checker that reveals whether a given web property is being flagged as deceptive or socially engineered, plus the local Lookup API for programmatic checks.

**When:** Checking whether a reported URL is actively defanged in Chrome/Firefox user bases, and automating dangerous-site checks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `https://transparencyreport.google.com/safe-browsing/search or the Safe Browsing Lookup API.`

**URL:** https://transparencyreport.google.com/safe-browsing/search

**Alternatives:** virustotal






## Awareness Training & User Reporting

KnowBe4 ⭐


#### KnowBe4 ⭐

Leading commercial security-awareness platform combining simulated phishing campaigns, template libraries, and training modules with per-user risk scoring, plus reporting that ties click rates to training completion.

**When:** Enterprise-scale awareness programs needing turnkey campaign templates, LMS-style training, and board-ready reports on phishing risk.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Sign up at https://www.knowbe4.com/ (SaaS).`

**URL:** https://www.knowbe4.com/

**Alternatives:** hoxhunt, cofense phishme


#### Hoxhunt

Commercial continuous-training platform built around real-world threat reporting: employees report suspicious mail, the service validates it and dispatches micro-learnings while feeding behavioral data to security teams.

**When:** Organizations that want reporting-led training that blends real user reports with simulations and automated follow-up.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Sign up at https://hoxhunt.com/ (SaaS).`

**URL:** https://hoxhunt.com/

**Alternatives:** knowbe4


#### Cofense PhishMe

Commercial phishing-defense platform that mixes simulated phishing, template management, and automation that ingests the precise phish employees report — with the Cofense Reporter add-in pushing sightings straight to the SOC.

**When:** Teams coupling simulation with a strong 'report the phish' culture and automated triage of what users actually receive.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Sign up via https://cofense.com/ (SaaS).`

**URL:** https://cofense.com/

**Alternatives:** knowbe4, hoxhunt


#### Employee Reporting Channels



##### Microsoft 365 Report Message Add-in ⭐

Free Microsoft add-in for Outlook/OWA that gives users a 'Report' button to flag phishing, junk, or not-junk straight to Microsoft and (with a user-reporting policy) to your security team's mailbox.

**When:** Giving every employee a zero-friction way to report suspected phish, then mining those submissions in table-top exercises and campaign post-mortems.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Deploy from M365 admin → Settings → Integrated apps; docs at https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/submissions-users-report-message-add-in-configure`

**URL:** https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/submissions-users-report-message-add-in-configure

**Alternatives:** cofense reporter


##### Cofense Reporter

Outlook/heb browser reporting add-in that forwards a reported email, with attachments and headers intact, to the organization's phishing mailbox and auto-prepends a standardized template for triage.

**When:** Structuring free-form employee reports so analysts receive complete headers/attachments from day one of an awareness program.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Deploy via https://cofense.com/ (Outlook add-in / browser toolbar).`

**URL:** https://cofense.com/

**Alternatives:** microsoft 365 report message add-in


#### Training Content & Tabletop Aids



##### SANS OUCH! Newsletter ⭐

Free monthly, non-technical security awareness newsletter from SANS covering phishing, social engineering, and reporting habits; can be licensed for redistribution to staff and reused as tabletop discussion material.

**When:** A pre-written, vetted security-awareness cadence for employees and a ready-made reading list before table-top exercises.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Subscribe at https://www.sans.org/ouch/.`

**URL:** https://www.sans.org/ouch/

**Alternatives:** jigsaw phishing quiz


##### Jigsaw Phishing Quiz

Free interactive quiz from Jigsaw by Google that walks participants through tricky real-world email screenshots and explains each phishing tell with instant feedback.

**When:** A low-stakes, engaging lter for kickoff of a training meeting or a fresh-start activity right after a failed simulation click.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Open https://phishingquiz.withgoogle.com/ (no install).`

**URL:** https://phishingquiz.withgoogle.com/

**Alternatives:** sans ouch





