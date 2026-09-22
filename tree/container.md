# 📦 Container & Kubernetes Security

Defending your own clusters: image scanning, SBOM, runtime detection, CIS posture, and admission policy.

## Image & Registry Vulnerability Scanning

### Trivy ⭐

Aqua Security's comprehensive scanner covering container images, filesystems, git repos, VMs, and Kubernetes; detects CVEs, misconfigurations, secrets, and licenses from one binary.

**When:** Gate every image build in CI and scan at push time; add trivy-operator (or Kubescape) for in-cluster image monitoring.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `brew install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** grype, syft (SBOM), kubescape scan image


### Grype

Anchore's fast vulnerability scanner for images, filesystems, and SBOMs; pairs with Syft and adds EPSS, KEV, and OpenVEX filtering to prioritize real risk.

**When:** Speed-first CI scans, or scan an SBOM you already generated instead of re-pulling and re-analyzing the image.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/grype

**Alternatives:** trivy, syft (SBOM)


## SBOM Generation & Management

### Syft ⭐

Generates SBOMs for container images, filesystems, and archives in CycloneDX, SPDX, and Syft JSON; feeds Grype directly and supports signed in-toto attestations.

**When:** Produce a machine-readable dependency inventory at build time and ship it with the image to prove supply-chain provenance.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sudo sh -s -- -b /usr/local/bin`

**URL:** https://github.com/anchore/syft

**Alternatives:** trivy, cyclonedx-cli


### Trivy

Cross-reference entry: `trivy image --format cyclonedx|spdx` emits SBOMs, and Trivy will also scan an existing SBOM document for vulnerabilities.

**When:** You standardize on Trivy already and want SBOM output without introducing a second cataloging tool.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install trivy`

**URL:** https://github.com/aquasecurity/trivy

**Alternatives:** syft


### cyclonedx-cli

OWASP CycloneDX CLI to validate, merge, diff, convert, sign, and verify CycloneDX and SPDX BOMs; exits non-zero on invalid input for CI gating.

**When:** Normalize third-party vendor SBOMs into one format, diff releases to catch dependency drift, or enforce schema-valid BOMs in the pipeline.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run --rm -v "$(pwd):/data" cyclonedx/cyclonedx-cli validate --input-file /data/sbom.json`

**URL:** https://github.com/CycloneDX/cyclonedx-cli

**Alternatives:** syft, trivy


## Runtime Threat Detection

### Falco ⭐

CNCF-graduated kernel monitoring agent (eBPF or driver) that watches syscalls enriched with container and Kubernetes metadata, alerting via a flexible rules engine.

**When:** Deploy on every production node for real-time detection of shells in containers, privileged pods, and sensitive-file access.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `helm repo add falcosecurity https://falcosecurity.github.io/charts && helm install falco falcosecurity/falco`

**URL:** https://github.com/falcosecurity/falco

**Alternatives:** docker-bench-security, kubescape (operator runtime)


### docker-bench-security

Docker's CIS Docker Benchmark script auditing the Docker/containerd host, daemon, and running containers against dozens of best-practice checks.

**When:** Harden and periodically re-audit the container host after workloads are deployed; quick compliance readout for a single host.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/docker/docker-bench-security.git && cd docker-bench-security && sudo sh docker-bench-security.sh`

**URL:** https://github.com/docker/docker-bench-security

**Alternatives:** falco


## Cluster Posture & Compliance

### Kubescape ⭐

CNCF-incubating Kubernetes security platform scanning clusters, manifests, Helm charts, git repos, and images against CIS, NSA-CISA, and MITRE ATT&CK; operator mode adds continuous posture and eBPF runtime.

**When:** First full-posture sweep of a cluster and as a CI gate on manifests; install the operator for continuous compliance monitoring.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | bash`

**URL:** https://github.com/kubescape/kubescape

**Alternatives:** kube-bench, kube-hunter, popeye


### kube-bench

Aqua's Go tool that runs the CIS Kubernetes Benchmark against control plane, etcd, and worker node configuration, matched to the running Kubernetes version.

**When:** Validate a specific hardened baseline after cluster upgrades, node onboarding, or as a scheduled per-node job.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml`

**URL:** https://github.com/aquasecurity/kube-bench

**Alternatives:** kubescape, docker-bench-security


### Popeye

Read-only live-cluster sanitizer that lints deployed workloads for misconfigurations, dead resources, port mismatches, and missing probes, scoring overall cluster health.

**When:** Periodic 'wide-open' sweep to catch drift and operational debt that static manifest review misses.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/derailed/popeye@latest`

**URL:** https://github.com/derailed/popeye

**Alternatives:** kubescape


### kube-hunter

Legacy Aqua pen-test tool that finds cluster weaknesses from an attacker's perspective (exposed dashboards, leaked secrets, weak RBAC); officially no longer under active development.

**When:** Offense-style spot check on a cluster you own; treat findings as a starting list since it is not actively maintained.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `docker run --rm -it aquasec/kube-hunter`

**URL:** https://github.com/aquasecurity/kube-hunter

**Alternatives:** kubescape, trivy (k8s scan)


## Admission Control & Policy-as-Code

### OPA Gatekeeper ⭐

CNCF policy controller that enforces Rego-based policy through constraint templates and constraints, with admission webhooks, audit, and mutation support.

**When:** Enforce registry allowlists, required labels, and security-context rules at admission when you already know Rego or want the largest policy ecosystem.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/deploy/gatekeeper.yaml`

**URL:** https://github.com/open-policy-agent/gatekeeper

**Alternatives:** kyverno, polaris


### Kyverno

CNCF-graduated Kubernetes-native policy engine using YAML (no new language) to validate, mutate, generate, and clean up resources; verifies image signatures via cosign.

**When:** Teams that prefer familiar YAML and want mutation, image verification, and policy-as-a-resource without learning Rego.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `helm repo add kyverno https://kyverno.github.io/helm-charts && helm install kyverno kyverno/kyverno -n kyverno --create-namespace`

**URL:** https://github.com/kyverno/kyverno

**Alternatives:** opa gatekeeper, polaris


### Polaris

Fairwinds policy-as-code with 30+ built-in checks across security, networking, reliability, and efficiency; runs as a dashboard, CI CLI, or mutating admission webhook.

**When:** Drop-in baseline enforcement with a visible compliance dashboard when full OPA or Kyverno is overkill.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `kubectl apply -f https://github.com/FairwindsOps/polaris/releases/latest/download/dashboard.yaml`

**URL:** https://github.com/FairwindsOps/polaris

**Alternatives:** kyverno, opa gatekeeper, popeye


## Dockerfile & Image Best-Practice Lint

### hadolint ⭐

Haskell Dockerfile linter that parses the Dockerfile AST and applies best-practice rules, delegating inline shell checks to ShellCheck (DL- and SC-prefixed findings).

**When:** Lint Dockerfiles in CI to catch untagged images, root users, and unsafe RUN commands before the image is ever built.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install hadolint`

**URL:** https://github.com/hadolint/hadolint

**Alternatives:** dockle, trivy (misconfig)


### dockle

Container image linter that audits the built image against CIS Docker image checkpoints and best practices (non-root user, HEALTHCHECK, setuid/setgid files, content trust).

**When:** Audit the built image itself, complementing Dockerfile lint, right before pushing to a production registry.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install goodwithtech/r/dockle`

**URL:** https://github.com/goodwithtech/dockle

**Alternatives:** hadolint

