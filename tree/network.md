# 📡 Network Attacks & Analysis

Packet capture, on-path interception, host discovery, and connectivity utilities for understanding and testing traffic on networks you operate.

## Packet Capture & Analysis

### Wireshark ⭐

Graphical packet analyzer that decodes hundreds of protocols, follows TCP streams, and reassembles sessions live or from a saved capture.

**When:** See the actual bytes and protocol conversations behind a traffic sample, or replay an issue from a .pcap taken on a machine you control.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install wireshark`

**URL:** https://www.wireshark.org

**Alternatives:** tshark, tcpdump, tcpflow


### tcpdump

Command-line packet capture using Berkeley Packet Filter (BPF) expressions; the standard for headless logging and scripted sniffing.

**When:** On servers, routers, or lab hosts where no GUI exists, or when writing a rolling capture to a file for later analysis.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install tcpdump`

**URL:** https://www.tcpdump.org

**Alternatives:** tshark, wireshark


### tshark

Wireshark's terminal sibling: captures, decrypts, and prints live or offline traffic with the full dissector set and CSV/JSON output.

**When:** Get Wireshark-grade dissection piped into grep, awk, or analysis scripts without launching a GUI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install tshark`

**URL:** https://www.wireshark.org/docs/man-pages/tshark.html

**Alternatives:** tcpdump, wireshark


### tcpflow

Reassembles TCP sessions from a capture into separate per-connection files, ignoring lower-level packet noise.

**When:** Reconstruct actual transferred content (files, HTTP bodies) from a .pcap you own instead of inspecting packets one at a time.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install tcpflow`

**URL:** https://github.com/simsong/tcpflow

**Alternatives:** wireshark, tshark


## On-Path & Interception Frameworks

### bettercap ⭐

Modular framework for MITM, ARP/DNS/DHCP spoofing, and credential sniffing with an interactive shell and RESTful API for scripting.

**When:** On a network you operate, to test which plaintext protocols (HTTP, FTP, telnet) leak over the wire and how clients react to spoofing.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install bettercap`

**URL:** https://www.bettercap.org

**Alternatives:** mitmproxy, responder


### mitmproxy

Interactive HTTPS interception proxy with a terminal UI, Python addon scripting, and TLS interception via its own CA you install on your devices.

**When:** Inspect and rewrite HTTP/HTTPS traffic from an app, device, or CLI you control, with the proxy cert explicitly trusted on that device.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pip install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** bettercap


### responder

Answers LLMNR/NBT-NS/mDNS name-resolution queries on a subnet and logs or relays credentials passed over those protocols to its own listeners.

**When:** Test Windows-style authentication flows in a lab and check whether clients will send net-NTLM hashes when their expected resolver goes silent.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install responder`

**URL:** https://github.com/lgandx/Responder

**Alternatives:** bettercap


## Host Discovery & Network Mapping

### arp-scan ⭐

Sends ARP requests to every address in a subnet and lists live hosts by IP and MAC/OUI vendor; the most reliable way to map a local network.

**When:** First step when on a network you administer: enumerate every physical host on the LAN, since ARP is answered even where ICMP is filtered.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install arp-scan`

**URL:** https://github.com/royhills/arp-scan

**Alternatives:** netdiscover, fping


### netdiscover

Active and passive ARP-based host discovery with a live-updating table of MAC address, vendor, and IP.

**When:** Continuous visual recon of a local network, or a quick live view while monitoring the LAN over time.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install netdiscover`

**URL:** https://github.com/netdiscover-scanner/netdiscover

**Alternatives:** arp-scan, fping


### fping

Bulk ICMP pinger that sweeps a range of targets in parallel and prints alive/dead results in a script-friendly stream.

**When:** Fast liveness check of a large IP range when hosts are off-subnet, where ARP-based discovery cannot reach.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install fping`

**URL:** https://fping.org

**Alternatives:** arp-scan, netdiscover


## Connectivity & Packet Crafting

### socat ⭐

Bidirectional relay that forwards, listens on, and connects across TCP, UDP, UNIX sockets, and files; flexible byte plumbing for testing services.

**When:** Expose a local service through a relay, forward ports between lab hosts, or inject/monitor raw data flows in ad-hoc setups.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install socat`

**URL:** http://www.dest-unreach.org/socat/

**Alternatives:** ncat, proxychains


### ncat

Nmap's free, MIT-licensed netcat: connect, listen, and relay TCP/UDP with TLS, proxy modes, and easy scripting built in.

**When:** Quick read/write tests against a listening port, banner grabbing, or one-shot TCP/UDP checks while debugging connectivity.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install ncat`

**URL:** https://nmap.org/ncat/

**Alternatives:** socat, netcat-openbsd (netcat-free)


### hping3

Packet-crafting tool that builds custom TCP/UDP/ICMP packets via raw sockets, with control over flags, timing, and fragmentation.

**When:** Answer questions like "does this firewall actually drop that flagged packet?" by sending hand-crafted probes from a host you control.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install hping3`

**URL:** http://www.hping.org/

**Alternatives:** nmap (recon)


### proxychains

Routes any TCP client through a strict, random, or dynamic chain of HTTP/SOCKS proxies, forcing connections out via chosen exits.

**When:** Test whether an application can be tunneled through proxies and observe the egress path a tool takes in controlled lab scenarios.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install proxychains4`

**URL:** https://github.com/haad/proxychains

**Alternatives:** socat, ncat


## DNS & IP Utilities

### dig ⭐

The standard DNS query tool from the BIND suite: any record type, MX priority, zone-transfer attempts, and query tracing against a chosen resolver.

**When:** Resolve names in isolation, verify records against a specific server, or trace how a lookup flows through resolvers in one command.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install dnsutils`

**URL:** https://www.isc.org/bind/

**Alternatives:** whois


### whois

Queries WHOIS/registration databases for domain ownership, registrar, name servers, and IP allocation details.

**When:** Collect registrant, registrar, and registration dates for a domain, or the owning organization of an IP range, before deeper analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install whois`

**URL:** https://github.com/rfc1036/whois

**Alternatives:** dig

