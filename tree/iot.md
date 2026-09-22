# 🔌 IoT, Embedded & Firmware Security

Reverse, emulate, and attack embedded devices in your lab: firmware extraction and boot-level emulation, UART/JTAG probing and flash dumping, side-channel and glitching rigs, RF protocol analysis (BLE/Zigbee/Z-Wave/MQTT), companion-app taping, and device databases.

## Firmware Extraction & Static Review




#### Extraction & Carving



##### binwalk ⭐

Scans firmware blobs by magic signature and carves out embedded kernels, U-Boot images, squashfs/cramfs/JFFS2/ubifs filesystems, and config partitions, with entropy plots to spot encrypted or compressed regions.

**When:** Every firmware image starts here: carve the filesystem out of the blob before anything else can be analyzed.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install binwalk`

**URL:** https://github.com/ReFirmLabs/binwalk

**Alternatives:** firmware-mod-kit


##### firmware-mod-kit (FMK)

Extract-and-repack toolkit for router firmware (squashfs/cramfs/JFFS2); lets you patch binaries or files and rebuild a bootable vendor image. Largely unmaintained, so expect to fix toolchain issues before it works.

**When:** When you actually need to modify and re-flash a vendor image (e.g. inject a telnetd) rather than merely read it.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/rampageX/firmware-mod-kit`

**URL:** https://github.com/rampageX/firmware-mod-kit

**Alternatives:** binwalk


##### U-Boot Tools

Bootloader utilities (mkimage, dumpimage, fw_printenv, fw_setenv, mkenvimage) that inspect, unpack, and modify U-Boot FIT images and boot-environment blobs.

**When:** Unpacking U-Boot FIT images, decoding kernel/dtb parts, or reading a target's boot environment from a flash dump.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install u-boot-tools`

**URL:** https://u-boot.readthedocs.io/en/latest/usage/index.html

**Alternatives:** binwalk


#### Root Filesystem Review



##### Firmwalker ⭐

Bash script that greps an extracted or mounted filesystem for secrets: shadow/passwd, SSL keys and certs, config files, admin/password keywords, dropbear/ssh artifacts, and URLs.

**When:** Ten seconds after extraction, to surface default creds, key material, and backdoors before you read anything by hand.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/craigz28/firmwalker`

**URL:** https://github.com/scriptingxss/firmwalker

**Alternatives:** binwalk


##### fwanalyzer

Filesystem audit tool from Cruise Automation that analyzes an extracted root filesystem image for setuid binaries, world-writable paths, insecure file modes, passwd-in-NSS, and other configuration smells, producing a custom report format.

**When:** A structured, repeatable triage pass over an extracted filesystem instead of ad-hoc grep hunting.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/cruise-automation/fwanalyzer && cd fwanalyzer && make`

**URL:** https://github.com/cruise-automation/fwanalyzer

**Alternatives:** Firmwalker


##### fwupd

Linux firmware-update framework (fwupdmgr/fwupdtool) that enumerates devices and applies signed firmware; in a lab it exposes device firmware versions, EFI capsules, and update/rollback flows on Linux-based research targets.

**When:** Exercising a Linux target's firmware update path and enumerating what firmware components it reports.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install fwupd`

**URL:** https://github.com/fwupd/fwupd

**Alternatives:** flashrom


#### Firmware Emulation & Dynamic Analysis



##### Automated Full-System Boot



###### FirmAE ⭐

Fully-automated emulation framework (Firmadyne-derived) that uses arbitration heuristics to boot router/IP-camera firmware at ~79% success, exposing the web UI and SSH so you can fuzz and exploit it dynamically.

**When:** Batch full-system dynamic analysis of Linux-based IoT firmware, on images Firmadyne-style boot failures block.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone --recursive https://github.com/pr0v3rbs/FirmAE && ./setup.sh`

**URL:** https://github.com/pr0v3rbs/FirmAE

**Alternatives:** FAT, QEMU


