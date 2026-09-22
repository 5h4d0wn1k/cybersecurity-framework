# 🔒 System Hardening, Compliance & Secure Configuration

Audit, harden, and prove it: system security scans, compliance benchmarks, config automation, and network-service lockdown for defenders securing their own systems.

## Linux & UNIX Host Hardening



#### System Auditing & Compliance Scans


##### Lynis ⭐

Agentless security-auditing tool for Linux, BSD, and macOS that runs 200+ checks across the whole OS, scores everything, and ends with a hardening index, disclosure status, and actionable remediation hints.

**When:** First pass on any UNIX-like host you own — run a baseline audit, apply the suggestions, then re-run to watch the hardening index climb.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install lynis`

**URL:** https://github.com/CISOfy/lynis

**Alternatives:** openscap, auditd


##### OpenSCAP

NIST-certified SCAP 1.2 toolkit: loads security content (XCCDF/OVAL data streams) and evaluates or remediates a system against specific profiles from the command line.

**When:** Repeatable, scriptable compliance evaluations against scap-security-guide content — the profile kills long manual audit checklists.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install openscap-scanner`

**URL:** https://github.com/OpenSCAP/openscap

**Alternatives:** scap-security-guide, lynis


##### auditd (Linux Audit)

Linux Audit framework userspace (auditd, auditctl, ausearch) recording privileged actions, file access, and security-relevant events to an immutable log across reboots.

**When:** Build the audit trail that CIS/STIG rules require before the auditor arrives; verify live rules with auditctl -l and query with ausearch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install auditd`

**URL:** https://github.com/linux-audit/audit-userspace

**Alternatives:** lynis, openscap


##### CIS Ubuntu Linux Benchmark

Free CIS configuration guide for Ubuntu with scored and unscored hardening entries that scanners and auditors measure against.

**When:** Hand-harden an Ubuntu/Debian-family host to a known-good baseline when no CIS-CAT scan is available.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://www.cisecurity.org/benchmark/ubuntu_linux

**Alternatives:** lynis, openscap


#### SELinux Policy & MAC Management


##### audit2allow ⭐

Core utility from policycoreutils that converts SELinux AVC denials from the audit log into targeted allow or dontaudit policy modules.

**When:** See denials in journal/AVC logs and turn the desired ones into a proper local policy module instead of disabling SELinux.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install policycoreutils`

**URL:** https://github.com/SELinuxProject/selinux

**Alternatives:** setools, selinux-refpolicy


##### SETools

SELinux Project's policy analysis suite: seinfo, sesearch, sediff, sedta, seinfoflow, and the apol GUI for querying rules and information-flow in the installed policy.

**When:** Reverse-engineer or audit what your SELinux policy actually allows between domains before writing new modules.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install setools`

**URL:** https://github.com/SELinuxProject/setools

**Alternatives:** audit2allow, selinux-refpolicy


##### SELinux Reference Policy

The community-maintained reference policy source tree that generated distributions extend; the base for understanding and building custom SELinux policy.

**When:** Contribute to or build custom policy from source, or learn the module structure behind your distro's policy.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/SELinuxProject/refpolicy.git`

**URL:** https://github.com/SELinuxProject/refpolicy

**Alternatives:** setools, audit2allow


#### Network Services Configuration


##### Host Firewalls


###### ufw ⭐

Ubuntu's uncomplicated frontend over iptables: allow/deny rules for ports and services in a few commands, with sane IPv6 defaults and a status view.

**When:** Simple proven host firewall on Debian/Ubuntu; default-deny inbound, allow only what a service genuinely needs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install ufw`

**URL:** https://launchpad.net/ufw

**Alternatives:** firewalld, nftables


###### firewalld

Dynamic firewall daemon with zone-based policy, a D-Bus service API, and runtime-vs-permanent config separation; the default firewall manager on RHEL/CentOS/Fedora/SUSE.

**When:** Host firewalling on RHEL-family systems: open only the services a zone needs and test in runtime before committing permanently.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install firewalld`

**URL:** https://firewalld.org

**Alternatives:** ufw, nftables


###### nftables

Netfilter's modern packet-filtering framework with a single, scriptable ruleset language that replaces iptables chains; the base engine ufw/firewalld sit on.

