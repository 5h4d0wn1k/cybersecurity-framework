# 📦 Container & Kubernetes Security

Defending your own clusters: image scanning, SBOM, runtime detection, CIS posture, admission policy, Sigstore signing, and offensive lab checks.

## Image & Registry Vulnerability Scanning



#### Standalone CVE scanners


##### Trivy ⭐

Aqua Security's comprehensive scanner covering container images, filesystems, git repos, VMs, and Kubernetes; detects CVEs, misconfigurations, secrets, and licenses from one binary.

**When:** Gate every image build in CI and scan at push time; add trivy-operator (or Kubescape) for in-cluster image monitoring.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** grype, syft (SBOM), kubescape scan image


##### Grype

Anchore's fast vulnerability scanner for images, filesystems, and SBOMs; pairs with Syft and adds EPSS, KEV, and OpenVEX filtering to prioritize real risk.

**When:** Speed-first CI scans, or scan an SBOM you already generated instead of re-pulling and re-analyzing the image.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/grype

**Alternatives:** trivy, syft (SBOM)


##### Clair

Quay/Red Hat's v4 vulnerability database server for registries: ingests manifests and exposes a gRPC API that clairctl, clair-hook, or admission controllers query for container-layer CVE data.

**When:** Deploy next to Quay (or your own registry) for server-side scanning of every pushed image instead of one-off CI scans.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d --name clair -p 6060:6060 quay.io/projectquay/clair:latest`

**URL:** https://github.com/quay/clair

**Alternatives:** trivy, anchore


##### Anchore (Enterprise)

Commercial policy-and-compliance platform built on the Grype/Syft engine with admission control (anchore-admission-controller) and scheduled registry scanning; the legacy open-source anchore-engine CLI is deprecated.

**When:** When you need continuous registry posture, feeds/webhooks, and audited policy gates as a platform rather than a single binary.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `helm repo add anchore https://charts.anchore.io && helm install anchore anchore/anchore-enterprise`

**URL:** https://anchore.com

**Alternatives:** grype, trivy, clair


#### Vendor & SaaS scanning


##### Docker Scout ⭐

Docker's image analyzer for CVEs, provenance, and supply-chain compliance; highlights CISA KEV reachability and suggests base-image/model upgrades, integrated into Docker Desktop and CI.

**When:** Fastest starting point for teams already on Docker — compare images, audit a registry, and enforce policies without another platform.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install docker/scout/docker-scout`

**URL:** https://github.com/docker/scout-cli

**Alternatives:** snyk container, trivy


##### Snyk Container

Snyk's container scanning CLI ('snyk container test') covering images plus Kubernetes/IaC config, with base-image upgrade paths and registry/workspace integration.

**When:** Teams already using Snyk for SCA/app-sec want container coverage in the same console and policy engine.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `npm install -g snyk`

**URL:** https://github.com/snyk/cli

**Alternatives:** docker scout, trivy


#### Dockerfile & image best-practice lint


##### hadolint ⭐

Haskell Dockerfile linter that parses the Dockerfile AST and applies best-practice rules, delegating inline shell checks to ShellCheck (DL- and SC-prefixed findings).

**When:** Lint Dockerfiles in CI to catch untagged images, root users, and unsafe RUN commands before the image is ever built.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install hadolint`

**URL:** https://github.com/hadolint/hadolint

**Alternatives:** dockle, trivy (misconfig)


##### dockle

Container image linter that audits the built image against CIS Docker image checkpoints and best practices (non-root user, HEALTHCHECK, setuid/setgid files, content trust).

**When:** Audit the built image itself, complementing Dockerfile lint, right before pushing to a production registry.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install goodwithtech/r/dockle`

**URL:** https://github.com/goodwithtech/dockle

**Alternatives:** hadolint



## SBOM Generation & Management



#### supplysec ◆ by 5h4d0wn1k

Supply-chain security gate — dependency manifest parsing, SBOM (CycloneDX/SPDX), offline advisory matching, policy gates, post-quantum scanning.

**When:** Gating CI builds on dependency/supply-chain posture before merge.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/supplysec`

**URL:** https://github.com/5h4d0wn1k/supplysec

**Alternatives:** Own tool — lab/authorized use only


#### Generators


