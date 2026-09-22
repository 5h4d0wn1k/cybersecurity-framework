# 🎣 Phishing & Social Engineering

Simulating the human factor: phishing campaigns, cloned logins, credential harvesting, and MFA-phishing proxies — all framed for authorized security-awareness testing.

## Phishing Campaign Frameworks

Gophish ⭐


#### Gophish ⭐

Go-based open-source phishing campaign platform: composes email templates, landing pages, target groups, and SMTP profiles, then tracks opens, clicks, and submitted credentials per recipient via web UI + REST API.

**When:** The standard engine for organizational awareness campaigns — schedule simulations against your own employees, export per-recipient results, and measure click-rate improvement over time.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install -v github.com/gophish/gophish@latest`

**URL:** https://github.com/gophish/gophish

**Alternatives:** king phisher, socialfish


#### King Phisher

Python client/server toolkit (SecureState) with parallel campaigns, web-page cloning, credential-harvesting landing pages, geo-location, and SPF checks. The project is declared no longer maintained — treat as legacy.

**When:** Legacy environments or when you need a fully self-hosted client-plus-server workflow; otherwise prefer Gophish.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `wget -q https://github.com/securestate/king-phisher/raw/master/tools/install.sh && sudo bash ./install.sh`

**URL:** https://github.com/securestate/king-phisher

**Alternatives:** gophish


#### SocialFish

Active Python toolkit for cloning modern, JavaScript-heavy login pages and reporting clicks and submissions; ships page-candidate templates useful in training demos. It also bundles cookie/OTP hooks — use only in authorized simulations against consenting participants.

**When:** A quick page-only replica of a current login page for a live security-awareness demo without standing up a full campaign framework.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/UndeadSec/SocialFish && cd SocialFish && pip3 install -r requirements.txt`

**URL:** https://github.com/UndeadSec/SocialFish

**Alternatives:** gophish, zphisher






## Social Engineering Kits

Social-Engineer Toolkit (SET) ⭐


#### Social-Engineer Toolkit (SET) ⭐

TrustedSec's menu-driven Python framework bundling social-engineering vectors — page cloning, credential harvesting, email mass-mailers, SMS, and more — behind one guided interface. Preinstalled on Kali and used by teams to run authorized awareness campaigns.

**When:** Guided multi-vector campaigns on a Kali box, e.g. a quick credential-harvest or mailer exercise in-house where one menu covers everything.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install set`

**URL:** https://github.com/trustedsec/social-engineer-toolkit

**Alternatives:** gophish, beef


#### BeEF

Browser Exploitation Framework: serves a JavaScript hook that, once a consenting user's browser loads it, gives the operator a live inside view of that browser session with modules including fake login prompts and environment probing.

**When:** Training where you show employees the inside of a compromised browser session live, or test whether your org detects browser-hook indicators.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install beef-xss`

**URL:** https://github.com/beefproject/beef

**Alternatives:** set


#### Wifiphisher

Rogue-access-point framework that drives nearby clients to a captive-portal page to collect Wi-Fi credentials. An authorized physical-testing and awareness tool for demonstrating Wi-Fi credential exposure on scoped, consenting networks.

**When:** On-site assessments where the goal is showing guests/employees how easily a lookalike Wi-Fi portal harvests creds — never on networks you do not own or lack written consent for.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install wifiphisher`

**URL:** https://github.com/wifiphisher/wifiphisher

**Alternatives:** set






## Reverse-Proxy & AitM Phishing

Evilginx2 ⭐


#### Evilginx2 ⭐

Go-based man-in-the-middle reverse proxy (authorized red-team phishing infrastructure) that fronts a real site and captures post-login session cookies, demonstrating why legacy 2FA alone does not protect a session. Requires a domain you control, TLS, and dedicated infrastructure; the reference tool for authorized MFA-phishing exercises.