**When:** Write a compact, atomic, version-controllable firewall ruleset for servers that need more control than ufw offers.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install nftables`

**URL:** https://netfilter.org/projects/nftables/

**Alternatives:** ufw, firewalld


##### SSH Hardening


###### ssh-audit ⭐

Audits SSH server and client configuration end-to-end: grades every KEX, cipher, MAC, and host-key algorithm, flags weak or vulnerable combos, and ships per-distro hardening guides.

**When:** Audit sshd before changing anything, apply the printed hardening guide, then re-scan until all-secure.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install ssh-audit`

**URL:** https://github.com/jtesta/ssh-audit

**Alternatives:** mozilla-openssh-config


###### Mozilla OpenSSH Configuration

Reference hardening guide for sshd_config with Modern/Intermediate/MFA profiles and concrete HostKey, KEX, cipher, and MAC lists for each OpenSSH generation.

**When:** Write a known-good SSH baseline, then confirm the result with ssh-audit.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web reference)`

**URL:** https://infosec.mozilla.org/guidelines/openssh

**Alternatives:** ssh-audit



## Windows Hardening



#### Hardening Tools & Local Policy


##### HardeningKitty ⭐

PowerShell tool that retrieves the current Windows configuration, assesses it against CIS Benchmarks, Microsoft baselines, STIG, and BSI guides, and can apply settings itself (HailMary mode).

**When:** Automated CIS/Microsoft-baseline audit of Windows endpoints with minimal setup and a CSV scorecard.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/scipag/HardeningKitty.git && Import-Module .\HardeningKitty.psm1`

**URL:** https://github.com/scipag/HardeningKitty

**Alternatives:** lgpo, cis-microsoft-windows-benchmark


##### LGPO.exe

Microsoft's local group-policy utility (shipped in the Security Compliance Toolkit) that imports/repairs registry.pol files and audits local policy settings.

**When:** Apply a downloaded security baseline GPO backup to standalone or non-domain machines and verify local policy compliance.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download from Microsoft Security Compliance Toolkit (55319)`

**URL:** https://www.microsoft.com/en-us/download/details.aspx?id=55319

**Alternatives:** hardeningkitty


#### Windows Baseline Guidance


##### CIS Microsoft Windows Benchmark ⭐

Free CIS configuration benchmark for Windows Server and client editions with scored and unscored hardening entries.

**When:** Know exactly which GPO/registry settings an auditor will check, and harden by hand when scanner licensing is unavailable.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://www.cisecurity.org/benchmark/microsoft_windows_desktop

**Alternatives:** microsoft-security-baselines, hardeningkitty


##### Microsoft Security Baselines

Microsoft's recommended security configuration settings curated from the Windows Security Configuration Framework, shipped as GPO backups ready for LGPO import.

**When:** Start from Microsoft's own baseline rather than writing group policy from scratch; the SCT download includes the LGPO import tooling.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (web docs)`

**URL:** https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines

**Alternatives:** cis-microsoft-windows-benchmark, lgpo



## Network Infrastructure Hardening



#### Vendor Device Hardening Guides


##### CIS Cisco IOS/XE Benchmark ⭐

CIS configuration benchmark covering Cisco IOS and IOS-XE: AAA, management-plane protection, SNMP, NTP, and platform-specific hardening entries.

**When:** Hardening Cisco routers/switches to a defensible baseline before a compliance scan or external assessment.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://www.cisecurity.org/benchmark/cisco

**Alternatives:** mikrotik-security-guide


##### MikroTik RouterOS Security Guide

RouterOS documentation covering access hardening, service lockdown, firewall filter rules, brute-force protection, and secure defaults for MikroTik devices.

**When:** Locking down MikroTik routers/switches you manage: follow the guide, restrict winbox/API, and add the recommended filter rules.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://help.mikrotik.com/docs/spaces/ROS/pages/328353/Securing+your+router

**Alternatives:** cis-cisco-benchmark, batfish


#### Device Config Validation


##### Batfish ⭐

Network configuration analyzer that parses real device configs and answers questions about reachability, ACLs, and announced routes without touching the network.

**When:** Validate that hardening changes (ACLs, filters, BGP policies) don't break intended reachability before pushing them.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -it batfish/allinone`

**URL:** https://github.com/batfish/batfish

**Alternatives:** cis-cisco-benchmark


#### TLS & Service Configuration Audit


##### testssl.sh ⭐

Command-line TLS checker that tests every cipher, protocol, certificate, and vulnerability (Heartbleed, ROBOT, BEAST, and friends) against a live endpoint and grades the config.

