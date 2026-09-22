# 🔑 Password Attacks & Cracking

Recover and test credentials you are authorized to attack: offline GPU/CPU hash cracking, hash identification, wordlists and rules, VPN PSK recovery, and lab-only NTLM relay, pass-the-hash and LSASS dumping chains.

## Offline Cracking Engines & Acceleration




#### CPU & GPU Engines



##### GPU-accelerated engines



###### Hashcat ⭐

World's fastest password recovery utility: GPU-optimized OpenCL/CUDA kernels for 590+ hash modes across dictionary (-a 0), mask (-a 3), hybrid (-a 6/7), PCFG and rule-based (-a 0 -r) attacks, with a slow-hash tuning engine for salted/costed formats.

**When:** The default for offline hashes you hold (dumps, configs, SAM/NTDS extract): benchmark, run wordlist + rules, then mask; benchmark against your own GPUs before buying cloud time.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install hashcat`

**URL:** https://github.com/hashcat/hashcat

**Alternatives:** John the Ripper, statsprocessor


###### hashcat-utils

MIT-licensed stdin/stdout pipeline utilities (cap2hccapx, combipow, len, cutb, rulegen…) that pre-process captures and wordlists into exactly the candidate and hash formats hashcat expects.

**When:** Convert WPA captures or normalize custom wordlists before a hashcat run; the companion tools to a serious cracking pipeline.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/hashcat/hashcat-utils && make`

**URL:** https://github.com/hashcat/hashcat-utils

**Alternatives:** maskprocessor, hashcat


##### CPU & classic engines



###### John the Ripper ⭐

The classic Unix password cracker with dictionary, incremental (Markov), and rule modes; runs on CPU out of the box, and on OpenCL/hosted hardware in jumbo builds.

**When:** First port of call for /etc/shadow-style hashes and any environment without working GPU drivers; pairs with your own .conf rules.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install john`

**URL:** https://www.openwall.com/john/

**Alternatives:** John the Ripper jumbo, hashcat


###### John the Ripper jumbo

Community 'bleeding-jumbo' branch adding hundreds of extra hash/cipher formats (NTLM, macOS, PDF, RAR, KeePass, FortiGate, IKE-PSK) plus the *2john converters used to package encrypted files before cracking.

**When:** Whenever your hash or file format is not covered by stock John or hashcat — the widest offline-format coverage available.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/openwall/john && ./configure && make -j`

**URL:** https://github.com/openwall/john

**Alternatives:** John the Ripper, hashcat


#### Cloud & Distributed Cracking



##### Orchestration & queue servers



###### Hashtopolis ⭐

Self-hosted client/server platform that distributes hashcat workloads across many GPUs on your own fleet, with task queues, chunking, and a web UI for assigning hash lists and attack modes.

**When:** Fill a lab or rented cloud-GPU rack with crack work: a Hashtopolis server dishes out chunks to each agent and consolidates results for your authorized recovery jobs.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/hashtopolis/server`

**URL:** https://github.com/hashtopolis/server

**Alternatives:** GoCrack, hashcat


###### GoCrack

FireEye's manager/worker framework written in Go for managing password-cracking tasks across a cluster of GPU hashcat workers, with a web panel for task packaging and result retrieval.

**When:** An alternative to Hashtopolis when you want a Go-native manager for a reclaimed GPU cluster; archived but still runnable for lab workflows.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/fireeye/gocrack`

**URL:** https://github.com/fireeye/gocrack

**Alternatives:** Hashtopolis


#### Wi-Fi / WPA-PSK Cracking (cross-ref)



##### Capture → crackable hash



###### hcxtools ⭐

Converts Wi-Fi captures (pcapng) and probe/eapol frames into the PMKID and PBKDF2 hashes that hashcat and John crack directly — the modern replacement for binary service packs.

