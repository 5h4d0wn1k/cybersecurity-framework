# 🎯 Red Team Infrastructure & Operations

Authorized red team tooling: offensive toolkits, operations & reporting, emulation replays, objectives, pivoting, and practice labs.

## Offensive Toolkits




#### Protocol & Network Toolkits



##### Impacket ⭐

Fortra's Python suite for network protocols: SMB/RPC/DCOM/WinRM/Kerberos plus the canonical example scripts (secretsdump, psexec, wmiexec, ntlmrelayx, GetADUsers) for credential harvesting and lateral movement.

**When:** The workhorse of Windows-lab lateral movement and credential extraction during authorized tests — and the tooling blue teams build artifacts for.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** netexec, responder


##### NetExec

The maintained successor to CrackMapExec: multi-protocol (SMB/WinRM/LDAP/MSSQL/SSH) networked exploitation toolkit with a plugin system and MCP integration.

**When:** Fast credential-spraying and share/deployment outreach across a Windows estate in an authorized engagement or AD lab.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pipx install netexec`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** impacket


##### Responder

lgandx's LLMNR/NBT-NS/mDNS responder that answers name-resolution queries on a test segment to reveal legacy protocol reliance and gather hashes for offline cracking.

**When:** In a lab or scoped internal test with an explicit rule of engagement, to demonstrate why legacy name-resolution protocols must be disabled.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/lgandx/Responder.git`

**URL:** https://github.com/lgandx/Responder

**Alternatives:** impacket, netexec


#### Post-Exploitation Libraries



##### PowerSploit ⭐

PowerShellMafia's PowerShell post-exploitation framework (CodeExecution, Recon, Exfiltration, Persistence, Privesc modules). Archived since 2021, yet it remains the canonical documented corpus of PowerShell tradecraft and a rich set of well-known signatures to exercise.

**When:** Studying classic PowerShell post-exploitation module patterns and testing AMSI/logging detections against well-known tool output.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/PowerShellMafia/PowerSploit.git`

**URL:** https://github.com/PowerShellMafia/PowerSploit

**Alternatives:** sharpsploit, nishang


##### SharpSploit

cobbr's C# post-exploitation library — the compiled mirror of PowerSploit-style tradecraft (execution, persistence, lateral movement, credentialing) for .NET agents.

**When:** Reference for .NET-based post-exploitation modules and for training why compiled tooling changes the detection story.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/cobbr/SharpSploit.git`

**URL:** https://github.com/cobbr/SharpSploit

**Alternatives:** powersploit, nishang


##### Nishang

samratashok's collection of PowerShell scripts (reverse shells, keylogging, persistence, scanners) that has historically driven entry-level and small-scope authorized testing.

**When:** Quick PowerShell payload/auxiliary scripts in a Windows lab without dragging in a full framework.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/samratashok/nishang.git`

**URL:** https://github.com/samratashok/nishang

**Alternatives:** powersploit


#### Knowledge Bases



##### PoC Feeds



###### PoC-in-GitHub ⭐

nomi-sec's curated index tracking the latest public proof-of-concept exploits by CVE, with cross-references to Exploit-DB, Metasploit, and Nuclei templates.

**When:** Keep a lab exploitation pipeline current: pull fresh, citation-tracked PoCs to evaluate and adapt in authorized testing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/git)`

**URL:** https://github.com/nomi-sec/PoC-in-GitHub

**Alternatives:** ired-team, hacktricks


##### Field Notes



###### ired.team ⭐

The 'red team notes & experiments' GitBook by @spotheplanet — a structured walkthrough of offensive techniques (code execution, injection, persistence, lateral movement) with tool usage and detection notes, documented for education.

**When:** Read-and-try technique references while building your own lab; the notes pair each experiment with what to look for from a defender's seat.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://ired.team

**Alternatives:** hacktricks, poc-in-github


###### HackTricks

The community wiki of pentesting techniques across web, Windows, Linux, AD, and cloud with tooling recipes and methodology — now maintained as the HackTricks-wiki GitBook project, runnable locally via Docker.

**When:** Look up a technique or methodology in seconds; the most current single reference for esoteric protocol abuse and tool recipes.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)  # or: docker run -p 3337:3000 ghcr.io/hacktricks-wiki/hacktricks-cloud/translator-image`

**URL:** https://github.com/HackTricks-wiki/hacktricks

**Alternatives:** ired-team, poc-in-github






## Operations & Reporting Platforms

RedEye ⭐


#### RedEye ⭐

CISA + PNNL's visual analytic for red-team operations: parses Cobalt Strike and other C2 logs, renders the multi-host attack graph, and supports 'campaign' export for blue-team handoff. Archived to maintenance mode — still the reference for C2 log visualization.

**When:** Turn raw C2 logs into a shareable, annotated attack-path visualization to debrief stakeholders after an assessment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the RedEye binary from https://github.com/cisagov/RedEye/releases`

**URL:** https://github.com/cisagov/RedEye

**Alternatives:** ghostwriter


#### Ghostwriter

SpecterOps' open-source web application for red-team operations: client tracking, report writing, engagement documents (report templates, infographics), and evidence storage in one place.

**When:** Run the operational/admin side of a red-team engagement — consistent client documentation, task tracking, and report generation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/GhostManager/Ghostwriter.git && cd Ghostwriter && docker compose up`

**URL:** https://github.com/GhostManager/Ghostwriter

**Alternatives:** redeye, pwndoc


#### PwnDoc

Operational reporting tool for keeping engagement notes, screenshots, and CVE references organized, with generated report templates for pentest deliverables.

**When:** Structure and export aggregated findings and evidence into a client-ready report during or right after an engagement.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker pull pwndoc/pwndoc`

