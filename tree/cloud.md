# ☁️ Cloud Security — AWS, Azure & GCP

Posture audits, scoped offense, and public-bucket checks across AWS, Azure, and GCP — nested by provider and by function for your own accounts and sanctioned assessments.

## Cross-Cloud Posture & Offense



#### cloudpwn ◆ by 5h4d0wn1k

Cloud & container penetration suite — AWS/GCP/Azure enumeration, S3, docker leaks, k8s secrets, terraform audit, vault, CSPM.

**When:** Posture-testing your own cloud tenants and IaC repos.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/cloudpwn`

**URL:** https://github.com/5h4d0wn1k/cloudpwn

**Alternatives:** Own tool — lab/authorized use only


#### crownjewel ◆ by 5h4d0wn1k

Cross-cloud identity federation auditor — Golden/Silver SAML, OAuth client-ID spoofing, OIDC validation, cross-cloud token replay; offline fixtures.

**When:** Auditing federated identity trust boundaries across your clouds.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/crownjewel`

**URL:** https://github.com/5h4d0wn1k/crownjewel

**Alternatives:** Own tool — lab/authorized use only


#### Config & Compliance Auditors


##### Prowler ⭐

Runs 1,000+ read-only checks across AWS, Azure, and GCP against CIS Benchmarks and 70+ compliance frameworks, with remediation guidance per finding.

**When:** Kick off every posture review with it — the default for CIS/NIST alignment on any provider, driven via CLI, Docker, or the API.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** Scout Suite, CloudSploit (Trivy Cloud)


##### Scout Suite

NCC Group's multi-cloud auditor pulls configuration from provider APIs and renders a browsable point-in-time HTML report of risk areas for AWS, Azure, and GCP.

**When:** Grab a clean visual report of config risk as a second opinion alongside Prowler; expect a quiet repo — last major release was 2022.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** Prowler, CloudSploit (Trivy Cloud)


##### CloudSploit (Trivy Cloud)

Aqua's Node.js CSPM scanner covering AWS, Azure, GCP, OCI, and GitHub with CIS/PCI/HIPAA modes; actively developed as the open-source half of the hosted Aqua Trivy Cloud / Wave platform.

**When:** Broad self-hosted multi-cloud config checks in CI; know that the maintained commercial route is Aqua Trivy Cloud.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/aquasecurity/cloudsploit.git && cd cloudsploit && npm install`

**URL:** https://github.com/aquasecurity/cloudsploit

**Alternatives:** Prowler, Scout Suite


##### Steampipe

Run SQL queries over live AWS, Azure, GCP, and 200+ other APIs, then reuse the same queries for compliance benchmarks (CIS) and ad-hoc posture checks.

**When:** When you want scriptable, queryable posture evidence: SQL across your accounts beats shell-script loops and feeds reporting directly.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install turbot/tap/steampipe`

**URL:** https://github.com/turbot/steampipe

**Alternatives:** Prowler, AWS CLI & Batch Scripts


#### Offensive Validation (Scoped Labs)


##### Exploitation Frameworks


###### Pacu ⭐

The AWS exploitation framework: modular post-compromise attacks covering IAM privilege escalation, Lambda backdoors, log tampering, and EC2 RCE, with a session database for clean reporting.

**When:** After you hold valid-but-least-privilege AWS keys and want to demonstrate what an attacker could escalate to — lab/own-account use only.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install -U pacu`

**URL:** https://github.com/RhinoSecurityLabs/pacu

**Alternatives:** CloudFox, IAMActionHunter


###### CloudFox

Bishop Fox's situational-awareness enumerator maps exploitable attack paths across AWS (34 commands) plus early Azure/GCP coverage, writing loot files for other tools.

**When:** Run `cloudfox aws --profile X all-checks` first on any fresh scope to learn the estate and spot privesc paths before deeper exploitation with Pacu.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/BishopFox/cloudfox@latest`

**URL:** https://github.com/BishopFox/cloudfox

**Alternatives:** Pacu, enumerate-iam



