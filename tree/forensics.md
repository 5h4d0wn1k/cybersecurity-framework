# 🔬 Digital Forensics & Incident Response

Analyze memory, disk, carved files, artifacts, and timelines from your own systems, lab evidence, and incident-response cases you legally possess.

## Memory Forensics

Volatility 3 ⭐


#### Volatility 3 ⭐

The de-facto memory forensics framework: plugin-based analysis of RAM dumps (raw, EWF, crash/hibernation) across Windows, Linux, macOS, and Android — process listing, network artifacts, injected code, and more.

**When:** Start here with any memory dump from a lab box or captured incident host; run pslist/pscan, netscan, and malfind to build the runtime picture.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pip install volatility3`

**URL:** https://github.com/volatilityfoundation/volatility3

**Alternatives:** MemProcFS, Volatility 2


#### Volatility 2

The classic Python 2 framework (archived but stable) with the deepest plugin ecosystem and profile-based analysis for older Windows, Linux, and macOS dumps.

**When:** Reach for it when a legacy or niche image lacks a Volatility 3 symbol table, or a plugin you need only exists in the classic tree.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/volatilityfoundation/volatility`

**URL:** https://github.com/volatilityfoundation/volatility

**Alternatives:** Volatility 3


#### MemProcFS

Mounts a memory dump or live target (PCILeech FPGA/LeechAgent) as a virtual filesystem of processes, registry, and artifacts, with a batch forensic mode and YARA scanning.

**When:** Fast interactive triage of a Windows dump without plugin CLI gymnastics, or live acquisition during your own incident response.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/ufrisk/MemProcFS`

**URL:** https://github.com/ufrisk/MemProcFS

**Alternatives:** Volatility 3






## Disk Forensics & Imaging

Autopsy ⭐


#### Autopsy ⭐

GUI platform built on The Sleuth Kit: opens images and live drives, recovers deleted files, and runs ingest modules for web history, keyword search, and carving inside a case workflow.

**When:** First-pass interactive examination of a drive or memory-card image from your own casework or a lab exercise — ingest everything, then drill into findings.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `download installer from https://www.sleuthkit.org/autopsy/download.php`

**URL:** https://www.sleuthkit.org/autopsy/

**Alternatives:** The Sleuth Kit


#### The Sleuth Kit

Command-line suite for raw/EWF images: mmls for partition layout, fls/icat to list and extract inodes, istat for metadata, and tsk_recover for file recovery — the engine under Autopsy.

**When:** Scripted or headless analysis, or when you need precise inode-level answers Autopsy hides behind its GUI.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install sleuthkit`

**URL:** https://sleuthkit.org/sleuthkit/

**Alternatives:** Autopsy


#### dc3dd

Forensic fork of GNU dd adding on-the-fly hashing, split output, pattern wiping, and detailed logging — evidence-grade imaging of a source drive to a file.

**When:** Capture a definitive image of your own drive or USB stick before analysis so you examine the copy, not the live evidence.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install dc3dd`

**URL:** https://sourceforge.net/projects/dc3dd/

**Alternatives:** Guymager


#### Guymager

GUI forensic imager for Linux producing flat (dd), EWF (E01), and AFF images with multi-threaded, pipelined reads for fast verified acquisitions.

**When:** Click-driven imaging with progress bars and check-verification when you prefer a window over dc3dd's command line.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install guymager`

**URL:** https://guymager.sourceforge.io/

**Alternatives:** dc3dd






## File Carving & Recovery

foremost ⭐


#### foremost ⭐

Header/footer and data-structure file carver (originally from AFOSI) that extracts JPEG, ZIP, PDF, and other signatures from raw images or drives via a configurable file-type table.

**When:** Unallocated-space fishing: run it on an image or free-space carve to recover deleted files the live filesystem no longer lists.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install foremost`

**URL:** https://foremost.sourceforge.net/

**Alternatives:** scalpel, PhotoRec/testdisk


#### bulk_extractor

Scans any input byte-by-byte and extracts emails, URLs, credit-card numbers, JPEGs, and JSON to feature files — recursively decoding compressed or encoded blocks without parsing the filesystem.

**When:** Rapid 'what is in this blob' extraction over images or wiped drives before deep filesystem analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install bulk-extractor`

