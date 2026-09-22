# 📡 Wireless & Bluetooth Security

WiFi capture and cracking, PMKID and precomputed tables, RF spectrum analysis, WPS auditing, and Bluetooth — all framed for labs and gear you own or are authorized to audit.

## Monitor Mode & Adapter Setup

airmon-ng ⭐

#### airmon-ng ⭐

Script from the aircrack-ng suite that flips a supported chipset into monitor mode (and back), kills interfering processes, and reports adapter capabilities.

**When:** First step of any authorized Wi-Fi test: enable monitor mode on the adapter you own and confirm chipset/driver support before capture or injection.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** iw, macchanger


#### iw

The nl80211 wireless CLI: lists radios and phy capabilities and sets interface modes (monitor/managed) without legacy wrapper scripts.

**When:** When airmon-ng's heuristics stall, set mode=monitor by hand on an interface you control and verify the phy supports injection.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install iw`

**URL:** https://wireless.wiki.kernel.org/en/users/documentation/iw

**Alternatives:** airmon-ng


#### macchanger

Spoofs a wireless interface's MAC address so lab captures originate from an anonymized, disposable local address.

**When:** Before a capture or wifite run in your lab when you want a clean identity that is trivially reset between tests.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install macchanger`

**URL:** https://github.com/alobbs/macchanger

**Alternatives:** airmon-ng


#### Capture Verification


##### tcpdump ⭐

Classic packet capture tool; on a monitor interface it proves the card actually sees 802.11 beacons, probe requests, and management frames.

**When:** Smoke-test the adapter: run tcpdump on mon0 and confirm frames before starting a long airodump or Kismet session on your own hardware.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install tcpdump`

**URL:** https://www.tcpdump.org

**Alternatives:** wireshark, kismet


#### WIDS & Wireless Defense


##### airguard ◆ by 5h4d0wn1k

Wireless defense & monitoring suite — WIDS sensor, deauth/evil-twin/rogue-AP detection, beacon anomaly scan, WPA3 survey.

**When:** Detecting rogue APs and deauth floods in your own wireless perimeter.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/airguard`

**URL:** https://github.com/5h4d0wn1k/airguard

**Alternatives:** Own tool — lab/authorized use only



## Probe & Access-Point Discovery

airodump-ng ⭐

#### airodump-ng ⭐

Channel-by-channel capture of BSSIDs, clients, signal, and encryption; logs raw PCAPc and collects probe requests and association traffic from nearby APs you can hear.

**When:** Start discovery here on hardware you control: target channels, capture beacon/probe data, and note handshake material for later offline work.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** kismet, horst


#### horst

Lightweight ncurses 802.11 monitor with channel scanning, signal histograms, and per-client statistics, no daemon or web UI required.

**When:** A minimal TUI for quick signal and channel-noise checks mid-test in your lab when Kismet is overkill.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/br101/horst && cd horst && make && sudo make install`

**URL:** https://github.com/br101/horst

**Alternatives:** airodump-ng, kismet


#### wiair ◆ by 5h4d0wn1k

Byte-exact 802.11/BLE frame crafting & parsing framework; offline-only and safety-gated.

**When:** Building raw wireless frames for protocol research and WIDS/emitter lab work.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/wiair`

**URL:** https://github.com/5h4d0wn1k/wiair

**Alternatives:** Own tool — lab/authorized use only


#### Passive Surveys & Packet Dissection


##### Kismet ⭐

Multi-protocol passive detector with server + web UI; tracks 802.11, Bluetooth, and SDR sources and logs probe traffic for long-running surveys.

**When:** Long-running passive mapping of your authorized airspace, or intrusion-detection-style monitoring over your own test environment.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install kismet`

**URL:** https://www.kismetwireless.net

**Alternatives:** airodump-ng, horst


##### Wireshark

Universal dissector with deep 802.11 and EAPOL support; supply the PMK to decrypt WPA traffic you captured from your own APs.

**When:** Post-capture dissection of handshakes, probe requests, and Bluetooth frames from gear you own.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install wireshark`

**URL:** https://www.wireshark.org

**Alternatives:** tcpdump, kismet



## WPA2 Handshake & PSK Testing



#### Forcing & Capturing Handshakes


##### wifite2 ⭐

Automated lab auditor: scans, lets you pick a target you own, then drives deauth, handshake capture, and cracking (or WPS work via reaver/bully) from one menu.

**When:** Repeatable capture-to-crack runs against your own APs where one command replaces a long manual chain.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/derv82/wifite2.git && cd wifite2 && sudo python3 setup.py install`

**URL:** https://github.com/derv82/wifite2