**When:** Process a 4-way-handshake or PMKID capture from your own access point on the way to an offline WPA2/WPA3 Purge PSK attack.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ZerBea/hcxtools && make && sudo make install`

**URL:** https://github.com/ZerBea/hcxtools

**Alternatives:** hashcat-utils, aircrack-ng


##### WPA/WPA2 attack engines



###### aircrack-ng ⭐

The de-facto Wi-Fi suite: airodump-ng for capture, aireplay-ng for handshake injection, and aircrack-ng for dictionary/PTW attacks against WEP and WPA/WPA2 across your own networks.

**When:** Authorized wireless testing of infrastructure you operate: capture the handshake, verify the client, then hand the hash to hashcat for the heavy lifting.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** hcxtools, hashcat






## Hash Identification & Formatting




#### Quick hash-type identification



##### hashid ⭐

Python regex identifier for 220+ hash types that prints the matching hashcat mode (-m) and John format, so the correct cracking command is chosen before the first run.

**When:** The moment you collect a hash (dump, config, CTF): identify it before picking -m/--format to avoid wrong-mode and line-length failures.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install hashid`

**URL:** https://github.com/psypanda/hashID

**Alternatives:** hash-identifier, hashcat example-hashes


##### Name-That-Hash

Friendly command-line and web-identifying hash analyst that recognizes her way through common formats and prints the matching hashcat and John modes with sample hashes.

**When:** A zero-friction second opinion on ambiguous hashes (e.g. distinguishing NTLM from MD4/NDSS) before you commit to a cracker.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install name-that-hash`

**URL:** https://github.com/HashPals/Name-That-Hash

**Alternatives:** hashid, hashes.com


#### Curated sample-hash lists



##### hashes.com sample hashes ⭐

Online database documenting sample hashes and lookup methods for a wide range of algorithms (MD5, NTLM, bcrypt, Argon2, Joomla, …) useful for confirming a suspect format.

**When:** Cross-check an unusual hash against documented samples, or eyeball expected lengths/salt formats before choosing an engine.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `web: https://hashes.com/en/decrypt/hash`

**URL:** https://hashes.com/en/decrypt/hash

**Alternatives:** hashid, hashcat example-hashes


#### Engine example-hash references



##### Hashcat example hashes ⭐

Official table with one valid sample hash per hashcat mode (password is always 'hashcat'), including VPN PSK (5300/5400/2500) and firewall (7000) formats; also embedded via hashcat --example-hashes.

**When:** Confirm your hash formatting and attack command offline before a live run, or label unknown samples in your own CTFs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) or hashcat --example-hashes`

**URL:** https://hashcat.net/wiki/doku.php?id=example_hashes

**Alternatives:** hashes.com, hashid






## Wordlists, Rules & Candidate Generation




#### Bundled & leaked-list dictionaries



##### SecLists ⭐

The security tester's companion collection: passwords (10k/1M/rockyou-derived), usernames, default router credentials, and discovery/fuzzing payloads in one tree.

**When:** First stop in any authorized recovery or login test — reach for its dictionaries before generating anything custom.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone --depth 1 https://github.com/danielmiessler/SecLists.git`

**URL:** https://github.com/danielmiessler/SecLists

**Alternatives:** rockyou.txt, CeWL


##### rockyou.txt

The 2009 RockYou leak (~14M real-world passwords) that remains the standard baseline dictionary for fast-hash testing; shipped with Kali and mirrored in SecLists.

**When:** Quick first-pass dictionary sweep against fast hashes you own before rule/mask work, exactly as Kali documents it.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install wordlists`

**URL:** https://github.com/danielmiessler/SecLists/tree/master/Passwords/Leaked-Databases

**Alternatives:** SecLists, CrackStation


#### Rule engines & curated rules



##### Hashcat rule-based attacks



###### OneRuleToRuleThemAll ⭐

Community-curated single hashcat .rule file merging the best of popular rule sets (NSAKEY, d3ad0ne, etc.) so one base wordlist yields high-coverage candidate mutations.

**When:** A proven default ruleset for the dictionary+rule phase (-a 0 -r) when you don't want to hand-tune your own .rule file.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NotSoSecure/password_cracking_rules`

**URL:** https://github.com/NotSoSecure/password_cracking_rules

**Alternatives:** hashcat best64.rule, hashcat


###### hashcat best64.rule

The stock best64.rule ships in the hashcat repo and applies 64 high-yield mangles (append digit, toggle case, leetspeak, suffix) — the quickest low-cost rule win.