###### Firmware Analysis Toolkit (FAT)

Attify's one-command wrapper around Firmadyne that boots Linux router firmware in QEMU without the PostgreSQL dependency; prints the emulated IP so you can reach its web server from the host.

**When:** Quick, scripted boot of a single firmware image to poke its web UI and userland by hand.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone --recursive https://github.com/attify/firmware-analysis-toolkit && ./setup.sh`

**URL:** https://github.com/attify/firmware-analysis-toolkit

**Alternatives:** FirmAE, QEMU


##### QEMU Emulation Backends



###### QEMU ⭐

Full-system and user-mode emulator covering ARM, MIPS, RISC-V, and more; boots extracted root filesystems end-to-end, and qemu-user builds run single cross-arch binaries, which every emulation framework sits on top of.

**When:** The foundation of the whole emulation stack: boot a rootfs, or dynamically trace one bare-metalstripped binary before standing up full-stack tooling.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install qemu-system-arm qemu-system-mips qemu-user-static`

**URL:** https://www.qemu.org

**Alternatives:** FirmAE, FAT






## Hardware Debug Ports, Flash & Fault Injection




#### UART Console & Bus Sniffing



##### Logic Analyzers



###### PulseView / sigrok ⭐

Open-source logic-analyzer software stack with protocol decoders for UART, SPI, I2C, and 1-Wire; works with cheap 8/24-channel analyzers (Saleae clones, fx2lafw) as well as the Bus Pirate.

**When:** Identifying unknown serial pads, decoding an unknown baud rate, and sniffing chip-to-chip buses on a target board you own.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install pulseview sigrok-cli`

**URL:** https://sigrok.org/wiki/PulseView

**Alternatives:** Saleae Logic 2


###### Saleae Logic 2

Polished commercial logic-analyzer software (free for low channel counts) with one-click UART/SPI/I2C decoding and robust triggering; pairs with genuine Logic 4/8/16 hardware or the popular HzKit clones.

**When:** Fast, friendly decoding and decode-while-capturing when you have the hardware on the bench.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `download from https://www.saleae.com/downloads/`

**URL:** https://www.saleae.com/downloads/

**Alternatives:** PulseView


###### Bus Pirate

Open-source serial multi-tool (current Bus Pirate 5): drives SPI/I2C/UART/1-Wire, reads SPI flash and EEPROMs, sniffs buses, and doubles as a low-speed logic analyzer and host adapter from any serial terminal.

**When:** Talking directly to a chip over SPI/I2C, reading EEPROMs, or probing a bus before you break out a dedicated analyzer.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `hardware (dangerousprototypes.com) + sudo apt install picocom`

**URL:** https://github.com/DangerousPrototypes/Bus_Pirate

**Alternatives:** PulseView, OpenOCD


##### Serial Terminals



###### minicom ⭐

The classic serial terminal for UART consoles at arbitrary baud rates; the everyday tool for reaching a bootloader, root shell, or firmware-upgrade prompt over the debug UART.

**When:** UART pads or test points are exposed, and you want bootloader or shell access immediately.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install minicom`

**URL:** https://salsa.debian.org/minicom-team/minicom

**Alternatives:** picocom, screen


###### picocom

Lightweight, scriptable serial terminal with freshline handling and a minimal config; drops into non-interactive scripts, so it's ideal for logging UART sessions or pasting bootloader commands.

**When:** Headless or scripted UART sessions where minicom's interactive menus get in the way.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install picocom`

**URL:** https://github.com/npat-efault/picocom

**Alternatives:** minicom, screen


#### Flash Dumping & Imaging



##### flashrom ⭐

Universal flash programmer with hundreds of supported chips and bus protocols (SPI, I2C, parallel, and via ch341a/mstarddc/ft2232 programmers); reads and writes BIOS, firmware, and SPI NOR chips with verification.

