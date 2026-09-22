# 🔬 Binary Exploitation & Reverse Engineering

Debug, disassemble, decompile, and understand binaries — your own code, lab targets, and CTF challenges.

## Static Analysis




#### Decompilers



##### Ghidra ⭐

Free software reverse-engineering suite with a GUI and a real decompiler that emits C-like pseudocode, plus a scriptable Python/Java API.

**When:** Full static analysis of binaries you own or CTF challenges — the decompiler output reads far closer to source than raw disassembly.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `Download the release zip from the Ghidra releases page, unzip, and run ./ghidraRun`

**URL:** https://github.com/NationalSecurityAgency/ghidra

**Alternatives:** IDA Free, Binary Ninja, radare2


##### IDA Free

Hex-Rays' freeware edition of IDA, a mature interactive disassembler with decompiler support for x86/x64/ARM and a plugin ecosystem.

**When:** A free, officially supported disassembler when you prefer IDA's workflow for x86/x64 binaries over the Ghidra GUI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (download the installer from hex-rays.com)`

**URL:** https://hex-rays.com/ida-free/

**Alternatives:** Ghidra, radare2


##### Binary Ninja

Commercial reverse-engineering platform with a modern Python API, cross-platform analysis, and both an interactive GUI and headless mode.

**When:** Scriptable binary analysis with an expressive API, or when team licensing matches your lab workflow.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `preinstalled (desktop download from binary.ninja)`

**URL:** https://binary.ninja/

**Alternatives:** Ghidra, Cutter


#### Disassembler frameworks



##### CLI engines



###### radare2 ⭐

Command-line reverse-engineering framework with built-in analyzer, disassembler, ESIL emulation, and scripting via r2pipe.

**When:** Headless or scripted analysis, quick on-box triage, and when the whole analysis pipeline should live in one terminal tool.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/radareorg/radare2 && cd radare2 && ./sys/install.sh`

**URL:** https://github.com/radareorg/radare2

**Alternatives:** rizin, Cutter


###### rizin

Actively maintained fork of radare2 aiming for a cleaner, better-tested codebase while staying command-compatible and offering rz-pipe bindings.

**When:** Same CLI workflow as radare2 when you prefer the fork under active development for its language bindings and released packages.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `brew install rizin`

**URL:** https://github.com/rizinorg/rizin

**Alternatives:** radare2, Cutter


##### Graphical front-ends



###### Cutter ⭐

Qt GUI built on the Rizin engine giving point-and-click disassembly, patching, control-flow graphs, and a decompiler view.

**When:** Visual exploration and annotation of binaries without a terminal-heavy workflow.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `brew install --cask cutter`

**URL:** https://github.com/rizinorg/cutter

**Alternatives:** radare2, rizin, Ghidra


#### Scripting & automation ecosystems



##### GhidraSnippets ⭐

Curated Python and Java snippets for the Ghidra scripting API covering common auto-analysis, function, and disassembly tasks.

**When:** Steal working, tested Ghidra script patterns instead of re-deriving the API for each new analysis task.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/HackOvert/GhidraSnippets`

**URL:** https://github.com/HackOvert/GhidraSnippets

**Alternatives:** ghidra-scripts, r2ghidra


##### ghidra-scripts

Maintained collection of Ghidra Python scripts for pattern-based analysis, function identification, and decompiler querying.

**When:** Drop-in automation scripts for reversing binaries or firmware in an iterative lab analysis session.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/0xdea/ghidra-scripts`

**URL:** https://github.com/0xdea/ghidra-scripts

**Alternatives:** GhidraSnippets


##### r2ghidra

Plugin that embeds the Ghidra decompiler into radare2/rizin so terminal workflows gain C-like pseudocode output.

**When:** Bring a decompiler view into your radare2/rizin session without switching to the Ghidra GUI.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `r2pm -ci r2ghidra`

**URL:** https://github.com/radareorg/r2ghidra

**Alternatives:** Ghidra, radare2






## Dynamic Analysis




#### Debuggers



##### GDB ⭐

GNU debugger supporting breakpoints, watchpoints, register and memory inspection, and scripting for ELF, PE, and Mach-O binaries.

**When:** The backbone of all dynamic work; run it plain for minimalism or host pwndbg/GEF on top of it.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install gdb`

**URL:** https://www.gnu.org/software/gdb/

