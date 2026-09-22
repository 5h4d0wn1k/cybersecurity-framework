# 🏰 Active Directory Security

Map, audit, and score Active Directory attack paths — graph enumeration, LDAP/ADSI querying, Kerberos/NTLM protocol tooling, legacy CVE PoCs, GPO/ACL abuse, credential-exposure testing, and risk health checks — for authorized assessments and blue-team defense.

## Attack-Path Enumeration & Graphing




#### BloodHound Pipeline



##### Collectors & Ingestors



###### Windows-native collection



###### SharpHound ⭐

C# collector for BloodHound CE that runs on a domain-joined Windows host and exports users, groups, sessions, local admins, ACLs, GPOs, trusts and more via LDAP and SMB — the dataset the whole graph is built from.

**When:** Authorized collection from a domain-joined host with valid credentials; feed the produced zip into BloodHound CE for graph analysis.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download the SharpHound CE collector from the BloodHound CE UI (Settings → Download Collectors) or the SpecterOps release page`

**URL:** https://github.com/SpecterOps/SharpHound

**Alternatives:** BloodHound.py


###### Linux-native collection



###### BloodHound.py ⭐

Python/Impacket ingestor that collects users, groups, trusts, ACLs, sessions, and local admins from Linux using only credentials — no Windows host or SharpHound binary required.

**When:** When you need BloodHound data for an authorized scope but only hold a Linux foothold or domain credentials.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dirkjanm/BloodHound.py && pip install -r requirements.txt (or the bloodhound-ce fork's CLI)`

**URL:** https://github.com/dirkjanm/BloodHound.py

**Alternatives:** SharpHound


##### Graph Analysis & Reporting



###### BloodHound CE ⭐

Current-generation attack-path engine: ingests SharpHound data into Neo4j and reveals how users, groups, computers, sessions, GPOs, ACLs, trusts, and ADCS enrollments chain into paths to Domain Admin, including ADCS, NTLM, and delegation abuse conditions.

**When:** The core analysis step after collection: visualize and triage which abusable identity relationships are the shortest paths to Tier-0 in your own estate.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -L https://ghst.ly/BHCE-QS | bash (official CE quickstart, or the Docker Compose deployment from the docs)`

**URL:** https://github.com/SpecterOps/BloodHound

**Alternatives:** PlumHound, Adalanche


###### PlumHound

Wraps BloodHound's Neo4j Cypher backend into repeatable HTML reports and task lists; surfaces the busiest paths to Domain Admin and which relationship to break to sever a given path.

**When:** Turn collected BloodHound data into operations-ready findings for blue/purple-team remediation planning and scheduled reporting.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install plumhound`

**URL:** https://github.com/PlumHound/PlumHound

**Alternatives:** BloodHound CE


##### Alternate visualizers



###### Adalanche ⭐

Standalone attack-graph visualizer from lkarlslund that collects and graph-explores who is *really* Domain Admin, rebuilding the effective reachability without a Neo4j stack.

**When:** A lighter-weight second opinion alongside BloodHound in labs or quick scoping when you want immediate graph answers without standing up the full CE stack.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download the release binary and run the built-in collector against your AD read credentials or an existing dump`

**URL:** https://github.com/lkarlslund/Adalanche

**Alternatives:** BloodHound CE


#### Domain-Wide Enumeration & Scoring



##### Privilege-escalation sweeps



###### adPEAS ⭐

Active-Directory-flavored PEAS: a PowerShell sweep that checklists misconfigurations across users, groups, GPOs, ACLs, Kerberos, and delegation from a single domain-joined run.

**When:** Fast, readable AD hygiene sweep during authorized testing or internal audits when you want a findings checklist before deeper graph work.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ajm4n/adPEAS && run adPEAS.ps1 from an authenticated domain session`

**URL:** https://github.com/ajm4n/adPEAS

**Alternatives:** PowerView, ldapdomaindump


##### Assessment scorecards



###### Purple Knight ⭐

Free commercial scoring (Semperis) that rates hybrid AD, Entra ID, and Okta estates against 150+ indicators of exposure and compromise, with MITRE ATT&CK mapping and prioritized guidance.

**When:** Complement PingCastle when you also manage Entra ID or Okta and want an easy scorecard plus IoC checks over the hybrid estate.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the Windows agent from https://www.semperis.com/purple-knight/ (free registration required)`