**When:** Audit the TLS posture of every service you expose before and after removing weak ciphers and protocols.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/drwetter/testssl.sh.git`

**URL:** https://github.com/drwetter/testssl.sh

**Alternatives:** sslscan


##### sslscan

Lightweight TLS/SSL scanner that enumerates supported ciphers, protocols, and certificate details using OpenSSL, ideal for scripting into pipeline checks.

**When:** Quick scriptable cipher/protocol inventory across many hosts when you only need raw output, not a full report.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install sslscan`

**URL:** https://github.com/rbsec/sslscan

**Alternatives:** testssl.sh



## Containers & Kubernetes Hardening



#### Image & Container Scanning


##### Trivy ⭐

Aqua's all-in-one scanner for OS packages, SBOMs, IaC misconfigs, and Kubernetes manifests/contexts; as a k8s subcommand it scans your cluster's deployed workload posture.

**When:** Scan container images in CI and scan the live cluster (trivy k8s) for image and config findings in one tool.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** kube-bench, checkov


#### Manifest & Policy Linting


##### kube-linter ⭐

StackRox's Kubernetes YAML checker with 50+ built-in lint checks for security anti-patterns such as privileged containers, runAsRoot, and host-network exposure.

**When:** Catch obvious YAML security anti-patterns in Git before charts reach the cluster.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install kube-linter`

**URL:** https://github.com/stackrox/kube-linter

**Alternatives:** checkov, kubesec


##### checkov

Bridgecrew/Prisma's policy-as-code scanner for Terraform, CloudFormation, Kubernetes, Helm, Dockerfile, and more, with 1000+ built-in checks including CIS Kubernetes.

**When:** Unified IaC-and-manifest scanning across your whole infrastructure-as-code estate in CI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install checkov`

**URL:** https://github.com/bridgecrewio/checkov

**Alternatives:** kube-linter, trivy


##### kubesec

Risk analysis tool that scores Kubernetes resources on 10+ security criteria (privileges, capabilities, runAsNonRoot) and returns a risk score with pointers.

**When:** Ten-second risk score for a single manifest before deploy or during review.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `docker run -i kubesec/kubesec scan /dev/stdin`

**URL:** https://github.com/controlplaneio/kubesec

**Alternatives:** kube-linter, checkov


#### Kubernetes CIS Benchmarking


##### kube-bench ⭐

Aqua's CIS Kubernetes Benchmark checker: audits control plane, etcd, worker nodes, and RBAC against the official benchmark, runnable as a DaemonSet or binary.

**When:** Prove your cluster meets the CIS Kubernetes benchmark and track remediation over time.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --pid=host -v /etc:/etc:ro aquasec/kube-bench:latest install`

**URL:** https://github.com/aquasecurity/kube-bench

**Alternatives:** kubescape, trivy


##### kubescape

ARMO's Kubernetes posture scanner covering NSA/CISA hardening guidance, MITRE ATT&CK, and 50+ frameworks, plus admission-controller enforcement of failed controls.

**When:** Full-framework posture scanning of a live cluster that goes beyond the CIS benchmark into runtime control enforcement.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install kubescape`

**URL:** https://github.com/kubescape/kubescape

**Alternatives:** kube-bench, kube-linter


#### Service Mesh & Network Policy


##### Istio ⭐

Service mesh providing mTLS between workloads, authorization policies (peer/request authentication), and encrypted east-west traffic for zero-trust workload identity.

**When:** Enforce workload-to-workload mTLS and least-privilege authorization policies in a cluster that already runs a mesh.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `curl -L https://istio.io/downloadIstio | sh -`

**URL:** https://istio.io/latest/docs/concepts/security/

**Alternatives:** cilium


##### Cilium

eBPF-based CNI that enforces identity-aware L3-L7 NetworkPolicies without sidecars, including encrypted traffic and observability at scale.

**When:** Enforce zero-trust network policy at the CNI layer when you don't want to adopt a full sidecar-based mesh.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `helm install cilium cilium/cilium --namespace kube-system`

**URL:** https://github.com/cilium/cilium

**Alternatives:** istio



## Cloud Configuration & Compliance



#### Cloud CIS Benchmarks


##### CIS Cloud Benchmarks ⭐

Free CIS benchmark sets for AWS, Azure, and GCP covering IAM, storage, networking, logging, and monitoring controls in each provider's console-accessible language.