**Alternatives:** pwndbg, GEF, LLDB


##### pwndbg

GDB plugin with exploit-focused conveniences: heap/stack views, ROP-gadget search, cyclic pattern generation, and prettier disassembly.

**When:** CTF pwn challenges or reversing binaries you own when plain GDB layout gets too noisy.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh`

**URL:** https://github.com/pwndbg/pwndbg

**Alternatives:** GEF, GDB


##### GEF

Dependency-light, single-script GDB plugin with heap visualizations, format-string helpers, and live memory introspection.

**When:** A pwndbg-style workflow with almost zero setup beyond one curl command, on any GDB build.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `wget -q -O- https://github.com/hugsy/gef/raw/main/scripts/gef.sh | sh`

**URL:** https://github.com/hugsy/gef

**Alternatives:** pwndbg, GDB


##### LLDB

LLVM's debugger, well integrated with clang-generated debug info and Mach-O, Swift, and Objective-C symbols.

**When:** Analyzing Apple-platform binaries or anything built with the LLVM toolchain where GDB support lags.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install lldb`

**URL:** https://lldb.llvm.org/

**Alternatives:** GDB


#### Instrumentation & tracing



##### Frida ⭐

Dynamic instrumentation toolkit that injects JavaScript into a running process to hook functions and read live memory without recompiling.

**When:** Trace calls, intercept functions, or inspect a live process — especially on targets where a traditional debugger struggles.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install frida-tools`

**URL:** https://frida.re/

**Alternatives:** GDB, strace / ltrace


##### strace / ltrace

Syscall and library-call tracers that log every system call (or libc call) a process makes, with arguments and timing.

**When:** Map a binary's runtime behavior by watching the syscalls it issues during a controlled run on your host.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install strace ltrace`

**URL:** https://github.com/strace/strace

**Alternatives:** GDB, Frida


#### Emulation & sandboxing



##### QEMU ⭐

Full-system and user-mode emulator running and tracing binaries for foreign architectures, with a GDB remote stub.

**When:** Execute and debug cross-architecture ELF (ARM, MIPS, PPC) from firmware or CTFs when no native hardware exists.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install qemu-user`

**URL:** https://www.qemu.org

**Alternatives:** Qiling, Unicorn


##### Qiling

Advanced binary emulation framework that runs and instruments cross-architecture binaries inside a controlled Python sandbox.

**When:** Automated, scripted emulation of cross-platform binaries with hooks, memory inspection, and reproducible lab runs.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `pip install qiling`

**URL:** https://github.com/qilingframework/qiling

**Alternatives:** QEMU, Unicorn


##### Unicorn

Lightweight CPU emulator framework exposing per-instruction hooks so you can emulate only the instruction flow you care about.

**When:** Embed instruction-level emulation into your own analysis or fuzzing scripts for lab targets.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install unicorn`

**URL:** https://github.com/unicorn-engine/unicorn

**Alternatives:** QEMU, Qiling






## Exploit-Dev Toolchains




#### Python exploit frameworks



##### pwntools ⭐

CTF pwn toolkit providing packing (p64/u64), ELF parsing, cyclic patterns, ROP-chain builders, and managed local/remote I/O.

**When:** Prototype and test exploit behavior against binaries in a lab or CTF — the standard glue for the whole workflow.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `pip install pwntools`

**URL:** https://github.com/Gallopsled/pwntools

**Alternatives:** angr, ROPgadget, one_gadget


##### angr

Python binary analysis framework using symbolic/concolic execution to explore paths and solve constraints against a binary you control.

**When:** Automated pathfinding — such as deriving inputs that satisfy checks — when manual reversing is too slow.

**Effort:** advanced  ·  **Rating:** 5/5

**Install:** `pip install angr`

**URL:** https://github.com/angr/angr

**Alternatives:** pwntools, Z3


#### ROP & gadget tooling



##### ROPgadget ⭐

Scans binaries for return-oriented-programming gadgets and can dump the full gadget set or filter specific instructions.

**When:** Collect usable ROP gadgets from a stripped binary you own before assembling a chain.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install ropgadget`

**URL:** https://github.com/JonathanSalwan/ROPgadget

**Alternatives:** Ropper, one_gadget, pwntools


##### Ropper

Python tool to inventory ROP gadgets and build chains from ELF, PE, and Mach-O binaries; powers gadget search inside pwndbg.

**When:** Quick gadget inventory across multiple binary formats in a lab when auditing which sequences are constructible.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install ropper`

