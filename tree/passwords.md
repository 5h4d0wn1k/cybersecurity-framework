# 🔑 Password Attacks & Cracking

Offline + online cracking of hashes and logins you own: GPU/CPU recovery, wordlists, archive and file password recovery.

## GPU & Accelerated Cracking

### Hashcat ⭐

World's fastest password recovery utility; GPU-optimized kernels for 590+ hash modes across dictionary (wordlist), mask/brute-force, hybrid, PCFG and rule-based attacks.

**When:** The go-to for offline hash recovery on your own system: first benchmark, then wordlist, then mask/rule attacks. Also the home of every -a 0/3/6/7 mode and .rule files.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install hashcat`

**URL:** https://github.com/hashcat/hashcat

**Alternatives:** hashcat-utils, John the Ripper


### hashcat-utils

Small MIT-licensed STDIN/STDOUT utilities (cap2hccapx, combipow, len, cutb, rulegen, …) meant to be chained into pipelines that feed hashcat candidates.

**When:** Pre-process wordlists or extract Wi-Fi/captured hashes into the exact format hashcat needs before launching an attack.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/hashcat/hashcat-utils && make`

**URL:** https://github.com/hashcat/hashcat-utils

**Alternatives:** maskprocessor, John the Ripper jumbo


### MaskProcessor

High-performance per-position word generator using hashcat-style masks (?l, ?u, ?d, ?s, ?a) and up to four custom charsets; generates candidate words hashcat guesses.

**When:** Generate a mask-only wordlist on CPU, or build rules/masks offline before feeding them to a GPU cracking session.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/hashcat/maskprocessor && make`

**URL:** https://github.com/hashcat/maskprocessor

**Alternatives:** hashcat, crunch, kwprocessor


## CPU & Classic Cracking

### John the Ripper ⭐

The classic Unix password cracker: dictionary, incremental (markov), and rule-based modes, plus hundreds of hash/cipher formats in its jumbo builds; runs on CPU, GPU (OpenCL) and more.

**When:** Default choice for /etc/shadow-style hashes and archive/doc hashes on any box, especially when GPU drivers are unavailable.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install john`

**URL:** https://www.openwall.com/john/

**Alternatives:** John the Ripper jumbo, hashcat, ophcrack


### John the Ripper jumbo

Community-enhanced jumbo edition (bleeding-jumbo branch): hundreds of extra formats (Windows NTLM, macOS, PDF, RAR, KeePass) and bundled *2john converters for encrypted files.

**When:** When your hash/source file is not handled by core John or hashcat yet - the widest format coverage for offline recovery.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/openwall/john && ./configure && make -j`

**URL:** https://github.com/openwall/john

**Alternatives:** John the Ripper, hashcat


### ophcrack

Windows LM/NTLM password cracker based on rainbow tables; GUI + LiveCD, with free XP/Vista tables and SAM dumping from your own Windows installs.

**When:** Recovering weak LM/NTLM hashes for accounts you administer, when rainbow tables beat per-hash brute forcing for short passwords.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install ophcrack`

**URL:** https://ophcrack.sourceforge.io/

**Alternatives:** John the Ripper, hashcat


## Online Login Attacks

### Hydra ⭐

Parallelized network login cracker supporting 50+ protocols/modules (ssh, rdp, http-get/post-form, ftp, smb, …) with -L/-P user/password lists and brute-force (-x).

**When:** Test login strength against a live service you own (your lab router web login, your SSH server) using lists from SecLists; lowest effort-to-coverage ratio.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install hydra`

**URL:** https://github.com/vanhauser-thc/thc-hydra

**Alternatives:** medusa, ncrack, patator


### Medusa

Thread-based modular parallel login brute-forcer (SMB, HTTP, MS-SQL, RDP, SSH, VNC and more), with combination files and host/user/password parallelism.

**When:** When you want threaded parallel testing against multiple hosts at once and cleaner control over per-module options than Hydra gives.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install medusa`

**URL:** https://github.com/jmk-foofus/medusa

**Alternatives:** hydra, ncrack, patator


### Ncrack

Nmap-team high-speed network authentication cracker with an Nmap-like CLI and timing templates; supports SSH, RDP, Telnet, HTTP(S), SMB, VNC, Redis and more.

**When:** Large-scale audited hosts with an nmap-flavored mindset; note that focus has moved to the NSE brute scripts and the standalone build is 0.7 (2019).

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install ncrack`

**URL:** https://nmap.org/ncrack/

**Alternatives:** hydra, medusa, patator


### Patator

Multi-purpose flexible brute-forcer written in Python with modules for http_fuzz (web login), ssh_login, ftp_login, rdp_login and more; built to be more reliable than its predecessors.

**When:** Web form logins and protocol guessing where you need predictable retry/ignore logic and precise module parameters.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install patator`

**URL:** https://github.com/lanjelot/patator

**Alternatives:** hydra, medusa, ncrack


## Wordlists & Generation

### SecLists ⭐

The security tester's companion collection: passwords (10k/1M/rockyou-derived), usernames, default/router credentials, fuzzing payloads and discovery lists in one place.

**When:** First stop in any cracking session - pull its built-in dictionaries before generating your own.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone --depth 1 https://github.com/danielmiessler/SecLists.git`

**URL:** https://github.com/danielmiessler/SecLists

**Alternatives:** rockyou.txt, cewl


### rockyou.txt

The 2009 RockYou breach password list (~14M passwords, historically the free default): a solid baseline dictionary for fast-hash testing on your own targets.