**When:** A fast, predictable ruleset that is safe to run on the default pool before heavier custom rules.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled in hashcat hashcat/rules/best64.rule`

**URL:** https://github.com/hashcat/hashcat/tree/master/rules

**Alternatives:** OneRuleToRuleThemAll


##### John the Ripper rules



###### Openwall John rules ⭐

John's rule engine and wiki-documented preset rules (dumb, wordlist, KoreLogic, single) mutate base words with case, suffix, prefix and substitution pipelines.

**When:** Applying John-side rule sets in jumbo-supported formats, especially when you are already cracking with john rather than hashcat.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled with john (->john.conf) — see wiki`

**URL:** https://github.com/openwall/john/wiki/Rules

**Alternatives:** hashcat best64.rule, John the Ripper


#### Frequency & password-statistics analysis



##### Pipal ⭐

Wordlist statistics analyzer that reports password length, character set, repeated digits, baseword frequency and pattern bias so you can shape the right attack.

**When:** Analyze your own leaked/test wordlist before building rules: learn the shape (e.g. 'capitalized word + 2 digits') and pick efficient masks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/digininja/pipal`

**URL:** https://github.com/digininja/pipal

**Alternatives:** statsprocessor, hashcat


##### statsprocessor

Hashcat's position-based password generator that derives per-position character frequencies from a wordlist and emits statistically weighted masks for -a 3 attacks.

**When:** Turning observations from your wordlist scans into a frequency-driven mask attack that outperforms naive charsets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/hashcat/statsprocessor && make`

**URL:** https://github.com/hashcat/statsprocessor

**Alternatives:** pipal, hashcat


#### Candidate & mangle generators



##### Mentalist ⭐

Graphical wordlist builder centered on human password paradigms: case mangling, keyboard walks, year/digit insertion, exporting full lists or ready-made hashcat/John rules.

**When:** Visually profile a candidate password space (vocab + year + symbol) when you prefer a GUI over hand-editing rule files.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/sc0tfree/mentalist && pip install .`

**URL:** https://github.com/sc0tfree/mentalist

**Alternatives:** kwprocessor, crunch, CeWL


##### kwprocessor

Hashcat-team keyboard-walk generator producing passwords that follow adjacent-key routes and basechars/config surprises for PINs and passphrases typed on keyboards.

**When:** Target PINs and passphrases your own devices generate along keyboard patterns, where walk-derived guesses beat pure randomization.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/hashcat/kwprocessor && make`

**URL:** https://github.com/hashcat/kwprocessor

**Alternatives:** crunch, Mentalist


##### crunch

Character-set wordlist generator enumerating all combinations/permutations with @,%^ pattern placeholders plus output splitting, resume and gzip/7z output.

**When:** Generate bounded, pattern-shaped candidate lists (known prefixes/suffixes, specific charsets) to feed hashcat or John.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install crunch`

**URL:** https://www.kali.org/tools/crunch/

**Alternatives:** kwprocessor, Mentalist


##### CeWL

Ruby spider that crawls a site to a depth and emits the unique words (plus author/email metadata) it finds — a vocabulary completely specific to that target.

**When:** Build organization-specific dictionaries (your own web app, a CTF) where site vocabulary beats generic lists.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/digininja/CeWL && bundle install`

**URL:** https://github.com/digininja/CeWL

**Alternatives:** pipal, SecLists


#### Online hash & password services



##### CrackStation ⭐

Free online hash cracker (MD5, SHA1, NTLM, and 220+ other algorithms) that matches your hashcat modes against massive precomputed tables.

**When:** A quick single-hash sanity lookup during analysis; treat as a confirmation aid, never as your primary recovery path for sensitive data.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `web: https://crackstation.net/`

**URL:** https://crackstation.net/

**Alternatives:** hashes.com






## Password Spraying & Low-Rate Login Testing




#### Kerberos & domain endpoints



##### Kerbrute ⭐

Go-based userenum/passwordspray tool that walks Kerberos pre-authentication: it discovers valid users from KDC error codes and tests one password against many accounts without lockouts.