**When:** Reading an on-board SPI flash out of circuit (or via clip) to obtain a full firmware image, or restoring one.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install flashrom`

**URL:** https://www.flashrom.org/

**Alternatives:** OpenOCD, CH341A


##### CH341A SPI Programmer

Five-dollar USB SPI/I2C/parallel programmer (and its clones) that flashrom drives directly; the budget way to dump 25-series SPI flash with a SOIC-8 clip without desoldering.

**When:** Cheap, disposable SPI reads on consumer hardware where you don't want to risk a J-Link or full probe.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install flashrom && use with ch341a_spi programmer`

**URL:** https://flashrom.org/supported_hw/supported_prog/ch341ab.html

**Alternatives:** flashrom


#### JTAG / SWD Debug Interfaces



##### OpenOCD ⭐

On-chip debugger for JTAG/SWD with a large catalog of CPU and flash targets, dozens of adapter drivers, and TCL scripting; halts CPUs, sets breakpoints, and reads back flash via the debug port.

**When:** You found a JTAG/SWD header (or expose a testpad): OpenOCD plus a cheap probe gives you a debugger, and its flash readback doubles as a dump path for lockdown-immune devices.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install openocd`

**URL:** https://openocd.org

**Alternatives:** J-Link, urJTAG, Bus Pirate


##### J-Link (SEGGER)

Commercial debug-probe family with polished SWD/JTAG software, flash loaders across thousands of microcontrollers, and RTT for fast printf-style logging from target firmware.

**When:** A board already exposes a J-Link/SWD header, or you want a trouble-free flash-and-debug flow instead of fighting adapter quirks.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial hardware + download J-Link Software pack from segger.com`

**URL:** https://www.segger.com/products/debug-probes/j-link/

**Alternatives:** OpenOCD, urJTAG


#### Soldering & Rework



##### Pinecil ⭐

USB-C smart soldering iron with fast heat-up, excellent temperature control, and a huge tip selection; the go-to for tacking flywires onto UART pads, test points, and SOIC-8 clips.

**When:** Practical lab work: soldering header pins, hooking UART/SPI flywires, and reattaching damaged pads before probing.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `hardware: order from pine64.com and power over 20V USB-C`

**URL:** https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/

**Alternatives:** TS100, Hot-air rework


##### Hakko FR-301

Self-contained desoldering gun that cleanly removes through-hole components and chip pulls without collateral pad damage, invaluable for harvesting flash chips or isolating a faulted module.

**When:** Removing a flash chip, connector, or BGA-adjacent through-hole part from a curious board without killing the board.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `hardware: FR-301 unit plus replacement nozzles`

**URL:** https://hakkousa.com/products/fr-301-df-portable-desoldering-tool.html

**Alternatives:** Pinecil


#### Side-Channel & Fault Injection



##### ChipWhisperer ⭐

Open-source, open-hardware lab for power/EM side-channel analysis and voltage/clock glitching: capture power traces, run correlation power analysis to recover keys, and glitch to skip checks (CW-Lite, CW-Husky).

**When:** Assessing a secure MCU's resistance to key extraction or fault injection on hardware you own, where the chip is the oracle.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `pip install chipwhisperer`

**URL:** https://github.com/newaetech/chipwhisperer

**Alternatives:** TrueRandom Debounce


##### TrueRandom Debounce Adapter

Solder-free tag-connect breakout kit from TrueRandom that reroutes narrow-pitch debug headers (and exposes them) so you can desolder nothing, attack multiple boards in series, or chain a glitcher into the target.

**When:** On small IoT modules whose debug adapters break off, or to insert a glitch/analog probe cleanly between connector and target.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `hardware: order the Debounce adapter set and clip onto the tag-connect header`

**URL:** https://github.com/TrueRandom

**Alternatives:** ChipWhisperer






## RF Protocol & Application Analysis




#### iotbreach ◆ by 5h4d0wn1k

IoT/SCADA/embedded offensive framework — MQTT/CoAP/UPnP/Modbus/CAN/BLE/Zigbee/433MHz, firmware extraction, ICS kill-chain simulation.

