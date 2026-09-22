# 🔌 IoT, Embedded & Firmware Security

Reverse, emulate, and attack embedded devices in your lab: firmware extraction, boot-level emulation, JTAG/UART probing, side-channels, and RFID.

## Firmware Extraction & Static Review

binwalk ⭐


#### binwalk ⭐

Identifies and extracts embedded files and filesystems (squashfs, cramfs, JFFS2, kernels, U-Boot) from a firmware image via magic signatures, with entropy analysis to find encrypted/compressed regions.

**When:** Every firmware image starts here: carve the filesystem out of the blob before anything else can run.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `cargo install binwalk`

**URL:** https://github.com/ReFirmLabs/binwalk

**Alternatives:** firmware-mod-kit, FirmWalker


#### FirmWalker

Bash script that greps an extracted or mounted root filesystem for secrets: etc/shadow and passwd, SSL keys/certs, config files, admin/password keywords, dropbear/ssh, and URLs.

**When:** Ten seconds after binwalk extraction to surface default creds, key material, and backdoors before you read anything by hand.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/craigz28/firmwalker`

**URL:** https://github.com/craigz28/firmwalker

**Alternatives:** binwalk


#### firmware-mod-kit (FMK)

Extract-and-rebuild toolkit for router firmware (squashfs/cramfs/JFFS2); lets you patch binaries or files and repack a bootable image. Legacy: descended from the Google Code project and largely unmaintained, so expect to fix toolchain issues.

**When:** When you actually need to modify and re-flash a vendor image (e.g. inject a telnetd) rather than just read it.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/rampageX/firmware-mod-kit`

**URL:** https://github.com/rampageX/firmware-mod-kit

**Alternatives:** binwalk






## Firmware Emulation & Dynamic Analysis

QEMU ⭐


#### QEMU ⭐

Full-system emulator covering ARM, MIPS, RISC-V, and more; boots extracted Linux root filesystems or bare-metal board images, and its user-mode builds runs single binaries or architectures different to your host.

**When:** The foundation for all emulation: boot the extracted filesystem, or dynamically analyze a single firmware binary before wiring up full-stack tooling.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install qemu-system-arm qemu-system-mips`

**URL:** https://www.qemu.org

**Alternatives:** FirmAE, FAT


#### FirmAE

Fully-automated emulation framework (Firmadyne-derived) that uses arbitration heuristics to boot router/IP-camera firmware at ~79% success, exposing the web UI/SSH so you can fuzz and exploit it dynamically.

**When:** Full-system dynamic analysis of Linux-based IoT firmware on a big batch, when Firmadyne-style boot failures are blocking you.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone --recursive https://github.com/pr0v3rbs/FirmAE`

**URL:** https://github.com/pr0v3rbs/FirmAE

**Alternatives:** FAT


#### Firmware Analysis Toolkit (FAT)

Attify's one-command wrapper around Firmadyne that boots Linux router firmware in QEMU without the PostgreSQL dependency; prints the emulated IP so you can hit its web server from the host.

**When:** Quick, scripted boot of a single firmware image to reach its web UI and poke at it by hand.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone --recursive https://github.com/attify/firmware-analysis-toolkit && ./setup.sh`

**URL:** https://github.com/attify/firmware-analysis-toolkit

**Alternatives:** QEMU, FirmAE






## Serial & Debug Ports (UART / JTAG / SWD)

OpenOCD ⭐


#### OpenOCD ⭐

On-chip debugger for JTAG/SWD with a large catalog of CPU and flash targets, dozens of adapter drivers, and scripting via TCL; reads flash dumps, halts CPUs, and sets breakpoints on running firmware.

**When:** You found a JTAG/SWD header (or pin out a testpad): OpenOCD + a cheap adapter gets you a debugger on nearly any target.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `sudo apt install openocd`

**URL:** https://openocd.org

**Alternatives:** urJTAG, J-Link, Bus Pirate


#### urJTAG

Universal JTAG library and tools, descendant of the old openwince tools; strong at boundary-scan and flash programming where OpenOCD lacks target or chain support.

**When:** JTAG chains, boundary scan over infrastructure, or obscure flash parts that OpenOCD doesn't have configured.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install urjtag`

**URL:** https://urjtag.sourceforge.io/

**Alternatives:** OpenOCD


#### Bus Pirate

Open-source serial multi-tool (Bus Pirate 5 current): drive SPI/I2C/UART/1-Wire, read serial flash and EEPROMs, sniff buses, act as a low-speed logic analyzer, and glitch a target — all from a serial terminal.

**When:** Dumping an SPI flash or EEPROM, sniffing an I2C/SPI bus between chips, or quick protocol probing before you break out a full logic analyzer.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `hardware (dangerousprototypes.com) + any serial terminal, e.g. sudo apt install picocom`

**URL:** https://buspirate.com/

**Alternatives:** OpenOCD


#### minicom

The classic serial terminal for UART consoles at arbitrary baud rates; the everyday tool for reaching a bootloader, root shell, or firmware upgrade prompt over the debug UART.

**When:** UART pads/traces are exposed and you want bootloader or shell access to the device quickly.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install minicom`

**URL:** https://salsa.debian.org/minicom-team/minicom

**Alternatives:** picocom, screen


#### J-Link (SEGGER)

Commercial debug-probe family (SEGGER) with polished SWD/JTAG software, flash loader support across thousands of micros, and RTT for fast printf-style logging from target firmware.

**When:** A board already exposes a J-Link/SWD header, or you want a trouble-free flash-and-debug flow on a supported MCU instead of fighting adapter quirks.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `commercial hardware + SEGGER J-Link software suite (segger.com)`

**URL:** https://www.segger.com/products/debug-probes/j-link/

**Alternatives:** OpenOCD, urJTAG






## Side-Channel & Fault Injection

ChipWhisperer ⭐


#### ChipWhisperer ⭐

Open-source, open-hardware lab for power/EM side-channel analysis and voltage/clock glitching: capture power traces, run correlation power analysis to recover keys, and glitch to skip checks (CW-Lite, CW-Husky).

**When:** Assessing a secure MCU's resistance to key extraction or fault injection — on a target board you own — where the hardware is the oracle.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `pip install chipwhisperer`

**URL:** https://github.com/newaetech/chipwhisperer

**Alternatives:** Proxmark3 (RFID — see rfid-nfc)






## RFID & NFC (Physical Access Tokens)

Proxmark3 ⭐


#### Proxmark3 ⭐

The Swiss-army RFID/NFC research device (125 kHz + 13.56 MHz) covering low- and high-frequency tags — Mifare, iClass, HID, ISO14443/ISO15693, EMV — to sniff, clone, and pen-test access credentials; use the actively maintained Iceman firmware fork.

**When:** Reading, sniffing, or cloning badges, keyfobs, and access-control cards you legitimately test, plus auditing a site's RFID exposure.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/RfidResearchGroup/proxmark3 && cd proxmark3 && make`

**URL:** https://github.com/RfidResearchGroup/proxmark3

**Alternatives:** libnfc


#### libnfc

Low-level NFC library with CLI tools (nfc-list, nfc-mfclassic, nfclibnfc) that read, write, and clone ISO14443A tags through cheap USB readers like the ACR122U.

**When:** Quick reads (UID, Mifare classic blocks) with a plain USB NFC reader before you reach for a full Proxmark3.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install libnfc-bin`

**URL:** https://github.com/nfc-tools/libnfc

**Alternatives:** Proxmark3