**URL:** https://www.semperis.com/purple-knight/

**Alternatives:** PingCastle, ADRecon






## LDAP & ADSI Directory Queries




#### Raw query clients



##### ldapsearch ⭐

OpenLDAP's ubiquitous CLI for anonymous and authenticated LDAP queries — users, groups, computers, GPOs, ACLs, and schema, filterable on any attribute.

**When:** The first read-only look at any authorized directory: quick non-invasive enumeration and attribute mining that touches nothing on disk.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `apt-get install -y ldap-utils`

**URL:** https://www.openldap.org/

**Alternatives:** ADFind, windapsearch, NetExec (nxc ldap)


##### ADFind

Joeware's battle-tested Windows LDAP search tool with terser output and built-in switches for common ADC, trust, PSO, and password-policy queries.

**When:** Scripted one-line AD queries from Windows during audits where switch-friendly output beats raw LDIF.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download adfind.exe from https://www.joeware.net/freetools/tools/adfind/`

**URL:** https://www.joeware.net/freetools/tools/adfind/

**Alternatives:** ldapsearch, windapsearch


##### windapsearch

Python LDAP enumerator tuned for penetration workflow: dumps domain users with their group memberships, computers, privileged groups, and more from a single credential.

**When:** Fast user/group enumeration during authorized testing when you want structured output instead of hand-rolled ldapsearch filters.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ropnop/windapsearch && pip install -r requirements.txt`

**URL:** https://github.com/ropnop/windapsearch

**Alternatives:** ldapdomaindump, ldapsearch


#### Bulk enumerators & GUI explorers



##### ldapdomaindump ⭐

Dumps the entire domain object surface — groups, users, computers, GPOs, DNS zones, trusts, and shares — to browesable grep-friendly files using just domain credentials.

**When:** Baseline full-directory export during authorized engagements for later offline review and scripted analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install ldapdomaindump`

**URL:** https://github.com/dirkjanm/ldapdomaindump

**Alternatives:** windapsearch, AD Explorer


##### Active Directory Explorer (AD Explorer)

Sysinternals viewer that snapshots and browsably compares the full AD database — including every security descriptor and ACL — with hex views of attribute values.