##### Syft ⭐

Generates SBOMs for container images, filesystems, and archives in CycloneDX, SPDX, and Syft JSON; feeds Grype directly and supports signed in-toto attestations.

**When:** Produce a machine-readable dependency inventory at build time and ship it with the image to prove supply-chain provenance.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sudo sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/syft

**Alternatives:** trivy, cyclonedx-cli


#### Validation & quality scoring


##### CycloneDX CLI ⭐

OWASP CycloneDX CLI to validate, merge, diff, convert, sign, and verify CycloneDX and SPDX BOMs; exits non-zero on invalid input for CI gating.

**When:** Normalize third-party vendor SBOMs into one format, diff releases to catch dependency drift, or enforce schema-valid BOMs in the pipeline.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run --rm -v "$(pwd):/data" cyclonedx/cyclonedx-cli validate --input-file /data/sbom.json`

**URL:** https://github.com/CycloneDX/cyclonedx-cli

**Alternatives:** sbomqs, syft


##### sbomqs

Interlynk's SBOM quality & compliance scorer: grades SPDX/CycloneDX BOMs on completeness, licensing, relationships, and format correctness, then filters by quality score.

**When:** Score vendor-supplied and generated SBOMs in CI so you can reject 'good enough' BOMs and see which tooling produces trustworthy output.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/interlynk-io/sbomqs@latest`

**URL:** https://github.com/interlynk-io/sbomqs

**Alternatives:** cyclonedx-cli



## Signing, Provenance & Base-Image Policy



#### Image signing (Sigstore / Notary)


##### Signing CLIs


###### Cosign ⭐

Sigstore CLI to sign and verify images, blobs, and SBOM attestations with keyless (OIDC) or key-based signatures stored as OCI artifacts, backed by the Rekor transparency log.

**When:** Sign every image in CI and verify at admission time (Kyverno, Gatekeeper, or the sigstore policy controller) to stop unsigned/mutated image pulls.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install cosign`

**URL:** https://github.com/sigstore/cosign

**Alternatives:** notation, docker content trust


###### Notation

CNCF Notary Project CLI (OCI 1.1 signatures) for signing and verifying artifacts with X.509/SPIFFE certificates; keeps signatures as native OCI artifacts and integrates with Azure/AWS KMS signers.

**When:** Enterprise environments that already run X.509 PKI/KMS and want cert-managed signing rather than Sigstore's ephemeral, keyless model.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install notation`

**URL:** https://github.com/notaryproject/notation

**Alternatives:** cosign


##### Verification & transparency infrastructure


###### Sigstore Policy Controller ⭐

Sigstore's admission controller that verifies signatures and attestations on every pod creation, mutating the request to enforce trust policies cluster-wide.

**When:** Cluster-wide 'only signed/attested images run here' enforcement as an image-policy layer, complementary to schema-style admission policies like Kyverno.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `helm repo add sigstore https://sigstore.github.io/helm-charts && helm install policy-controller sigstore/policy-controller -n cosign-system --create-namespace`

**URL:** https://github.com/sigstore/policy-controller

**Alternatives:** kyverno (verify-images), cosign verify


###### Rekor CLI

Query and verify entries in the Rekor transparency log (DSSE/tekton/blob/cosign types): confirm a signature was logged at a point in time and detect tampered/duplicate entries.

**When:** Forensic checks that complement signature verification — prove an artifact existed in the log, correlate with incident timelines, or audit your own signing records.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install sigstore/tap/rekor-cli`

**URL:** https://github.com/sigstore/rekor

**Alternatives:** cosign verify --certificate-log-url


#### Distroless base images


##### Distroless ⭐

Google's minimal base images with no shell, package managers, or runtimes — static, cc, and Debian variants with nonroot tags that slash attack surface and image size.

**When:** Production images that never need a shell: shift all debugging to the builder stage or sidecars and run the runtime stage as non-root by default.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `FROM gcr.io/distroless/static-debian12:nonroot`

**URL:** https://github.com/GoogleContainerTools/distroless

**Alternatives:** wolfi, chainguard images


##### Wolfi

Chainguard's apk-based, no-glibc-bloat OS purpose-built for containers — the upstream of hardened Chainguard images, reproducibly assembled with apko into slim distroless-style images.

**When:** Teams needing a lean, fully open-source base where you still install apk packages and build tools inside multi-stage builds without bloating the runtime image.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `FROM cgr.dev/chainguard/wolfi-base:latest`

**URL:** https://github.com/wolfi-dev/os

**Alternatives:** distroless



## Kubernetes Cluster Security



#### CIS benchmark & compliance


##### kube-bench ⭐

Aqua's Go tool that runs the CIS Kubernetes Benchmark against control plane, etcd, and worker node configuration, matched to the running Kubernetes version.

**When:** Validate a specific hardened baseline after cluster upgrades, node onboarding, or as a scheduled per-node job.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml`