**When:** Authorized domain testing where you need lockout-safe spraying via AS-REP pre-auth and user enumeration against your own KDC.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download release binary from the repo, or go install github.com/ropnop/kerbrute@latest`

**URL:** https://github.com/ropnop/kerbrute

**Alternatives:** NetExec, Spray


##### NetExec

The fork-lifted successor to CrackMapExec; its kerberos module performs password spraying and user enumeration across your SMB/Kerberos estate with clean protocol handling.

**When:** Office-wide spray validation when you already carry a NetExec install and want one client for SMB, LDAP, Kerberos and SSH checks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install netexec`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** Kerbrute, CrackMapExec


#### On-premises targeted sprayers



##### Unix / cross-platform sprayers



###### Spray ⭐

Small Python sprayer that takes a forged inventory of usernames and a handful of passwords, sleeps between attempts, and reports hits plus failed-auth stats.

**When:** Lockout-conscious spraying against your own AD from a Linux attack box with randomized delays.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Greenwolf/Spray`

**URL:** https://github.com/Greenwolf/Spray

**Alternatives:** DomainPasswordSpray, TREVORspray


###### TREVORspray

Python sprayer against Microsoft 365/Azure AD and AD with strong anti-lockout controls (seasonable delays, account randomization, MFA-threshold guardrails).

**When:** Azure AD/Office 365 authorized spray testing where you must respect MFA lockout and per-account backoff.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install trevorspray`

**URL:** https://github.com/blacklanternsecurity/TREVORspray

**Alternatives:** MSOLSpray, Spray


##### PowerShell domain sprayers



###### DomainPasswordSpray ⭐

The canonical community PowerShell sprayer: enumerates domain users from AD, tests one password across them, detects lockdown policies and can pass an existing password.

**When:** Classic AD password-spray validation in your own estate with built-in user enumeration and graceful exit on failure.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dafthack/DomainPasswordSpray`

**URL:** https://github.com/dafthack/DomainPasswordSpray

**Alternatives:** Spray, TREVORspray


#### Cloud identity providers



##### MSOLSpray

Python sprayer for Azure Active Directory / Microsoft 365: validates tenant, tests credentials via MSOL endpoints and reports valid user texture plus lockout status.

**When:** Authorize-and-run check of Azure AD accounts in your own tenant without tripping global lockout thresholds.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dafthack/MSOLSpray && python3 msolspray.py -u <user> -p <password> [-t <tenant>]`

**URL:** https://github.com/dafthack/MSOLSpray

**Alternatives:** TREVORspray, o365spray


##### o365spray ⭐

Username enumeration and password spraying against Microsoft 365 / Azure AD with built-in rate limiting, module-based spraying and user check against MSOL open endpoints.

**When:** Coverage of M365 as the primary cloud sprayer when you need mature lockout-safe logic built in.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install o365spray`

**URL:** https://github.com/0xZDH/o365spray

**Alternatives:** MSOLSpray, TREVORspray






## NTLM Relay, Pass-the-Hash & Harvesting (Lab)




#### NTLM capture, spoof & relay



##### Responder + mitm6 poisoning



###### Responder ⭐

LLMNR/NBT-NS/mDNS poisoner in a lab: it answers name-resolution queries and captures NTLMv1/v2 challenge-response hashes from clients that voluntarily submit them.

**When:** Lab/pentest only: run it to demonstrate why your own network filters these protocols, and feed captured that to a relay or cracker.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/lgandx/Responder && cd Responder && sudo proxychains4 -i tcp -v python3 responder.py -I eth0`

**URL:** https://github.com/lgandx/Responder

**Alternatives:** mitm6, impacket ntlmrelayx


###### mitm6

IPv6 abuser for labs: advertises a rogue DHCPv6 server so Windows clients register DNS and hand over WPAD traffic that can feed NTLM credential relaying.

**When:** Building a relaying pipeline against your own IPv6-enabled lab where clients trust rogue DHCPv6 — pair with ntlmrelayx, lab only.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install mitm6`

**URL:** https://github.com/dirkjanm/mitm6

**Alternatives:** Responder


##### SMB/LDAP relay servers



###### impacket ntlmrelayx ⭐

The relay half of the chain: accepts captured NTLM authentications and replays them to SMB/LDAP on targets you control, enabling hash history recording or relayed logins without knowing the plaintext password.

**When:** The canonical lab relay server after a poisoning daemon harvests NTLM; keep every target in your own lab scope.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install impacket; python3 ntlmrelayx.py -t smb://<lab-target>`