## Amazon Web Services



#### Audit & Compliance Posture


##### Prowler (AWS) ⭐

Prowler pinned to AWS (`-p aws`): 300+ AWS-specific checks across CIS 1.x/2.x, NIST 800-53, and Well-Architected focus areas, with per-finding remediation and CSV/JSON/SARIF output.

**When:** The primary AWS compliance gate in CI or on a schedule; run alongside GuardDuty-focused triage for config findings.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** Scout Suite (AWS), cloud-inquisitor, Pacu


##### Scout Suite (AWS)

Scout Suite run with AWS credentials: point-in-time dumps of IAM, S3, EC2, and Security Group posture into a navigable HTML report annotated with risk rules.

**When:** Fast visual sweep of one AWS account when you want a self-contained report artifact to share, not another CLI table.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite && scout aws --profile prod`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** Prowler (AWS), Steampipe


##### cloud-inquisitor

Riot Games' config-audit and incident-response platform: scans accounts against custom rules, auto-remediates (e.g., open S3 buckets), and ships a web dashboard; only lightly maintained since 2021.

**When:** When you want rule-driven auto-remediation on legacy AWS estates and accept a quiet project — otherwise prefer Prowler or Steampipe.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/RiotGames/cloud-inquisitor.git && docker-compose up -d`

**URL:** https://github.com/RiotGames/cloud-inquisitor

**Alternatives:** Prowler (AWS), Steampipe


##### AWS CLI & Batch Scripts

The built-in `aws` CLI plus shell one-liners and jq pipelines for service inventory, bucket ACL listing, unused IAM keys, and cross-account drift — endless and dependency-free.

**When:** Quick targeted checks while Prowler/Steampipe are overkill: `aws iam list-access-keys --no-user-paginate`, `aws s3api get-bucket-acl`, etc.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install awscli`

**URL:** https://aws.amazon.com/cli/

**Alternatives:** Steampipe, CloudSploit (Trivy Cloud)


#### IAM & Permission Mapping


##### PMapper ⭐

NCC Group's Principal Mapper builds a graph of IAM users/groups/roles and their effective permissions, then computes shortest privilege-escalation and takeover paths.

**When:** Model least-privilege drift: generate the graph in minutes and query for principals reaching admin via any path.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install principalmapper`

**URL:** https://github.com/nccgroup/PMapper

**Alternatives:** IAMActionHunter, CloudFox


##### enumerate-iam

Brute-forces every read-only AWS API call against a credential set to print exactly which IAM permissions it holds.

**When:** You recovered AWS keys of unknown privilege and need the permission list fast, before choosing an escalation path.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/andresriancho/enumerate-iam.git && cd enumerate-iam && pip3 install -r requirements.txt`

**URL:** https://github.com/andresriancho/enumerate-iam

**Alternatives:** IAMActionHunter, CloudFox


##### IAMActionHunter

Collects and queries AWS IAM policy statements to surface users and roles holding privesc-relevant permissions (iam:create*, iam:put*...) and exports CSV; also ships as a Pacu module.

**When:** Hunt least-privilege violations and privilege-escalation levers across a large account in minutes, then review the CSV.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install iamactionhunter`

**URL:** https://github.com/RhinoSecurityLabs/IAMActionHunter

**Alternatives:** enumerate-iam, PMapper


#### Object Storage Misconfiguration


##### S3Scanner ⭐

Scans lists of bucket names across AWS and S3-compatible stores (GCP, DigitalOcean, Linode, Scaleway) for existence, tests every permission path for misconfigurations, and can enumerate or dump objects.

**When:** Find your own exposed buckets at scale: feed candidate names, get back which are public, listable, or readable.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install -v github.com/sa7mon/s3scanner@latest`

**URL:** https://github.com/sa7mon/S3Scanner

**Alternatives:** CloudFox



## Microsoft Azure



#### Benchmarks & Threat Research


##### Microsoft Cloud Security Benchmark (docs) ⭐

Microsoft's authoritative Azure security baseline: control families (identity, network, storage, data protection) with CSPM tooling guidance and mapping to NIST/CIS regulatory frameworks.

**When:** Your reference before running scanners — know which controls the tool checks and which ones Azure Policy/Defender must enforce, since no scanner covers a benchmark alone.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Reference guide — no install; mapped controls ship as built-in Azure Policy initiatives`