**URL:** https://github.com/aquasecurity/kube-bench

**Alternatives:** kubescape, docker-bench-security


##### docker-bench-security

Docker's CIS Docker Benchmark script auditing the Docker/containerd host, daemon, and running containers against dozens of best-practice checks.

**When:** Harden and periodically re-audit the container host on worker nodes after workloads are deployed; quick compliance readout for a single host.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/docker/docker-bench-security.git && cd docker-bench-security && sudo sh docker-bench-security.sh`

**URL:** https://github.com/docker/docker-bench-security

**Alternatives:** kube-bench


#### Continuous posture & drift


##### Kubescape ⭐

CNCF-incubating Kubernetes security platform scanning clusters, manifests, Helm charts, git repos, and images against CIS, NSA-CISA, and MITRE ATT&CK; operator mode adds continuous posture and eBPF runtime.

**When:** First full-posture sweep of a cluster and as a CI gate on manifests; install the operator for continuous compliance monitoring.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | bash`

**URL:** https://github.com/kubescape/kubescape

**Alternatives:** kube-bench, popeye


##### Popeye

Read-only live-cluster sanitizer that lints deployed workloads for misconfigurations, dead resources, port mismatches, and missing probes, scoring overall cluster health.

**When:** Periodic 'wide-open' sweep to catch drift and operational debt that static manifest review misses.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/derailed/popeye@latest`

**URL:** https://github.com/derailed/popeye

**Alternatives:** kubescape


#### Manifest & YAML lint


##### kube-linter ⭐

StackRox (Red Hat) static analyzer for Kubernetes YAML and Helm charts with 40+ built-in checks (privileged containers, insecure service types, missing resource limits) and SARIF output for CI.

**When:** Pre-deploy linting in CI — catch risky manifests before apply, complementing runtime posture and admission checks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install kube-linter`

**URL:** https://github.com/stackrox/kube-linter

**Alternatives:** kubeaudit, popeye


##### kubeaudit

Audits manifests and live clusters against security controls (privileged, hostNetwork, capabilities, allowPrivilegeEscalation) and can auto-fix them; repo is archived and the brew formula deprecated as of 2025.

**When:** Only where an existing pipeline integrates its autofix mode; otherwise prefer kube-linter + kube-bench for actively maintained coverage.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `brew install kubeaudit`

**URL:** https://github.com/Shopify/kubeaudit

**Alternatives:** kube-linter, kube-bench


#### Admission control & policy-as-code


##### Policy engines


###### OPA Gatekeeper ⭐

CNCF policy controller that enforces Rego-based policy through constraint templates and constraints, with admission webhooks, audit, and mutation support.

**When:** Enforce registry allowlists, required labels, and security-context rules at admission when you already know Rego or want the largest policy ecosystem.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/deploy/gatekeeper.yaml`

**URL:** https://github.com/open-policy-agent/gatekeeper

**Alternatives:** kyverno, polaris


###### Kyverno

CNCF-graduated Kubernetes-native policy engine using YAML (no new language) to validate, mutate, generate, and clean up resources; verifies image signatures via cosign.

**When:** Teams that prefer familiar YAML and want mutation, image verification, and policy-as-a-resource without learning Rego.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `helm repo add kyverno https://kyverno.github.io/helm-charts && helm install kyverno kyverno/kyverno -n kyverno --create-namespace`

**URL:** https://github.com/kyverno/kyverno

**Alternatives:** opa gatekeeper, polaris


###### Polaris

Fairwinds policy-as-code with 30+ built-in checks across security, networking, reliability, and efficiency; runs as a dashboard, CI CLI, or mutating admission webhook.

