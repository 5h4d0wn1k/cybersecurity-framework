# 📱 Mobile Application Security (Android & iOS)

Testing your own or authorized Android & iOS apps: static analysis, decompilation, runtime instrumentation, traffic interception, emulators, and CTF practice grounds.

## Android Static Analysis




#### mobsek ◆ by 5h4d0wn1k

Offline mobile app security suite — APK/AXML/DEX, Mach-O, X.509 analysis, Frida hooks, deterministic threat score.

**When:** Triage mobile apps you have permission to analyze.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/5h4d0wn1k/mobsek`

**URL:** https://github.com/5h4d0wn1k/mobsek

**Alternatives:** Own tool — lab/authorized use only


#### Decompilers



##### jadx ⭐

One-step DEX-to-Java decompiler (CLI and GUI) that rebuilds readable Java source, resources, and AndroidManifest.xml into a searchable project view.

**When:** Default first pass on a fresh APK you are authorized to test: navigate the reconstructed project and follow flows across classes.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download the latest zip from GitHub releases (or brew install jadx)`

**URL:** https://github.com/skylot/jadx

**Alternatives:** jadx-gui, apktool


##### jadx-gui

The graphical frontend bundled with jadx for interactive cross-referencing, renaming obfuscated identifiers, and exporting decompiled selections.

**When:** Interactive exploration and annotation when reading a flat decompile is not enough and you want quick class-to-class navigation.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Launch the gui main class from the jadx release zip (or brew install jadx)`

**URL:** https://github.com/skylot/jadx

**Alternatives:** jadx, bytecode viewer


#### APK & Bytecode Tooling



##### apktool ⭐

Decodes resources and AndroidManifest.xml into editable form and exposes smali/baksmali bytecode, then rebuilds the APK for repackaging tests.

**When:** Edit res/ or smali and repackage the APK for behavior/repackage checks on apps you are authorized to modify.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `Download the jar wrapper from GitHub releases (or sudo apt install apktool)`

**URL:** https://github.com/iBotPeaches/Apktool

**Alternatives:** jadx, smali


##### Bytecode Viewer

Swing viewer that combines dex2jar, CFR, and Procyon so one window shows decompiled Java plus raw bytecode for side-by-side review.

**When:** Triage a stubborn APK when a single decompiler misses, and compare decompiler output in one place.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the release jar from GitHub releases`

**URL:** https://github.com/Konloch/Bytecode-Viewer

**Alternatives:** jadx, apktool


##### Packed Code Recovery



###### frida-dexdump ⭐

Dumps in-memory DEX files from a running app through Frida, defeating packers and protectors that only materialize code at runtime.

**When:** Analyze a hardened or packed app: launch it on your test device, dump the loaded dex, then feed the recovered classes back into jadx.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install frida-dexdump`

**URL:** https://github.com/hluwa/frida-dexdump

**Alternatives:** jadx, apktool


#### Analysis Engines



##### androguard ⭐

Python library plus CLI to parse DEX/APK graphs, list permissions and exported components, and script custom static checks.

**When:** Scriptable static analysis and bespoke rules on apps you test when click-through GUI tools are not enough.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install androguard`

**URL:** https://github.com/androguard/androguard

**Alternatives:** quark-engine, mobsf


##### Behavior Scoring



###### Quark-Engine ⭐

Obfuscation-aware APK scoring engine that matches the app's call graph against suspicious-behavior rules (crypto misuse, dynamic dex loading, C2 calls) with confidence scores.

**When:** Quick second opinion on an APK for risky behavior patterns after MobSF, or building your own detection rules from reversed code.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install -U quark-engine && freshquark`

**URL:** https://github.com/quark-engine/quark-engine

**Alternatives:** mobsf, apkid


##### Packer & Obfuscator Detection



###### APKiD ⭐

YARA-based detector of packers, protectors, and obfuscators (DexProtector, Bangcle, qihoo) inside an APK or DEX before any reversing effort.

**When:** Scope a hardened app early: knowing it is packed tells you static-only analysis is not enough and runtime dexdump is needed.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install apkid`

**URL:** https://github.com/rednaga/APKiD

**Alternatives:** quark-engine, mobsf






## Android Dynamic & Runtime Testing




#### Instrumentation & Hooking



##### Frida (Android) ⭐

Injects frida-server onto a device to hook functions at runtime: bypass SSL pinning and root detection, trace crypto calls, and inspect memory.

**When:** The runtime layer of most Android tests — bypass pinning, trace sensitive APIs, and probe internals static analysis cannot reach.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install frida-tools && push a matching-version frida-server to the device`

**URL:** https://frida.re

**Alternatives:** objection, drozer


##### objection

Frida-powered runtime exploration toolkit: one-liners to disable SSL pinning and root checks and browse storage (SharedPrefs, cache) without writing JS.

**When:** Quick interactive runtime pass on your own app when hand-rolled Frida scripts are overkill.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install objection`

**URL:** https://github.com/sensepost/objection

**Alternatives:** frida (android)