**When:** Know which cloud console/service settings an auditor checks, provider by provider.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web docs)`

**URL:** https://www.cisecurity.org/benchmark/amazon_web_services

**Alternatives:** prowler, scoutsuite


#### Cloud Posture Scanning


##### Prowler ⭐

Runs 1,000+ read-only checks across AWS, Azure, and GCP against CIS Benchmarks and 70+ compliance frameworks, with remediation guidance per finding.

**When:** Default CIS/NIST posture review of any account you own; the coverage map and remediation pointers make fixing straightforward.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** scoutsuite, cis-cloud-benchmarks


##### Scout Suite

NCC Group's multi-cloud auditor pulls configuration from provider APIs and renders a browsable point-in-time HTML report of risk areas for AWS, Azure, and GCP.

**When:** A clean visual HTML report of config risk in one account as a second opinion alongside Prowler.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** prowler



## Compliance Benchmarks & Baseline Content



#### zerotrustmirror ◆ by 5h4d0wn1k

Zero-trust readiness engine — ZTA pillar scoring with evidence and multichannel correlation across your environment.

**When:** Measuring progress against NIST/CISA zero-trust pillars before rolling out changes.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/zerotrustmirror`

**URL:** https://github.com/5h4d0wn1k/zerotrustmirror

**Alternatives:** Own tool — lab/authorized use only


#### Benchmark & Baseline Content


##### scap-security-guide ⭐

OpenSCAP's official security content: prebuilt SCAP data streams with profiles for CIS, DISA STIG, PCI-DSS, and HIPAA, plus bundled bash and Ansible remediation scripts that apply the fixes.

**When:** Every compliance scan starts here — grab the data stream for your distro, feed it to openscap, review failures, then remediate with the generated scripts.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install scap-security-guide`

**URL:** https://github.com/OpenSCAP/scap-security-guide

**Alternatives:** cis-benchmarks, stig-viewer


##### CIS Benchmarks

Free, consensus-built configuration guides (PDF) for hundreds of OS, server, cloud, and application targets — the de-facto hardening standard auditors and scanners measure against.

**When:** Hand-hardening to a known-good baseline with no scanner available; open the benchmark PDF for your platform and apply the entries manually.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — free PDF download after registering a CIS account`

**URL:** https://www.cisecurity.org/cis-benchmarks

**Alternatives:** stig-viewer, scap-security-guide


##### STIG Viewer

Browser database of the entire DISA Security Technical Implementation Guide set — rule-by-rule requirements with severity, CCI/NIST 800-53 mappings, and concrete fix text.

**When:** Federal or DISA-style compliance: look up the exact configuration a STIG rule demands before touching config files.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.stigviewer.com

**Alternatives:** cis-benchmarks, scap-security-guide


#### Policy-as-Code Assessment


##### InSpec ⭐

Chef's open-source compliance language that turns CIS/STIG baselines into executable profile code (many public profiles exist) and runs them over local and remote systems.

**When:** Version-controllable, reusable compliance profiles that you run in CI or on-demand without a commercial scanner.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `gem install inspec-bin`

**URL:** https://github.com/inspec/inspec

**Alternatives:** cis-cat-pro, scap-security-guide


##### CIS-CAT Pro Assessor

Commercial CIS scanner (SecureSuite membership) that turns CIS Benchmarks into automated scans and compliance score/report output; a free CIS-CAT Lite covers a small set of select benchmarks.

**When:** Audits that must document conformance to a specific CIS Benchmark version with vendor-supported mapping and reporting.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (web) — SecureSuite member portal download`

**URL:** https://www.cisecurity.org/cybersecurity-tools/cis-cat-pro

**Alternatives:** inspec, openscap



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

**When:** Zero-install per-service hardening review on any systemd host — tighten the worst offenders on long-running units.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `preinstalled (systemd)`

**URL:** https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html

**Alternatives:** ansible-hardening, lynis


#### endpointaegis ◆ by 5h4d0wn1k

EDR-lite host-hardening auditor — 0-100 score, persistence/service/patch/socket audits, drift baselines, HTML+JSON reports.

**When:** Scoring and tracking host hardening across windows hosts/endpoints you manage.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/endpointaegis`

**URL:** https://github.com/5h4d0wn1k/endpointaegis

**Alternatives:** Own tool — lab/authorized use only