**URL:** https://github.com/fortra/impacket

**Alternatives:** Responder, mitm6


#### Pass-the-hash & remote shell



##### impacket psexec / wmiexec ⭐

Impacket's psexec and wmiexec use an NTLM hash directly to open an administrative service/exec on a Windows host — no password needed, lab authors' flagship use case for hash validation.

**When:** After you hold a hash for a machine in-scope: psexec for a service-metered shell, wmiexec for a cleaner WMI-backed execution.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install impacket; python3 psexec.py 'DOMAIN/user@host' -hashes :NTHASH`

**URL:** https://github.com/fortra/impacket

**Alternatives:** evil-winrm, NetExec


##### NetExec (pass-the-hash)

Netexec smb/winrm handles pass-the-hash logins (-H) at scale, checks admin rights and executes commands — replacing CrackMapExec workflows with an active fork.

**When:** Sweep several lab hosts with one hash to map who accepts admin hash logins; identical protocol coverage keeps it a natural psexec alternative.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install netexec; nxc smb 127.0.0.1 -u admin -H :NTHASH`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** impacket psexec / wmiexec, evil-winrm


##### evil-winrm

WinRM shell client that authenticates with a password or NTLM hash and gives an interactive PowerShell session for post-hash validation.

**When:** Clean, HTTP-bound lab session when WinRM is open and you prefer a stable PowerShell interactive to service-write tricks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `gem install evil-winrm`

**URL:** https://github.com/Hackplayers/evil-winrm

**Alternatives:** impacket psexec / wmiexec, NetExec


#### LSASS secret extraction (lab)



##### Mimikatz ⭐

The lab-standard post-exploitation credential extractor: reads LSASS memory to dump plaintext passwords, NTLM hashes, Kerberos tickets and DPAPI keys on systems you administer.

**When:** Authorized lab/engagement 'logonpasswords' runs on endpoints you own to prove how cached secrets age; always on-lab, never stealth marginal.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download release from the repo and run sekurlsa::logonpasswords on your own host`

**URL:** https://github.com/gentilkiwi/mimikatz

**Alternatives:** lsassy, DonPAPI


##### lsassy

Python library that grabs and parses LSASS memory via WMI/remote scripts without landing a binary on the target, returning parsed credentials for lab review.

**When:** Remote-to-itself lab extraction on Windows endpoints you operate, minimizing artefact noise compared to writing a standalone dump.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install lsassy`

**URL:** https://github.com/Hackndo/lsassy

**Alternatives:** mimikatz, DonPAPI


##### DonPAPI

DPAPI-centric credential dumper that walks LSASS and protected-store databases plus DPAPI master keys on remote machines, carving secrets and their derivation chains.

**When:** Lab DPAPI-focused extraction where you want the credential chain laid out and don't need a full interactive shell.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/login-securite/DonPAPI && pip install -r requirements.txt`

**URL:** https://github.com/login-securite/DonPAPI

**Alternatives:** mimikatz, lsassy






## Credential Extraction & Decryption (Authorized)




#### Browser & web-credential vaults



##### Firefox / Thunderbird login stores



###### firepwd ⭐

Pure-Python decryptor for Mozilla Firefox/Thunderbird logins.json driven by the derived master-password key; recovers saved site credentials from a copy you own.

**When:** Inspect the saved logins of your own Firefox profile (e.g. a forgotten master password) on a copy, never someone else's browser data.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/lclevy/firepwd && python3 firepwd.py -d ~/.mozilla/firefox/PROFILE`

**URL:** https://github.com/lclevy/firepwd

**Alternatives:** LaZagne, SharpDPAPI


##### Windows browser DPAPI stores



###### SharpDPAPI ⭐

C# DPAPI toolkit from the GhostPack family that decrypts Chrome/Edge vaults, DPAPI master keys and credential files on Windows — the standard for authorized browser-store recovery.