**Alternatives:** airodump-ng, hcxdumptool, aircrack-ng


##### Deauthentication & Frame Injection


###### aireplay-ng ⭐

Frame injection and replay from aircrack-ng: sends deauthentication frames and replays captured packets to force a fresh 4-way handshake from an idle station.

**When:** In your lab, deauth a stationary test client to accelerate handshake capture and PSK policy validation on APs you manage.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** mdk4, wifite2


###### mdk4

Multi-purpose 802.11 tool with aggressive deauthentication, probe-testing, and fuzzing modes (mdk4 w / m / f) for validating client and AP reactions.

**When:** Stress the deauth resistance of APs you own and verify clients reconnect cleanly and re-associate after interference.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/aircrack-ng/mdk4 && cd mdk4 && make && sudo make install`

**URL:** https://github.com/aircrack-ng/mdk4

**Alternatives:** aireplay-ng


##### PMKID Capture


###### hcxdumptool ⭐

Raw PCAPNG capture of PMKID and EAPOL material using a single adapter; PMKID needs no connected client and no deauthentication.

**When:** On APs you own that expose PMKID, grab the token passively and skip the whole deauth-and-reassociate dance.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ZerBea/hcxdumptool.git && cd hcxdumptool && make && sudo make install`

**URL:** https://github.com/ZerBea/hcxdumptool

**Alternatives:** aircrack-ng, airodump-ng


###### hcxtools

Converts hcxdumptool PCAPNG captures into hashcat/john-ready hash formats (mode 22000), filtering duplicates and invalid entries.

**When:** After capture, normalize EAPOL/PMKID material into 22000 format so GPU testing can start on your own hashes.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ZerBea/hcxtools.git && cd hcxtools && make && sudo make install`

**URL:** https://github.com/ZerBea/hcxtools

**Alternatives:** hashcat, aircrack-ng


#### Offline PSK Cracking


##### aircrack-ng ⭐

The suite's cracking core validates WPA/WPA2 handshakes against wordlists (and PTW for WEP), verifying recovered keys against the captured material.

**When:** Offline verification of PSK strength from captures taken against your own access points.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** hashcat, cowpatty


##### Wordlist & GPU Cracking


###### hashcat ⭐

GPU password cracker with native WPA-PBKDF2-PMKID+EAPOL kernels (mode 22000) for turning captured handshake hashes into keys at high speed.

**When:** When masks/rules outgrow aircrack-ng and you have a GPU available for faster PMK derivation in your lab.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install hashcat`

**URL:** https://github.com/hashcat/hashcat

**Alternatives:** aircrack-ng, cowpatty


###### cowpatty

Wordlist PSK verifier that confirms candidate passphrases against captured handshake material without extra dependencies.

**When:** Clean no-frills confirmation that a candidate passphrase matches your capture before moving on.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install cowpatty`

**URL:** https://github.com/joswr1ght/cowpatty

**Alternatives:** aircrack-ng


##### PMK Precomputation


###### airolib-ng ⭐

Builds precomputed PMK tables keyed by (ESSID, password) from wordlists and serves hashes to aircrack-ng for instant reuse.

**When:** Repeatedly audit the same ESSID: precompute its PMK table once, then crack many captured handshakes instantly in your lab.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** genpmk


###### genpmk

cowpatty's companion that precomputes the per-ESSID PMK seed file from a wordlist for fast later handshake verification.

**When:** One-off ESSID precompute when you do not want the full airolib database machinery.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install cowpatty`

**URL:** https://github.com/joswr1ght/cowpatty

**Alternatives:** airolib-ng



## WPS Auditing



#### wash

Passive scanner for WPS-enabled access points: reports WPS state and lockout status without launching an active registrar exchange.

**When:** Recon your own estate for WPS-enabled APs before deciding a PIN audit is even worthwhile.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install reaver`

**URL:** https://gitlab.com/kalilinux/packages/reaver

**Alternatives:** reaver


#### WPS PIN Bruteforce


##### Reaver ⭐

The reference WPS registrar brute-forcer: probes PIN transaction logic and, on vulnerable lab routers, recovers the WPS PIN and derived WPA-PSK.

**When:** Confirm your lab AP's WPS lockout and PIN policy — most modern routers lock out after failures, which is the outcome you want to verify.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://gitlab.com/kalilinux/packages/reaver && cd reaver && ./configure && make`

**URL:** https://gitlab.com/kalilinux/packages/reaver

**Alternatives:** bully, wash


##### Bully

C reimplementation of the WPS PIN attack with more forgiving association handling and clearer logging than reaver.

