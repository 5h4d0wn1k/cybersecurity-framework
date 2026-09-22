# ⬆️ Privilege Escalation (Linux & Windows)

Local audit of Linux & Windows privilege boundaries: lax permissions, exposed SUID/sudo surface, scheduler jobs, and unpatched escalations — on systems you own.

## Linux Local Escalation




#### Host Enumeration



##### LinPEAS ⭐

Runs hundreds of privilege-boundary checks — SUID/GUID binaries, writable PATHs, cron entries, capabilities, credentials in files, known-vuln hints — on Linux/Unix/MacOS and color-codes findings by severity.

**When:** First pass on any Linux host you are authorized to assess; `-s` for a faster/stealthier run, `-e` to enable extra checks before you dig into anything manually.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh`

**URL:** https://github.com/peass-ng/PEASS-ng

**Alternatives:** LinEnum, linux-smart-enumeration, linuxprivchecker


##### LinEnum

Single-shell-script Linux enumeration collecting user, sudo, cron, SUID, PATH, and file-permission checks into one grep-able report; still ships as the Kali/BlackArch `linenum` package.

**When:** A quick, dependency-free sweep when you want a portable .sh you can drop on a box and read results calmly offline.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh && chmod +x LinEnum.sh && ./LinEnum.sh -t`

**URL:** https://github.com/rebootuser/LinEnum

**Alternatives:** LinPEAS, linux-smart-enumeration, linuxprivchecker


##### linux-smart-enumeration (lse)

Ranked Linux enumerator that reveals findings progressively by importance level (-l0..-l2) and can watch for recurring cron/process activity while it runs.

**When:** When you want signal-first output instead of a full dump; escalate verbosity only if the default level comes up empty.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `curl "https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh" -Lo lse.sh && chmod 700 lse.sh && ./lse.sh -l1`

**URL:** https://github.com/diego-treitos/linux-smart-enumeration

**Alternatives:** LinPEAS, LinEnum, linuxprivchecker


#### Sudo & SUID Boundaries



##### SUID3NUM ⭐

Standalone Python SUID enumerator that separates default binaries from custom ones, cross-matches custom binaries against GTFOBins, and can auto-exploit non-destructive cases.

**When:** After LinPEAS flags SUID binaries: use it to distinguish vanilla OS binaries from operator-installed ones and jump straight to the GTFOBins-relevant entries.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `curl -k -O https://raw.githubusercontent.com/Anon-Exploiter/SUID3NUM/master/suid3num.py && chmod +x suid3num.py && python3 suid3num.py`

**URL:** https://github.com/Anon-Exploiter/SUID3NUM

**Alternatives:** SudoKiller, GTFOBins, GTFOBLookup


##### SudoKiller

Sudo-focused escalation auditor that checks for misconfigured sudo rules, sudo-version CVEs with prerequisites, dangerous GTFOBins entries, environment-variable abuse, and missing scripts referenced by sudoers.

**When:** A host where `sudo -l` reveals a non-trivial rule set and you want a catalog of candidate commands plus CVE-flagged sudo versions to try manually.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/TH3xACE/SUDO_KILLER && cd SUDO_KILLER && ./SUDO_KILLERv3.sh -c -a -e -r report.txt -p /tmp`

**URL:** https://github.com/TH3xACE/SUDO_KILLER

**Alternatives:** SUID3NUM, GTFOBins, LinPEAS


##### Reference: GTFOBins lookups



###### GTFOBins ⭐

Reference site (not a tool): documents how standard Unix binaries — when sudo, SUID, or capability-misconfigured — can escape restricted contexts, read/write files, or escalate.

**When:** Look up every SUID binary and sudo rule your enumeration surfaced; if the binary is listed, the page shows the exact boundary you wrongly granted.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://gtfobins.org

**Alternatives:** GTFOBLookup, SudoKiller, LOLBAS


###### GTFOBLookup

Offline command-line lookup utility that mirrors GTFOBins, LOLBAS, WADComs, and HijackLibs to disk so you can search abuse vectors without a browser or internet.

**When:** Air-gapped hosts or terminal-only workflows where you need to query GTFOBins/LOLBAS by executable name and category from the CLI.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `pipx install git+https://github.com/nccgroup/GTFOBLookup.git && gtfoblookup.py update`

