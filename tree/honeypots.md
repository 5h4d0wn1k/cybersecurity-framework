# 🍯 Honeypots & Deception Technology

Deception for defenders: fake services, canaries, honeynets, and tripwires placed inside your own estate to catch attackers early and learn their methods.

## Deception Platforms & Honeynets



#### honeynet ◆ by 5h4d0wn1k

Honeypot farm + deception grid — multi-protocol honeypots, attacker fingerprinting, dwell/risk scoring, quarantine.

**When:** Deploying decoys on ranges you own to observe attacker behavior.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/honeynet`

**URL:** https://github.com/5h4d0wn1k/honeynet

**Alternatives:** Own tool — lab/authorized use only


#### All-in-One Platforms


##### T-Pot ⭐

Bundles 20+ honeypots (Cowrie, Dionaea, Conpot, Snare, Log4Pot, qeeqbox) behind one Docker Compose deploy, with the Elastic stack, Kibana dashboards, Suricata, and a live attack map from the German PSNC/Telekom Security team.

**When:** Stand up a whole instrumented honeynet with dashboards in a weekend instead of wiring sensors together — the standard starting point for a lab or personal deception farm.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `env bash -c "$(curl -sL https://github.com/telekom-security/tpotce/raw/master/install.sh)"`

**URL:** https://github.com/telekom-security/tpotce

**Alternatives:** HFish, Modern Honey Network


##### HFish

Golang-based enterprise honeypot platform (HackLC) shipping SSH, Telnet, FTP, Redis, MySQL, VNC, HTTP(S), and deep-module decoys with a web dashboard, alerting, and distributed-cluster support.

**When:** When you want a corporate-feel deception console with many built-in service decoys and low operational overhead beyond T-Pot's all-Docker weight.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `bash <(curl -sL https://raw.githubusercontent.com/hacklcx/HFish/master/docs/webinstall.sh)`

**URL:** https://github.com/hacklcx/HFish

**Alternatives:** T-Pot, Modern Honey Network


##### Modern Honey Network

Centralized server and web UI that deploys sensors (Cowrie, Dionaea, Conpot, Glastopf) over SSH and aggregates events via HPFeeds into Elasticsearch for viewing and searching.

**When:** Fleet-manage many sensors from one Python-2-era control plane on an older distro — expect friction, as the project is effectively unmaintained and community forks carry the torch.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/pwnlandia/mhn && cd mhn && ./install.sh`

**URL:** https://github.com/pwnlandia/mhn

**Alternatives:** T-Pot, HFish


#### Sensor Orchestration & Event Transport


##### HPFeeds ⭐

Honeynet Project's authenticated publish-subscribe protocol that ships JSON and binary honeypot events (dionaea.capture, cowrie.sessions, conpot.events) from sensors to collectors, MISP, ELK, and SIEMs.

**When:** The glue beneath MHN, T-Pot, and community honeynets once you run several sensors: consume structured channels instead of scraping individual logs.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -p 20000:20000 -p 9431:9431 hpfeeds/hpfeeds-broker:latest`

**URL:** https://github.com/hpfeeds/hpfeeds

**Alternatives:** T-Pot, honeynet-filebeat


##### honeynet-filebeat

Honeynet Project's custom Filebeat image for shipping T-Pot and honeypot JSON logs from sensors to a central Elasticsearch cluster without inventing your own transport.

**When:** Batch-forward tpot/honeypot logs to your existing ELK or SIEM pipeline when you are not using an HPFeeds-based collector.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/honeynet-filebeat && cd honeynet-filebeat && docker build -t honeynet-filebeat .`

**URL:** https://github.com/honeynet/honeynet-filebeat

**Alternatives:** HPFeeds



## Network Service Honeypots



#### SSH & Telnet


##### Medium-interaction Fake-shell emulators


###### Cowrie ⭐

Medium-to-high interaction SSH and Telnet honeypot that emulates a fake UNIX filesystem, logs every keystroke and transferred file, records replayable sessions, and can proxy to real boxes.

**When:** The default SSH honeypot — let credential stuffers 'win' and replay exactly what a post-breach attacker does, from recon commands to malware staging.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `docker run -p 2222:2222 cowrie/cowrie:latest`

**URL:** https://github.com/cowrie/cowrie

**Alternatives:** Beelzebub, sshesame


###### kippo

The original medium-interaction SSH honeypot whose fake 'ubuntu' root shell recorded replayable TTY sessions; Cowrie is its direct fork and successor.

**When:** Never for fresh deployments — read its Python-2 source and session-replay utilities to understand how Cowrie's fake-shell design evolved.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/desaster/kippo && cd kippo && pip install -r requirements.txt`

**URL:** https://github.com/desaster/kippo

**Alternatives:** Cowrie


###### Beelzebub

Low-code Go deception runtime (a T-Pot 24.04 component) that serves YAML-defined decoy SSH, HTTP, TCP, Telnet, and MCP services, with LLM backends generating convincing real-time replies.

**When:** When static command emulation is too thin and you want adaptive high-interaction engagement plus prompt-injection traps, with an OpenAI or local Ollama key in hand.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/mariocandela/beelzebub && cd beelzebub && docker compose up -d`

**URL:** https://github.com/mariocandela/beelzebub

**Alternatives:** Cowrie, sshesame


##### Lightweight telemetry decoys


###### sshesame ⭐

Go-based fake SSH server that lets any login through, never executes anything, and logs channels, requests, commands, and port-forward activity as JSON.

**When:** A one-binary lab or public decoy when you want configurable, JSON-logged session telemetry without emulating a whole filesystem.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget https://github.com/jaksi/sshesame/releases/download/v0.0.39/sshesame-linux-amd64 && chmod +x sshesame-linux-amd64 && ./sshesame`

**URL:** https://github.com/jaksi/sshesame

**Alternatives:** ssh-honeypot, Cowrie


###### ssh-honeypot

C-based fake sshd (droberson) that accepts connections and logs IP, username, and password plus HASSH-fingerprints the SSH client — without granting a shell.

**When:** When you care only about brute-force credential and client-fingerprint telemetry with a tiny footprint, not full shell-level interaction.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `apt install libssh-dev libjson-c-dev libpcap-dev libssl-dev && make`

**URL:** https://github.com/droberson/ssh-honeypot

**Alternatives:** sshesame, Cowrie


#### SMB, FTP & File Services


##### Dionaea ⭐

Nepenthes-successor low-interaction honeypot emulating SMB, FTP, HTTP, MSSQL, MySQL, SIP, UPnP, and more; embeds Python, uses libemu to detect captured shellcode, and stashes malware binaries.

**When:** Attract self-spreading worms and malware ripping over SMB/FTP/MS-RPC and capture their payloads, complementing a credential-focused SSH honeypot.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -it -p 21:21 -p 445:445 -p 1433:1433 -p 3306:3306 -p 5060:5060 dinotools/dionaea`

**URL:** https://github.com/DinoTools/dionaea

**Alternatives:** HoneyPy, glutton


##### HoneyPy

Python low-to-medium interaction honeypot (fooSpider/Twisted) with plugins for SMTP, FTP, POP3, IMAP, SSH, Telnet, Elasticsearch, and more, plus Twitter and HoneyDB loggers (archived 2024).

**When:** When you want one lightweight daemon with pluggable protocol emulation and HoneyDB/Redis-backed logging — treat it as legacy but stable.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/foospidy/HoneyPy && cd HoneyPy && pip install -r requirements.txt && python Honey.py -c etc/honeypy.cfg`

**URL:** https://github.com/foospidy/HoneyPy

**Alternatives:** Dionaea, qeeqbox honeypots


#### Web Application


##### Snare + TANNER ⭐

Glastopf's successor: SNARE clones real web pages into sensor traps and forwards every request to TANNER, a central classification service that evaluates the attack and decides the reply.

**When:** Realistic web deception with a central 'brain': point several SNARE clones at one TANNER to store, classify, and steer web-application attack responses.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/mushorg/snare && cd snare && pip3 install -r requirements.txt && python3 setup.py install`

**URL:** https://github.com/mushorg/snare

**Alternatives:** Glastopf, Dionaea


##### Glastopf

Honeynet Project's original web-application honeypot emulating vulnerability types (LFI/RFI/SQLi) with a built-in PHP sandbox and Google dork luring; archived, with maintainers pointing to SNARE/TANNER.

**When:** Historical study only: inspect the PHP-sandbox emulation and dork-collection design to learn how modern web honeypots behave — do not deploy fresh.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip install glastopf`

**URL:** https://github.com/mushorg/glastopf

**Alternatives:** Snare + TANNER, Dionaea


#### Multi-protocol & Lightweight Sensors


##### glutton ⭐

Honeynet Project's generic low-interaction honeypot written in Go that proxies connections through PIPELINE-like protocol emulation and can chain to real services for high-interaction depth.

**When:** When you want a protocol-agnostic sensor that buffers, parses, and replays many TCP service interactions and can fail over into a real honeypot backend.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `go install github.com/mushorg/glutton@latest`

**URL:** https://github.com/mushorg/glutton

**Alternatives:** qeeqbox honeypots, HoneyPy


##### qeeqbox honeypots

30 low-to-high interaction honeypots in one PyPI package: dhcp, dns, elastic, ftp, http(s), imap, ldap, mssql, mysql, ntp, pop3, postgres, rdp, redis, sip, smb, smtp, snmp, socks5, ssh, telnet, vnc.

**When:** Spin up many protocol decoys in seconds with one pip install and simple --setup flags, or embed sensors inside T-Pot where it ships as a component.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install honeypots && honeypots --setup ssh,smtp,dns`

**URL:** https://github.com/qeeqbox/honeypots

**Alternatives:** glutton, HoneyPy


##### honeyd

Classic low-interaction daemon (Niels Provos) that fabricates thousands of virtual hosts with spoofed OS personalities and configurable fake TCP/UDP services on unused IP space.

**When:** Instrument a whole dark/empty subnet rather than a single box — legacy research tooling (last original release 2007) built from the hobbyist-maintained fork.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/cowrie/honeyd && cd honeyd && mkdir build && cd build && cmake .. && sudo make install`

**URL:** https://github.com/cowrie/honeyd

**Alternatives:** glutton, T-Pot


#### ICS, OT & Device Deception


##### Conpot ⭐

Honeynet Project's ICS/SCADA honeypot emulating Modbus, S7, BACnet, EtherNet/IP, IEC-104, SNMP, and HTTP HMI stacks with tunable response delays to look like a real industrial process.

**When:** Detect and profile OT/SCADA targeting — plant a fake PLC/HMI on your network before adversaries reach real controllers.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run -it -p 80:80 -p 102:102 -p 502:502 -p 161:161/udp honeynet/conpot /bin/sh`

**URL:** https://github.com/mushorg/conpot

**Alternatives:** RIoTPot, DICOMHawk


##### RIoTPot

Honeynet Project's IoT/OT hybrid proxy honeypot that fronts emulated SSH, Telnet, HTTP, Modbus, MQTT, and CoAP services and can route interactions to any backend honeypot via a web UI.

**When:** When your focus is IoT/OT protocol coverage (MQTT, CoAP, Modbus) and you want a Honeynet-endorsed plugin-architected emulator — expect a young, source-built project.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/riotpot && cd riotpot && make`

**URL:** https://github.com/honeynet/riotpot

**Alternatives:** Conpot, qeeqbox honeypots


##### DICOMHawk

Honeynet Project's DICOM (medical imaging) honeypot that detects and logs unauthorized access attempts against radiology PACS/DICOM endpoints that attackers increasingly probe.

**When:** Deploy where healthcare DICOM devices must not be reached directly — catch unauthorized modality/PACS scans in medical environments.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/DICOMHawk && cd DICOMHawk && pip install -r requirements.txt`

**URL:** https://github.com/honeynet/DICOMHawk

**Alternatives:** Conpot, sweetcam


##### sweetcam

Honeynet Project's IP-camera honeypot: lures attackers with a fake webcam admin stream and logs their interactions, mirroring the flood of IoT camera scanning.

**When:** When you want decoys that mimic the most-scanned IoT device category on your network to catch and log automated camera/IP-cam exploitation.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/sweetcam && cd sweetcam && python -m http.server 8080`

**URL:** https://github.com/honeynet/sweetcam

**Alternatives:** RIoTPot, Conpot



## Email, DNS & Communication Decoys



#### SMTP & Email


##### Mailoney ⭐

Modern low-interaction SMTP honeypot (2.x rewrite) that simulates a vulnerable mail server, captures auth attempts and credentials, and stores sessions in PostgreSQL; ships AS open-relay and Postfix-cred modules.

**When:** Detect spam, credential-harvesting, and open-relay abuse on port 25 while keeping structured DB logs you can feed your SIEM.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/phin3has/mailoney && cd mailoney && docker compose up -d`

**URL:** https://github.com/phin3has/mailoney

**Alternatives:** mailhon, hermes


##### mailhon

Minimalistic Python3 SMTP honeypot built on aiosmtpd that emulates an open relay and writes every interaction as JSON to a log file.

**When:** When you want a tiny, dependency-light open-relay decoy that logs JSON for quick parsing without a database layer.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/CMSecurity/mailhon && cd mailhon && pip3 install -r requirements.txt && python3 main.py`

**URL:** https://github.com/CMSecurity/mailhon

**Alternatives:** Mailoney, hermes


##### hermes

Avast's SMTP honeypot built on the Salmon mail server with SMTP AUTH support, exim4 integration, MQTT telemetry, and configurable relay policy to sieve real spam flows.

**When:** When you need a fuller-featured SMTP sink with AUTH and relay controls, saving attachments and eml files for analysis, over the simplest cred-capturing daemons.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/avast/hermes && cd hermes && docker build -t hermes . && docker run -p 25:25 hermes`

**URL:** https://github.com/avast/hermes

**Alternatives:** Mailoney, mailhon


#### DNS Decoys


##### dns-honeypot ⭐

Simple low-interaction DNS honeypot in Python/Twisted that answers queries on 53/5353 and logs every lookup, surfacing scan and exfil-style DNS traffic.

**When:** A cheap tripwire for DNS probing and suspicious query patterns on a segment where only your resolver should be queried.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/0xNslabs/dns-honeypot && cd dns-honeypot && pip install twisted && python3 dns.py --host 0.0.0.0 --port 53`

**URL:** https://github.com/0xNslabs/dns-honeypot

**Alternatives:** FakeDns, qeeqbox honeypots


##### FakeDns

Regular-expression based Python DNS server that resolves against a config or proxies unmatched queries upstream; the classic for DNS-tunneling and rebinding deception during engagements.

**When:** When you want regex-ruled DNS answers (rebinding, round-robin) that log every query, ideal for malware C2/DNS-exfil detection labs.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/Crypt0s/FakeDns && cd FakeDns && ./fakedns.py -c dns.conf.example -i 10.0.0.1`

**URL:** https://github.com/Crypt0s/FakeDns

**Alternatives:** dns-honeypot, qeeqbox honeypots



## Tokens, Canaries & Tripwires

Canarytokens ⭐

#### Canarytokens ⭐

Thinkst's free hosted (or self-hosted Docker) tripwire factory generating DNS, URL, document (PDF/Word), AWS-key, QR-code, and Slack tokens that alert by email/webhook the instant someone touches them.

**When:** A full honeypot is overkill: sprinkle fake DNS names, URLs, or documents across AD, share drives, and public infra for cheap, near-instant detection of unauthorized access.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (canarytokens.org) - self-host: git clone https://github.com/thinkst/canarytokens-docker && docker compose up`

**URL:** https://github.com/thinkst/canarytokens

**Alternatives:** OpenCanary


#### OpenCanary

Thinkst's open-source multi-protocol honeypot daemon (SSH, telnet, HTTP, FTP, SNMP, SMB, RDP, MySQL, ...) that fires syslog, email, Slack, and webhook alerts on any probe.

**When:** Drop a near-zero-footprint daemon onto a jump host, file server, or DMZ and get alerting on unexpected interaction across ~10 protocols at once.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install opencanary && opencanaryd --copyconfig`

**URL:** https://github.com/thinkst/opencanary

**Alternatives:** Canarytokens, qeeqbox honeypots



## Monitoring, Logging & Analysis



#### Attack Analysis & Visualization


##### ochi ⭐

Honeynet Project's Go-based network visualization showing co-occuring attack ports, source ASNs, and services across your honeypot logs in an interactive graph.

**When:** Understand, present, and spot patterns in attacker traffic after the honeypots have run — the visualization Honeynet themselves use.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/ochi && cd ochi && go build && ./ochi`

**URL:** https://github.com/honeynet/ochi

**Alternatives:** T-Pot Kibana, GreedyBear


##### GreedyBear

Threat-intel platform for T-Pot deployments that ingests honeypot events via Elasticsearch, flags malicious IPs, maintains feeds, and publishes T-Pot-derived IOCs to ThreatFox.

**When:** Turn your T-Pot farm's captures into a continuous IOC feed for your SIEM or ThreatFox instead of leaving payloads and IPs stuck in logs.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/GreedyBear-Project/GreedyBear && cd GreedyBear && docker compose up`

**URL:** https://github.com/GreedyBear-Project/GreedyBear

**Alternatives:** ochi, ThreatFox


#### Vulnerability-decoy Sinks


##### Log4Pot ⭐

Low-interaction honeypot for the Log4Shell (CVE-2021-44228) family: detects exploitation in request lines and headers, deobfuscates JNDI payloads, and recursively downloads exploit payloads.

**When:** Catch and study Log4j/Log4Shell exploitation attempts on ports where vulnerable Java apps might sit, and collect the payloads attackers drop.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/thomaspatzke/Log4Pot && cd Log4Pot && pip install -r requirements.txt && python log4pot.py @log4pot.conf`

**URL:** https://github.com/thomaspatzke/Log4Pot

**Alternatives:** minecraft-log4j-honeypot


##### minecraft-log4j-honeypot

Go honeypot that runs a fake Minecraft server waiting to be hit by Log4Shell exploit variants targeting the game, saving captured payload classes to disk.

**When:** Monitor for Log4j scanning aimed at game servers and other odd ports where naive exploit attempts still land.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `docker run --rm -it -p 25565:25565 adikso/minecraft-log4j-honeypot:latest`

**URL:** https://github.com/Adikso/minecraft-log4j-honeypot

**Alternatives:** Log4Pot


#### Honeypot Scouting & QA


##### honeyscanner ⭐

Honeynet Project's vulnerability analyzer that automatically attacks a given honeypot to determine whether it is vulnerable to specific attack families (DDoS, sploit, fuzz, ssh).

**When:** QA your own honeypots before exposing them: prove a decoy is safe to face the internet and characterize what it can and cannot absorb.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/honeyscanner && cd honeyscanner && pipenv install && pipenv shell`

**URL:** https://github.com/honeynet/honeyscanner

**Alternatives:** checkpot


##### checkpot

Honeynet Project's Honeypot Checker (GSoC 2018): validates honeypot containers and checks whether deployed honeypots detect, replay, and act correctly on attacks.

**When:** Regression-test a fleet of honeypot containers after upgrading or building new sensors — the scouting companion to honeyscanner's vuln assessment.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/honeynet/checkpot && cd checkpot && docker build -t checkpot . && docker run checkpot --help`

**URL:** https://github.com/honeynet/checkpot

**Alternatives:** honeyscanner



