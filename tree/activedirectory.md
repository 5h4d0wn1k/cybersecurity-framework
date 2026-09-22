# 🏰 Active Directory Security

Map, audit, and score Active Directory attack paths — graph enumeration, Kerberos/protocol tooling, credential-exposure testing, and risk health checks — for authorized assessments and blue-team defense.

## Attack-Path Enumeration & Graphing

BloodHound CE ⭐


#### BloodHound CE ⭐

The current-generation attack-path engine: ingests SharpHound data into a Neo4j graph and reveals how users, groups, computers, sessions, GPOs, ACLs, trusts, and ADCS enrollments chain into paths to Domain Admin — including ADCS, NTLM, and delegation abuse conditions.

**When:** The core analysis step after collection: visualize and triage which abusable identity relationships are the shortest paths to Tier-0, and why they matter to defenders.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz (see the CE Quickstart for the Docker-Compose deployment)`

**URL:** https://github.com/SpecterOps/BloodHound

**Alternatives:** SharpHound, PlumHound, BloodHound.py


#### SharpHound

C# data collector for BloodHound CE that runs on domain-joined Windows and exports a zip of users, groups, sessions, local admins, ACLs, GPOs, trusts, and more via LDAP and SMB — the dataset the graph is built from.

**When:** Run first from any authorized domain-joined host or as a standalone binary, then feed the output into BloodHound CE for graph analysis.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download the SharpHound CE binary from the BloodHound CE UI (Settings → Download Collectors) or the GitHub releases page`

**URL:** https://github.com/SpecterOps/SharpHound

**Alternatives:** BloodHound.py


#### PlumHound

Wraps BloodHound's Neo4j Cypher backend into repeatable HTML reports and task lists; surfaces the busiest paths to Domain Admin and which relationship to break to sever a given path.

**When:** Turn a collected BloodHound graph into consumable, operations-ready findings for blue/purple-team remediation planning and scheduled reporting.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install plumhound`

**URL:** https://github.com/PlumHound/PlumHound

**Alternatives:** BloodHound CE, BloodHound.py






## Protocol Toolkit (Linux-side)

NetExec ⭐


#### Impacket

Fortra's Python library of Windows network protocol implementations plus ~100 example scripts — secretsdump (remote SAM/LSA/NTDS credential extraction over DRSUAPI/DCOM/registry in mimikatz-compatible hash format), psexec/wmiexec/atexec remote execution, ntlmrelayx, and a full Kerberos toolbox.

**When:** The foundation for nearly all Linux-side AD work: secretsdump is the standard way to audit credential hygiene on controllers and hosts during an authorized assessment.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** NetExec


#### NetExec ⭐

The maintained successor to CrackMapExec: multi-protocol (SMB, LDAP, MSSQL, SSH, WinRM, RDP) credential validation that rapidly tests which identities work where, sprays passwords, and enumerates shares, users, sessions, domains, and password policy across a fleet.

**When:** Fast credential-driven health-check across many hosts in one pass — who is effective as admin, which policy is weakest, and which shares are open.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install git+https://github.com/Pennyw0rth/NetExec`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** Impacket


#### Kerbrute

Go tool that validates AD usernames and tests passwords through Kerberos AS-REQ/AS-REP exchanges; its userenum mode never triggers account lockout, while passwordspray/bruteforce do and are meant for policy-aware testing.

**When:** Discover which candidate usernames actually exist during recon, and safely prove a single reused weak password across a user list you monitor in your own logs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/ropnop/kerbrute@latest`

**URL:** https://github.com/ropnop/kerbrute

**Alternatives:** Rubeus, NetExec


#### Rubeus

C# toolset for raw Kerberos interaction — ticket requests and passthe-ticket, overpass-the-hash, golden/silver/diamond ticket forging, Kerberoasting, AS-REP roasting, and s4u delegation testing, compiled to run on Windows.

**When:** Windows-side Kerberos validation: check which service accounts are Kerberoastable and how delegation and ticket caching expose lateral movement in your domain.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Prebuilt binaries ship under Rubeus/Release — or compile with dotnet build against the repo source`

**URL:** https://github.com/GhostPack/Rubeus

**Alternatives:** Impacket (getTGT/getTGS), Kerbrute






## Credential Exposure Testing

Mimikatz ⭐


#### Mimikatz ⭐

The canonical Windows credential tool: sekurlsa extracts plaintext passwords, NTLM hashes, PINs, and Kerberos tickets from LSASS memory, while lsadump covers SAM, LSA secrets, DCSync, and DCShadow, plus pass-the-hash/ticket and token manipulation.

**When:** On an authorized host with local admin to prove whether LSASS-accessible credentials leak and whether protections like LSA Protection or Credential Guard actually hold.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download prebuilt binaries from https://github.com/gentilkiwi/mimikatz/releases`

**URL:** https://github.com/gentilkiwi/mimikatz

**Alternatives:** pypykatz, lsassy


#### pypykatz