**URL:** https://github.com/nccgroup/GTFOBLookup

**Alternatives:** GTFOBins, LOLBAS


#### Misconfiguration Scanners



##### linuxprivchecker ⭐

Python script that enumerates base system info and hunts world-writable files, misconfigurations, and cleartext passwords; written to suggest investigation targets rather than run exploits.

**When:** An OSCP-friendly second opinion after LinPEAS when you want a leaner, Python-based cross-check on the same host.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget https://raw.githubusercontent.com/sleventyeleven/linuxprivchecker/master/linuxprivchecker.py && python3 linuxprivchecker.py -w`

**URL:** https://github.com/sleventyeleven/linuxprivchecker

**Alternatives:** unix-privesc-check, LinPEAS, LinEnum


##### unix-privesc-check

PentestMonkey's classic shell script for weak file permissions and simple escalation vectors (world-writable files, exposed .netrc/.ssh), packaged in Kali; mature but only lightly maintained.

**When:** A conservative, read-only check on aged Unix boxes (also Solaris/AIX/HP-UX) where you want a second, low-noise opinion on file-permission drift.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install unix-privesc-check && unix-privesc-check standard`

**URL:** https://github.com/pentestmonkey/unix-privesc-check

**Alternatives:** linuxprivchecker, LinPEAS, linux-smart-enumeration


#### Process & File Watching



##### pspy ⭐

Unprivileged process snooper: uses /proc scans triggered by inotify events to catch short-lived processes (cron jobs, root scripts, and the arguments they carry) that a normal `ps` sweep never sees.

**When:** Park it for a couple of minutes after enumeration on a Linux host; timing-dependent scheduler jobs that static scans miss appear as they fire.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -L -o pspy64 https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 && chmod +x pspy64 && ./pspy64`

**URL:** https://github.com/DominicBreuker/pspy

**Alternatives:** inotifywait, fatrace, linux-smart-enumeration


##### inotifywait

inotify-based file/directory event watcher (create/modify/access/delete) from the inotify-tools package; the building block for precise, pattern-able watching scripts.

**When:** Point it at a specific writable directory or config file (e.g. a scheduler-owned path) and see exactly when and which files change on boxes you own.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install inotify-tools && inotifywait -m -r /tmp/watchme`

**URL:** https://github.com/inotify-tools/inotify-tools

**Alternatives:** fatrace, pspy


##### fatrace

fanotify-based system-wide file-access reporter (read/write/open/close per PID and path) — useful when a scheduled job touches files too briefly for process listing to catch.

**When:** Wide-surface file watching on your own host where inotify recursion gets unwieldy; narrow it with `--dir` to a single directory of interest.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install fatrace && sudo fatrace --dir /var/spool`

**URL:** https://github.com/martinpitt/fatrace

**Alternatives:** inotifywait, pspy






## Windows Local Escalation




#### Host Enumeration



##### WinPEAS ⭐

Windows counterpart to LinPEAS from the same PEASS suite: scans services, scheduled tasks, unquoted paths, AlwaysInstallElevated, stored credentials, and patch gaps; ships as winPEAS.exe (x64/x86) and winPEAS.bat in one release.

**When:** First pass on any Windows host you are authorized to assess; run as a low-integrity user, then re-run elevated to compare the privilege surface.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -L -o winPEASx64.exe https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEASx64.exe && ./winPEASx64.exe`

**URL:** https://github.com/peass-ng/PEASS-ng

**Alternatives:** Seatbelt, PrivescCheck, WES-NG


##### Seatbelt

GhostPack C# host-survey tool bundling dozens of 'safety-check' modules (token privileges, services, autoruns, credential stores, scheduled tasks) runnable in grouped or single-command mode.

**When:** Focused follow-up enumeration when you need a specific answer (e.g. only TokenPrivileges, Services, or the LOLBAS module); supports clean txt/json output.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/GhostPack/Seatbelt && cd Seatbelt && dotnet build -c Release`

**URL:** https://github.com/GhostPack/Seatbelt

**Alternatives:** WinPEAS, PrivescCheck, windows-privesc-check


##### PrivescCheck

itm4n's PowerShell-only enumeration script covering Windows privesc vulnerabilities and configuration issues, with Base/Extended/Audit check tiers and HTML/TXT/CSV report formats.