**When:** When your authorized red-team scope includes proving session-token exposure or comparing legacy 2FA against phishing-resistant FIDO2/passkeys in your own environment.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/kgretzky/evilginx2 && cd evilginx2 && make`

**URL:** https://github.com/kgretzky/evilginx2

**Alternatives:** modlishka, credsniper, evilgophish


#### Modlishka

Go reverse proxy that transparently proxies a whole multi-domain HTTPS site through a single phishing domain and captures credentials and session tokens (authorized red-team phishing infrastructure). Pioneered the modern Adversary-in-the-Middle technique in research; its author restricts use to authorized testing and defensive awareness.

**When:** Authorized engagements that need whole-domain transparent proxying without client certificate installs, or historical demos of the AitM technique.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `go install github.com/drk1wi/Modlishka@latest`

**URL:** https://github.com/drk1wi/Modlishka

**Alternatives:** evilginx2, credsniper


#### CredSniper

Flask/Jinja2 framework serving cloned multi-step login pages (username → password → 2FA token) with Let's Encrypt SSL and an API for collected submissions. Unmaintained since 2020; use only in authorized test campaigns.

**When:** Small scoped engagements that want a page-only credential collector with a results API; prefer Evilginx2/Modlishka for session-level testing.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/ustayready/CredSniper && cd CredSniper && ./install.sh`

**URL:** https://github.com/ustayready/CredSniper

**Alternatives:** evilginx2, modlishka


#### EvilGophish

Combines the Gophish campaign engine with an evilginx2-class reverse proxy in one toolchain so an authorized red team can schedule phishing emails and capture session tokens from a single console.

**When:** When you want Evilginx2-grade token capture plus Gophish-style campaign scheduling and reporting in one deployment.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/fin3ss3g0d/EvilGophish && cd EvilGophish && sudo bash setup.sh`

**URL:** https://github.com/fin3ss3g0d/EvilGophish

**Alternatives:** evilginx2, modlishka






## Credential Harvesting Pages

zphisher ⭐


#### zphisher ⭐

Automated login-page cloning kit with 30+ ready templates for email and social platforms, served over localhost, cloudflared, or ngrok links with submissions logged locally. The most widely used open tool for building credential-phishing awareness demos.

**When:** Entry-level awareness demos or in-house training where a ready-made lookalike login page is enough and no campaign engine is needed.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone --depth=1 https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh`

**URL:** https://github.com/htr-tech/zphisher

**Alternatives:** phishx, credsniper


#### PhishX

Front-end-driven spear-phishing field kit (maintained fork of the original noobhackers PhishX) with ready login-page templates, tunnel serving, and a web dashboard for collected submissions and visit metadata. Authorized awareness use only.

**When:** Fast, lightweight setup for cloning a social/email logon page and serving it from a tunnel during in-house training.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/rezaaksa/PhishX && cd PhishX && pip3 install -r requirements.txt`

**URL:** https://github.com/rezaaksa/PhishX

**Alternatives:** zphisher, credsniper


#### Credential Harvester (SET)

SET's website-cloner + credential-harvester module: pulls a live login page, serves a lookalike, and logs POSTed usernames/passwords with a redirect after capture. Ships inside SET; use only against your own organization's employees in scoped campaigns.

**When:** A single-page password-capture exercise without building a full framework — run it from the SET menu when authorized.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install set`

**URL:** https://github.com/trustedsec/social-engineer-toolkit

**Alternatives:** zphisher, phishx






## Email & Attachment Payloads

PhishMailer ⭐


#### PhishMailer ⭐

Generates realistic HTML and plain-text email messages with attachments for in-house phishing simulations, including per-recipient personalization and SMTP sending. Fills the content-creation step in authorized awareness campaigns.

**When:** When you need convincing message and attachment content to feed into Gophish or your own SMTP as part of an approved simulation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/BiZken/PhishMailer && cd PhishMailer && pip install -r requirements.txt`

**URL:** https://github.com/BiZken/PhishMailer

**Alternatives:** king phisher, gophish