Pure-Python reimplementation of Mimikatz's sekurlsa: parses live LSASS memory or minidump files on any OS to recover NT hashes, plaintext credentials, Kerberos tickets, and DPAPI keys.

**When:** Analyze an LSASS dump from Linux during incident response or assessment when you hold the dump rather than a live Windows host.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install pypykatz`

**URL:** https://github.com/skelsec/pypykatz

**Alternatives:** Mimikatz, lsassy


#### lsassy

Python tool that remotely dumps LSASS (comsvcs, Procdump, nanodump, and more methods) over SMB/WMI from whole fleets at once and extracts credentials in place with pypykatz.

**When:** When you hold admin on a set of Windows hosts and want to audit logged-on credential exposure across the fleet without interactive sessions on each box.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install lsassy`

**URL:** https://github.com/login-securite/lsassy

**Alternatives:** Mimikatz, pypykatz






## PowerShell & Scripted Enumeration

PowerView ⭐


#### PowerView ⭐

Pure-PowerShell AD enumerator (PowerSploit) turning LDAP into one-liner cmdlets for users, groups, computers, GPOs, ACLs, shares, and trust maps; also hunts which machines specific users log into and where you have local admin.

**When:** From a domain-joined PowerShell session when you need fast, scriptable situational awareness without dropping a binary on disk — and to see exactly what attackers enumerate first.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/PowerShellMafia/PowerSploit && Import-Module .\Recon\PowerView.ps1`

**URL:** https://github.com/PowerShellMafia/PowerSploit

**Alternatives:** PowerUp, BloodHound.py


#### PowerUp

PowerSploit module that audits a Windows host for common local privilege-escalation misconfigurations — unquoted service paths, writable service binaries, modifiable services, AlwaysInstallElevated — and reports each with abuse-ready detail.

**When:** Local privilege-escalation audit of a single host during sanctioned testing or as part of hardening a fleet that lacks LAPS and least-privilege discipline.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/PowerShellMafia/PowerSploit && Import-Module .\Privesc\PowerUp.ps1`

**URL:** https://github.com/PowerShellMafia/PowerSploit

**Alternatives:** PowerView


#### BloodHound.py

Python/Impacket ingestor for BloodHound CE that collects users, computers, groups, trusts, ACLs, sessions, and local admins from Linux using only credentials — no Windows host or SharpHound binary required.

**When:** When you need BloodHound data but have no Windows foothold; the Linux-native collection counterpart to SharpHound.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install bloodhound-ce (bloodhound-ce branch adds the bloodhound-ce-python CLI)`

**URL:** https://github.com/dirkjanm/BloodHound.py

**Alternatives:** PowerView






## AD Risk & Health Auditing

PingCastle ⭐


#### PingCastle ⭐

Active Directory risk and maturity audit (by Netwrix) that scores a domain 0–100 across ~10 axes — accounts, ADCS, Kerberos, trusts, delegation, GPOs, infrastructure — and emits a CISO-ready HTML report with prioritized remediation via a read-only healthcheck.

**When:** The default first formal AD security assessment: minutes to run, zero writes, and ideal as a recurring blue-team health check or engagement kickoff.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download standalone PingCastle.exe from https://github.com/netwrix/pingcastle/releases and run on a domain-joined Windows host (.NET 8)`

**URL:** https://github.com/netwrix/pingcastle

**Alternatives:** Purple Knight, ADRecon


#### Purple Knight

Free commercial assessment from Semperis scoring hybrid AD, Entra ID, and Okta estates against 150+ indicators of exposure and compromise, with MITRE ATT&CK mapping and prioritized executive guidance.

**When:** Complement PingCastle when you also manage Entra ID or Okta and want an easy scorecard plus IoC checks across the hybrid estate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the Windows agent from https://www.semperis.com/purple-knight/ (free registration required)`

**URL:** https://www.semperis.com/purple-knight/

**Alternatives:** PingCastle, ADRecon


#### ADRecon

PowerShell tool that extracts a wide slice of AD state — users, groups, OUs, GPOs, trusts, ACLs, password policies, DNS zones, and optionally LAPS/BitLocker keys and Kerberoastable SPNs — and consolidates it into a summary Excel workbook.

**When:** Broad read-only documentation of an environment for audit reports; runs as an ordinary domain user and works from non-member hosts over LDAP.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/adrecon/ADRecon && .\ADRecon.ps1 on a Windows host`

**URL:** https://github.com/adrecon/ADRecon

**Alternatives:** PingCastle, AD-Audit


#### AD-Audit

Modular PowerShell auditing suite aligned to Microsoft security best practices: user/computer hygiene, group policy, domain-controller security, credential-theft prevention, least privilege, AD FS, event monitoring, and ADCS checks with SQLite-backed findings.

**When:** Teams wanting an extensible, automation-friendly policy-check audit (CI/CD output) rather than a single maturity score.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/adrian207/AD-Audit && Import-Module .\AD-Audit.psd1 (requires PowerShell 5.1+ and the RSAT ActiveDirectory module)`

**URL:** https://github.com/adrian207/AD-Audit

**Alternatives:** ADRecon, PingCastle





