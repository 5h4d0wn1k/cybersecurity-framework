# 🔬 Digital Forensics & Incident Response

Analyze memory, disk, carved files, artifacts, and timelines from your own systems, lab evidence, and incident-response cases you legally possess.

## Disk Imaging & Forensic Acquisition




#### Command-Line Imagers



##### dd ⭐

GNU coreutils bit-copy utility that creates a byte-for-byte image of any block device — the universal imaging baseline every forensics distro ships.

**When:** Quick raw image of your own drive, USB stick, or SD card when you just need a faithful copy and will hash it yourself.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install coreutils`

**URL:** https://www.gnu.org/software/coreutils/

**Alternatives:** dc3dd, ddrescue


##### ddrescue

GNU data-recovery imager that resists read errors, logs bad blocks, and retries them after the rest of the media is copied — built to salvage failing or damaged storage.

**When:** The drive clicks or returns I/O errors: let ddrescue build a mostly-complete image first, then analyze the rescued copy instead of the failing disk.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gddrescue`

**URL:** https://www.gnu.org/software/ddrescue/

**Alternatives:** dc3dd


##### dc3dd

Forensic fork of GNU dd that adds on-the-fly hashing, split output, pattern wiping, and a detailed acquisition log — evidence-grade imaging in one pass.

**When:** Capture a definitive, hash-verified image of a source drive before analysis so you examine the copy, not the live evidence.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install dc3dd`

**URL:** https://sourceforge.net/projects/dc3dd/

**Alternatives:** dd, guymager


#### GUI Imagers



##### FTK Imager ⭐

Exterro's free, widely-used acquisition and preview tool: images drives/memory to raw, E01, and AFF formats, computes hashes, and mounts images for instant browsing.

**When:** Click-driven imaging with E01 support (or compressed raw) straight to a case folder; it also does live RAM acquisition when needed.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download the free installer from exterro.com and run FTK Imager`

**URL:** https://www.exterro.com/digital-forensics-software/ftk-imager

**Alternatives:** guymager


##### Guymager

Linux GUI forensic imager producing flat (dd), EWF (E01), and AFF images with multi-threaded pipelined reads and verification progress per device.

**When:** Window-based imaging with progress bars and check-verification on a Linux analysis box when you prefer a GUI over dc3dd's command line.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install guymager`

**URL:** https://guymager.sourceforge.io

**Alternatives:** dc3dd, ftk-imager






## Collection, Carving & Data Recovery




#### forensicsiso ◆ by 5h4d0wn1k

Full DFIR workstation — disk/memory/log/pcap/registry/browser/email parsing, super-timelining, cross-artifact correlation, chain-of-custody.

**When:** Running end-to-end incident-response analysis on acquired evidence.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/5h4d0wn1k/forensicsiso`

**URL:** https://github.com/5h4d0wn1k/forensicsiso

**Alternatives:** Own tool — lab/authorized use only


#### Fast Collection & RAM Capture



##### KAPE ⭐

Kroll Artifact Parser and Extractor: selects forensically useful artifacts (registry hives, EVTX, Prefetch, MFT, browser files) from a live device or mounted image, then parses them with bundled tools in minutes.

**When:** Speed triage in your own incident response or lab: point it at a live Windows box or mounted image and get parsed artifacts quickly; extend with community KapeFiles targets.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download KAPE from Kroll's site (or GitHub releases) and run kape.exe`

**URL:** https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kape

**Alternatives:** ericzimmerman-tools


##### Magnet RAM Capture

Free Windows memory acquisition tool that dumps physical RAM to raw .DMP files with a small footprint and optional command-line mode — ideal for preserving volatile evidence before it disappears.