**URL:** https://learn.microsoft.com/en-us/security/benchmark/azure/introduction

**Alternatives:** Azure Threat Research Matrix


##### Azure Threat Research Matrix (ATRM)

MSTIC's community threat matrix documenting Azure/AWS/GCP attack vectors (reconnaissance, persistence, privilege escalation) with real examples and KQL hunting queries.

**When:** Understand how attackers actually move in a tenant so your posture checks and MicroBurst-style simulations target the realistic paths.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/MSTIC-Jupyter/Azure-Threat-Research-Matrix.git`

**URL:** https://github.com/MSTIC-Jupyter/Azure-Threat-Research-Matrix

**Alternatives:** Microsoft Cloud Security Benchmark (docs)


#### Audit & Compliance Posture


##### Prowler (Azure) ⭐

Prowler pinned to Azure (`-p azure --az-cli-auth`): 100+ read-only checks over Entra ID, subscriptions, storage, key vault, and network config against CIS Microsoft Azure 1.x/2.x.

**When:** The main automated Azure compliance pass in CI or on a schedule; complements but does not replace Azure Policy assignments.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler && prowler azure --az-cli-auth`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** Scout Suite (Azure), MicroBurst


##### Scout Suite (Azure)

Scout Suite's Azure provider: one-command dump of subscription posture (ARM resources, RBAC, storage, NSGs) into an HTML report with risk annotations.

**When:** A point-in-time visual Azure report that mirrors your AWS workflow and is easy to archive as an evidence artifact.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite && scout azure --cli`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** Prowler (Azure), Microsoft Cloud Security Benchmark (docs)


#### Recon & Post-Exploitation


##### MicroBurst ⭐

NetSPI's PowerShell toolkit for attacking Azure: service discovery, weak-config auditing, credential dumping (AzPasswords), and post-exploitation on VMs, Key Vault, and Automation accounts.

**When:** The default Azure toolkit in authenticated engagements on your own tenant; Windows-only, so run it from a PowerShell host with the Az modules installed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/MicroBurst.git && Import-Module .\MicroBurst.psm1`

**URL:** https://github.com/NetSPI/MicroBurst

**Alternatives:** Stormspotter, ATEAM


##### Stormspotter

Microsoft Azure Red Team's attack-graph tool: collects subscription and ARM resources into Neo4j and renders the attack surface with pivot opportunities.

**When:** Map a large tenant visually and find cross-resource pivot paths once you hold reader-level access in a sanctioned assessment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Azure/Stormspotter && docker-compose up`

**URL:** https://github.com/Azure/Stormspotter

**Alternatives:** MicroBurst, ATEAM


##### ATEAM

NetSPI's unauthenticated reconnaissance tool probes name permutations across App Services, Key Vault, Storage, DevOps, SharePoint, and Databricks to discover Azure resources and attribute tenant IDs.

**When:** From outside, discover forgotten Azure resources whose names leak a tenant — ideal for attack-surface checks on your own domains before logging in.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/ATEAM.git && cd ATEAM && pip3 install -r requirements.txt`

**URL:** https://github.com/NetSPI/ATEAM

**Alternatives:** MicroBurst, Azure Threat Research Matrix (ATRM)



## Google Cloud Platform



#### Audit & Compliance Posture


##### Scout Suite (GCP) ⭐

Scout Suite's GCP provider: gathers project posture across IAM, GCE, GCS, GKE, and Cloud SQL into a browsable HTML risk report, including Org-level IAM.

