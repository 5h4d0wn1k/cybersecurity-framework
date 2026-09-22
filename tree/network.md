# 📡 Network Attacks & Analysis

Host discovery, port scanning, pivoting, packet capture, on-path interception, and network service auditing for understanding and testing traffic on networks you operate.

## Discovery & Network Mapping




#### Scanning Engines



##### Port & Service Scanning



###### Nmap ⭐

The reference network mapper: full- and half-open TCP/UDP scans, service/version detection, OS fingerprinting with -O, and a 600+ script engine (NSE) for targeted checks.

**When:** Every assessment starts here — run a -sV service audit on hosts you own after a broad port sweep, then drill into specific services with scripts.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install nmap`

**URL:** https://nmap.org

**Alternatives:** naabu, masscan, RustScan


###### masscan

Asynchronous TCP port scanner that sweeps entire CIDRs at line rate; its results pipe directly into Nmap or naabu for follow-up.

**When:** Scan very large ranges fast — your whole lab estate or an entire /8 you operate — before focused Nmap work.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install masscan`

**URL:** https://github.com/robertdavidgraham/masscan

**Alternatives:** Nmap, naabu, RustScan


###### RustScan

Rust port scanner that finds open ports across a /16-class range in seconds, then hands the results to Nmap automatically.

**When:** Fast all-ports sweeps where speed beats verbosity; pair with -- -sV to keep Nmap's service-detection depth.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `cargo install rustscan`

**URL:** https://github.com/RustScan/RustScan

**Alternatives:** naabu, masscan, Nmap


###### naabu

ProjectDiscovery's fast SYN scanner focused on top-N port lists with parallel host/port batching; the port layer of the httpx/nuclei pipeline.

**When:** Quick broad discovery feeding a recon pipeline: naabu --top-ports 1000 then export JSON to httpx.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest`

**URL:** https://github.com/projectdiscovery/naabu

**Alternatives:** RustScan, masscan, Nmap


##### OS & Service Fingerprinting



###### p0f ⭐

Passive OS fingerprinting via TCP/IP stack quirks (TTL, window size, DF) and HTTP signatures; needs no packets of its own, only observed traffic.

**When:** Identify OSes on a network you operate without direct scans — feed it a capture or live traffic mirrored from your switch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install p0f`

**URL:** https://github.com/p0f/p0f

**Alternatives:** nbtscan


###### nbtscan

Scans NetBIOS name services for hostnames, logged-in users, MAC addresses, and shared-disk hints across a Windows LAN.

**When:** On an authorized Windows segment, census machine names and shares quickly when ICMP and ARP answers are filtered.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install nbtscan`

**URL:** http://www.unixwiz.net/tools/nbtscan.html

**Alternatives:** p0f, enumerate shares with smbclient


##### NSE & Scripted Probes



###### Nmap NSE ⭐

Nmap's scripting engine ships 600+ community scripts (smb-*, ssl-*, dns-*, vuln-*) that interrogate services after a scan; run category- or name-filtered sets.

**When:** After port discovery, run safe script categories (--script default,safe) or a specific script like smb-enum-shares against hosts you own.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install nmap`

**URL:** https://nmap.org/nsedoc/

**Alternatives:** nmap-vulners


###### nmap-vulners

NSE script set that queries the Vulners API with detected CPE/service versions and annotates scan output with matching advisories and exploit links.