**When:** Testing embedded/IoT targets in your own lab.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/iotbreach`

**URL:** https://github.com/5h4d0wn1k/iotbreach

**Alternatives:** Own tool — lab/authorized use only


#### Link-Layer Radios (Z-Wave / Zigbee / BLE)



##### Z-Wave



###### Controller & Inspector



###### Z-Wave JS UI ⭐

Standalone web front-end (formerly Home Assistant's add-on) over node-zwave-js that pairs, configures, and interrogates Z-Wave devices through a USB stick, exposing command classes, values, and raw frames.

**When:** Lab controller to inspect what a Z-Wave device advertises and to script device interactions while researching its behavior.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `docker run -d -p 8091:8091 --device /dev/ttyUSB0 ghcr.io/zwave-js/zwave-js-ui:latest`

**URL:** https://github.com/zwave-js/zwave-js-ui

**Alternatives:** Z-Wave JS, Home Assistant


###### Protocol Stack Library



###### Z-Wave JS ⭐

The core Node.js Z-Wave protocol stack powering Home Assistant and Z-Wave JS UI; parses command classes at a protocol level and is directly scriptable to send raw, non-standard frames to a device.

**When:** Driving Z-Wave from code for fuzzing or deep protocol interrogation, or extending Home Assistant-based research setups.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `npm install zwave-js`

**URL:** https://github.com/zwave-js/node-zwave-js

**Alternatives:** Z-Wave JS UI


##### Zigbee / 802.15.4



###### Packet Injection & Replay



###### Killerbee ⭐

Python framework for 802.15.4/ZigBee security testing: scanning channels, sniffing and decrypting (default-link-key) traffic, and injecting/replaying frames with a supported radio (ATUSB/RZUSBstick).

**When:** Live ZigBee interception and frame injection against Personal Area Networks in your own test environment.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `pip install killerbee`

**URL:** https://github.com/riverloopsec/killerbee

**Alternatives:** ZigDiggity


###### ZigDiggity

Bishop Fox's Zigbee pentest toolkit with a hardware setup around the RaspBee/Atmel RZUSBstick; ships attack scripts for insecure rejoins, ACK attacks, and lock identifier/enumeration against Zigbee home networks.

**When:** Structured attack playbooks (beacon, scan, unlock, insecure-rejoin) beyond ad-hoc Killerbee usage.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/bishopfox/zigdiggity && pip3 install -r requirements.txt`

**URL:** https://github.com/bishopfox/zigdiggity

**Alternatives:** Killerbee


###### Device Control & Emulation



###### zigbee2mqtt ⭐

Bridges off-the-shelf Zigbee adapters instead of vendor hubs so devices are attached and controlled over plain MQTT; exposes the individual clusters/eps of devices, ideal for observing how 'dumb' devices really communicate.

**When:** Local lab network to enroll consumer Zigbee devices and drive them from MQTT while you capture and study their traffic.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `docker run -it --rm --network host koenkk/zigbee2mqtt:latest`

**URL:** https://github.com/Koenkk/zigbee2mqtt

**Alternatives:** ZigDiggity


##### Bluetooth Low Energy



###### Scan & GATT Interaction



###### BetterCap (BLE modules) ⭐

Swiss-army network tool whose ble.recon/ble.sniff/ble.spam/ble.uart modules enumerate BLE devices, read/write GATT characteristics, sniff packets, and even drive a serial-over-BLE UART on a target.

**When:** Rapid BLE recon, characteristic enumeration, and interactive testing of a wearable or smart device's GATT service.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install bettercap`

**URL:** https://github.com/bettercap/bettercap

**Alternatives:** nRF Connect


###### nRF Connect

Nordic's desktop/mobile app that scans BLE devices and browses GATT services, characteristics, and descriptors with clear D-Bus-ish tree views; the fastest way to map what a peripheral exposes.

