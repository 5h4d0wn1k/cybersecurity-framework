# 📡 Wireless & Bluetooth Security

WiFi capture and cracking, RF spectrum analysis, WPS auditing, and Bluetooth — for testing networks and gear you own or are authorized to audit.

## WiFi Capture & Cracking

aircrack-ng ⭐


#### aircrack-ng ⭐

The reference 802.11 suite: captures WEP and WPA/WPA2-PSK handshakes, cracks them against wordlists/dictionaries, and verifies recovered keys; ships the airodump-ng and aireplay-ng binaries.

**When:** Start every authorized Wi-Fi audit here: put a supported adapter into monitor mode and validate the key strength and fallback behavior of your own AP.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** wifite2, hcxdumptool, airodump-ng


#### airodump-ng

Packet-capture and display tool that enumerates nearby access points and clients, logs capture files, and grabs 4-way handshakes for offline cracking.

**When:** Any authorized Wi-Fi audit needs it first: channel-by-channel capture of BSSIDs, signal, encryption type, and handshake material on hardware you run.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** aircrack-ng, wifite2, kismet


#### aireplay-ng

Frame-injection and replay tool of the suite: sends deauthentication frames and replays captured packets to trigger a fresh 4-way handshake when a station won't associate on its own.

**When:** On a lab client that sits idle, use deauth to force a new handshake so you can verify your own PSK policy faster.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** aircrack-ng, wifite2


#### Wifite2

Automated Wi-Fi auditing wrapper: scans with a monitor-mode adapter, lets you pick targets from a menu, and chains deauth, handshake capture, and cracking (or WPS PIN work via bully/reaver) in one run.

**When:** Fast repeatable lab checks on your own networks where you want the whole capture-to-crack pipeline driven from a single interactive menu.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/derv82/wifite2.git && cd wifite2 && sudo python3 setup.py install`

**URL:** https://github.com/derv82/wifite2

**Alternatives:** aircrack-ng, hcxdumptool, reaver


#### hcxdumptool

Raw PCAPNG capture tool for PMKID and handshake material using a single adapter; often the fastest way to gather WPA test data without injection tricks.

**When:** Verify PSK strength on an AP you own that advertises PMKID — one passive-ish run beats orchestrating deauths.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ZerBea/hcxdumptool.git && cd hcxdumptool && make && sudo make install`

**URL:** https://github.com/ZerBea/hcxdumptool

**Alternatives:** aircrack-ng, wifite2






## WiFi Analysis & RF

Kismet ⭐


#### Kismet ⭐

Multi-protocol passive wireless detector and logging framework; captures and tracks 802.11, Bluetooth, and SDR sources with server + web UI.

**When:** Long-running passive surveys and signal mapping of your own test environment, plus intrusion detection on your authorized airspace.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install kismet`

**URL:** https://www.kismetwireless.net

**Alternatives:** horst, wireshark


#### Wireshark

Universal packet dissector with deep 802.11 and Bluetooth protocol support; decrypts WPA/EAPOL traffic when supplied the PMK/keys.

**When:** Post-capture forensics: walk frame-by-frame through handshakes, probe requests, and BT packets from your own gear to understand protocol behavior.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install wireshark`

**URL:** https://www.wireshark.org

**Alternatives:** kismet, horst


#### gqrx

Software-defined radio receiver built on GNU Radio; tunes an RTL-SDR dongle and demodulates, decodes, and spectrally displays received signals.

**When:** Scan the ISM band around your lab to identify transmitters or interference sources before blaming your own Wi-Fi gear.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gqrx-sdr`

**URL:** https://gqrx.dk

**Alternatives:** rtl-sdr, inspectrum


#### RTL-SDR

Cheap USB software-defined radio receiver with drivers and command-line utilities (rtl_fm, rtl_tcp, rtl_test) for raw spectral sampling.

**When:** The base RF monitoring hardware and tooling: stream IQ captures into gqrx or inspectrum for analysis of signals in your own environment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install rtl-sdr`