**URL:** https://github.com/simsong/bulk_extractor

**Alternatives:** foremost


#### scalpel

Filesystem-independent carver using a header/footer definition database — a fast rewrite of foremost's carving engine with tunable per-type carve-size limits.

**When:** When you need per-type carve-size tuning or an alterative engine for a stubborn image carve beyond foremost defaults.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install scalpel`

**URL:** https://www.kali.org/tools/scalpel/

**Alternatives:** foremost, PhotoRec/testdisk


#### PhotoRec/testdisk

Signature-based recovery of 440+ file formats plus TestDisk for partition-table repair and undelete; no filename reconstruction, but deep salvage on corrupted or reformatted media.

**When:** Last-ditch recovery from a reformatted or damaged partition or thumb drive in your own hardware lab.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install testdisk`

**URL:** https://www.cgsecurity.org/

**Alternatives:** foremost, scalpel






## Timeline & Log Analysis

plaso/log2timeline ⭐


#### plaso/log2timeline ⭐

log2timeline extracts timestamped events (filesystem, registry, EVTX, browser, application logs) from an image or mount point into a Plaso storage file; psort turns it into a filtered super-timeline.

**When:** Build the master super-timeline of an image: collect once with log2timeline, then slice and filter per question with psort.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pip install plaso`

**URL:** https://github.com/log2timeline/plaso

**Alternatives:** Timesketch


#### Timesketch

Google's web front-end for collaborative timeline analysis: import Plaso output and search, filter, star, and annotate events in your browser.

**When:** Turn a giant Plaso timeline into something huntable — collaborative review and annotation for your own case and lab reports.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/google/timesketch`

**URL:** https://github.com/google/timesketch

**Alternatives:** plaso/log2timeline






## Windows Artifact Analysis

KAPE ⭐


#### KAPE ⭐

Kroll Artifact Parser and Extractor: selects forensically useful artifacts (registry hives, EVTX, Prefetch, MFT, browser files) from a live device or mounted image, then parses them with bundled tools in minutes.

**When:** Speed triage in your own incident response or lab: point it at a live Windows box or image and get parsed artifacts quickly; extend via community KapeFiles targets.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `download from ericzimmerman.github.io (Get-KAPE)`

**URL:** https://github.com/EricZimmerman/KapeFiles

**Alternatives:** Eric Zimmerman's Tools


#### Eric Zimmerman's Tools

Suite of focused parsers — RECmd/Registry Explorer, PECmd (Prefetch), LECmd (LNK), JLECmd (JumpLists), ShellBags, Amcache, MFTECmd — answering execution-timeline questions from individual artifacts.

**When:** Deep-dive a targeted artifact set: ask 'what executed, when, by whom' via Prefetch, LNK/JumpList, Amcache, and registry traces.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Get-ZimmermanTools.ps1 (PowerShell)`

**URL:** https://ericzimmerman.github.io/

**Alternatives:** KAPE






## Incident Response & Triage

Velociraptor ⭐


#### Velociraptor ⭐

Open-source endpoint visibility and collection platform: deploy lightweight agents, run prebuilt forensic artifacts and fleet-wide hunts via VQL, and pull process, disk, and registry data to a central server.

**When:** Your own lab or home-network incident: stand up a server, install agents, and answer 'what happened on these hosts' with artifacts and hunts.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `download velociraptor binary from GitHub releases; run server and deploy agent`

**URL:** https://github.com/Velocidex/velociraptor

**Alternatives:** UAC


#### UAC

Unix-like Artifacts Collector: no-install shell script collecting processes, users, logs, cron, running-file hashes, and bodyfiles from Linux/macOS/BSD/ESXi in order of volatility, packaged for handoff.

**When:** Rapid live triage on a Linux box you're responding to — run from a USB or read-only medium and hand the archive to your analysis machine.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/tclahr/uac`

**URL:** https://github.com/tclahr/uac

**Alternatives:** Velociraptor