**When:** First look at a BLE device's services and charactistics before you script anything with a full toolchain.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `download nRF Connect for Desktop from nordicsemi.com (deb/AppImage)`

**URL:** https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop

**Alternatives:** BetterCap


###### Packet Sniffing



###### nRF Sniffer for Bluetooth LE ⭐

Wireshark plug-in plus nRF52840 dongle firmware that decodes BLE advertising and data channels, with RSSI trackers; the de facto way to observe full BLE link-layer traffic, including encrypted sessions for offline analysis.

**When:** Capture-level BLE analysis (advertising, pairing, connection events) without modifying the target in any way.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `download nRF Sniffer for Bluetooth LE from nordicsemi.com and load .pcap into Wireshark`

**URL:** https://www.nordicsemi.com/Products/Development-tools/nrf-sniffer-for-bluetooth-le

**Alternatives:** BetterCap, Ubertooth One


#### Application Layer (MQTT, Cloud & Companion Apps)



##### MQTT Broker Probing



###### mqtt-pwn ⭐

Akamai's Python toolchain (mqttez, mqtts-tv, mqttgama) that scans MQTT brokers, recovers credentials from device images, and lets you interact with topics (subscribe/inject) against smart devices running MQTT.

**When:** Assessing an MQTT-enabled IoT fleet on a lab broker: credential hunting and topic-level injection.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/akamai/mqtt-pwn && pip install -r requirements.txt`

**URL:** https://github.com/akamai-threat-research/mqtt-pwn

**Alternatives:** mosquitto_pub, MQTT Explorer


###### MQTT Explorer

Desktop broker browser that visualizes topics as a live tree structure with retain/retained values and history, making it trivial to spot insecure 'state' topics or mis-labeled sensor data.

**When:** Grabbing a visual, real-time map of topics and retained payloads when investigating a live broker in the lab.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `download AppImage from GitHub releases`

**URL:** https://github.com/thomasnordquist/MQTT-Explorer

**Alternatives:** MQTTX


###### MQTTX

Cross-platform MQTT client with scripting and a clean multi-connection UI; handy for pushing crafted payloads to topics and replaying captured values at scale.

**When:** Scripted by-hand publishing/subscribing to MQTT topics during protocol testing of smart devices.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask mqttx`

**URL:** https://github.com/emqx/MQTTX

**Alternatives:** MQTT Explorer


##### Consumer Cloud & Vendor Backend



###### tuya-convert ⭐

Jailbreaks firmware-locked Tuya IoT devices (wall switches, bulbs) by MITM-ing their provisioning phase and flashing an open firmware over the air, removing vendor-cloud dependency for lab control and re-flashing.

**When:** Liberating a Tuya-based device from vendor cloud services so you can flash, control, and analyze it locally.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ct-Open-Source/tuya-convert && ./start_flash.sh`

**URL:** https://github.com/ct-Open-Source/tuya-convert

**Alternatives:** Tasmota


###### Tasmota

Open-source firmware for ESP8266/ESP32 smart-home hardware that replaces vendor builds; its console exposes serial/MQTT/web interfaces and detailed logs that make a repurposed device an instrumented research target.

**When:** Running a stable, instrumented firmware on a device you control, with full console and MQTT logging for traffic observation.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `flash release .bin with esptool or tuya-convert`

**URL:** https://github.com/arendst/Tasmota

**Alternatives:** tuya-convert


##### Mobile Companion App Analysis



###### Frida ⭐

Dynamic instrumentation framework for Android/iOS that injects JS/TS hooks into a running companion app to trace crypto, dump secrets, bypass SSL pinning, and call internal APIs live.

**When:** Tapping the device's companion app to observe cloud interactions, API calls, and key handling in real time.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install frida-tools`

**URL:** https://frida.re

**Alternatives:** objection


###### objection

Runtime mobile exploration toolkit built on Frida that patches APKs/IPAs, bypasses root, disables SSL pinning, and dumps the app's runtime state (keychains, class instances) without writing hooks by hand.