**When:** Grab the memory of a live lab or incident host before anything else — the .DMP output feeds straight into Volatility.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Fill the download form at magnetforensics.com and run the standalone capture utility`

**URL:** https://www.magnetforensics.com/resources/magnet-ram-capture/

**Alternatives:** volatility-3


#### Filesystem Analysis Engines



##### The Sleuth Kit ⭐

Command-line suite for raw/EWF images: mmls for partition layout, fls/icat to list and extract inodes, istat for metadata, and tsk_recover for recovery — the engine underneath Autopsy.

**When:** Scripted or headless analysis, or when you need precise inode-level answers Autopsy hides behind its GUI.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install sleuthkit`

**URL:** https://sleuthkit.org/sleuthkit/

**Alternatives:** autopsy


##### Autopsy

GUI platform built on The Sleuth Kit: opens images and live drives, recovers deleted files, and runs ingest modules for web history, keyword search, and carving inside a case workflow.

**When:** First-pass interactive examination of a drive or memory-card image from your own casework or lab — ingest everything, then drill into findings.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the installer from sleuthkit.org/autopsy and run it`

**URL:** https://www.sleuthkit.org/autopsy/

**Alternatives:** sleuth-kit


#### File Carving & Recovery



##### foremost ⭐

AFOSI-origin header/footer and data-structure carver that extracts JPEG, ZIP, PDF, and other signatures from raw images or drives via a configurable file-type table.

**When:** Unallocated-space fishing: run it on an image or free-space carve to recover deleted files the live filesystem no longer lists.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install foremost`

**URL:** https://foremost.sourceforge.net/

**Alternatives:** scalpel, testdisk


##### scalpel

Filesystem-independent carver using a header/footer definition database — a rewrite of foremost's engine with per-type carve-size tuning; the original repo is stale, machn1k/scalpel-2.0 carries it on.

**When:** Stubborn image carries where you need tuned per-type size limits or a second carving engine beyond foremost defaults.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install scalpel`

**URL:** https://github.com/machn1k/scalpel-2.0

**Alternatives:** foremost, testdisk


##### TestDisk / PhotoRec

Signature-based recovery of 440+ file formats plus TestDisk for partition-table repair and undelete; no filename reconstruction, but deep salvage on corrupted or reformatted media.

**When:** Last-ditch recovery from a reformatted or damaged partition or thumb drive in your own hardware lab.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install testdisk`

**URL:** https://www.cgsecurity.org

**Alternatives:** foremost, scalpel


#### Feature & Digital-Object Extraction



##### bulk_extractor ⭐

Scans any input byte-by-byte and extracts emails, URLs, credit-card numbers, JPEGs, and JSON to feature files — recursively decoding compressed or encoded blocks without parsing the filesystem.

**When:** Rapid 'what is in this blob' extraction over images or wiped drives before deep filesystem analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install bulk-extractor`

**URL:** https://github.com/simsong/bulk_extractor

**Alternatives:** foremost






## Memory Forensics




#### Analysis Frameworks



##### Standard CLI Frameworks



###### Volatility 3 ⭐

The de-facto memory forensics framework: plugin-based analysis of RAM dumps (raw, EWF, crash/hibernation) across Windows, Linux, macOS, and Android — processes, network artifacts, injected code, and more.

**When:** Start here with any memory dump from a lab box or captured incident host; run pslist/pscan, netscan, and malfind to build the runtime picture.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pip install volatility3`

**URL:** https://github.com/volatilityfoundation/volatility3

**Alternatives:** volatility-2, memprocfs


###### Volatility 2

The classic Python 2 framework (archived but stable) with the deepest plugin ecosystem and profile-based analysis for older Windows, Linux, and macOS dumps.