**URL:** https://github.com/osmocom/rtl-sdr

**Alternatives:** gqrx, inspectrum, kismet


#### inspectrum

Offline signal-analysis tool that renders recorded IQ or audio files into an interactive waterfall for visual protocol and modulation identification.

**When:** Analyze captured RF bursts (from RTL-SDR or other taps) to spot modulation patterns and packet structures after the fact.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install inspectrum`

**URL:** https://github.com/miek/inspectrum

**Alternatives:** gqrx, rtl-sdr


#### horst

Lightweight ncurses 802.11 traffic analyzer with channel scanning, signal histograms, and per-client statistics in a terminal.

**When:** A minimal TUI alternative to Kismet for quick signal and traffic checks in the field on authorized networks.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/br101/horst && cd horst && make && sudo make install`

**URL:** https://github.com/br101/horst

**Alternatives:** kismet, wireshark






## Bluetooth

Ubertooth ⭐


#### Ubertooth ⭐

Open-source 2.4 GHz radio hardware plus host software for Bluetooth capture and injection; analyzes frequency-hopping patterns, Classic BT, and BLE advertising on the Ubertooth One dongle.

**When:** Hardware-level Bluetooth auditing of your own peripherals: sniffing hop patterns, identifying weak pairing, and verifying advertising behavior.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/greatscottgadgets/ubertooth && cd ubertooth/host && mkdir build && cd build && cmake .. && make && sudo make install`

**URL:** https://github.com/greatscottgadgets/ubertooth

**Alternatives:** btlejack, bettercap


#### bettercap

Modular network attack/monitoring framework whose Bluetooth modules enumerate and intercept BLE and Classic BT devices and connections from the local host.

**When:** Scriptable Bluetooth enumeration and connection monitoring against your own test devices without extra RF hardware.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install bettercap`

**URL:** https://github.com/bettercap/bettercap

**Alternatives:** bluez


#### btlejack

Sniffs and interacts with BLE advertising and connection channels using nRF24-family USB dongles; supports jamming and session recovery using previously captured keys.

**When:** Low-cost BLE protocol auditing of your own accessories: map advertising channels and check whether session keys are reused across connections.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/virtualabs/btlejack && cd btlejack && make && sudo make install`

**URL:** https://github.com/virtualabs/btlejack

**Alternatives:** ubertooth, bettercap


#### BlueZ

The Linux Bluetooth protocol stack: hcitool, hcidump, btmon, and bluetoothctl expose controller state, HCI packets, and link logs.

**When:** Free, instant BT visibility on Linux before reaching for dedicated hardware like Ubertooth.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install bluez bluez-hcidump`

**URL:** https://github.com/bluez/bluez

**Alternatives:** bettercap






## WPS Tools

Reaver ⭐


#### Reaver ⭐

The reference WPS PIN brute-force tool: probes the registrar PIN transaction logic and, on vulnerable APs in your lab, recovers the WPS PIN and derived WPA-PSK.

**When:** Validate whether a lab AP's WPS implementation is brute-force resistant — many modern routers lock out after failures, which is the outcome you want to confirm.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install reaver`

**URL:** https://github.com/t6x/reaver-wps-fork-linux

**Alternatives:** bully, wash


#### Wash

Companion scanner shipped with reaver that detects WPS-enabled access points and reads their WPS state (version, locked or not) without launching an active attack.

**When:** Passive WPS recon across your own network estate before deciding whether a PIN-based audit is even relevant.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install reaver`

**URL:** https://github.com/t6x/reaver-wps-fork-linux

**Alternatives:** reaver, bully


#### Bully

Reimplementation of the WPS PIN brute-force client in C with tighter packet timing and tolerance for flaky associations than reaver's original implementation.

**When:** When reaver stalls against your own AP, Bully's more robust locking logic often completes the audit where reaver cannot.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install bully`

**URL:** https://github.com/aanarchyy/bully

**Alternatives:** reaver, wash