**When:** Interactive ACL/attribute forensics and before-after comparison of changes during an authorized assessment or blue-team review.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download AD Explorer from the Microsoft Sysinternals page (https://learn.microsoft.com/sysinternals/downloads/adexplorer)`

**URL:** https://learn.microsoft.com/sysinternals/downloads/adexplorer

**Alternatives:** ADSI Edit, ldapdomaindump


##### ADSI Edit (MMC)

Microsoft's built-in snap-in for direct read/write access to every AD object and attribute, including configuration and schema partitions.

**When:** Point-and-click verification of specific attribute values and ACLs during audits without writing scripts.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Add via 'Turn Windows features on or off' → AD DS and AD LDS Tools (native on domain controllers)`

**URL:** https://learn.microsoft.com/windows-server/identity/ad-ds/get-started/adsi-edit

**Alternatives:** AD Explorer, ldapsearch


#### Fleet-wide LDAP & credential validation



##### NetExec ⭐

The maintained successor to CrackMapExec: multi-protocol (SMB, LDAP, MSSQL, SSH, WinRM, RDP) credential validation that rapidly tests which identities work where, sprays passwords, and enumerates shares, users, sessions, domains, and password policy across a fleet.

**When:** Fast credential-driven health-check across many hosts in one pass — including `nxc ldap` for user/policy enumeration — during authorized assessments.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pipx install git+https://github.com/Pennyw0rth/NetExec`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** windapsearch, ldapdomaindump






## Kerberos Attacks & Ticket Abuse




#### Roasting



##### Kerberoasting



###### Rubeus ⭐

C# toolset for raw Kerberos interaction — ticket requests, passthe-ticket, overpass-the-hash, ticket forging, Kerberoasting, AS-REP roasting, and s4u delegation testing, compiled to run on Windows.

**When:** Windows-side Kerberos validation: check which service accounts are Kerberoastable and how delegation and ticket caching expose lateral movement in your domain.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/GhostPack/Rubeus && dotnet build (or run a compiled release binary)`

**URL:** https://github.com/GhostPack/Rubeus

**Alternatives:** Impacket GetUserSPNs, kekeo


###### Impacket GetUserSPNs

Impacket example script that requests TGS tickets for every registered SPN account and exports the encrypted segments in crackable hashcat/Hashcat format from Linux.

**When:** Linux-side Kerberoasting with just domain credentials — pair the output with hashcat to prove weak service-account passwords in authorized tests.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** Rubeus


##### AS-REP Roasting



###### Impacket GetNPUsers ⭐

Impacket example script that requests pre-authentication-free AS-REPs for accounts with 'Do not require Kerberos pre-authentication' and exports crackable hash segments.

**When:** Identify and prove weak passwords on accounts without Kerberos pre-auth during authorized audits from Linux.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** ASREPRoast


###### ASREPRoast

HarmJ0y's PowerShell toolkit that retrieves crackable hashes from KRB5 AS-REP responses for user enumeration and pre-auth-disabled account auditing.

**When:** Windows-side AS-REP roasting when you are already in a network session and want the native PowerShell route.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/HarmJ0y/ASREPRoast`

**URL:** https://github.com/HarmJ0y/ASREPRoast

**Alternatives:** Impacket GetNPUsers


#### Ticket requests & delegation



##### Impacket getTGT / getST ⭐

Impacket scripts that obtain TGTs (with password or NT hash via AES/RC4) and service tickets via S4U2Self/S4U2Proxy, enabling constrained-delegation and resource-based-delegation validation from Linux.

**When:** Prove unconstrained/constrained/resource-based delegation abuse paths in authorized tests without any Windows-side pieces.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** Rubeus, kekeo


##### kekeo

Gentilkiwi's Kerberos suite for ticket generation, renewal, and fabrication (including golden/silver tickets and s4u abuse) as a lighter companion to Mimikatz.

**When:** Windows-native ticket forging and delegation testing where you want a purpose-built alternative to the C# tooling.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/gentilkiwi/kekeo && build with Visual Studio (binaries under x64/Release)`

**URL:** https://github.com/gentilkiwi/kekeo

**Alternatives:** Rubeus, Impacket getTGT / getST


#### Username enumeration & password spraying



##### Kerbrute ⭐

Go tool that validates AD usernames and tests passwords through Kerberos AS-REQ/AS-REP exchanges; its userenum mode never triggers account lockout, while passwordspray/bruteforce do and are meant for policy-aware testing.

**When:** Discover which candidate usernames actually exist during recon, and safely prove a single reused weak password across a user list you monitor in your own logs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/ropnop/kerbrute@latest`

**URL:** https://github.com/ropnop/kerbrute

**Alternatives:** DomainPasswordSpray, NetExec


##### DomainPasswordSpray

Dafthack's PowerShell sprayer that gathers the user list from AD, checks the domain lockout policy, and tests one password per user (or a small set) with delay controls to stay under thresholds.

**When:** Lockout-safe password-spray audit of your own domain when you need built-in policy-awareness and randomized delays.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dafthack/DomainPasswordSpray && .\DomainPasswordSpray.ps1`

**URL:** https://github.com/dafthack/DomainPasswordSpray

**Alternatives:** Kerbrute, NetExec






## NTLM Relaying & Protocol Poisoning




#### Name-resolution poisoning (LLMNR / NBT-NS / mDNS)



##### Responder ⭐

The reference LLMNR/NBT-NS/mDNS poisoner and SMB/HTTP/LDAP rogue-server that captures NetNTLMv2 challenges for cracking or relay in lab and authorized bipedal-spook-and-serve testing.

**When:** Confirm whether name resolution poisoned traffic and NTLM challenge responses are being accepted on your own lab network.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/lgandx/Responder && sudo python3 Responder.py -I eth0`

**URL:** https://github.com/lgandx/Responder

**Alternatives:** Inveigh, mitm6


##### mitm6

IPv6 DNS poisoning tool (by the PetitPotam author) that answers DHCPv6/RA traffic to route a victim's updates to an attacker-controlled DNS, enabling WPAD or LDAP relay chains.

**When:** IPv6-first poisoning in lab environments to demonstrate why IPv6 without mitigations is a relay avenue.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install mitm6`

**URL:** https://github.com/dirkjanm/mitm6

**Alternatives:** Responder


##### Inveigh

Kevin-Robertson's Windows PowerShell/C# LLMNR/NBT-NS/mDNS/SMBv1 responder and NTLMv1/v2 challenge-capturer with Console and Web GUI views.

**When:** Windows-native poisoning lab where you want a pure-PowerShell or compiled alternative to the Linux Responder.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `iwr https://raw.githubusercontent.com/Kevin-Robertson/Inveigh/master/Scripts/Inveigh.ps1`

**URL:** https://github.com/Kevin-Robertson/Inveigh

**Alternatives:** Responder


#### Relay chains



##### Impacket ntlmrelayx ⭐

Impacket's NTLM relay server that forwards captured NetNTLM challenges to SMB, LDAP(S), HTTP(S), and MSSQL targets, with built-in modules for dumping SAM, creating users, and targeting printers (CVE-2019-1040 MIC-removal support).

**When:** In a controlled lab, relay an intercepted challenge to an authorized target to prove what NTLM-signing-off and relay protections are really enforcing.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** Responder


#### Auth coercion (printer-bug family)



##### printerbug.py ⭐

Decoder-it's DCERPC-only printerbug.py that triggers the MS-RPRN printer bug to coerce a host into authenticating to your listener — the cornerstone of unconstrained/relay abuse chains.

**When:** Coerce an authorized target machine account to authenticate to your relay/responder in lab environments for relay and delegation abuse scenarios.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/decoder-it/printerbugnew && python3 printerbug.py domain/user:pass@target attacker_ip`

**URL:** https://github.com/decoder-it/printerbugnew

**Alternatives:** SpoolSample, PetitPotam


##### SpoolSample

The original MS-RPRN spoolsv.exe abuse PoC that forces a target to authenticate back to you, historically tuned for unconstrained delegation attacks.

**When:** Lab-only coercion lab where you want the original Windows-side compiled spooler-sampler reference implementation.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/leechristensen/SpoolSample && build with Visual Studio`

**URL:** https://github.com/leechristensen/SpoolSample

**Alternatives:** printerbug.py






## Legacy Attack Labs (PoC repos — lab only)




#### Critical CVE PoCs



##### Zerologon PoC (CVE-2020-1472) ⭐

Dirkjanm's canonical PoC for the Zerologon Netlogon cryptographic bypass that resets a DC machine-account password to empty and allows Domain-Admin takeover.

**When:** Practice reproducing a fully-patched-against critical flaw in an isolated lab domain controller only; restore passwords immediately as in dirkjanm's reinstall/restore flow.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dirkjanm/CVE-2020-1472 && pip3 install -r requirements.txt (lab VMs only)`

**URL:** https://github.com/dirkjanm/CVE-2020-1472

**Alternatives:** PetitPotam


##### PetitPotam

EFS-prone authentication coercion PoC (CVE-2021-36942) that forces a Windows host to authenticate to your listener via the Encrypting File System RPC — enabling relay to LDAP-based DC-auth abuse.

**When:** Lab demonstrations of EFS-based coercion and NTLM relay to LDAP(S) signing; SMB signing and LDAP channel-binding mitigations should be validated as the control.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/topotam/PetitPotam && python3 PetitPotam.py attacker_ip target (lab only)`

**URL:** https://github.com/topotam/PetitPotam

**Alternatives:** printerbug.py, Zerologon PoC (CVE-2020-1472)


#### NTLMv1 downgrade & legacy protocol testing



##### smbclient (NTLMv1 dialect) ⭐

Samba's authenticated SMB client whose `-m NT1` mode forces the legacy NTLMv1/RC4 dialect, making it a quick probe for whether a host still accepts NTLMv1.

**When:** Lab-only check that a test host rejects NTLMv1 (LanMan-compat) as configured, or proving a downgrade lane in an isolated test environment.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `apt-get install -y smbclient`

**URL:** https://www.samba.org/samba/docs/current/man-html/smbclient.1.html

**Alternatives:** Responder






## GPO & ACL Exploitation Tooling




#### ACL analysis & abuse



##### ADACLScanner ⭐

the SysArc ADACL scanner that reports dangerous ACL entries — GenericAll/WriteDacl/WriteOwner/ForceChangePassword — across domain, OUs, groups, and users in readable HTML.

**When:** Read-only ACL risk sweep of your own domain to find object-owner and self-abuse-style issues before an attacker graphs them.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/canix1/ADACLScanner && .\ADACLScan.ps1 from a domain-joined Windows host`

**URL:** https://github.com/canix1/ADACLScanner

**Alternatives:** Impacket dacledit, BloodHound CE


##### Impacket dacledit

Impacket example script that leverages a control-established object ace (WriteDACL/WriteOwner/GenericAll) to edit target ACLs — including adding a full-control ACE for the attacker.

**When:** Step through shelf ACL-abuse chains in a lab — the standard 'I own the ACE, so I own this object' proof step.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** ADACLScanner


#### Group Policy abuse



##### SharpGPOAbuse ⭐

C# tool that edits GPO DACLs you already control to add immediate scheduled tasks, services, or registry changes — the standard Writeable-GPO machine-takeover primitive (kept alive by the ReversecLabs mirror).

**When:** Demonstrate the impact of writable GPOs in authorized tests once a user holds a GPO-modify privilege; roll back the GPO after testing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ReversecLabs/SharpGPOAbuse && dotnet build (or run a compiled release binary)`

**URL:** https://github.com/ReversecLabs/SharpGPOAbuse

**Alternatives:** pyGPOAbuse, PowerView (Get-GPO)


##### pyGPOAbuse

Hackndo's Python port that adds an immediate scheduled task to a writable GPO from Linux, mirroring SharpGPOAbuse without a Windows binary.

**When:** GPO-edit proof from a Linux foothold during authorized multi-step chain construction in labs.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/Hackndo/pyGPOAbuse && python3 gpoabuse.py -d domain -u user -p pass ...`

**URL:** https://github.com/Hackndo/pyGPOAbuse

**Alternatives:** SharpGPOAbuse






## Credential-Access Testing




#### LSASS & memory credential access



##### Mimikatz ⭐

The canonical Windows credential tool: `sekurlsa` extracts plaintext passwords, NTLM hashes, PINs, and Kerberos tickets from LSASS memory while `lsadump` covers SAM, LSA secrets, DCSync, and DCShadow.

**When:** On an authorized host with local admin to prove whether LSASS-accessible credentials leak and whether protections like LSA Protection or Credential Guard actually hold.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download prebuilt binaries from https://github.com/gentilkiwi/mimikatz/releases`

**URL:** https://github.com/gentilkiwi/mimikatz

**Alternatives:** pypykatz, lsassy


##### pypykatz

Pure-Python reimplementation of Mimikatz's sekurlsa that parses live LSASS memory or minidumps on any OS to recover NT hashes, plaintext credentials, Kerberos tickets, and DPAPI keys.

**When:** Analyze an LSASS minidump from Linux during incident-response or assessment when you hold the dump rather than a live Windows host.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install pypykatz`

**URL:** https://github.com/skelsec/pypykatz

**Alternatives:** Mimikatz


##### lsassy

Python tool that remotely dumps LSASS (comsvcs, Procdump, nanodump, and more methods) over SMB/WMI from whole fleets and extracts credentials in place with pypykatz.

**When:** When you hold admin on an authorized set of Windows hosts and want to audit logged-on credential exposure across the fleet without interactive sessions.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install lsassy`

**URL:** https://github.com/login-securite/lsassy

**Alternatives:** Mimikatz, pypykatz


#### Remote domain-credential extraction



##### Impacket secretsdump ⭐

Impacket's flagship script that remotely extracts SAM/LSA/DRSUAPI/NTDS passwords and hashes in mimikatz-compatible format over DCOM, registry, and hypothetical replication.

**When:** The standard authorized way to audit password-hash hygiene on DCs and hosts from Linux — directory-replication rights permitting.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** lsassy, Mimikatz






## PowerShell Scripted Enumeration




#### AD recon cmdlets



##### PowerView ⭐

Pure-PowerShell AD enumerator (PowerSploit) turning LDAP into one-liner cmdlets for users, groups, computers, GPOs, ACLs, shares, and trust maps; also hunts which machines specific users log into.

**When:** From a domain-joined PowerShell session when you need fast, scriptable situational awareness without dropping a binary on disk — and to see exactly what attackers enumerate first.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/PowerShellMafia/PowerSploit && Import-Module .\Recon\PowerView.ps1`

**URL:** https://github.com/PowerShellMafia/PowerSploit

**Alternatives:** adPEAS, BloodHound.py


#### Local privilege-escalation auditing



##### PowerUp ⭐

PowerSploit module that audits a Windows host for common local privesc misconfigurations — unquoted service paths, writable service binaries, modifiable services, AlwaysInstallElevated — with abuse-ready detail.

**When:** Local privilege-escalation audit of a single host during sanctioned testing or hardening a fleet that lacks LAPS and least-privilege discipline.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/PowerShellMafia/PowerSploit && Import-Module .\Privesc\PowerUp.ps1`

**URL:** https://github.com/PowerShellMafia/PowerSploit

**Alternatives:** PowerView






## Blue-Team Visibility & Lab Hardening




#### Local admin password (LAPS) hygiene



##### LAPSToolkit ⭐

Leoloobeek's PowerShell suite that audits LAPS-deployed estates — enumerating computers with expired/missing passwords, readable LAPS attributes, and delegations that expose admin passwords.

**When:** Verify LAPS coverage and that delegation groups can't read passwords, before attackers abuse unexpired or overly-broad LAPS delegation.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/leoloobeek/LAPSToolkit && .\LAPSToolkit.ps1 (Windows LAPS also ships as built-in AD/Entra policy tooling)`

**URL:** https://github.com/leoloobeek/LAPSToolkit

**Alternatives:** ADRecon, PingCastle


#### AD health & risk scoring



##### PingCastle ⭐

Active Directory risk and maturity audit (by Netwrix) that scores a domain 0–100 across ~10 axes — accounts, ADCS, Kerberos, trusts, delegation, GPOs, infrastructure — with a CISO-ready HTML report via read-only healthcheck.

**When:** The default first formal AD security assessment: minutes to run, zero writes, ideal as a recurring blue-team health check or engagement kickoff.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download standalone PingCastle.exe from https://github.com/netwrix/pingcastle/releases and run on a domain-joined Windows host (.NET 8)`

**URL:** https://github.com/netwrix/pingcastle

**Alternatives:** Purple Knight, ADRecon


##### ADRecon

PowerShell tool that extracts a wide slice of AD state — users, groups, OUs, GPOs, trusts, ACLs, password policies, DNS zones, optionally LAPS/BitLocker keys and Kerberoastable SPNs — into a summary Excel workbook.

**When:** Broad read-only documentation of an environment for audit reports; runs as an ordinary domain user and works from non-member hosts over LDAP.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/adrecon/ADRecon && .\ADRecon.ps1 on a Windows host`

**URL:** https://github.com/adrecon/ADRecon

**Alternatives:** PingCastle, ADACLScanner