#### IPC & Component Attack Surface



##### drozer ⭐

On-device agent that assumes another app's identity to enumerate and test exported activities, content providers, services, and broadcast receivers from a console.

**When:** After static analysis, map the app's IPC/component attack surface and probe each exported component for authorization and data-exposure flaws.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/ReversecLabs/drozer.git && cd drozer && pip install . (plus the drozer agent APK on the device)`

**URL:** https://github.com/ReversecLabs/drozer

**Alternatives:** objection, adb


#### Practice Apps to Battle



##### DIVA (Damn Insecure Vulnerable App) ⭐

Deliberately vulnerable Android app with a dozen fixed challenge categories (insecure logging, input validation, hardcoded keys) built for hands-on practice.

**When:** Warming up static/dynamic skills or validating your toolchain before touching a real engagement target.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download the APK from GitHub releases and install it with adb install`

**URL:** https://github.com/payatu/diva-android

**Alternatives:** insecurebankv2, mastg


##### InsecureBankv2

Purposefully vulnerable banking app exposing auth bypass, SQL injection, and exposed adb port issues for controlled practice.

**When:** Practicing mobile banking app tests (auth, crypto, IPC, storage) in an environment you fully control.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/dineshshetty/Android-InsecureBankv2 && run the bundled server, then install the APK via adb`

**URL:** https://github.com/dineshshetty/Android-InsecureBankv2

**Alternatives:** diva, mastg






## Traffic Interception & API Testing




#### Intercepting Proxies



##### mitmproxy ⭐

Interactive HTTPS intercepting proxy built for mobile workflows: install its CA on the device, rewrite or replay HTTP/2 and gRPC, and script with Python addons.

**When:** Any network-level test of your own apps — log, tamper, or replay API traffic from a rooted device or emulator, paired with a Frida pinning bypass.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install mitmproxy`

**URL:** https://mitmproxy.org

**Alternatives:** charles proxy, burp suite (see web domain)


##### Charles Proxy

Commercial GUI HTTPS proxy with click-through SSL proxying, breakpoints, and a request timeline — the macOS-centric alternative to a terminal proxy.

**When:** Point-and-click interception and rewriting during manual iOS testing on a workstation when you prefer a GUI over mitmproxy.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `Download from charlesproxy.com (trial, then paid license)`

**URL:** https://www.charlesproxy.com

**Alternatives:** mitmproxy


#### Automated Analysis & Scanning



##### MobSF (Mobile Security Framework) ⭐

All-in-one analyzer for APK and IPA: permissions, exported components, insecure crypto and network config, hardcoded secrets, all surfaced in a web UI with a REST API; its dynamic module also captures app HTTP traffic.

**When:** Always the first automated pass on a binary you are authorized to test — read the findings report, then drill into specific hits manually.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `docker run --rm -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest`

**URL:** https://github.com/MobSF/Mobile-Security-Framework-MobSF

**Alternatives:** quark-engine, apkid






## Emulators & Test Devices

Genymotion ⭐


#### Genymotion ⭐

Fast x86 Android emulator with snapshots, sensor simulation, and drag-and-drop APK install — a convenient third-party run target for testing.

**When:** When Android Studio's AVD is too heavy and you want quick snapshots and containerized test images for your own apps.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download the Genymotion bundle from genymotion.com (free personal-use desktop license)`

**URL:** https://www.genymotion.com

**Alternatives:** waydroid


#### Waydroid

Container-based Android that boots a full Android userspace directly on Linux without a VM, scriptable from the CLI.

**When:** Android testing on your Linux workstation with a container-native device instead of a heavyweight emulator.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install waydroid`

**URL:** https://github.com/waydroid/waydroid

**Alternatives:** genymotion


#### Device Bridge & Rooting



##### adb (Android Debug Bridge) ⭐

Google's core device bridge from Android platform-tools: install apps, push/pull files, shell in, install CA certificates, capture logcat, and port-forward.

**When:** Every device setup step — reach the emulator or handset, push frida-server and test certificates, and snapshot app data before and after a run.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `sudo apt install adb`

**URL:** https://developer.android.com/tools/adb

**Alternatives:** waydroid, genymotion


##### Magisk

Systemless root with module support for dedicated test devices; gives Frida, adb, and injected agents the root context most dynamic tests need.

**When:** Prepare a personal test device with an unlocked bootloader when an app refuses to run on stock or detects the emulator.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `Install the Magisk APK or fastboot boot a patched boot image on an unlocked-bootloader device`

**URL:** https://github.com/topjohnwu/Magisk

**Alternatives:** adb, frida (android)






## Android Platform-Specific




#### Custom ROMs & Controlled Builds



##### LineageOS ⭐

The most widely used custom ROM: build or flash a controlled test image on your own device, enable adb root, and strip vendor bloat for cleaner testing.

**When:** Standing up a long-lived controlled Android test device with root and current security patches before dynamic testing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Follow the device build instructions on wiki.lineageos.org and flash via adb/fastboot`