**When:** Recover Chrome/Edge saved credentials on machines you administer, using your own user context/master key.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the compiled release or build from source, run from your own session`

**URL:** https://github.com/GhostPack/SharpDPAPI

**Alternatives:** LaZagne, firepwd


###### LaZagne

Python credential-store dumper that walks browsers, WiFi profiles, mail clients, SSH keys and many desktop apps, recovering stored logins and passwords from your own machine.

**When:** One-shot sweep of every local credential store on a system you own for DR/hygiene or lab inventory.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/AlessandroZ/LaZagne && cd LaZagne && python3 laZagne.py all`

**URL:** https://github.com/AlessandroZ/LaZagne

**Alternatives:** SharpDPAPI, firepwd


#### VPN pre-shared keys & encrypted configs



##### IKE/Cisco IPSEC PSK recovery



###### hashcat VPN PSK modes (IKE-PSK 5300/5400, Cisco-IPSEC 2500) ⭐

Dedicated hashcat modes crack IKE pre-shared keys (5300/5400) and Cisco IPSEC VPN hashes (2500/500) captured from phase-1 handshakes, alongside FortiGate (7000) formats for firewall admin hashes.

**When:** Recover a PSK for a VPN you administer when the key was mis-remembered; pair with ike-scan for the phase-1 capture first.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `hashcat -m 5300 ike.hash wordlist.txt -r rules/best64.rule`

**URL:** https://hashcat.net/wiki/doku.php?id=example_hashes

**Alternatives:** ike-scan, hashcat


###### ike-scan

IKE discovery and testing tool that sends phase-1 negotiation to a VPN gateway and captures the responder's hash — the handshake you feed straight into hashcat's IKE-PSK modes.

**When:** Grab a legitimate IKE PSK exchange from a VPN endpoint you own, then crack it offline with hashcat for key-hygiene validation.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install ike-scan`

**URL:** https://github.com/royhills/ike-scan

**Alternatives:** hashcat VPN PSK modes






## Encrypted File & Document Recovery




#### Archive & container formats



##### John *2john archive converters ⭐

zip2john, rar2john and 7z2john turn encrypted ZIP/RAR/7z archives into $zip$/$rar$/$7z$ hashes that john jumbo or hashcat crack by password.

**When:** Recover a forgotten password on your own archive: convert once, then crack with john -jumbo or hashcat after wordlist+rule passes.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install john`

**URL:** https://github.com/openwall/john

**Alternatives:** fcrackzip, hashcat


##### fcrackzip

Fast zip password cracker with dictionary and brute-force modes (libzip-based fork runs far faster than the unzip-spawning original).

**When:** A quick direct brute/dictionary check of a small single ZIP without standing up a John pipeline; superseded by *2john for real workloads.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install fcrackzip`

**URL:** https://github.com/hyc/fcrackzip

**Alternatives:** John *2john archive converters


#### Documents & credential vaults



##### pdf2john ⭐

John/jumbo converter that extracts the hash from password-protected PDFs (RC4 and AES variants) and feeds it to john or hashcat for offline recovery.

**When:** Open a PDF you own whose password was lost: convert to the $pdf$ format and crack on your own CPU/GPU.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install john`

**URL:** https://github.com/openwall/john

**Alternatives:** pdfcrack, John the Ripper jumbo


##### keepass2john

John jumbo converter that packages a sealed .kdbx KeePass vault into a $keepass$ hash crackable by John or hashcat, covering the current PBKDF2 runtime cost.

**When:** Unlock your own KeePass vault after the master password drifted; always work on the copy you own, never a database you don't control.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install john`

**URL:** https://github.com/openwall/john

**Alternatives:** John the Ripper jumbo, hashcat


##### pdfcrack

Dedicated GPL tool recovering owner/user passwords from PDFs using the classic security handler (rev 2-4) via wordlist or brute force with state save/restore.

**When:** Recover legacy (pre-AES-256 rev 5) PDFs you own; on modern AES R4/R6 documents prefer pdf2john's formats instead.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install pdfcrack`

**URL:** https://www.kali.org/tools/pdfcrack/

**Alternatives:** pdf2john, John the Ripper jumbo