**When:** Drop-in baseline enforcement with a visible compliance dashboard when full OPA or Kyverno is overkill.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `kubectl apply -f https://github.com/FairwindsOps/polaris/releases/latest/download/dashboard.yaml`

**URL:** https://github.com/FairwindsOps/polaris

**Alternatives:** kyverno, opa gatekeeper, popeye


##### Local policy testing & OPA tooling


###### Conftest ⭐

Tests Kubernetes manifests, Helm values, Terraform, and CUE against Rego policies from the CLI; CI-friendly and shares the same policy language as OPA Gatekeeper.

**When:** Control-plane-free policy checks in pre-commit/CI, or validate the exact Rego you will enforce with Gatekeeper before installing anything.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install conftest`

**URL:** https://github.com/open-policy-agent/conftest

**Alternatives:** opa gatekeeper, kyverno CLI test


#### Network policy enforcement


##### Cilium ⭐

eBPF-based CNI enforcing Kubernetes NetworkPolicy and extended CiliumNetworkPolicy with identity-based rules (no IP juggling), plus Hubble for policy-aware flow observability.

**When:** Strict workload micro-segmentation with per-L4/L7 rules and visibility; it replaces your CNI, so plan a rollout, not a drop-in patch.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `helm repo add cilium https://helm.cilium.io && helm install cilium cilium/cilium --namespace kube-system`

**URL:** https://github.com/cilium/cilium

**Alternatives:** calico


##### Calico

Project Calico/Tigera CNI delivering the Kubernetes NetworkPolicy API plus GlobalNetworkPolicy and host-endpoint policy for traffic entering/leaving nodes.

**When:** Clusters already on Calico, or when you need global (not just namespace-scoped) network policy that covers host endpoints.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml`

**URL:** https://github.com/projectcalico/calico

**Alternatives:** cilium


#### Adversarial assessment (self-check)


##### kube-hunter ⭐

Legacy Aqua pen-test tool that finds cluster weaknesses from an attacker's perspective (exposed dashboards, leaked secrets, weak RBAC); officially no longer under active development.

**When:** Offense-style spot check on a cluster you own; treat findings as a starting list since it is not actively maintained.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `docker run --rm -it aquasec/kube-hunter`

**URL:** https://github.com/aquasecurity/kube-hunter

**Alternatives:** kubescape, trivy (k8s scan)



## Runtime Threat Detection & RBAC



#### eBPF kernel detection


##### Falco ⭐

CNCF-graduated kernel monitoring agent (eBPF or driver) that watches syscalls enriched with container and Kubernetes metadata, alerting via a flexible rules engine.

**When:** Deploy on every production node for real-time detection of shells in containers, privileged pods, and sensitive-file access.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `helm repo add falcosecurity https://falcosecurity.github.io/charts && helm install falco falcosecurity/falco`

**URL:** https://github.com/falcosecurity/falco

**Alternatives:** tetragon, kubescape (operator runtime)


##### Tetragon

Cilium's eBPF-based runtime security and observability with no userspace for traffic paths: policy-driven tracing of syscalls and network events, plus kubectl-level enrichment.

**When:** High-throughput, eBPF-first detection with built-in network insights and lower operational moving parts than a driver-based agent.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `helm repo add cilium https://helm.cilium.io && helm install tetragon cilium/tetragon -n kube-system`

**URL:** https://github.com/cilium/tetragon

**Alternatives:** falco


#### RBAC review & least privilege


##### rbac-lookup ⭐

Fairwinds CLI that reverses RBAC: give it a user, service account, or group and it prints every Role/ClusterRole bound to that identity, resolving the bindings for you.

