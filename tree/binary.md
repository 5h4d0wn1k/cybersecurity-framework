# 🔬 Binary Exploitation & Reverse Engineering

Debug, disassemble, decompile, and understand binaries — your own code, lab targets, and CTF challenges.

## Debuggers & Dynamic Analysis

### GDB ⭐

The GNU Debugger — breakpoints, watchpoints, register/memory inspection, and scripting for any ELF or Mach-O binary you control.

**When:** The backbone of all dynamic work here; run it plain for a minimal setup or host pwndbg/GEF on top of it.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install gdb`

**URL:** https://www.gnu.org/software/gdb/

**Alternatives:** pwndbg, gef, lldb


### pwndbg

GDB plugin adding exploit-focused conveniences: heap/stack/register views, ROP-gadget search, cyclic pattern generation, and prettier disassembly.

**When:** Drop it into GDB for CTF pwn challenges or when reversing a binary you own, to spot useful gadgets and mitigations instantly.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh`

**URL:** https://github.com/pwndbg/pwndbg

**Alternatives:** gef


### GEF

Standalone, dependency-light GDB plugin (a single script) with heap visualizations, format-string helpers, and live memory introspection.

**When:** Want the pwndbg-style workflow with zero setup beyond one curl command, on any GDB build.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `wget -q -O- https://github.com/hugsy/gef/raw/main/scripts/gef.sh | sh`

**URL:** https://github.com/hugsy/gef

**Alternatives:** pwndbg


### LLDB

LLVM's debugger, well integrated with Mach-O binaries, clang-generated debug info, and Swift/Objective-C symbols.

**When:** Analyzing Apple-platform binaries or anything built with the LLVM toolchain where GDB support lags.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install lldb`

**URL:** https://lldb.llvm.org/

**Alternatives:** gdb


### Frida

Dynamic instrumentation toolkit that injects JavaScript into a running process (yours or a lab/CTF target) to hook functions and read live memory without recompiling.

**When:** Trace calls, intercept functions, or inspect a live process dynamically — especially on targets where GDB struggles.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install frida-tools`

**URL:** https://frida.re/

**Alternatives:** lldb, gdb


## Disassemblers & Decompilers

### Ghidra ⭐

NSA's free reverse-engineering suite with a GUI and a real decompiler that emits C-like pseudocode from machine code, plus a scriptable API.

**When:** Full static analysis of a binary you own or a CTF challenge — the decompiler output reads far closer to source than raw disassembly.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download the current release zip from the GitHub releases page, unzip, and run ./ghidraRun`

**URL:** https://github.com/NationalSecurityAgency/ghidra

**Alternatives:** radare2, cutter, rizin


### radare2

Command-line reverse-engineering framework with an analyzer, disassembler, and ESIL emulation, scriptable via r2pipe.

**When:** Headless or scripted analysis, quick on-box triage, and when everything should live in one terminal tool.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/radareorg/radare2 && cd radare2 && ./sys/install.sh`

**URL:** https://github.com/radareorg/radare2

**Alternatives:** rizin, cutter


### rizin

Community fork of radare2 aiming for a cleaner, better-tested codebase while staying command-compatible and offering rz-pipe scripting and Rust bindings.

**When:** Same CLI workflow as radare2 when you prefer the actively focused fork or need its language bindings.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install rizin`

**URL:** https://github.com/rizinorg/rizin

**Alternatives:** radare2, cutter


### Cutter

Qt GUI front-end for the Rizin reversing engine giving point-and-click disassembly, patching, and analysis in a visual workspace.

**When:** Visual exploration and annotation of binaries without a terminal-heavy workflow.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask cutter`

**URL:** https://github.com/rizinorg/cutter

**Alternatives:** radare2, rizin, ghidra


## Binary Exploitation Helper Libraries

### pwntools ⭐

CTF pwn toolkit providing packing (p64/u64), ELF parsing, cyclic patterns, ROP-chain builders, and managed local/remote I/O for exploit prototyping.

**When:** Prototype and test exploit behavior against binaries in a lab or CTF; the standard glue for the whole workflow.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install pwntools`

**URL:** https://github.com/Gallopsled/pwntools

**Alternatives:** angr, ropper, one_gadget


### angr

Python binary analysis framework using symbolic/concolic execution to explore paths and solve constraints against a binary you control.

**When:** Automated pathfinding — such as deriving inputs that satisfy checks — when manual reversing is too slow.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `pip install angr`

**URL:** https://github.com/angr/angr

**Alternatives:** pwntools, ropper


### Ropper

Python tool that inventories ROP gadgets and builds chains from ELF, PE, and Mach-O binaries; also powers the ROP search inside pwndbg.

**When:** Quick gadget inventory of a binary in a lab to audit what sequences are constructible.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install ropper`

**URL:** https://github.com/sashs/Ropper

**Alternatives:** one_gadget, pwntools


### one_gadget

Matches libc builds to single-address execve('/bin/sh') gadgets whose register constraints are simple to satisfy.

**When:** You have a libc build in a lab or CTF and want short candidate gadget addresses before scripting the constraints.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `gem install one_gadget`

**URL:** https://github.com/david942j/one_gadget

**Alternatives:** ropper, pwntools


## Binary Inspection Utilities

### checksec ⭐

Bash/Python script that reads ELF headers and reports the active mitigations: PIE, NX, canaries, RELRO, Fortify, and more.

**When:** First move on any binary in a lab or CTF — establish the mitigation baseline before choosing deeper tooling.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/slimm609/checksec.sh`

**URL:** https://github.com/slimm609/checksec.sh

**Alternatives:** objdump/readelf, file


### file

Identifies a file's type by reading magic bytes and headers, including the format and target architecture (e.g. ELF 64-bit x86-64).

**When:** Instant triage of any unknown artifact to confirm what you are looking at before deeper analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install file`

**URL:** https://www.darwinsys.com/file/

**Alternatives:** strings, objdump/readelf


### strings

Prints printable character sequences from a binary, exposing embedded literals, format strings, and library references without executing it.

**When:** Grab a quick inventory of interesting strings — prompts, /bin/sh, format specifiers — before disassembling.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install binutils`

**URL:** https://www.gnu.org/software/binutils/

**Alternatives:** file, objdump/readelf


### objdump/readelf

binutils disassembler and ELF reader: symbol tables, sections, headers, dynamic imports, and per-arch disassembly of your own binaries.

**When:** Zero-dependency static lookups — grep symbols, inspect section layout, or dump disassembly without a full RE suite.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install binutils`

**URL:** https://www.gnu.org/software/binutils/

**Alternatives:** file, strings


### xorsearch

Finds payloads XORed with single-byte or multi-byte keys by matching against known plaintext strings inside packed or obfuscated binaries.

**When:** Spot obfuscated strings or embedded shellcode in a lab binary — like strings, but for the XOR layer.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget -O xorsearch https://raw.githubusercontent.com/DidierStevens/DidierStevensSuite/master/xorsearch.py && chmod +x xorsearch`

**URL:** https://github.com/DidierStevens/DidierStevensSuite

**Alternatives:** strings

