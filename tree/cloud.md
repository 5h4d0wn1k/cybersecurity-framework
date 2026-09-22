# ☁️ Cloud Security — AWS, Azure & GCP

Posture, offense, and public-bucket checks across AWS, Azure, and GCP — for auditing your own accounts and sanctioned assessments.

## Cloud Posture & Compliance Audit

### Prowler ⭐

Runs 1,000+ read-only checks across AWS, Azure, and GCP against CIS Benchmarks and 70+ compliance frameworks, with remediation guidance per finding.

**When:** Kick off the posture review of any account you own; it is the default for CIS/NIST alignment across all three clouds and exposes findings via CLI or API.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** Scout Suite, CloudSploit


### Scout Suite

NCC Group's multi-cloud auditor pulls configuration from provider APIs and renders a browsable point-in-time HTML report of risk areas for AWS, Azure, and GCP.

**When:** When you want a clean visual report of config risk in one account as a second opinion alongside Prowler; last major release was 2022.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** Prowler, CloudSploit


### CloudSploit

Aqua-maintained Node.js CSPM scanner for AWS, Azure, GCP, OCI, and GitHub misconfigurations with CIS/PCI/HIPAA compliance modes; also sold as the hosted Aqua Wave SaaS.

**When:** Use the self-hosted scanner for broad multi-cloud config checks in CI; know that the actively maintained commercial route is the hosted Aqua Wave platform.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/aquasecurity/cloudsploit.git && cd cloudsploit && npm install`

**URL:** https://github.com/aquasecurity/cloudsploit

**Alternatives:** Prowler, Scout Suite


## AWS Offense — Enumeration & Privilege Escalation

### Pacu ⭐

The AWS exploitation framework: modular post-compromise attacks covering IAM privilege escalation, Lambda backdoors, log tampering, and EC2 RCE, with a session database for clean reporting.

**When:** After you hold valid-but-least-privilege AWS keys and want to demonstrate what an attacker could escalate to; the offensive complement to Prowler on your own account.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install -U pacu`

**URL:** https://github.com/RhinoSecurityLabs/pacu

**Alternatives:** CloudFox, enumerate-iam, IAMActionHunter


### CloudFox

Bishop Fox's situational-awareness enumerator maps exploitable attack paths across AWS (34 commands) plus early Azure/GCP coverage, writing loot files for other tools.

**When:** Run `cloudfox aws --profile X all-checks` first on any fresh AWS scope to learn the estate and spot privesc paths before deeper exploitation with Pacu.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/BishopFox/cloudfox@latest`

**URL:** https://github.com/BishopFox/cloudfox

**Alternatives:** Pacu, enumerate-iam, IAMActionHunter


### enumerate-iam

Brute-forces every read-only AWS API call against a credential set to print exactly which IAM permissions it holds.

**When:** You recovered AWS keys of unknown privilege and need the permission list fast, before choosing an escalation path.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/andresriancho/enumerate-iam.git && cd enumerate-iam && pip3 install -r requirements.txt`

**URL:** https://github.com/andresriancho/enumerate-iam

**Alternatives:** IAMActionHunter, CloudFox


### IAMActionHunter

Collects and queries AWS IAM policy statements to surface users and roles holding privesc-relevant permissions (iam:create*, iam:put*...) and exports CSV; also ships as a Pacu module.

**When:** Hunt least-privilege violations and privilege-escalation levers across a large account in minutes, then review the CSV.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install iamactionhunter`

**URL:** https://github.com/RhinoSecurityLabs/IAMActionHunter

**Alternatives:** enumerate-iam, Pacu


## Azure Offense — Discovery, Graph & Post-Exploitation

### MicroBurst ⭐

NetSPI's PowerShell toolkit for attacking Azure: service discovery, weak-config auditing, credential dumping (AzPasswords), and post-exploitation on VMs, Key Vault, and Automation accounts.

**When:** The default Azure toolkit in authenticated engagements; Windows-only, so run it from a PowerShell host with the Az modules installed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/MicroBurst.git && Import-Module .\MicroBurst.psm1`

**URL:** https://github.com/NetSPI/MicroBurst

**Alternatives:** Stormspotter, ATEAM


### Stormspotter

Microsoft Azure Red Team's attack-graph tool: collects subscription and ARM resources into Neo4j and renders the attack surface with pivot opportunities.

**When:** Map a large tenant visually and find cross-resource pivot paths once you hold reader-level access.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Azure/Stormspotter && docker-compose up`

**URL:** https://github.com/Azure/Stormspotter

**Alternatives:** MicroBurst, ATEAM


### ATEAM

NetSPI's unaudited reconnaissance tool probes name permutations across App Services, Key Vault, Storage, DevOps, SharePoint, and Databricks to discover Azure resources and attribute their tenant IDs.

**When:** From outside, discover forgotten Azure resources whose names leak a tenant — ideal for attack-surface checks on your own domains before logging in.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/ATEAM.git && cd ATEAM && pip3 install -r requirements.txt`

**URL:** https://github.com/NetSPI/ATEAM

**Alternatives:** MicroBurst


## GCP Offense — Credential Scoping & Privilege Escalation

### gcp-scanner ⭐

Google's scanner determines what a compromised credential can reach across GCE, GCS, GKE, Cloud SQL, BigQuery, KMS, and more, pulling from VM metadata, SA keys, or OAuth tokens.

**When:** Assess blast radius after a leaked service account key or compromised VM, without needing gcloud installed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install gcp_scanner`

**URL:** https://github.com/google/gcp_scanner

**Alternatives:** gcpwn, GCP IAM Privilege Escalation


### GCP IAM Privilege Escalation

Rhino's documented GCP IAM privesc methods plus a scanner (enumerate_member_permissions.py then check_for_privesc.py) that flags principals able to escalate.

**When:** Audit who in your projects could privilege-escalate to org ownership and validate hardened role design.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation.git`

**URL:** https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation

**Alternatives:** gcp-scanner, gcpwn


### gcpwn

NetSPI's GCP and Workspace pentesting framework: enumerates and downloads project data, builds BloodHound OpenGraph models, and bundles credential and exploit tooling.

**When:** Deep GCP/Workspace engagements where you want structured enumeration feeding BloodHound-style attack-path analysis.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/gcpwn.git`

**URL:** https://github.com/NetSPI/gcpwn

**Alternatives:** gcp-scanner


## Public Bucket & Object-Storage Scan

### S3Scanner ⭐

Scans lists of bucket names across AWS and S3-compatible stores (GCP, DigitalOcean, Linode, Scaleway) for existence, tests every permission path for misconfigurations, and can enumerate or dump objects.

**When:** Find your own exposed buckets at scale: feed candidate names, get back which are public, listable, or readable.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/sa7mon/s3scanner@latest`

**URL:** https://github.com/sa7mon/S3Scanner

**Alternatives:** GCPBucketBrute, CloudFox (aws-offense)


### GCPBucketBrute

Enumerates Google Storage buckets from keyword permutations and reports per-bucket access, flagging public, writable, and privilege-escalation-prone buckets (storage.buckets.setIamPolicy).

**When:** Check which of your GCS buckets are reachable or writable without auth, including permission escalations visible from a service account.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/RhinoSecurityLabs/GCPBucketBrute.git && cd GCPBucketBrute && pip3 install -r requirements.txt`

**URL:** https://github.com/RhinoSecurityLabs/GCPBucketBrute

**Alternatives:** S3Scanner