**When:** Fast triage of version-fatigued service lists: run -sV --script vulners on your own hosts to surface known-CVE matches to patch.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/vulnersCom/nmap-vulners && sudo cp nmap-vulners/*.nse /usr/share/nmap/scripts/`

**URL:** https://github.com/vulnersCom/nmap-vulners

**Alternatives:** Nmap NSE


#### Live Host & Range Discovery



##### ARP & Layer-2 Discovery



###### arp-scan ⭐

ARPs whole subnets and lists live hosts with MAC/OUI vendor — the most reliable L2 census, answered even where ICMP is filtered.

**When:** First step on any network you operate: enumerate every physical host on the LAN before scanning services.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install arp-scan`

**URL:** https://github.com/royhills/arp-scan

**Alternatives:** netdiscover, fping


###### netdiscover

Active and passive ARP discovery with a live table of IP, MAC, and vendor; passively learns hosts from traffic without sending a packet.

**When:** A visual live view of your LAN, or passive L2 discovery when you want to stay quiet while monitoring your own segment.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install netdiscover`

**URL:** https://github.com/netdiscover-scanner/netdiscover

**Alternatives:** arp-scan, fping


##### ICMP & Range Sweeps



###### fping ⭐

Parallel ICMP pinger that sweeps ranges and prints alive/dead hosts in script-friendly output.

**When:** Fast liveness check of large or off-subnet ranges where ARP-based tools cannot reach.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install fping`

**URL:** https://fping.org

**Alternatives:** arp-scan, masscan


##### Bulk DNS Resolution



###### massdns ⭐

High-performance DNS resolver that resolves and brute-forces huge name lists at tens of thousands of queries per second, emitting A/AAAA/CNAME results.

**When:** Resolve or brute candidate subdomain lists on your own estate in minutes instead of hours of single-threaded dig.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/blechschmidt/massdns && cd massdns && make`

**URL:** https://github.com/blechschmidt/massdns

**Alternatives:** dnsx, dig






## Pivoting & Tunneling




#### Tunneling Frameworks



##### Reverse & Forward Tunnels



###### chisel ⭐

Single-binary TCP/UDP tunnel over HTTP(S) with reverse and SOCKS5 modes; one client, one server, no special privileges.

**When:** Run a chisel client on a host you own and forward ports back through an HTTP egress that filters plain SOCKS.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/jpillora/chisel@latest`

**URL:** https://github.com/jpillora/chisel

**Alternatives:** frp, ligolo-ng


###### frp

Fast reverse proxy that exposes local services behind NAT via a public server; config-driven with TLS, auth, and load balancing.

**When:** Stable exposure of lab services or a pivot point behind restrictive NAT you control.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `wget https://github.com/fatedier/frp/releases/latest/download/frp_linux_amd64.tar.gz && tar xzf frp_linux_amd64.tar.gz`

**URL:** https://github.com/fatedier/frp

**Alternatives:** chisel, stowaway


###### stowaway

Multi-hop proxy chain builder (agent/admin model) supporting TCP/UDP and dynamic forwards chained across several hops.

**When:** Build long multi-hop chains across several hosts you control when a single tunnel is insufficient.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/ph4ntonn/Stowaway && cd Stowaway/Client && go build`

**URL:** https://github.com/ph4ntonn/Stowaway

**Alternatives:** chisel, frp, ligolo-ng


###### rpivot

SOCKS4 reverse proxy: a client on an internal host you own connects out through your listening server, opening a tunnel into that internal network.

**When:** When the internal host can egress only toward your server; lightweight Python, no agent install beyond the script.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/klsecservices/rpivot`

**URL:** https://github.com/klsecservices/rpivot

**Alternatives:** chisel, ligolo-ng


##### VPN-style / TUN Pivots



###### ligolo-ng ⭐

TUN-based tunneling: the agent builds an encrypted tunnel to your proxy, which routes full IP traffic into the agent's network as if you had a real VPN.

**When:** Full network pivoting across a host you own — route arbitrary hosts/subnets without per-port forwarding.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `go install github.com/nicocha30/ligolo-ng/cmd/proxy@latest && go install github.com/nicocha30/ligolo-ng/cmd/agent@latest`

**URL:** https://github.com/nicocha30/ligolo-ng

**Alternatives:** chisel, sshuttle


#### Traffic Routing & Proxy Chains



##### Process & System Routing



###### proxychains ⭐

Forces any TCP client through a chain of HTTP/SOCKS proxies by shimming its socket calls via LD_PRELOAD.

**When:** Route existing CLIs through your tunnel(s) without rewriting them — proxychains nmap <target>.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install proxychains4`

**URL:** https://github.com/haad/proxychains

**Alternatives:** sshuttle, socat


###### sshuttle

Transparent VPN over SSH that forwards arbitrary TCP/UDP/DNS for whole subnets through an SSH connection without per-port forwards.

**When:** Pivot your whole routing table through a jump host you administer using just an SSH key.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install sshuttle`

**URL:** https://github.com/sshuttle/sshuttle

**Alternatives:** ligolo-ng, proxychains


##### Raw Socket Relays & Plumbing



###### socat ⭐

Bidirectional relay between TCP, UDP, UNIX sockets, and files, with SSL and FORK support — the byte-plumbing workhorse.

**When:** Expose or forward services between hosts, wrap TLS around a plaintext target, or daemonize a listener in controlled lab setups.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install socat`

**URL:** http://www.dest-unreach.org/socat/

**Alternatives:** ncat, proxychains


###### Ncat

Nmap's netcat with TLS, proxy chaining, IPv6, and connection brokering built into a MIT-licensed binary.

**When:** Read/write test a service, grab a banner, or relay a plaintext session without extra tooling.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install ncat`

**URL:** https://nmap.org/ncat/

**Alternatives:** socat






## Traffic Capture & On-Path Testing




#### Capture & Analysis



##### Live Capture



###### Wireshark ⭐

Graphical packet analyzer decoding hundreds of protocols with stream following, session reassembly, and deep dissection.

**When:** Investigate a specific conversation or replay a .pcap from your network — the closest thing to seeing the bytes yourself.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install wireshark`

**URL:** https://www.wireshark.org

**Alternatives:** tshark, tcpdump


###### tshark

Wireshark's terminal sibling: captures and dissects live or file traffic with the full dissector set and JSON/CSV field output.

**When:** Capture or parse on a headless host and pipe structured output into scripts.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install tshark`

**URL:** https://www.wireshark.org/docs/man-pages/tshark.html

**Alternatives:** tcpdump, Wireshark


###### tcpdump

Command-line packet capture with Berkeley Packet Filter expressions; the standard for headless and rolling capture.

**When:** Capture on a server you administer or dump to files with -w for later analysis — trivially scriptable.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install tcpdump`

**URL:** https://www.tcpdump.org

**Alternatives:** tshark, Wireshark


##### Session & Stream Reassembly



###### tcpflow ⭐

Reassembles TCP sessions from captures into per-connection files, reconstructing transferred content instead of packet fragments.

**When:** Pull actual payloads (files, HTTP bodies, plaintext credentials) out of a .pcap you own.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install tcpflow`

**URL:** https://github.com/simsong/tcpflow

**Alternatives:** Wireshark, tshark


#### On-Path & MITM Frameworks



##### LAN / ARP Interception



###### bettercap ⭐

Modular MITM framework — ARP/DNS/DHCP spoofing, sniffing, HTTP proxies — with an interactive shell, caplets, and a REST API.

**When:** Full-featured on-path testing on a network you operate: spoof, sniff, and log plaintext from clients you control.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install bettercap`

**URL:** https://www.bettercap.org

**Alternatives:** ettercap, Responder, mitmproxy


###### ettercap

Classic MITM suite with ARP poisoning, sniffing, filters, and plugin-based interception of plaintext protocols.

**When:** Traditional LAN MITM lab work when you want the legacy plugin and filter ecosystem.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install ettercap-text-only`

**URL:** https://www.ettercap-project.org

**Alternatives:** bettercap, Responder


##### Application Proxy Interception



###### mitmproxy ⭐

Interactive HTTPS interception proxy with a terminal UI and Python addons for rewriting and scripting flows.

**When:** Inspect or rewrite HTTP(S) from an app or device you control, with mitmproxy's CA explicitly trusted on that device.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** bettercap, Responder


##### Name-Resolution Poisoning



###### Responder ⭐

LLMNR/NBT-NS/mDNS poisoner that answers resolution queries on a segment you operate and logs the Net-NTLMv1/v2 hashes clients send to it.

**When:** Validate whether your own Windows clients leak credentials when their resolver goes quiet — to justify disabling LLMNR/NBT-NS.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install responder`

**URL:** https://github.com/lgandx/Responder

**Alternatives:** mitm6, bettercap


###### mitm6

Poisons DNS via IPv6 router advertisements so Windows clients look up WPAD and other names through your server on the v6 network.

**When:** Test IPv6 spoofing of your own dual-stack Windows clients to confirm mitigations (WPAD removal, RA filtering) are in place.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `pipx install mitm6`

**URL:** https://github.com/dirkjanm/mitm6

**Alternatives:** Responder


#### Packet Crafting & Raw Probes



##### Raw Packet Crafting



###### hping3 ⭐

Crafts custom TCP/UDP/ICMP packets via raw sockets with hand-tuned flags, timing, payloads, and fragmentation.

**When:** Probe how your own firewalls treat malformed or flagged packets, or test a service on non-standard ports.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install hping3`

**URL:** http://www.hping.org/

**Alternatives:** Scapy, nmap


###### Scapy

Python packet library for crafting, forging, and dissecting virtually any protocol; can send, sniff, capture, and fuzz from a REPL or scripts.

**When:** Build bespoke probes or protocol fuzzers for your own services when off-the-shelf tools cannot express the exact packet.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install python3-scapy`

**URL:** https://scapy.net

**Alternatives:** hping3, nmap






## Network Service Clients & Auditing




#### Directory & Management Protocols



##### SNMP Auditing



###### snmpwalk ⭐

Net-SNMP's tree walker: pulls entire OID subtrees (sysDescr, interfaces, processes, routing) when a community string is read-accessible.

**When:** Dump as much SNMP-visible detail as possible from one of your managed devices using the read community after discovery.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install snmp`

**URL:** https://github.com/net-snmp/net-snmp

**Alternatives:** snmp-check, onesixtyone


###### snmp-check

Perl enumerator that turns SNMP walks into human-readable reports — system, network, routing, and listening ports in one shot.

**When:** Quick presentation-ready SNMP summary of a device you manage without memorizing OIDs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install snmpcheck`

**URL:** http://www.nothink.org/codes/snmpcheck/index.php

**Alternatives:** snmpwalk, onesixtyone


###### onesixtyone

Fast SNMP scanner that blasts sysDescr requests across a range with multiple community strings and logs responders.

**When:** Discover which of your own network devices run SNMP with default or weak read communities across a whole estate.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install onesixtyone`

**URL:** https://github.com/trailofbits/onesixtyone

**Alternatives:** snmpwalk, snmp-check


##### LDAP & Directory Auditing



###### ldapsearch ⭐

OpenLDAP's query client: filters, attribute selection, base DN control, and search limits for directory interrogation.

**When:** Query directory objects (users, groups, OUs, attributes) on a directory you administer or are authorized to audit.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install ldap-utils`

**URL:** https://github.com/openldap/openldap

**Alternatives:** ldapdomaindump


###### ldapdomaindump

Dumps Active Directory users, computers, groups, nested memberships, GPOs, and more from a single LDAP query with any valid account.

**When:** One-shot AD network object dump for analysis and reporting during an authorized directory audit.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install ldapdomaindump`

**URL:** https://github.com/dirkjanm/ldapdomaindump

**Alternatives:** ldapsearch


#### File Share & Storage Protocols



##### SMB / NetBIOS



###### Clients & Share Enumeration



###### smbclient ⭐

Samba's SMB/CIFS client for browsing, listing, and transferring files against Windows and Samba shares with full auth options.

**When:** Test share access and anonymous or null listings on hosts you operate before deeper tooling.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install smbclient`

**URL:** https://www.samba.org/samba/

**Alternatives:** enum4linux-ng, NetExec, rpcclient


###### enum4linux-ng

Maintained Python successor to enum4linux; automates SMB/RPC null-session enumeration of users, shares, password policy, and sessions.

**When:** Complete legacy SMB enumeration (users, shares, policy) in one command against an assessed host.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pipx install git+https://github.com/cddmp/enum4linux-ng`

**URL:** https://github.com/cddmp/enum4linux-ng

**Alternatives:** smbclient, NetExec, rpcclient


###### Fleet & Protocol Audits



###### NetExec ⭐

Successor to CrackMapExec: multi-protocol (SMB, LDAP, MSSQL, WinRM, RDP) credential-validated enumeration of shares, users, sessions, and policy across fleets.

**When:** Credentialed health-check across many Windows hosts at once during an authorized assessment — who is admin where, which shares are open.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install git+https://github.com/Pennyw0rth/NetExec`

**URL:** https://github.com/Pennyw0rth/NetExec

**Alternatives:** Impacket, smbclient, CrackMapExec (predecessor)


###### Impacket

Fortra's Python implementations of Windows network protocols with ~100 example scripts — smbclient, secretsdump, psexec, wmiexec, getTGT, and more.

**When:** Protocol-level SMB/RPC/directory work from Linux when you need scriptable, low-level control over the wire.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install impacket`

**URL:** https://github.com/fortra/impacket

**Alternatives:** NetExec, smbclient


##### NFS & RPC



###### showmount ⭐

Queries the NFS mount daemon for exported filesystems (showmount -e) on NFS servers, listing paths and export flags.

**When:** Enumerate which NFS exports a host you operate offers, and with what flags — first step before any mount testing.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install nfs-common`

**URL:** http://www.linux-nfs.org/

**Alternatives:** rpcclient


###### rpcclient

Samba's RPC client that interrogates MS-RPC endpoints — user, domain, SID, and session lookups, often over null sessions.

**When:** Legacy SMB/RPC enumeration (SID and user queries) when standard SMB clients are blocked on a network you're authorized to test.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install samba-client`

**URL:** https://www.samba.org/samba/

**Alternatives:** smbclient, enum4linux-ng


#### Remote Access Protocols



##### RDP Clients



###### xfreerdp ⭐

FreeRDP's client: connects over RDP from the CLI with drive and clipboard forwarding, screenshots, and full NLA support.

**When:** Access a Windows RDP host you manage for GUI testing, session capture, or share-mount tests.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install freerdp2-x11`

**URL:** https://github.com/FreeRDP/FreeRDP

**Alternatives:** rdesktop


###### rdesktop

Veteran open-source RDP client with single-session support and configurable codec and bitmap options.

**When:** Lightweight RDP client for older Windows services where FreeRDP is overkill.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install rdesktop`

**URL:** https://github.com/rdesktop/rdesktop

**Alternatives:** xfreerdp


##### SSH Configuration Audits



###### ssh-audit ⭐

Actively probes an SSH server and scores its configuration — kex, ciphers, MACs, key types — against known weaknesses and current advisories.

**When:** Audit the SSH policy of your own hosts; ships CI-friendly JSON and HTML report output.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pipx install ssh-audit`

**URL:** https://github.com/jtesta/ssh-audit

**Alternatives:** nmap (ssh2-enum-algos)


##### FTP & File Transfer



###### lftp ⭐

Feature-rich FTP/FTPS/SFTP/HTTP client with mirroring, resuming, scripting, and batch transfers.

**When:** Poke an FTP service you run: anonymous-login checks, recursive listing, and large recursive mirrors.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install lftp`

**URL:** https://lftp.yar.ru

**Alternatives:** curl