**When:** The quickest visual read of GCP config risk in one project — pair with Prowler for covered CIS controls.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install scoutsuite && scout gcloud --project-id PROJECT`

**URL:** https://github.com/nccgroup/ScoutSuite

**Alternatives:** Prowler (GCP), gcloud CLI & Scripted Audits


##### Prowler (GCP)

Prowler pinned to GCP (`-p gcp`): 100+ read-only checks against the Google Cloud CIS 1.x benchmark covering IAM, logging, networking, and storage.

**When:** The compliance-first GCP pass in CI; best paired with its AWS/Azure siblings for org-wide reporting.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip3 install prowler && prowler gcp --organization-id "..."`

**URL:** https://github.com/prowler-cloud/prowler

**Alternatives:** Scout Suite (GCP), Forseti (retired)


##### Forseti (retired)

Google's old inventory-and-policy engine for detecting GCP misconfigurations; officially retired by the Google Cloud team and no longer developed.

**When:** Only revisit for legacy estates already running it — for new work use Prowler/Scout Suite plus Policy Controller and Assured workloads.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/forseti-security/forseti-security.git`

**URL:** https://github.com/forseti-security/forseti-security

**Alternatives:** Prowler (GCP), Scout Suite (GCP)


##### gcloud CLI & Scripted Audits

The `gcloud` CLI plus `gcloud asset`, IAM recommender, and `gcloud projects get-iam-policy` pipelines for fast targeted checks and drift reporting.

**When:** Quick focused questions — who can do what in a project, which buckets changed, logging disabled — without a full scanner run.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `curl https://sdk.cloud.google.com | bash`

**URL:** https://cloud.google.com/sdk/docs

**Alternatives:** Steampipe, Scout Suite (GCP)


#### Recon & Privilege Escalation


##### gcp-scanner ⭐

Google's scanner determines what a compromised credential can reach across GCE, GCS, GKE, Cloud SQL, BigQuery, KMS, and more, pulling from VM metadata, SA keys, or OAuth tokens.

**When:** Assess blast radius after a leaked service account key or compromised VM, without needing gcloud installed.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip3 install gcp_scanner`

**URL:** https://github.com/google/gcp_scanner

**Alternatives:** gcpwn, GCP IAM Privilege Escalation Toolkit


##### gcpwn

NetSPI's GCP and Workspace pentesting framework: enumerates and downloads project data, builds BloodHound OpenGraph models, and bundles credential and exploit tooling.

**When:** Deep GCP/Workspace engagements where you want structured enumeration feeding BloodHound-style attack-path analysis.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/NetSPI/gcpwn.git`

**URL:** https://github.com/NetSPI/gcpwn

**Alternatives:** gcp-scanner, CloudFox


##### GCP IAM Privilege Escalation Toolkit

Rhino's documented GCP IAM privesc methods plus a scanner (enumerate_member_permissions.py then check_for_privesc.py) that flags principals able to escalate.

**When:** Audit who in your projects could privilege-escalate to org ownership and validate hardened role design.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation.git`

**URL:** https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation

**Alternatives:** gcp-scanner, PMapper


#### Public Storage & Bucket Scan


##### GCPBucketBrute ⭐

Enumerates Google Storage buckets from keyword permutations and reports per-bucket access, flagging public, writable, and privilege-escalation-prone (storage.buckets.setIamPolicy) buckets.

**When:** Check which of your GCS buckets are reachable or writable without auth, including escalations visible from a service account.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/RhinoSecurityLabs/GCPBucketBrute.git && cd GCPBucketBrute && pip3 install -r requirements.txt`

**URL:** https://github.com/RhinoSecurityLabs/GCPBucketBrute

**Alternatives:** S3Scanner, gcloud CLI & Scripted Audits



## IaC & Container Misconfiguration



#### Terraform & IaC Scanners


##### Checkov ⭐

Prisma Cloud-maintained IaC static analyzer with 1,000+ built-in policies for Terraform (incl. plan output), CloudFormation, Kubernetes, Helm, Dockerfile, Bicep, ARM, and Serverless; graph-based and multi-resource aware.