**When:** Audit 'what can this identity actually do?' across namespaces — the fastest path from a SA name to a least-privilege review.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install FairwindsOps/tap/rbac-lookup`

**URL:** https://github.com/FairwindsOps/rbac-lookup

**Alternatives:** kubectl auth can-i, kubiScan


##### kubectl auth can-i

Built-in kubectl authorization self-check; 'kubectl auth can-i --list -A' dumps the full permission matrix for the current context in one shot.

**When:** Zero-install RBAC sanity checks in an incident or review loop — verify a spyed SA cannot escalate before trusting it.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `kubectl auth can-i --list -A`

**URL:** https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/

**Alternatives:** rbac-lookup



## CI/CD Pipeline Security Gates



#### GitHub Actions for scan & SBOM


##### Trivy Action ⭐

aquasecurity/trivy-action wraps Trivy in GitHub Actions for image, filesystem, config, and SBOM scans with severity gates and SARIF upload to code scanning.

**When:** Per-PR image/filesystem scanning that fails the build above a severity threshold and feeds findings into GitHub Security tab.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `uses: aquasecurity/trivy-action@main`

**URL:** https://github.com/aquasecurity/trivy-action

**Alternatives:** anchore scan action, snyk action


##### Anchore Scan Action

anchore/scan-action runs Grype with fine-grained gating (only-fixed, severity cutoff, OpenVEX) and emits SARIF, JSON, or CycloneDX outputs from images, paths, or existing SBOMs.

**When:** Grype-grounded, license-clean security scanning where you want VEX and fix-availability filters ahead of generic fail-on-high scans.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `uses: anchore/scan-action@v4`

**URL:** https://github.com/anchore/scan-action

**Alternatives:** trivy action


##### SBOM Action

anchore/sbom-action generates Syft SBOMs in CI, publishing them as release artifacts or GitHub SBOM attestations so downstream scanners (Clair, Grype, Docker Scout) consume them.

**When:** Attach a CycloneDX/SPDX BOM to every released image git-tag artifact, proving what shipped for audit and supply-chain consumers.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `uses: anchore/sbom-action@v0`

**URL:** https://github.com/anchore/sbom-action

**Alternatives:** syft


#### Policy libraries for pipelines & clusters


##### Kyverno Policies ⭐

Kyverno's community policy library: 130+ tested YAML policies covering Pod Security Standards, image signatures, network policy checks, and compliance presets.

**When:** Start from a maintained, battle-tested policy set and adapt, rather than authoring every admission rule from scratch.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/kyverno/policies`

**URL:** https://github.com/kyverno/policies

**Alternatives:** polaris, conftest



## Attack Paths & Container Escapes (Lab / Offense)



#### Kubernetes attack-graph analysis


##### KubeHound ⭐

DataDog's attack-graph engine: a collector ingests cluster RBAC, workload, and network data, then a graph query layer returns BloodHound-style attack paths between assets.

**When:** Continuously model 'can this workload or identity reach the kubelet/cluster?' — ideal for validating least privilege and red-team path enumeration on your own cluster.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `brew install kubehound`

**URL:** https://github.com/DataDog/KubeHound

**Alternatives:** kubiScan


##### KubiScan

CyberArk's RBAC attack-path scanner: lists risky roles, subjects, and clusterrolebindings, and highlights the write-access paths (secrets, exec) an attacker can abuse for cluster takeover.

**When:** Systematically map RBAC escape routes on clusters you own and gather remediation evidence (which SA grants secret read, exec into pods, etc.).

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/CyberArk/KubiScan.git && cd KubiScan && sudo python3 setup.py install`

**URL:** https://github.com/CyberArk/KubiScan

**Alternatives:** kube-hound, rbac-lookup


#### Container escape & post-exploitation


##### deepce ⭐

DEEPCE (Docker Enumeration, Escalation of Privileges and Container Escapes) is a single bash script that enumerates capabilities, mounts, sockets, env, and metadata, then suggests and attempts escapes.

**When:** Fast assessment of a container you own in a lab/engagement: one script goes from recon to working escape candidates before you write custom exploit code.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/stealthcopter/deepce.git && bash deepce/deepce.sh --run-all`

**URL:** https://github.com/stealthcopter/deepce

**Alternatives:** cdk


##### CDK

Zero-dependency Go container/Kubernetes penetration toolkit: capability evaluation, no-curl/wget binary delivery, and exploits for runC, docker.sock, containerd, etcd tokens, plus tunneling and reverse shells.

**When:** Post-exploitation payload to drop into minimal/scratch containers where curl and wget are absent but you still need networking, probes, and K8s API calls.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the release binary from github.com/cdk-team/CDK/releases`

**URL:** https://github.com/cdk-team/CDK

**Alternatives:** deepce