**When:** When reaver stalls against your own AP, bully's retry logic often completes the audit where reaver cannot.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install bully`

**URL:** https://github.com/aanarchyy/bully

**Alternatives:** reaver, wash


#### Pixie-Dust (Offline PIN Recovery)


##### pixiewps ⭐

Offline WPS computation tool (R1/R2/RB) that takes the e-S1/e-S2 nonces captured by reaver/bully and recovers the PIN without brute force.

**When:** On older WPS APs you own with predictable RNG, run pixiewps over a reaver capture to recover the PIN in seconds instead of hours.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/wiire/pixiewps && cd pixiewps && make && sudo make install`

**URL:** https://github.com/wiire/pixiewps

**Alternatives:** reaver, bully



## Evil Twin & Rogue AP (Lab Only)



#### airbase-ng

Creates 802.11 software access points from a monitor-mode card; the primitive behind most fake-AP tests, including WEP/WPA emulation and injection.

**When:** Stand up a disposable simulated AP in your own lab for behavior tests and client-device compatibility checks.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install aircrack-ng`

**URL:** https://github.com/aircrack-ng/aircrack-ng

**Alternatives:** hostapd-wpe


#### Rogue AP & Enterprise Credential Capture


##### hostapd-wpe ⭐

Patched hostapd that adds WPA enterprise (PEAP/MSCHAPv2) credential capture for controlled authentication tests in your lab.

**When:** Building an enterprise authentication test rig against client configs you control, capturing challenge/response pairs for offline review.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://gitlab.com/kalilinux/packages/hostapd-wpe && cd hostapd-wpe && sudo make -C hostapd install`

**URL:** https://gitlab.com/kalilinux/packages/hostapd-wpe

**Alternatives:** airbase-ng, eaphammer


#### Automated Twins & Phishing Pages


##### wifiphisher ⭐

Carries out evil-twin attacks with a real captive portal: clones a target AP you own, then serves phishing templates to harvest credentials and PMKID.

**When:** Demo rogue-AP and social-engineering tradecraft only against APs and clients you own or explicitly control in the lab.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/wifiphisher/wifiphisher && cd wifiphisher && sudo python3 setup.py install`

**URL:** https://github.com/wifiphisher/wifiphisher

**Alternatives:** fluxion, eaphammer


##### fluxion

Evil-twin toolkit that deauths a target you own, runs a cloned fake AP, and feeds a captive-login page to collect passphrases.

**When:** Scripted WPA2 capture plus captive-portal phishing against your own APs and test accounts.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/FluxionNetwork/fluxion && cd fluxion && sudo ./fluxion.sh`

**URL:** https://github.com/FluxionNetwork/fluxion

**Alternatives:** wifiphisher, hostapd-wpe


##### eaphammer

Targeted evil-twin and enterprise attack tool with WPA/WPA2 enterprise automation, KARMA, and credential-database harvesting for lab demos.

**When:** Enterprise (802.1X) test scenarios against your own lab RADIUS and client fleets before touching production gear.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://gitlab.com/kalilinux/packages/eaphammer && cd eaphammer && ./kali-setup`

**URL:** https://gitlab.com/kalilinux/packages/eaphammer

**Alternatives:** hostapd-wpe, wifiphisher



## Bluetooth & Bluetooth LE



#### bettercap

Host-side network and monitoring framework whose BLE module runs recon, sniffs, and offers a ble.proxy that can pose as a peripheral for lab devices.

**When:** Scriptable, host-based BLE enumeration and proxy testing of your own peripherals without dedicated sniffing hardware.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install bettercap`

**URL:** https://github.com/bettercap/bettercap

**Alternatives:** bluez, btlejack


#### Sniffing, Capture & Injection


##### Ubertooth ⭐

Open 2.4 GHz radio plus host software for Bluetooth capture and injection; follows Classic BT hopping patterns and BLE channels on the Ubertooth One dongle.

**When:** Hardware-level analysis of hop patterns, advertising data, and pairing behavior of peripherals you own.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/greatscottgadgets/ubertooth && cd ubertooth/host && mkdir build && cd build && cmake .. && make && sudo make install`

**URL:** https://github.com/greatscottgadgets/ubertooth

**Alternatives:** btlejack, bettercap


##### btlejack

Sniffs and interacts with BLE connections via nRF24-family USB dongles; supports jamming and session recovery from previously captured keys.