**When:** Fast-win companion-app poking: unpin, dump keystore, and inspect the app's live memory before writing custom Frida scripts.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install objection`

**URL:** https://github.com/sensepost/objection

**Alternatives:** Frida


###### jadx

Dex-to-Java decompiler with a GUI and CLI that turns a companion APK into readable source for static review of hardcoded creds, endpoints, and embedded SDK calls.

**When:** Static pass over a companion app: find API keys, vendor-cloud endpoints, and logging before you attack the running app.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `snap install jadx`

**URL:** https://github.com/skylot/jadx

**Alternatives:** apktool






## Internet-Scale Device Discovery




#### IoT & Service Search Engines



##### Shodan ⭐

The internet-wide device search engine par excellence; query banners, ports, and products to catalog exposed routers, cameras, PLCs, and MQTT brokers, with Shodan CLI/scripts for pipelining results.

**When:** Mapping exposure of a device model or product family (support/account required) before any lab testing against your own instances.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install shodan`

**URL:** https://www.shodan.io/

**Alternatives:** Censys


##### Censys

Internet-wide scan and certificate transparency search (sweeping TLS/SSH/HTTP banners) that indexes devices by product string, useful for wide data pulls on banners and certificates for IoT gear.

**When:** Banner/certificate-level device fingerprinting at scale, especially where Shodan's vantage set differs.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install censys`

**URL:** https://search.censys.io/

**Alternatives:** Shodan






## Exploit & Device Databases




#### CVE & Vulnerability Lookup



##### cve-search (CIRCL) ⭐

Offline CVE database with Mongo/Elastic backends that correlates CVEs to vendors, products, and CPE strings, letting you answer 'what is known-bad for this router chipset' without touching the internet.

**When:** Correlating a firmware version or chipset CPE against published CVEs during lab triage.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/cve-search/cve-search && cd cve-search && make`

**URL:** https://github.com/cve-search/cve-search

**Alternatives:** NVD API


##### NVD API

NIST's public REST API for the National Vulnerability Database; keyword-searchable CVE records with descriptions, CVSS, and affected configurations for quick lookups indexed by product.

**When:** Direct, no-infra CVE lookups scoped to a product/CPE during a device assessment.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `curl 'https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:lynx:...'`

**URL:** https://nvd.nist.gov/developers/vulnerabilities

**Alternatives:** cve-search


#### IoT Vulnerability Wikis



##### Exploitee.rs ⭐

Wiki aggregating router/IoT hardware exploits, firmware analysis write-ups, and device-specific notes maintained by the community; excellent starting reference before you re-derive anything yourself.

**When:** Looking up an existing method or exploit note for a specific router/device model during lab research.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `browse: https://www.exploitee.rs/`

**URL:** https://www.exploitee.rs/

**Alternatives:** cve-search






## RFID & NFC (Physical Access Tokens)

Proxmark3 ⭐


#### Proxmark3 ⭐

The Swiss-army RFID/NFC research device (125 kHz + 13.56 MHz) covering low- and high-frequency tags, Mifare, iClass, HID, ISO14443/ISO15693, and EMV; use the actively maintained Iceman (RfidResearchGroup) firmware fork for sniff, clone, and direct attacks.

**When:** Reading, sniffing, or cloning badges, keyfobs, and access-control cards you legitimately test, plus auditing a site's RFID exposure.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/RfidResearchGroup/proxmark3 && cd proxmark3 && make`

**URL:** https://github.com/RfidResearchGroup/proxmark3

**Alternatives:** libnfc


#### libnfc

Low-level NFC library with CLI tools (nfc-list, nfc-mfclassic) that read, write, and clone ISO14443A tags through cheap USB readers like the ACR122U.

**When:** Quick reads (UID, Mifare classic blocks) with a plain USB NFC reader before reaching for a full Proxmark3.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install libnfc-bin`

**URL:** https://github.com/nfc-tools/libnfc

**Alternatives:** Proxmark3





