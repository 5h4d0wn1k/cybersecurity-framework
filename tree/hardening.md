# 🔒 System Hardening, Compliance & Secure Configuration

Audit, harden, and prove it: system security scans, compliance benchmarks, config automation, and network-service lockdown for defenders securing their own systems.

## System Security Auditing & Compliance Scans

Lynis ⭐


#### Lynis ⭐

Agentless security-auditing tool for Linux, BSD, and macOS that runs 200+ checks across the whole OS, scores everything, and ends with a hardening index, disclosure status, and actionable remediation hints.

**When:** First pass on any UNIX-like host you own — run a baseline audit, apply the hardening suggestions, then run again to watch the hardening index climb.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install lynis`

**URL:** https://github.com/CISOfy/lynis

**Alternatives:** openscap, cis-cat pro assessor


#### OpenSCAP

NIST-certified SCAP 1.2 toolkit: loads security content (XCCDF/OVAL data streams) and evaluates or remediates a system against specific profiles from the command line.

**When:** Repeatable, scriptable compliance evaluations against scap-security-guide content — the profile kills long manual audit checklists.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install openscap-scanner`

**URL:** https://github.com/OpenSCAP/openscap

**Alternatives:** lynis, cis-cat pro assessor


#### CIS-CAT Pro Assessor

Commercial CIS scanner (SecureSuite membership) that turns CIS Benchmarks into automated scans and compliance score/report output; a free CIS-CAT Lite covers a small set of select benchmarks.

**When:** Audits that must document conformance to a specific CIS Benchmark version with vendor-supported mapping and reporting.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — SecureSuite member portal download`

**URL:** https://www.cisecurity.org/cybersecurity-tools/cis-cat-pro

**Alternatives:** openscap, lynis


#### auditd

Linux Audit framework userspace (auditd, auditctl, ausearch) recording privileged actions, file access, and security-relevant events to an immutable log across reboots.

**When:** Build the audit trail that CIS/STIG rules require before the auditor arrives; verify live rules with auditctl -l and query with ausearch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install auditd`

**URL:** https://github.com/linux-audit/audit-userspace

**Alternatives:** lynis






## Compliance Benchmarks & Baseline Content

scap-security-guide ⭐


#### scap-security-guide ⭐

OpenSCAP's official security content: prebuilt SCAP data streams with profiles for CIS, DISA STIG, PCI-DSS, and HIPAA, plus bundled bash and Ansible remediation scripts that actually apply the fixes.

**When:** Every compliance scan starts here — grab the data stream for your distro, feed it to openscap, review failures, then remediate with the generated scripts.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install scap-security-guide`

**URL:** https://github.com/OpenSCAP/scap-security-guide

**Alternatives:** cis benchmarks, stig viewer


#### CIS Benchmarks

Free, consensus-built configuration guides (PDF) for hundreds of OS, server, cloud, and application targets — the de-facto hardening standard that auditors and scanners measure against.

**When:** Hand-hardening a system to a known-good baseline with no scanner available; open the benchmark PDF for your platform and apply the entries manually.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — free PDF download after registering a CIS account`

**URL:** https://www.cisecurity.org/cis-benchmarks

**Alternatives:** stig viewer


#### STIG Viewer

Browser database of the entire DISA Security Technical Implementation Guide set — rule-by-rule requirements with severity, CCI/NIST 800-53 mappings, and concrete fix text.

**When:** Federal or DISA-style compliance: look up the exact configuration a STIG rule demands and its severity before touching config files.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.stigviewer.com

**Alternatives:** cis benchmarks






## Automated Hardening & Configuration

ansible-hardening ⭐


#### ansible-hardening ⭐

dev-sec's battle-tested Ansible collection (devsec.hardening) that hardens OS, SSH, nginx, and MySQL/MariaDB at scale, aligned with the InSpec baselines the same team maintains.

**When:** Apply the same hardening repeatedly to many hosts you manage — idempotent automation beats hand-editing configs on every box.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `ansible-galaxy collection install devsec.hardening`

**URL:** https://github.com/dev-sec/ansible-collection-hardening


#### systemd-analyze security

Built-in systemd command that scores each service unit 0-10 on exposure (PrivateTmp, NoNewPrivileges, ProtectSystem, and more) and lists the exact directives dragging the score down.

**When:** Zero-install per-service hardening review on any systemd host — run it on your long-running units and tighten the worst offenders.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (systemd)`

**URL:** https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html

**Alternatives:** ansible-hardening






## Network & Service Hardening

ssh-audit ⭐


#### ssh-audit ⭐

Audits SSH server and client configuration end-to-end: grades every KEX, cipher, MAC, and host-key algorithm, flags weak or vulnerable combos, and ships per-distro hardening guides.

**When:** Audit sshd before changing anything, apply the printed hardening guide, then re-scan until the tool reports all-secure.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install ssh-audit`

**URL:** https://github.com/jtesta/ssh-audit

**Alternatives:** mozilla openssh config


#### firewalld

Dynamic firewall daemon with zone-based policy, a D-Bus service API, and runtime-vs-permanent config separation; the default firewall manager on RHEL/CentOS/Fedora/SUSE.

**When:** Host firewalling on RHEL-family systems: open only the services a zone needs and test changes in runtime before committing them permanently.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install firewalld`

**URL:** https://firewalld.org

**Alternatives:** ufw


#### ufw

Ubuntu's uncomplicated frontend over iptables: allow/deny rules for ports and services in a few commands, with sane IPv6 defaults and a status view.

**When:** Simple proven host firewall on Debian/Ubuntu where firewalld is not the default; same job, less ceremony.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install ufw`

**URL:** https://launchpad.net/ufw

**Alternatives:** firewalld


#### Mozilla OpenSSH Config

Reference hardening guide for sshd_config and moduli with Modern/Intermediate/MFA profiles and concrete HostKey, KEX, cipher, and MAC lists for each OpenSSH generation.

**When:** Write a known-good SSH baseline — put the right profile block into /etc/ssh/sshd_config, then confirm the result with ssh-audit.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web reference)`

**URL:** https://infosec.mozilla.org/guidelines/openssh

**Alternatives:** ssh-audit