**URL:** https://github.com/pwndoc/pwndoc

**Alternatives:** ghostwriter, writehat


#### WriteHat

Black Lantern Security's full-stack Python pentest reporting server with a Django admin and WeasyPrint pipeline that turns structured findings into polished PDF reports.

**When:** Generate clean PDF deliverables from structured findings without hand-assembling Word templates.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/blacklanternsecurity/writehat.git`

**URL:** https://github.com/blacklanternsecurity/writehat

**Alternatives:** pwndoc, ghostwriter






## Emulation & Replay Engines

MITRE Caldera ⭐


#### MITRE Caldera ⭐

Apache Caldera: automated adversary-emulation platform that deploys agents and replays ATT&CK-mapped abilities, letting you re-run a campaign end-to-end and capture artifacts on each pass.

**When:** Replay the same emulated operation repeatedly after detection changes and measure which signals fire each run.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone --recursive https://github.com/apache/caldera.git`

**URL:** https://github.com/apache/caldera

**Alternatives:** attack-flow, vectr


#### MITRE Attack Flow

Center for Threat-Informed Defense's STIX-based model and toolchain for linking individual ATT&CK techniques into the flow of a full campaign.

**When:** Document an entire emulated campaign — not isolated techniques — so reporting shows the attack path from initial access to objective.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/center-for-threat-informed-defense/attack-flow.git`

**URL:** https://github.com/center-for-threat-informed-defense/attack-flow

**Alternatives:** mitre-caldera, vectr






## Objectives & Planning

VECTR ⭐


#### VECTR ⭐

Security Risk Advisors' free platform for tracking red/blue test cases and campaign outcomes against MITRE ATT&CK, trending detection coverage over time.

**When:** Capture objectives and results for each engagement and trend coverage improvements across your program.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/SecurityRiskAdvisors/VECTR.git`

**URL:** https://github.com/SecurityRiskAdvisors/VECTR

**Alternatives:** attack-navigator


#### MITRE ATT&CK Navigator

Web UI for annotating and exploring ATT&CK matrices with shareable layer files — the standard way to plan and communicate engagement objectives.

**When:** Scope an engagement by marking intended technique coverage, then save the layer for the reporting phase.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://github.com/mitre-attack/attack-navigator

**Alternatives:** vectr, mitre-attack


#### MITRE ATT&CK

The authoritative knowledge base of adversary tactics, techniques, and data sources — the shared vocabulary for defining engagement objectives.

**When:** Resolve technique IDs and constraints before planning, and align each engagement's objectives to the matrix.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web)`

**URL:** https://attack.mitre.org

**Alternatives:** attack-navigator






## Practice Labs




#### Active Directory Labs



##### GOAD ⭐

Orange Cyberdefense's 'Game of Active Directory' (v3): a vulnerable multi-forest AD lab built with Vagrant/Ansible/Packer, with GOAD-Light and other variants for smaller hardware.

**When:** An isolated, purpose-built AD domain range for rehearsing the attack paths your toolkits will run in authorized tests.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/Orange-Cyberdefense/GOAD.git`

**URL:** https://github.com/Orange-Cyberdefense/GOAD

**Alternatives:** badblood, metasploitable3


##### BadBlood

Secframe's PowerShell script that fills a lab AD domain with thousands of randomized users, groups, computers, OUs, and ACLs so lab data resembles a real enterprise.

**When:** Before practicing enumeration and credential techniques, populate an otherwise empty DC to get realistic object counts and permissions.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/davidprowe/BadBlood.git`

**URL:** https://github.com/davidprowe/BadBlood

**Alternatives:** goad


#### Training Ranges & VMs



##### Metasploitable 3 ⭐

Rapid7's intentionally vulnerable Windows VM (Vagrant/Packer) packed with unpatched services, weak creds, and web/SMB flaws — a standard target for rehearsing toolkits and C2 staging.

**When:** A reproducible target for lateral-movement and exploitation run-throughs in an isolated VirtualBox/VMware range.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/rapid7/metasploitable3.git`

**URL:** https://github.com/rapid7/metasploitable3

**Alternatives:** vulnhub, goad


##### VulnHub

Library of intentionally vulnerable virtual machines and walkthroughs for practicing the full exploratory-to-root workflow at low hardware cost.

**When:** Practice methodology and tooling against curated vulnerable VMs before applying them to authorized targets.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.vulnhub.com

**Alternatives:** metasploitable3






## Pivoting & Tunnels

sshuttle ⭐


#### sshuttle ⭐

Lightweight VPN-like pivot using SSH; routes traffic through a jump host without requiring root on the target.

**When:** Need simple, reliable lateral routing to access internal networks from a single jump host during authorized engagements or labs.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install sshuttle`

**URL:** https://github.com/sshuttle/sshuttle

**Alternatives:** frp, chisel


#### frp

Fast reverse proxy for exposing local services through a remote server; stable and well-documented.

**When:** Need controlled reverse proxying for lab infrastructure or authorized test setups behind NAT.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/fatedier/frp@latest`

**URL:** https://github.com/fatedier/frp

**Alternatives:** sshuttle


#### proxychains-ng

Force any TCP application through a chain of proxies for controlled routing in authorized testing.

**When:** Need to route existing tooling through a proxy chain during authorized red team exercises or lab scenarios.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/rofl0r/proxychains-ng && cd proxychains-ng && ./configure --prefix=/usr && make && sudo make install`

**URL:** https://github.com/rofl0r/proxychains-ng

**Alternatives:** sshuttle





