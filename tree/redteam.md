# 🎯 Red Team Infrastructure & Operations

Authorized red team tooling: pivoting, tunnels, proxying, and practice lab environments.

## Pivoting & Tunnels

sshuttle ⭐


#### sshuttle ⭐

Lightweight VPN-like pivot using SSH; routes traffic through a jump host without requiring root on the target.

**When:** Need simple, reliable lateral routing to access internal networks from a single jump host during authorized engagements or labs.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install sshuttle`

**URL:** https://github.com/sshuttle/sshuttle

**Alternatives:** chisel, ligolo-ng


#### chisel

Fast TCP/HTTP tunneling over a single port with reverse or forward modes; portable and minimal.

**When:** Tunneling a specific service through restrictive firewalls or NAT during controlled testing.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `go install github.com/jpillora/chisel@latest`

**URL:** https://github.com/jpillora/chisel

**Alternatives:** sshuttle, frp


#### ligolo-ng

TUN-based tunneling agent for pivoting with automatic routes; simple interface for authorized red team operations.

**When:** Need full network access through a pivot host with automatic routing in a lab or authorized engagement environment.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install github.com/nicocha30/ligolo-ng@latest`

**URL:** https://github.com/nicocha30/ligolo-ng

**Alternatives:** sshuttle, frp


#### frp

Fast reverse proxy for exposing local services through a remote server; stable and well-documented.

**When:** Need controlled reverse proxying for lab infrastructure or authorized test setups behind NAT.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/fatedier/frp@latest`

**URL:** https://github.com/fatedier/frp

**Alternatives:** chisel






## Proxy Management

proxychains-ng ⭐


#### proxychains-ng ⭐

Force any TCP application through a chain of proxies for controlled routing in authorized testing.

**When:** Need to route existing tooling through a proxy chain during authorized red team exercises or lab scenarios.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/rofl0r/proxychains-ng && cd proxychains-ng && ./configure --prefix=/usr && make && sudo make install`

**URL:** https://github.com/rofl0r/proxychains-ng






## Active Directory Labs & Practice

GOAD ⭐


#### GOAD ⭐

Great Oxide Active Directory lab for realistic, authorized red team practice with vulnerable AD domains.

**When:** Practicing authorized AD attack/defense techniques in an isolated, controlled lab environment.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/Orange-Cyberdefense/GOAD`

**URL:** https://github.com/Orange-Cyberdefense/GOAD

**Alternatives:** VECTR


#### VECTR

Purple team tracking and assessment framework for mapping techniques to MITRE ATT&CK in controlled exercises.

**When:** Running structured, authorized red/purple team exercises with measurable objectives and reporting.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/SecurityRiskAdvisors/VECTR`

**URL:** https://github.com/SecurityRiskAdvisors/VECTR

**Alternatives:** GOAD