**When:** Low-cost BLE session auditing of your own accessories — map advertising channels and check for key reuse across connections.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/virtualabs/btlejack && cd btlejack && make && sudo make install`

**URL:** https://github.com/virtualabs/btlejack

**Alternatives:** ubertooth


#### Host Stack & GATT


##### BlueZ ⭐

Linux's Bluetooth stack: bluetoothctl, btmon, hcitool, and gatttool expose controller state, HCI packets, and GATT services.

**When:** Free host-side visibility before reaching for RF hardware; btmon gives clean pairing and connection traces for your own adapters.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install bluez bluez-hcidump`

**URL:** https://github.com/bluez/bluez

**Alternatives:** bettercap


#### Active Service Audit


##### bt_audit (BTSD) ⭐

The BTSD Bluetooth audit suite: psm_scan maps L2CAP PSM services and rfcomm_scan enumerates RFCOMM channels on local or paired devices.

**When:** A quick authorized inventory of services your own BT peripherals expose before deeper hardware testing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download bt_audit-0.1.1.tar.gz from betaversion.net, extract, and run make in the src directory`

**URL:** http://www.betaversion.net/btdsd/download/

**Alternatives:** bluez, bettercap



## RFID & NFC Testing

Proxmark3 (Iceman) ⭐

#### Proxmark3 (Iceman) ⭐

Proxmark3 hardware plus the Iceman project firmware: read, clone, and analyze low- and high-frequency tags including MIFARE, ISO14443, and iCLASS.

**When:** Physical badge and tag auditing of assets you own — sniff reader/tag sessions and validate card copy resistance.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/RfidResearchGroup/proxmark3 && cd proxmark3 && make`

**URL:** https://github.com/RfidResearchGroup/proxmark3

**Alternatives:** libnfc, mfoc


#### NFC Tooling


##### libnfc ⭐

Portable NFC library with CLI tools (nfc-list, nfc-read, nfc-mfclassic) for enumerating and reading tags through USB readers.

**When:** With an ACR122U-class reader, enumerate and read blocks on cards you own without dedicated hardware.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install libnfc-bin`

**URL:** https://github.com/nfc-tools/libnfc

**Alternatives:** proxmark3, mfoc


#### MIFARE Classic Cracking


##### mfoc ⭐

The classic MIFARE Classic hardnested tool: exploits leaked (weak) keys to recover the full key set of a card you own.

**When:** Recover all sectors of a weak-key MIFARE Classic card in your lab for badge cloning and access-control red-team tests.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/nfc-tools/mfoc && cd mfoc && ./autogen.sh && ./configure && make && sudo make install`

**URL:** https://github.com/nfc-tools/mfoc

**Alternatives:** mfcuk, libnfc


##### mfcuk

MIFARE Classic dark-side attack tool that recovers keys on cards whose PRNG hands out predictable nonces.

**When:** When mfoc's hardnested path fails against a card you own, mfcuk's dark-side vector is the fallback.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/nfc-tools/mfcuk && cd mfcuk && ./autogen.sh && ./configure && make && sudo make install`

**URL:** https://github.com/nfc-tools/mfcuk

**Alternatives:** mfoc, proxmark3



## Software-Defined Radio

RTL-SDR ⭐

#### RTL-SDR ⭐

Cheap USB software-defined radio receiver: drivers plus rtl_test, rtl_fm, and rtl_tcp for raw IQ sampling and streaming.

**When:** The base RF capture hardware and tooling: stream IQ captures into gqrx or inspectrum for analysis of signals in your own environment.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install rtl-sdr`

**URL:** https://github.com/osmocom/rtl-sdr

**Alternatives:** gqrx, inspectrum


#### Receivers & Tuning


##### gqrx ⭐

GNU Radio-based desktop receiver that demodulates and displays spectrum and waterfall from an SDR dongle.

**When:** Interactively scan ISM bands and identify transmitters or interference sources before blaming your own Wi-Fi gear.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gqrx-sdr`

**URL:** https://gqrx.dk

**Alternatives:** rtl-sdr, inspectrum


#### Signal Analysis & Protocol Reverse


##### inspectrum ⭐

Offline analysis of recorded IQ or audio: renders interactive water-falls to identify modulation, timing, and packet structure.

**When:** After recording bursts with rtl_sdr, step through symbols to identify the modulation type before deeper decoding.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install inspectrum`

**URL:** https://github.com/miek/inspectrum

**Alternatives:** gqrx, rtl-sdr


#### Processing & Flowgraph Frameworks


##### GNU Radio ⭐

Flow-graph framework for designing and running custom demodulators and decoders; the engine underneath gqrx and many SDR toolchains.

**When:** When you must decode a custom protocol from captured samples of signals you are authorized to receive.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install gnuradio`

**URL:** https://github.com/gnuradio/gnuradio

**Alternatives:** gqrx, inspectrum