**When:** A single PowerShell script where you want consolidated, report-ready output without artifacts touching disk; use `-Extended` when the base run comes up empty.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl -LO https://raw.githubusercontent.com/itm4n/PrivescCheck/master/dist/PrivescCheck.ps1 && powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report TXT,HTML"`

**URL:** https://github.com/itm4n/PrivescCheck

**Alternatives:** WinPEAS, Seatbelt


#### Misconfiguration Scanners



##### windows-privesc-check ⭐

PentestMonkey's standalone executable (Python via PyInstaller) that audits securable objects for weak ACLs: services, service executables, %ProgramFiles% DLLs, %PATH%, registry RunOnce, and FAT installs.

**When:** Older/legacy Windows images where you want a misconfig-focused audit (not a patch check) runnable as a single portable .exe, ideally as Administrator.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `wget https://raw.githubusercontent.com/pentestmonkey/windows-privesc-check/master/windows-privesc-check2.exe && ./windows-privesc-check2.exe --dump -T report.txt`

**URL:** https://github.com/pentestmonkey/windows-privesc-check

**Alternatives:** PrivescCheck, WinPEAS, Seatbelt


#### Living-Off-the-Land Abuse



##### LOLBAS ⭐

Windows sibling of GTFOBins: catalogs living-off-the-land binaries, scripts, and libraries that legitimate shipped Windows components can be coerced into doing beyond their intended job.

**When:** Cross-check any signed binary or allowlisted script your enumeration surfaces on a Windows host — each entry lists the exact abuse command and MITRE mapping.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://lolbas-project.github.io

**Alternatives:** GTFOBLookup, GTFOBins, WinPEAS






## Kernel Exploit Checkers




#### Linux



##### linux-exploit-suggester ⭐

Off-host Linux audit tool (LES): reads kernel/distro fingerprints and cross-references them against current public exploit/PoC sets to rank exposure to known local privilege-escalation bugs.

**When:** After enumeration, when you want a ranked, CVE-linked shortlist of which kernel-era exploits are plausibly worth testing on your own lab or CTF hosts.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `wget -O les.sh https://raw.githubusercontent.com/The-Z-Labs/linux-exploit-suggester/master/linux-exploit-suggester.sh && bash les.sh --check-all`

**URL:** https://github.com/The-Z-Labs/linux-exploit-suggester

**Alternatives:** linux-exploit-suggester-2, GTFOBins


##### linux-exploit-suggester-2

Perl-based next-gen suggester that matches kernel/package versions against an exploit-db-derived list and can pull matching PoCs for review.

**When:** A second candidate shortlist when LES disagrees, or old-style searching where you want the actual exploit source downloaded into your lab to read first.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/jondonas/linux-exploit-suggester-2 && cd linux-exploit-suggester-2 && ./linux-exploit-suggester-2.pl -k`

**URL:** https://github.com/jondonas/linux-exploit-suggester-2

**Alternatives:** linux-exploit-suggester


#### Windows



##### Watson ⭐

.NET tool that enumerates missing KBs on a Windows host and suggests exploits for applicable local privilege-escalation CVEs, with exploit links per finding.

**When:** On lab Windows 10 (1507–2004) / Server 2016–2019 builds to map a CVE-to-exploit table fast; superseded for newer builds by WES-NG, which tracks the live MSRC feed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/rasta-mouse/Watson && cd Watson && dotnet build -c Release`

**URL:** https://github.com/rasta-mouse/Watson

**Alternatives:** WES-NG, Windows-Exploit-Suggester (legacy), WinPEAS


##### WES-NG (wesng)

Windows Exploit Suggester - Next Generation: takes a `systeminfo` dump (or missing-patch list) and maps it against a continuously updated MSRC/NVD dataset to list missing patches and known exploits.