**When:** The default IaC gate: scan Terraform/K8s/Dockerfile in CI and on terraform plan to catch exposed resources and weak IAM before apply.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install checkov`

**URL:** https://github.com/bridgecrewio/checkov

**Alternatives:** tfsec, Terrascan (archived), Trivy


##### tfsec

Fast Terraform-specific static scanner with 400+ rules and custom Rego/policy support; development has wound down as scanning moved into Trivy (trivy config).

**When:** Lightweight, human-friendly Terraform warnings in pre-commit; for maintained updates run the same checks via Trivy config.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install tfsec`

**URL:** https://github.com/aquasecurity/tfsec

**Alternatives:** Checkov, Trivy


##### Terrascan (archived)

Tenable's Rego-policy IaC scanner for Terraform, CloudFormation, ARM, K8s, Helm, and Docker; the repository was archived November 2025 and is read-only.

**When:** Only for aligning with existing Terrascan policy sets on frozen pipelines — new IaC work should use Checkov or KICS.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `brew install terrascan`

**URL:** https://github.com/tenable/terrascan

**Alternatives:** Checkov, KICS


#### CloudFormation Policy


##### cfn-guard ⭐

AWS's official CloudFormation policy-as-code tool: validates templates and yes, live stacks, against declarative rules written in a purpose-built Guard DSL; ships AWS managed rule collections.

**When:** Enforce organizational CloudFormation rules (allowlists, encryption, tag policies) in CI against templates before deploy.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install cloudformation-guard`

**URL:** https://github.com/aws-cloudformation/cloudformation-guard

**Alternatives:** cfn-nag, Checkov


##### cfn-nag

Stelligent's rule-based CloudFormation linter that flags over-permissive IAM wildcards, plaintext secrets, and open security groups across templates.

**When:** Fast, opinionated CloudFormation warnings with zero configuration; a solid first pass before cfn-guard rules.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `gem install cfn-nag`

**URL:** https://github.com/stelligent/cfn_nag

**Alternatives:** cfn-guard, Checkov


#### Kubernetes & Helm


##### kube-bench ⭐

Aqua's CIS Kubernetes benchmark runner that checks control-plane nodes (kube-apiserver, etcd) and workloads against the CIS K8s Benchmark 1.9+ sections.

**When:** Baseline your clusters against CIS on install and after upgrades; run from the node or via the official image.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run --rm -v /etc/kubernetes:/etc/kubernetes aquasec/kube-bench:latest`

**URL:** https://github.com/aquasecurity/kube-bench

**Alternatives:** kube-score, KICS


##### kube-score

Opinionated static analysis of Kubernetes object manifests scoring against best practices: resource requests, probes, securityContext, network policies.

**When:** Per-manifest linting in CI for the small, common mistakes — complements policy-heavy gatekeepers like Kyverno and kube-bench.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install kube-score`

**URL:** https://github.com/zegl/kube-score

**Alternatives:** KICS, Checkov


##### KICS

Checkmarx's open-source IaC scanner (Keeping Infrastructure as Code Secure) running thousands of queries across 20+ platforms — Terraform, K8s, Docker, Helm, CloudFormation, Ansible — with SARIF output and OPA/Rego custom queries.

**When:** A complementary cross-check on IaC after Checkov, or the pick when you want OPA/Rego policy authoring (the slot archived Terrascan used to fill).

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -t -v "$PWD":/path checkmarx/kics:latest scan -p /path -o /path`

**URL:** https://github.com/Checkmarx/kics

**Alternatives:** Checkov, kube-score


#### Container Images & Registries


##### Trivy ⭐

Aqua's all-in-one scanner: OS/library package CVEs in images and filesystems, SBOM generation, IaC misconfigs (absorbed tfsec), Kubernetes scanning, and registry CI — one binary, zero daemon.

**When:** The single tool to add to a container build: `trivy image`, `trivy fs --scanners vuln,secret,misconfig`, and `trivy sbom` cover images to source in one install.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `brew install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** Grype + Syft, Checkov



