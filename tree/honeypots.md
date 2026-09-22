# 🍯 Honeypots & Deception Technology

Deception for defenders: fake services, canaries, honeynets, and tripwires placed inside your own estate to catch attackers early and analyze their methods.

## Honeypot Platforms & Deception Networks

T-Pot ⭐


#### T-Pot ⭐

Bundles 20+ honeypots (Cowrie, Dionaea, Conpot, Snare, Mailoney, LLM-based traps) behind one Docker Compose deploy, with the Elastic stack, Kibana dashboards, Suricata, and a live attack map from the German PSNC/Telekom Security team.

**When:** When you want a whole instrumented honeynet with dashboards in a weekend instead of wiring sensors together by hand — the standard starting point for a personal or lab deception farm.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `env bash -c "$(curl -sL https://github.com/telekom-security/tpotce/raw/master/install.sh)"`

**URL:** https://github.com/telekom-security/tpotce

**Alternatives:** mhn, hpfeeds


#### Modern Honey Network

Centralized server and web UI that deploys honeypot sensors (Cowrie, Dionaea, Conpot, Glastopf) over SSH and aggregates their events via HPFeeds into Elasticsearch for viewing and searching.

**When:** When you need fleet management of many sensors from one control plane on an older minimal distro — expect friction; the project is effectively unmaintained (Python-2 era) and the torch passes to community forks.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/pwnlandia/mhn && cd mhn && ./install.sh`

**URL:** https://github.com/pwnlandia/mhn

**Alternatives:** t-pot, hpfeeds


#### Honeyd

Classic low-interaction daemon (Niels Provos) that fabricates thousands of virtual hosts, each with a spoofed nmap/xprobe OS personality and configurable fake TCP/UDP services, on unused IP space.

**When:** When you want to instrument a whole dark/empty subnet rather than a single box — treat it as legacy research tooling (last original release 2007), built from source in the hobbyist-maintained fork.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/cowrie/honeyd && cd honeyd && mkdir build && cd build && cmake .. && sudo make install`

**URL:** https://github.com/cowrie/honeyd

**Alternatives:** t-pot, mhn


#### HPFeeds

Honeynet Project's authenticated publish-subscribe protocol that ships JSON and binary honeypot events (dionaea.capture, cowrie.sessions, conpot.events,...) from sensors to collectors, MISP, ELK, and SIEMs.

**When:** The glue beneath MHN, T-Pot, and community honeynets once you run several sensors: subscribe to each honeypot channel so your own analysis stack consumes structured events instead of you scraping logs.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `docker run -p 20000:20000 -p 9431:9431 hpfeeds/hpfeeds-broker:latest`

**URL:** https://github.com/hpfeeds/hpfeeds

**Alternatives:** t-pot, mhn






## SSH & Telnet Honeypots

Cowrie ⭐


#### Cowrie ⭐

Medium-to-high interaction SSH and Telnet honeypot that emulates a fake UNIX filesystem, logs every keystroke and transferred file, records replayable sessions, and can proxy to a real box or use LLMs for dynamic replies.

**When:** The default SSH honeypot — let credential stuffers 'win' and replay exactly what a post-breach attacker does, from recon commands to download-and-exec malware staging.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `docker run -p 2222:2222 cowrie/cowrie:latest`

**URL:** https://github.com/cowrie/cowrie

**Alternatives:** ssh-honeypot, sshesame


#### ssh-honeypot

C-based fake sshd (droberson) that accepts connections and logs IP, username, and password plus HASSH-fingerprints the SSH client — without ever granting a shell.

**When:** When you care only about brute-force credential and client-fingerprint telemetry with a tiny footprint (popular in attack/defend CTFs), not full shell-level interaction.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `apt install libssh-dev libjson-c-dev libpcap-dev libssl-dev && make && bin/ssh-honeypot -r ssh-honeypot.rsa`

**URL:** https://github.com/droberson/ssh-honeypot

**Alternatives:** cowrie, sshesame


#### sshesame

Go-based fake SSH server that lets any login through, never executes anything on the host, and logs channels, requests, commands, and port-forward activity as JSON.

**When:** A one-binary lab honeypot or public-facing decoy when you want configurable, JSON-logged session telemetry without emulating a whole filesystem.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget https://github.com/jaksi/sshesame/releases/download/v0.0.39/sshesame-linux-amd64 && chmod +x sshesame-linux-amd64 && ./sshesame`

**URL:** https://github.com/jaksi/sshesame

**Alternatives:** cowrie, ssh-honeypot


#### Beelzebub

Low-code Go deception runtime (a T-Pot 24.04 component) that serves YAML-defined decoy SSH, HTTP, TCP, Telnet, and MCP services, with LLM backends generating convincing real-time replies to keep attackers engaged.