**When:** Grab `systeminfo` from your Windows lab host, run wes.py on your workstation, and correlate patches offline for any supported OS from XP to Windows 11.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install wesng && wes.py --update && wes.py systeminfo.txt`

**URL:** https://github.com/bitsadmin/wesng

**Alternatives:** Watson, Windows-Exploit-Suggester (legacy), linux-exploit-suggester


##### Windows-Exploit-Suggester (legacy)

The 2014 original that coined the term; now archived because it depends on Microsoft's Security Bulletin Excel dump, which has been frozen since Q1 2017 — it can only address XP/Vista-era systems.

**When:** Only retro lab images from before 2017; for any current Windows host use WES-NG, which reads the live MSRC feed instead.

**Effort:** easy  ·  **Rating:** 2/5

**Install:** `git clone https://github.com/GDSSecurity/Windows-Exploit-Suggester && cd Windows-Exploit-Suggester && python windows-exploit-suggester.py --update`

**URL:** https://github.com/GDSSecurity/Windows-Exploit-Suggester

**Alternatives:** WES-NG, WinPEAS






## Kernel & Userspace Exploit POCs

Dirty Pipe (CVE-2022-0847) ⭐


#### Dirty Pipe (CVE-2022-0847) ⭐

Root POC for CVE-2022-0847 (Linux 5.8–5.16.x): abuses an uninitialized pipe_buffer flag to overwrite read-only page-cache data; this build overwrites /etc/passwd and restores it after popping a shell.

**When:** On lab or CTF kernels inside the affected range when no misconfiguration path exists; expect it to fail cleanly on 5.16.11+ or backported-fix kernels.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Arinerron/CVE-2022-0847-DirtyPipe-Exploit && cd CVE-2022-0847-DirtyPipe-Exploit && gcc -o exploit exploit.c && ./exploit`

**URL:** https://github.com/Arinerron/CVE-2022-0847-DirtyPipe-Exploit

**Alternatives:** dirtycow (CVE-2016-5195), PwnKit (CVE-2021-4034), linux-exploit-suggester


#### PwnKit (CVE-2021-4034)

Qualys-reported pkexec (polkit) memory-corruption exploit giving a one-command root shell on unpatched systems; technically a setuid userspace flaw, not the kernel, but near-unrivaled in reliability when present.

**When:** Applies to many distros of 2009–2022 vintage; `make dry-run` tests whether your own host is vulnerable without popping a shell.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/berdav/CVE-2021-4034 && cd CVE-2021-4034 && make && ./cve-2021-4034`

**URL:** https://github.com/berdav/CVE-2021-4034

**Alternatives:** Dirty Pipe (CVE-2022-0847), dirtycow (CVE-2016-5195), linux-exploit-suggester


#### dirtycow (CVE-2016-5195)

The archived Dirty COW race-condition family (CVE-2016-5195) for kernels roughly up to 4.8.3: PoCs write into read-only mappings, e.g. splicing a new root account into /etc/passwd.

**When:** Only legacy or sandboxed images that still run pre-2016-fix kernels; treat it as a historical exercise — modern distros are not exposed.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/firefart/dirtycow && cd dirtycow && gcc -pthread dirty.c -o dirty -lcrypt && ./dirty`

**URL:** https://github.com/firefart/dirtycow

**Alternatives:** Dirty Pipe (CVE-2022-0847), PwnKit (CVE-2021-4034)






## Active Directory & Kerberos Cross-ref




#### Kerberoasting & Delegation



##### Rubeus ⭐

C# Kerberos abuse toolkit covering kerberoast, AS-REP roast, S4U constrained/unconstrained delegation, and golden/silver/diamond ticket forgery from any domain-joined host.

**When:** Escalation inside Active Directory when you own an SPN-bearing or delegation-active account: request service tickets for offline cracking or impersonate users through s4u.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/GhostPack/Rubeus && cd Rubeus && dotnet build -c Release`

**URL:** https://github.com/GhostPack/Rubeus

**Alternatives:** Impacket (GetUserSPNs.py), Mimikatz


##### Impacket (GetUserSPNs.py)

Python Kerberos suite whose GetUserSPNs.py requests TGS tickets for services running under user accounts (Kerberoasting) and GetNPUsers.py hunts pre-auth-disabled accounts (AS-REProasting).

**When:** Roasting from a Linux attack box (or WSL) where you have valid domain credentials but no Windows shell; also handles delegation-related ticket replay.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `python3 -m pipx install impacket && GetUserSPNs.py -request -dc-ip 10.0.0.1 corp.local/user`

**URL:** https://github.com/fortra/impacket

**Alternatives:** Rubeus, Kekeo