**When:** Quick first-pass dictionary attack before rule/mask work when you need a proven real-world wordlist (Kali ships it under /usr/share/wordlists).

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install wordlists`

**URL:** https://github.com/danielmiessler/SecLists/tree/master/Passwords/Leaked-Databases

**Alternatives:** SecLists


### CeWL

Ruby spider that crawls a site to a depth, collects unique words (plus email/author metadata) and emits a custom wordlist for password recovery.

**When:** Recovering passwords tied to a site's own vocabulary - e.g. your own web app or a CTF - where organization-specific words beat generic dictionaries.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/digininja/CeWL && bundle install`

**URL:** https://github.com/digininja/CeWL

**Alternatives:** crunch, mentalist


### crunch

Wordlist generator that enumerates all combinations/permutations of a charset with pattern support (@,%^ placeholders), file-splitting, resume and gzip/7z output.

**When:** Generate targeted candidate lists (fixed charset, known pattern positions, e.g. TailNumbers-like masks) to feed hashcat or John.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install crunch`

**URL:** https://sourceforge.net/projects/crunch-wordlist/

**Alternatives:** maskprocessor, kwprocessor, mentalist


### kwprocessor

Advanced keyboard-walk generator that produces passwords following keyboard routes (adjacent-key walks, zxcvbn-style patterns) from configurable basechars, keymaps and route files.

**When:** Targeting PINs/passphrases typed along keyboard patterns (your own router/phone PINs) where left-right walks are more likely than random strings.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/hashcat/kwprocessor && make`

**URL:** https://github.com/hashcat/kwprocessor

**Alternatives:** crunch, maskprocessor


### Mentalist

Graphical wordlist generator built on human password paradigms (case mangling, keyboard walks, adding years/digits); exports full wordlists or ready-made hashcat and John rules.

**When:** Visually build a password profile (organization vocab + year + symbol) when you prefer a GUI over hand-rolling rule files.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/sc0tfree/mentalist && pip install .`

**URL:** https://github.com/sc0tfree/mentalist

**Alternatives:** cewl, crunch


## Hash Identification

### hashid ⭐

Python tool identifying 220+ hash types via regex, printing the matching hashcat mode number and John format so your next command is correct the first time.

**When:** Immediately after collecting a hash (dump, CTF, config) - before picking -m / --format, to avoid line-length and wrong-mode failures.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install hashid`

**URL:** https://github.com/psypanda/hashID

**Alternatives:** hash-identifier, HashCat example-hashes


### hash-identifier

Classic interactive script that asks candidate lines and guesses the hash algorithm family; the free counterpart hashid was written to supersede.

**When:** A zero-dependency interactive sanity check on a single odd-looking hash when you don't have pip/Git access.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/blackploit/hash-identifier && python3 hash-id.py`

**URL:** https://github.com/blackploit/hash-identifier

**Alternatives:** hashid, HashCat example-hashes


### HashCat example-hashes

Official reference table with one valid sample hash per hashcat mode (password is always 'hashcat'); the canonical way to confirm a hash type and test an attack command.

**When:** Verify your command and hash formatting offline (also embedded in `hashcat --example-hashes`) before real runs, or to label samples in CTFs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://hashcat.net/wiki/doku.php?id=example_hashes

**Alternatives:** hashid, hash-identifier


## Encrypted File & Archive Recovery

### zip2john ⭐

John the Ripper utility that converts encrypted ZIPs (and via siblings like rar2john, 7z2john, pdf2john) into a crackable hash for john or hashcat; fast and dependency-free.

**When:** Recovering a forgotten password on your own ZIP/Office/PDF archive: convert first, crack with john -jumbo or hashcat after.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install john`

**URL:** https://github.com/openwall/john

**Alternatives:** fcrackzip, John the Ripper jumbo


### fcrackzip

Fast zip password cracker with dictionary and brute-force modes (libzip-based fork runs ~1000x faster than the original unzip-spawning version).

**When:** Quick direct brute/dictionary check of a single small ZIP without setting up John pipelines; keep in mind upstream notes it is largely superseded by zip2john + jumbo.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install fcrackzip`

**URL:** https://github.com/hyc/fcrackzip

**Alternatives:** zip2john, John the Ripper jumbo


### pdfcrack

Small GPL tool recovering owner/user passwords from PDFs using the standard security handler (rev 2-4) via wordlist or brute force, with job save/load state.

**When:** Recover your own locked PDF (user or owner password) when the PDF predates AES-256 rev 5; on modern AES R2/R3 PDFs prefer john's pdf2john formats.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install pdfcrack`

**URL:** https://pdfcrack.sourceforge.net/

**Alternatives:** zip2john, John the Ripper jumbo


### rarcrack

Brute-force password recovery for RAR, ZIP and 7Z archives with automatic resume via XML state file and thread/charset control; dormant since ~2010.

**When:** Legacy rar3 archives only; on modern hardware and rar5 prefer rar2john + john/hashcat since rarcrack is no longer maintained.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install rarcrack`

**URL:** https://rarcrack.sourceforge.net/

**Alternatives:** zip2john, John the Ripper jumbo


### keepass2john

John jumbo converter that extracts a sealed .kdbx KeePass database into a PBKDF2/AES hash crackable by john or hashcat ($keepass$ format).

**When:** Unlock your own KeePass vault after losing the master password - always on a copy you own, never a stored database you don't.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install john`

**URL:** https://github.com/openwall/john

**Alternatives:** John the Ripper jumbo

