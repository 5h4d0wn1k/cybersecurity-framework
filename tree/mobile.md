# 📱 Mobile Application Security (Android & iOS)

Testing your own or authorized Android & iOS apps: static analysis, decompilation, runtime instrumentation, traffic interception, and attack-surface automation.

## Static Analysis & Vulnerability Scanning

### MobSF (Mobile Security Framework) ⭐

Automated all-in-one analyzer for APK, IPA, and Windows mobile binaries: permissions, exported components, insecure manifest/crypto config, hardcoded secrets, and OWASP MASTG-style checks surfaced in a clean web UI plus REST API for CI.

**When:** Always the first pass on an app binary you are authorized to test — upload the APK or IPA, read the findings report, then drill into specific hits for manual follow-up.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest`

**URL:** https://github.com/MobSF/Mobile-Security-Framework-MobSF

**Alternatives:** quark-engine, apkid


### Quark-Engine

Obfuscation-neglect APK scoring engine (distinct from the old LinkedIn 'qark'): matches the app's call graph against a rule set of suspicious behaviors — crypto misuse, dynamic dex loading, accessibility/SMS abuse, C2 calls — and emits confidence-scored reports.

**When:** Quick second opinion on an APK for risky behavior patterns after MobSF, or to generate new detection rules from code you reverse yourself.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install -U quark-engine && freshquark`

**URL:** https://github.com/quark-engine/quark-engine

**Alternatives:** mobsf, apkid


### APKiD

YARA-based detector for packers, protectors, and obfuscators (DexProtector, Bangcle, qihoo, etc.) inside an APK/DEX before any reversing effort begins.

**When:** Scope a hardened app early: knowing it is packed tells you static-only analysis is not enough and you will need runtime dexdump (frida-dexdump).

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install apkid`

**URL:** https://github.com/rednaga/APKiD

**Alternatives:** quark-engine, mobsf


## Decompilers & APK Tooling

### jadx ⭐

One-step DEX-to-Java decompiler with GUI and CLI that rebuilds readable Java source, resources, and AndroidManifest.xml into a searchable whole-project view.

**When:** Default decompilation of a fresh APK: navigate the reconstructed project, follow flows across classes, and copy logic into notes.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download the latest zip from GitHub releases (or 'brew install jadx')`

**URL:** https://github.com/skylot/jadx

**Alternatives:** apktool, dex2jar


### apktool

Decodes Android resources and AndroidManifest.xml into editable form and rebuilds the APK; exposes smali/baksmali bytecode for patching when Java source is not needed.

**When:** Modify res/ or smali and repackage the APK (behavior/repackage tests), or pull the manifest cleanly when jadx output gets mangled.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download the jar wrapper from GitHub releases (or 'sudo apt install apktool')`

**URL:** https://github.com/iBotPeaches/Apktool

**Alternatives:** jadx, dex2jar


### frida-dexdump

Dumps in-memory DEX files from a running app via Frida, defeating packers and protectors that only materialize code at runtime.

**When:** Analyze a packed/hardened app: launch it on a device, dump the loaded dex at runtime, then feed the recovered classes back into jadx.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install frida-dexdump`

**URL:** https://github.com/hluwa/frida-dexdump

**Alternatives:** jadx, apktool


### dex2jar

The classic DEX-to-JAR converter (paired with JD-GUI for a quick Java view); effectively unmaintained but still the format older guides and toolchains expect.

**When:** Legacy fallback decompile when jadx chokes on an unusual format, or when a downstream tooling chain requires .jar/.class input.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Download dex2jar-2.x.zip from GitHub releases`

**URL:** https://github.com/pxb1988/dex2jar

**Alternatives:** jadx, apktool


## Dynamic Instrumentation & Runtime Testing

### Frida ⭐

Cross-platform dynamic instrumentation toolkit: inject a frida-server process onto Android/iOS to hook functions, bypass SSL pinning and root detection, trace crypto calls, and invoke internal methods from a Python/JS REPL.

**When:** The runtime layer of most mobile tests — bypass cert pinning, trace sensitive functions, dump buffers, and poke internals static analysis cannot reach.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install frida-tools && push a matching-version frida-server to the device`

**URL:** https://frida.re

**Alternatives:** objection, magisk


### objection

Frida-powered runtime exploration toolkit: one-liners to disable SSL pinning and root checks, browse Android/iOS storage (Keychain, SharedPrefs, Bundle), and explore exported classes without writing custom JS.

**When:** Quick interactive runtime pass on your own app — disable pinning/root detection and inspect stored data — when hand-writing Frida scripts is overkill.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install objection`

**URL:** https://github.com/sensepost/objection

**Alternatives:** frida


### Magisk

Systemless rooting framework for physical Android devices and emulators that gives Frida, adb, and your injected agents the root context most dynamic tests need; it is a rooting kit first, not a pentest tool.

**When:** Prepare a dedicated test device with an unlocked bootloader when an app refuses to run on stock or detects the emulator you were using.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `Install the Magisk APK or 'fastboot boot magisk_patched-<hash>.img' on an unlocked-bootloader device`

**URL:** https://github.com/topjohnwu/Magisk

**Alternatives:** frida, objection


### adb (Android Debug Bridge)

Google's core device bridge from Android platform-tools: install apps, push/pull files, shell in, port-forward, install CA certificates, and capture logcat.

**When:** Every device setup step — enumerate devices, push frida-server and test certificates, and snapshot app data before and after a test run.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install adb`

**URL:** https://developer.android.com/tools/adb

**Alternatives:** magisk, frida


## Traffic Interception & Analysis

### mitmproxy ⭐

Interactive HTTPS intercepting proxy built for mobile workflows: install its CA on the device, replay or rewrite HTTP/2 and gRPC flows, and script custom handling with Python addons; pair with a Frida/objection pinning bypass to decrypt app TLS.

**When:** Any network-level test of your own apps — log, tamper, or replay API traffic from a rooted device, emulator, or iOS simulator.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** charles proxy, burp suite (see web domain)


### Charles Proxy

Commercial GUI HTTPS proxy with click-through SSL proxying, rewrite/breakpoints, and a visual request timeline — the macOS-centric alternative to a terminal proxy.

**When:** Point-and-click interception and rewriting during manual iOS testing on a workstation when you prefer a GUI over mitmproxy's keyboard-driven flow.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Download from charlesproxy.com (trial, then paid license)`

**URL:** https://www.charlesproxy.com

**Alternatives:** mitmproxy


## Attack-Surface Automation & Fuzzing

### Drozer ⭐

The reference Android attack-surface framework: an on-device agent lets you assume the role of another app and enumerate/exploit exported activities, content providers, services, and broadcast receivers from a console.

**When:** After static analysis, map the app's IPC/component attack surface and probe each exported component for authorization and data-exposure flaws.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/ReversecLabs/drozer.git && cd drozer && pip install . (plus the drozer agent APK on the device)`

**URL:** https://github.com/ReversecLabs/drozer

**Alternatives:** android tamer


### Android Tamer

Linux distro/VM prebundling dozens of Android-sec tools (jadx, apktool, MobSF, AndroBugs, Frida, radare2). Tamer 4 is end-of-life and Tamer 5 is under construction, so it is a convenience starting point, not a project to build on.

**When:** Stand up a one-shot preconfigured Android-tools VM for a specific engagement; otherwise skip — each tool here installs more reliably on your own base OS.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `Download the Tamer 4 VM from TamerPlatform and import into VirtualBox/VMware`

**URL:** https://github.com/AndroidTamer/AndroidTamer

**Alternatives:** mobsf, frida