**When:** Reach for it when a legacy or niche image lacks a Volatility 3 symbol table, or a plugin you need only exists in the classic tree.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/volatilityfoundation/volatility`

**URL:** https://github.com/volatilityfoundation/volatility

**Alternatives:** volatility-3


###### Rekall

Google-origin memory forensics framework born from Volatility during the 2.x era — effectively dormant since ~2020 with legacy artifacts in gray matter for older Windows/Linux images.

**When:** Reading old IR research or cross-checking a niche plugin result on a vintage dump; expect to maintain it yourself.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `pip install rekall`

**URL:** https://github.com/google/rekall

**Alternatives:** volatility-3


##### Live Mount & GUI Alternatives



###### MemProcFS ⭐

Mounts a memory dump or live target (PCILeech FPGA/LeechAgent) as a virtual filesystem of processes, registry, and artifacts, with a batch forensic mode and YARA scanning.

**When:** Fast interactive triage of a Windows dump without plugin CLI gymnastics, or live acquisition during your own incident response.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/ufrisk/MemProcFS`

**URL:** https://github.com/ufrisk/MemProcFS

**Alternatives:** volatility-3


###### Redline

Mandiant's free endpoint and memory investigation GUI: collects a volatile data set (processes, network, services, registry) from a live host or a memory dump and flags suspicious items with ATT&CK mapping — slower-moving now but still used in FTK/IR workflows.

**When:** Point-and-click triage of a live Windows endpoint or captured memory when the CLI frameworks feel heavy for your own casework.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download Redline from Mandiant's free-tools page and let the wizard collect or open a memory image`

**URL:** https://www.mandiant.com/resources/redline

**Alternatives:** memprocfs, volatility-3


#### Quick String Hunts



##### strings ⭐

GNU binutils classic that extracts printable ASCII/Unicode sequences from a raw memory dump — still the fastest way to spot C2 URLs, commands, and keys before the framework work.

**When:** Instant grep-ish pass over a dump for notable indicators, or targeted hunting using the output piped into a socket/crypto-constant search.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install binutils && strings <dump> | grep -E '[0-9]+\.'`

**URL:** https://www.gnu.org/software/binutils/

**Alternatives:** bulk-extractor






## Log, Timeline & Windows Artifact Analysis




#### Windows Artifact Parsers



##### Eric Zimmerman's Tools ⭐

Suite of focused parsers — RECmd/Registry Explorer, PECmd (Prefetch), LECmd (LNK), JLECmd (JumpLists), ShellBags, Amcache, MFTECmd — answering execution-timeline questions from individual artifacts.

**When:** Deep-dive a targeted artifact set: ask 'what executed, when, by whom' via Prefetch, LNK/JumpList, Amcache, and registry traces.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Get-ZimmermanTools.ps1 (PowerShell)`

**URL:** https://ericzimmerman.github.io/

**Alternatives:** kape, evtxecmd


##### EvtxECmd

Eric Zimmerman's direct EVTX event-log parser turning .evtx databases into CSV/JSON with formatted timestamps and named fields, ready for Timeline Explorer.

**When:** Convert raw Windows event logs from a mounted image or collection set into a queryable CSV before building your timeline.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download from EricZimmerman GitHub releases (part of Get-ZimmermanTools)`

**URL:** https://github.com/EricZimmerman/evtx

**Alternatives:** ericzimmerman-tools, hayabusa


#### Event-Log Hunting



##### Fast EVTX Detection Engines



###### Hayabusa ⭐

Yamato Security's Rust-based Windows event-log fast forensics tool that applies a huge Mitre-Attack-mapped sigma-rule library to EVTX dumps and outputs alert timelines in seconds.

**When:** Hunt lateral movement, logon anomalies, and persistence across a full C:\Windows\System32\winevt\Logs collection or exported .evtx set.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download the release binary for your OS and run hayabusa csv-timeline -d <evtx_dir>`

**URL:** https://github.com/Yamato-Security/hayabusa

**Alternatives:** evtxecmd, apt-hunter


###### APT-Hunter

Python-based EVTX analysis tool feeding exported Windows event logs through threat-hunting queries to detect hacking activity and TTPs via suspicious event correlations.