**When:** When static command emulation is too thin and you want adaptive, high-interaction-deep engagement plus prompt-injection traps for LLM agents — with an OpenAI or local Ollama key in hand.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/mariocandela/beelzebub && cd beelzebub && docker compose up -d`

**URL:** https://github.com/mariocandela/beelzebub

**Alternatives:** cowrie, sshesame


#### kippo

The original medium-interaction SSH honeypot (Upi Tamminen) whose fake 'ubuntu' root shell lured attackers into recording complete shell interactions with replayable TTY logs; Cowrie is its direct fork and successor.

**When:** Never for fresh deployments — read its Python-2 source and session-replay utilities to understand how Cowrie's fake-shell design evolved, or mine its playback for training labs.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/desaster/kippo && cd kippo && pip install -r requirements.txt`

**URL:** https://github.com/desaster/kippo

**Alternatives:** cowrie






## Service & Web Honeypots

Dionaea ⭐


#### Dionaea ⭐

Nepenthes-successor low-interaction honeypot emulating SMB, FTP, HTTP, MSSQL, MySQL, SIP, UPnP, and more; embeds Python, uses libemu to detect captured shellcode, and stashes malware binaries and connection metadata for analysis.

**When:** When you want to attract self-spreading worms and malware that rips over SMB/FTP/MS-RPC and capture their payloads, complementing a credential-focused SSH honeypot.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -it -p 21:21 -p 445:445 -p 1433:1433 -p 3306:3306 -p 5060:5060 dinotools/dionaea`

**URL:** https://github.com/DinoTools/dionaea

**Alternatives:** snare, glastopf


#### Snare (w/ Tanner)

Glastopf's successor: SNARE clones real web pages into sensor traps and forwards every request to TANNER, a central classification service that evaluates the attack and decides the reply — dynamic camouflage across many sensors.

**When:** When you want realistic web deception with a central 'brain': point several SNARE clones at one TANNER to store, classify, and steer web-application attack responses in one place.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/mushorg/snare && cd snare && pip3 install -r requirements.txt && python3 setup.py install`

**URL:** https://github.com/mushorg/snare

**Alternatives:** glastopf, dionaea


#### Glastopf

Honeynet Project's original web-application honeypot that emulated vulnerability types (LFI/RFI/SQLi) with a built-in PHP sandbox and Google dork luring; archived, with maintainers pointing to SNARE/TANNER as the successor.

**When:** Historical study only: inspect the PHP-sandbox emulation and dork-collection design to learn how modern web honeypots behave; do not deploy to fresh systems today.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip install glastopf`

**URL:** https://github.com/mushorg/glastopf

**Alternatives:** snare (successor), dionaea






## Tokens, Tripwires & Canaries

Canarytokens ⭐


#### Canarytokens ⭐

Thinkst's free hosted (or self-hosted Docker) tripwire factory generating DNS, URL, document (PDF/Word), AWS-key, QR-code, and Slack tokens that alert by email/webhook the instant someone touches them.

**When:** When a full honeypot is overkill: sprinkle a few fake DNS names, URLs, or documents across AD, share drives, and public infra for cheap, near-instant detection of unauthorized access.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (canarytokens.org) — self-host: git clone https://github.com/thinkst/canarytokens-docker && cd canarytokens-docker && docker compose up`

**URL:** https://github.com/thinkst/canarytokens

**Alternatives:** opencanary


#### OpenCanary

Thinkst's open-source multi-protocol honeypot daemon (SSH, telnet, HTTP, FTP, SNMP, SMB, RDP, MySQL, and more) that fires syslog, email, Slack, and webhook alerts on any probe; the OSS sibling of the commercial Thinkst Canary.

**When:** Drop a near-zero-footprint daemon onto a jump host, file server, or DMZ and get alerting on unexpected interaction across ~10 common protocols at once, without standing up a sensor farm.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install opencanary && opencanaryd --copyconfig`

**URL:** https://github.com/thinkst/opencanary

**Alternatives:** canarytokens






## ICS, IoT & Hardware Deception

Conpot ⭐


#### Conpot ⭐

Honeynet Project's ICS/SCADA honeypot emulating Modbus, S7, BACnet, EtherNet/IP, IEC-104, SNMP, and HTTP HMI stacks to look like a real industrial process, with tunable service response delays for realism.

**When:** When you want to detect and profile targeting of OT/SCADA or smart-infrastructure equipment — replant a fake PLC/HMI on your own network before adversaries reach real controllers.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run -it -p 80:80 -p 102:102 -p 502:502 -p 161:161/udp honeynet/conpot /bin/sh`

**URL:** https://github.com/mushorg/conpot

**Alternatives:** riotpot


#### RIoTPot

Honeynet Project's IoT and OT honeypot: a hybrid proxy that fronts emulated services — SSH, Telnet, HTTP, Modbus, MQTT, CoAP — and can route interactions to any backend honeypot, managed through a small web UI.

**When:** When your focus is IoT/OT protocol coverage (MQTT, CoAP, Modbus) and you want a Honeynet-endorsed, plugin-architected emulator instead of gluing single-service traps — expect a young, source-built project.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/riotpot && cd riotpot && make`

**URL:** https://github.com/honeynet/riotpot

**Alternatives:** conpot