**URL:** https://github.com/LineageOS

**Alternatives:** waydroid, magisk


#### System & Framework App Dissection



##### smali/baksmali ⭐

Assembler and disassembler for DEX bytecode: decode framework and system app code, patch small runtime checks, and reassemble for re-signing tests.

**When:** Analyzing preinstalled or framework APKs on devices you own, or patching a specific smali check and rebuilding the APK.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Download smali-2.x.jar and baksmali-2.x.jar from GitHub releases`

**URL:** https://github.com/JesusFreke/smali

**Alternatives:** apktool, jadx






## iOS Static Analysis




#### Exported Binaries & Headers



##### class-dump ⭐

Dumps Objective-C class interfaces from a Mach-O binary, exposing the app's object graph and method signatures for review.

**When:** Mapping an app's Objective-C surface from a decrypted IPA you are authorized to test before deeper reversing.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Download class-dump from the project page and place it in /usr/local/bin`

**URL:** https://github.com/nygard/class-dump

**Alternatives:** frida-ios-dump, ipatool


#### IPA Acquisition & Decryption



##### frida-ios-dump ⭐

Dumps the decrypted IPA from a jailbroken device using Frida, turning App Store-encrypted slices into analyzable binaries.

**When:** Get a decryptable binary from your own jailbroken test device before starting static analysis.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/AloneMonkey/frida-ios-dump && cd frida-ios-dump && pip install -r requirements.txt && python3 dump.py <AppName>`

**URL:** https://github.com/AloneMonkey/frida-ios-dump

**Alternatives:** ipatool, frida (ios)


##### ipatool

Downloads IPAs directly from the App Store using your own Apple ID, enabling analysis of publicly available apps you lawfully retrieve.

**When:** Pulling an IPA for review where you hold a valid Apple ID and authorization for the app.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install github.com/majd/ipatool/v2@latest`

**URL:** https://github.com/majd/ipatool

**Alternatives:** frida-ios-dump






## iOS Dynamic Analysis




#### Instrumentation on Jailbroken Devices



##### Frida (iOS) ⭐

frida-server on a jailbroken device hooks and swizzles classes and traces methods for runtime inspection of your test apps.

**When:** Tracing iOS app runtime behavior, bypassing cert pinning, and dumping decrypted classes on a device you control.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `Install frida-server via Sileo/Cydia and keep the version matched to the host pip install of frida-tools`

**URL:** https://frida.re

**Alternatives:** objection, cycript


##### objection (iOS)

objection on iOS: disable SSL pinning, browse Keychain and UserDefaults, and explore classes from a single console without custom Frida JS.

**When:** Fast runtime checks on your own jailbroken test device when writing Frida scripts is overkill.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `pip install objection`

**URL:** https://github.com/sensepost/objection

**Alternatives:** frida (ios)


#### REPLs & Runtime Scripting



##### cycript ⭐

Runtime REPL mixing Objective-C and JavaScript to poke live processes and objects on jailbroken devices.

**When:** Interactive in-process class inspection and object manipulation during authorized iOS testing.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `Download the binary/dylib from cycript.org and launch with cycript -p <pid>`

**URL:** http://www.cycript.org/

**Alternatives:** frida (ios)


#### Tweak & Package Management



##### Sileo ⭐

Modern package manager for jailbroken devices and the clean way to install frida-server, debuggers, and testing tweaks on your test device.

**When:** Bootstrap a jailbroken lab device: install Frida, ldid, and testing utilities from one UI.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `Install Sileo from its GitHub release on a jailbroken device`

**URL:** https://github.com/Sileo/Sileo

**Alternatives:** frida (ios)






## CTF Classics & Practice Grounds

OWASP MASTG & UnCrackable Apps ⭐


#### OWASP MASTG & UnCrackable Apps ⭐

The Mobile Security Testing Guide plus the UnCrackable APPv1-v4 challenge apps with documented solutions — the reference mobile CTF syllabus.

**When:** Learning or validating a technique on trusted challenge apps before applying it to an authorized engagement.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/OWASP/MASTG && run the UnCrackable APKs under Frida/objection on your test device`

**URL:** https://github.com/OWASP/MASTG

**Alternatives:** diva, dvia


#### DVIA (Damn Vulnerable iOS App)

Deliberately vulnerable iOS app for practicing jailbreak-based runtime testing around keychain, transport security, and privacy.

**When:** Controlled iOS practice that mirrors real runtime vulnerabilities before touching your own production-grade apps.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `Build it from source in Xcode and deploy to a device you own`

**URL:** https://github.com/prateek147/DVIA

**Alternatives:** mastg, insecurebankv2


#### Frida CodeShare

Community hub of reusable Frida scripts (pinning bypasses, trace templates, dexdump variants) for accelerating script authoring.

**When:** Find a proven hooking pattern before writing your own custom script for an authorized app.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `Browse codeshare.frida.re and run a script with frida -l script.js`

**URL:** https://codeshare.frida.re

**Alternatives:** frida (android), objection