**When:** Point it at your exported .evtx logs for a quick attacker-TTP posture check before going deep with sigma/hunting frameworks.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ahmedkhlief/APT-Hunter && python3 APT-Hunter.py --evtx <evtx_folder>`

**URL:** https://github.com/ahmedkhlief/APT-Hunter

**Alternatives:** hayabusa


#### Timeline & Super-Timelines



##### plaso / log2timeline ⭐

log2timeline extracts timestamped events (filesystem, registry, EVTX, browser, application logs) from an image or mount point into a Plaso storage file; psort turns it into a filtered super-timeline.

**When:** Build the master super-timeline of an image: collect once with log2timeline, then slice and filter per question with psort.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `python3 -m pip install plaso`

**URL:** https://github.com/log2timeline/plaso

**Alternatives:** timeline-explorer, timesketch


##### Timeline Explorer

Eric Zimmerman's high-performance CSV timeline viewer with filters, bookmarks, and quick histogramning — the companion screen for Plaso/EvtxECmd CSV output.

**When:** Load a super-timeline or artifact CSV and filter/hide columns interactively to answer 'what happened when' without SQL.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download from ericzimmerman.github.io (Chocolatey: choco install timelineexplorer)`

**URL:** https://ericzimmerman.github.io/

**Alternatives:** plaso






## Browser & Internet Artifacts




#### History Database Decoders



##### Hindsight ⭐

Obsidian Forensics' Chromium/Chrome/Edge history parser: decrypts login data, decodes History/SQLite, typed URLs, cookies, and downloads into a readable report with timestamp decoding.

**When:** Extract reconstructable browser activity from the Chrome/Edge profile directory of a mounted image or live host in your own case.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip install hindsight`

**URL:** https://github.com/obsidianforensics/hindsight

**Alternatives:** browserhistoryviewer


##### DB Browser for SQLite

Full-featured GUI for reading and querying SQLite databases — the manual backstop when you need to poke raw browser History/places.sqlite rows yourself.

**When:** Directly inspect a browser database (history, cookies, bookmarks, cache index) when a parser misses a field or you want ad-hoc SQL.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install sqlitebrowser`

**URL:** https://sqlitebrowser.org

**Alternatives:** hindsight


#### History & Cache Viewers



##### BrowserHistoryViewer ⭐

Foxton Forensics' free viewer for Chrome, Edge, Firefox, IE, and Safari history with keyword/date filtering, timezone-aware timestamps, and easy CSV export.

**When:** Quick, clean table of browsing history with proper timestamp conversion for a report or super-timeline merge.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download the free installer from foxtonforensics.com`

**URL:** https://www.foxtonforensics.com/browser-history-viewer

**Alternatives:** browsinghistoryview, hindsight


##### BrowsingHistoryView

NirSoft utility that reads history from all major browsers (Firefox, Chrome, IE/Edge, Opera) into one table across all user profiles, local or from an external drive.

**When:** One-pass aggregation of every browser profile's history on a live system or mounted image into a single viewable export.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download BrowsingHistoryView.zip from nirsoft.net and run the executable`

**URL:** https://www.nirsoft.net/utils/browsing_history_view.html

**Alternatives:** browserhistoryviewer


##### ChromeHistoryView

NirSoft tool focused purely on Chrome/Chromium-based history: reads the local History database and dumps entries to CSV/HTML with optional read from the live profile.

**When:** Chrome-only deep dive when you want granular control and export options Eclipse the general aggregators.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Download ChromeHistoryView.zip from nirsoft.net`

**URL:** https://www.nirsoft.net/utils/chrome_history_view.html

**Alternatives:** browsinghistoryview


##### ChromeCacheView

NirSoft Chrome cache reader that lists files stored in the Cache/Cache_Data folders with URLs, sizes, and download times, plus option to copy recoverable cached files to a folder.

**When:** Recover cached images/videos being staged by a live chrome user, or enumerate what content was browsed even after history deletion.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Download ChromeCacheView.zip from nirsoft.net`

**URL:** https://www.nirsoft.net/utils/chrome_cache_view.html

**Alternatives:** browsinghistoryview