**URL:** https://github.com/sashs/Ropper

**Alternatives:** ROPgadget, one_gadget


##### one_gadget

Matches libc builds to single-address execve('/bin/sh') gadgets whose register constraints are simple to satisfy.

**When:** You have a libc build in a lab or CTF and want short candidate gadget addresses before scripting the constraints.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `gem install one_gadget`

**URL:** https://github.com/david942j/one_gadget

**Alternatives:** ROPgadget, Ropper


#### Constraint solving



##### Z3 ⭐

Microsoft's SMT solver used to solve constraints over bitvectors, powering automated deobfuscation and input recovery.

**When:** Solve the arithmetic and bitvector equations that symbolic execution or manual analysis hands you.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install z3-solver`

**URL:** https://github.com/Z3Prover/z3

**Alternatives:** angr


#### Speculative-execution research kits



##### Speculator ⭐

IBM Research framework to analyze speculative-execution attacks (ret2spec/spectre class) and their mitigations across architectures.

**When:** Academic-lab study of ret2spec-family microarchitectural attacks and how current mitigations cover them.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/ibm-research/speculator`

**URL:** https://github.com/ibm-research/speculator

**Alternatives:** Retbleed PoC


##### Retbleed PoC

Research proof-of-concept from the ret2spec lineage demonstrating arbitrary speculative code execution via return instructions.

**When:** Reproduce published speculative-execution research artifacts in a lab to measure the impact of mitigations.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/comsec-group/retbleed`

**URL:** https://github.com/comsec-group/retbleed

**Alternatives:** Speculator






## Binary Navigation




#### Instruction engines



##### Capstone ⭐

Disassembly engine that decodes raw bytes into platform-pinned instructions for many architectures, usable from Python, C, and more.

**When:** Programmatically decode instruction streams inside your own scripts, emulators, or plugin code.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install capstone`

**URL:** https://github.com/capstone-engine/capstone

**Alternatives:** Keystone, radare2


##### Keystone

Assembly engine that turns mnemonics into machine code at runtime, complementing Capstone for code generation.

**When:** Assemble shellcode or encoding routines on the fly inside your own lab scripts and tooling.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `pip install keystone-engine`

**URL:** https://github.com/keystone-engine/keystone

**Alternatives:** Capstone, pwntools


#### Header & string inspection



##### checksec ⭐

Bash/Python script that reads ELF headers and reports active mitigations: PIE, NX, canaries, RELRO, Fortify, and more.

**When:** First move on any binary in a lab or CTF — establish the mitigation baseline before choosing deeper tooling.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/slimm609/checksec.sh`

**URL:** https://github.com/slimm609/checksec.sh

**Alternatives:** file, objdump / readelf, strings


##### file

Identifies a file's type from magic bytes, including format and target architecture (e.g. ELF 64-bit x86-64).

**When:** Instant triage of any unknown artifact to confirm what you are looking at before deeper analysis.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install file`

**URL:** https://www.darwinsys.com/file/

**Alternatives:** strings, objdump / readelf


##### strings

Prints printable character sequences from a binary, exposing embedded literals, format strings, and library references without executing it.

**When:** Grab a quick inventory of interesting strings — prompts, /bin/sh, format specifiers — before disassembling.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install binutils`

**URL:** https://www.gnu.org/software/binutils/

**Alternatives:** file, objdump / readelf


##### objdump / readelf

binutils disassembler and ELF reader providing symbol tables, sections, headers, dynamic imports, and per-arch disassembly.

**When:** Zero-dependency static lookups — grep symbols, inspect section layout, or dump disassembly without a full RE suite.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install binutils`

**URL:** https://www.gnu.org/software/binutils/

**Alternatives:** file, strings


#### Binary diffing



##### Diaphora ⭐

Binary diffing tool matching functions across two binaries and importing names and symbols, working with Ghidra, IDA, and Binary Ninja.

**When:** Compare patched vs unpatched firmware or file versions to spot the instruction-level changes behind a fix.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/joxeankoret/diaphora`

**URL:** https://github.com/joxeankoret/diaphora

**Alternatives:** Ghidra, Binary Ninja





