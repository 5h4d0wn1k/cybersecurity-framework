# 🧮 Cryptography Toolkit & Cryptoanalysis

Decode/encode data, identify encodings, and break weak ciphers and RSA on materials you own: CTF crypto, historical ciphers, and flawed implementations. Password recovery lives in 'passwords'.

## Encoding & Format Identification




#### Decode & Encode



##### CyberChef ⭐

GCHQ's browser 'Cyber Swiss Army Knife': 480+ chainable operations for decoding/encoding (Base64, hex, URL, Rot13), hashing, XOR and compression, plus the Magic operation that auto-detects and unwraps multi-layer encodings. Entirely client-side, zero install.

**When:** First stop for any blob, hex dump or encoded string: click the Magic icon to auto-decode, then drag operations to peel off the layers you identify.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web — https://gchq.github.io/CyberChef/)`

**URL:** https://github.com/gchq/CyberChef

**Alternatives:** CyberChef (self-hosted), dCode


##### CyberChef (self-hosted)

The same GCHQ app run from the official pre-built Docker image (or a downloadable static build) so every operation executes inside your own network with no outbound traffic.

**When:** Offline, air-gapped or VM work where the input must never leave your machine - identical recipes and Magic, no internet dependency after the image pull.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `docker run -it -p 8080:8080 ghcr.io/gchq/cyberchef:latest`

**URL:** https://gchq.github.io/CyberChef/

**Alternatives:** CyberChef


#### Hash & File Format Identification



##### hashID ⭐

Python 3 tool identifying 220+ hash types by regex and reporting the matching hashcat mode (-m) and John format (-j) for each candidate, replacing the outdated hash-identifier.

**When:** Any recovered hash before cracking: feed it the value, note the top algorithm plus its hashcat/John mode, then jump to the passwords domain.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip install hashid && hashid '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1' -mj`

**URL:** https://github.com/psypanda/hashID

**Alternatives:** file (libmagic), dCode, RsaCtfTool


##### file (libmagic)

The standard `file` command built on libmagic: identifies thousands of file types from magic bytes, from PEM/DER keys and PKCS#12 bundles to plaintext/uncompressed containers.

**When:** Determine what a raw blob actually is before decoding — distinguish a DER key, a zlib stream, a base64 text, or a random-looking ciphertext file.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `sudo apt install file && file suspect.bin`

**URL:** https://darwinsys.com/file/

**Alternatives:** hashID, CyberChef






## Cipher Attack & Cryptanalysis




#### Classical & Historical Ciphers



##### dCode ⭐

Web reference hosting hundreds of small solvers for classical schemes (Caesar, Vigenère, Enigma, ADFGVX, Playfair...) plus a Cipher Identifier that scores which of 300+ ciphers a message fits via n-gram and index-of-coincidence analysis.

**When:** CTF or challenge text in a historical cipher: paste it into the Cipher Identifier for a ranked guess, then open the matching solver for the plaintext.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web)`

**URL:** https://www.dcode.fr

**Alternatives:** CrypTool, CyberChef, xortool


##### CrypTool

Legacy university/open-source cryptology suite (CrypTool 2.1 + JCrypTool) for experimenting with classical ciphers (Caesar, Vigenère, Enigma, ADFGVX) and their built-in automated cryptanalysis on paste-in text.

**When:** Interactive analysis of historical substitution/transposition ciphers or learning the attack against a classical scheme on your own text, where a GUI beats hand-rolled scripts.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `download CrypTool 2.1 installer from https://www.cryptool.org/en/ct2/download`

**URL:** https://www.cryptool.org

**Alternatives:** dCode, xortool


#### XOR & Stream Ciphers



##### xortool ⭐

Python tool for multi-byte XOR cipher analysis: guesses key length via equality-based scoring, recovers key bytes from the most frequent plaintext character, with charset filtering and known-plaintext (-p) options to confirm candidates.

**When:** Ciphertext is XOR-encoded with an unknown repeating key - feed the raw bytes, let it rank key lengths, then solve for the right length and character.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install xortool`

**URL:** https://github.com/hellman/xortool

**Alternatives:** cribdrag, CyberChef, dCode


##### cribdrag

Interactive crib-dragging script for stream-cipher keystream reuse: XOR two ciphertexts (or against a guessed crib) and step through candidate plaintext substrings interactively.

**When:** Two ciphertexts share a one-time pad key, or a stream cipher reuses its keystream — drag a known plaintext word to recover the keystream and decrypt the rest by hand.

**Effort:** easy  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/SpiderLabs/cribdrag && python2 cribdrag.py encrypted.hex`

**URL:** https://github.com/SpiderLabs/cribdrag

**Alternatives:** xortool, CyberChef


#### Block Cipher Padding Attacks



##### PadBuster ⭐

Perl script automating padding-oracle attacks: decrypts arbitrary CBC ciphertext, encrypts arbitrary plaintext, and probes an endpoint to fingerprint the oracle that leaks padding validity.

**When:** A web app returns distinguishable error codes on bad PKCS#7 padding and the app is yours to test — recover and forge CBC messages without the key.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/GDSSecurity/PadBuster && cd PadBuster && perl padBuster.pl https://app.example/decrypt -encoding 0`

**URL:** https://github.com/GDSSecurity/PadBuster

**Alternatives:** CyberChef, xortool






## Hash Cracking Context & Attacks




#### Hash Length Extension



##### hash_extender ⭐

Ron Bowes' C tool for the hash length-extension attack on MD4/MD5/RIPEMD-160/SHA-0/SHA-1/SHA-256/SHA-512/Whirlpool: given a secret-prefix hash, forges a valid hash for appended data without knowing the secret, iterating guessed secret lengths.

**When:** A service signs 'secret || message' with a Merkle-Damgård hash (CTF or your own app) and you can control appended data - produce the new payload+signature pair the server accepts.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/iagox86/hash_extender && make`

**URL:** https://github.com/iagox86/hash_extender

**Alternatives:** Hashcat, RsaCtfTool


#### Crackers (cross-ref to passwords)



##### Hashcat ⭐

GPU/CPU password cracker with 300+ attack modes and thousands of hash types; the full profile and masking/rule tooling live in the passwords domain. Linked here so crypto-work can confirm hash formats and modes.

**When:** A recovered hash or extracted TGS ticket needs cracking; pair the hashcat mode from hashID with a rule/mask attack after confirming the target algorithm.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install hashcat && hashcat -m 1000 ntlm.hash rockyou.txt`

**URL:** https://hashcat.net/hashcat/

**Alternatives:** John the Ripper, hashID


##### John the Ripper

CPU-first cracker (jumbo build) covering hundreds of hash formats including magic formats like Kerberoast/AS-REP tickets and encrypted OpenSSL/archive containers; full profile lives in the passwords domain.

**When:** Cracking on CPU with the jumbo format set, or when a target format (gpg, ssh, rakefile) is only handled by John rather than Hashcat.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install john && john --wordlist=rockyou.txt hashes.txt`

**URL:** https://www.openwall.com/john/

**Alternatives:** Hashcat






## RSA Attacks & Factorization




#### Multi-Attack Solvers



##### RsaCtfTool ⭐

Python RSA multi-attack harness (60+ attacks): weak-key factorization (Fermat, Pollard rho, ECM, SIQS), lattice attacks on small d (Wiener, Boneh-Durfee), Hastad broadcast, shared-factor pools, ROCA, past-CTF/gimmick primes and Factordb integration; recovers the private key and/or decrypts files.

**When:** Given a weak RSA public key and ciphertext (CTF, lab, keys you own) without knowing the weakness - run the default attack set, then target the specific winning attack.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/RsaCtfTool/RsaCtfTool && cd RsaCtfTool && pip3 install -r requirements.txt`

**URL:** https://github.com/RsaCtfTool/RsaCtfTool

**Alternatives:** factorDB, rsatool, SageMath


##### Manual Math Toolkit



###### SageMath ⭐

Open-source mathematics system with built-in number theory used for RSA cryptanalysis: lattice basis reduction (LLL), Pollard p-1/p-ρ, discrete log, small-roots (Coppersmith), and private-key reconstruction from recovered parameters.

**When:** When no one-shot tool covers the attack — hand-build a lattice basis, solve a modular equation, or derive d from partial parameters with a few lines of Sage.

**Effort:** advanced  ·  **Rating:** 4/5

**Install:** `sudo apt install sagemath`

**URL:** https://www.sagemath.org

**Alternatives:** RsaCtfTool, rsatool, yafu


#### Integer Factorization Engines



##### FactorDB ⭐

Online database of integer factorizations with a plain API (https://factordb.com/api?query=N) that returns a number's status (FF/C/PRP) and known factors, including factorized prime records.

**When:** A modulus (or any big integer) may already be factored in the public corpus - script the API from curl; RsaCtfTool queries it automatically via --attack factordb.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://factordb.com

**Alternatives:** RsaCtfTool, yafu, msieve


##### yafu

Automated integer-factoring command-line utility chaining trial division, Pollard, ECM, SIQS, and GNFS on numbers up to ~200 digits, with prebuilt Windows binaries and clean `factor(n)` syntax.

**When:** A 256–1024-bit modulus you own that defeats online lookup — run `yafu 'factor(n)'` and let it auto-select the fastest factoring stage.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/bbuhrow/yafu && cd yafu && make yafu`

**URL:** https://github.com/bbuhrow/yafu

**Alternatives:** FactorDB, msieve, SageMath


##### msieve

Quadratic-sieve and number-field-sieve library/demo for factoring integers up to ~120 digits (QS) and larger via GNFS, the classic engine behind CTF modulus-factorization writeups.

**When:** Factoring tasks where yafu stalls or where you want the standalone QS/NFS engine; typically invoked from a script that feeds candidates one at a time.

**Effort:** advanced  ·  **Rating:** 3/5

**Install:** `git clone https://github.com/radii/msieve && cd msieve && make`

**URL:** https://github.com/radii/msieve

**Alternatives:** yafu, FactorDB, RsaCtfTool


#### Key Reconstruction



##### rsatool ⭐

Small Python tool that reconstructs the full RSA key set (n, e, d, p, q, CRT params) and writes an OpenSSL-compatible PEM/DER private key from just (p, q) or (n, d), including n+dp-based factoring.

**When:** After any attack yields p and q (or n+d): turn recovered parameters into a real private key file you can decrypt with, instead of rolling the CRT math by hand.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget -O rsatool.py https://raw.githubusercontent.com/ius/rsatool/master/rsatool.py && pip3 install gmpy2 pyasn1`

**URL:** https://github.com/ius/rsatool

**Alternatives:** Factordb, RsaCtfTool, SageMath






## SSL/TLS Configuration Analysis




#### TLS / Cipher Auditors



##### testssl.sh ⭐

Bash TLS cipher/protocol testing on any port: enumerates protocols and cipher suites, flags weaknesses (BEAST, heartbleed, ROBOT, TLS1.0/1.1, weak DHE), checks client simulation, and emits JSON/CSV/HTML.

**When:** Full TLS configuration audit of an endpoint you own; the default single-line invocation yields findings graded vulnerable/weak/OK you can drop straight into a report.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `git clone --depth 1 https://github.com/testssl/testssl.sh && ./testssl.sh example.com`

**URL:** https://github.com/testssl/testssl.sh

**Alternatives:** SSLyze, sslscan, OpenSSL


##### sslscan

Fast TLS cipher scanner built on a rewritten backend that detects SSLv2/SSLv3 and TLSv1.3 regardless of linked OpenSSL, flags CBC (POODLE), 3DES, RC4, NULL/weak ciphers, and weak DHE keys, with XML output.

**When:** A quick closed-port cipher enumeration or legacy-protocol check where you want one line per cipher and color-coded strength annotations.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `sudo apt install sslscan && sslscan example.com:443`

**URL:** https://github.com/rbsec/sslscan

**Alternatives:** testssl.sh, SSLyze


##### SSLyze

Python TLS scanning library/CLI: cert, cipher suite, and elliptic-curve analysis plus known-attack checks (Heartbleed, ROBOT, CCS injection), with Mozilla-config comparison and JSON output for automation.

**When:** Automated TLS gate in CI/CD or bulk scanning of many hosts; exit code flips on Mozilla 'intermediate' non-compliance, so it doubles as a regression check.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `pip3 install sslyze && python3 -m sslyze example.com`

**URL:** https://github.com/nabla-c0d3/sslyze

**Alternatives:** testssl.sh, sslscan






## Key & Certificate Toolkit

OpenSSL ⭐


#### OpenSSL ⭐

The de-facto CLI crypto Swiss-army knife: AES/ChaCha20/RSA/ECDSA encryption and decryption, key generation and parsing (PEM/DER), X.509 cert/genrsa/inspect, digests, and CMS/PKCS#7 envelopes in one command.

**When:** Quick symmetric or asymmetric encrypt/decrypt of your files, dumping or inspecting keys and certificates, and validating algorithm behavior against a standards reference implementation.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install openssl`

**URL:** https://www.openssl.org

**Alternatives:** GnuPG, GnuTLS certtool, age


#### GnuPG

GNU Privacy Guard: full OpenPGP implementation for asymmetric and symmetric encryption, signing/verification, keyring management, and export/import interop with PGP e-mail workflows.

**When:** Working with .gpg/PGP messages or OpenPGP keys where the PGP container format - not raw OpenSSL cipher - is expected.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `sudo apt install gnupg`

**URL:** https://www.gnupg.org

**Alternatives:** age, OpenSSL


#### age

Simple, modern, audited file encryption (X25519, optional passphrase; hybrid post-quantum ML-KEM-768 since v1.3) with small explicit keys, no configuration and UNIX-style composability; interoperable Rust port is 'rage'.

**When:** Modern default for encrypting archives/files you own end-to-end (backups, secrets transfer) when you want minimal friction and small keys over legacy OpenPGP keyrings.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `go install filippo.io/age/cmd/age@latest`

**URL:** https://github.com/FiloSottile/age

**Alternatives:** GnuPG, OpenSSL


#### GnuTLS certtool

CLI from the GnuTLS project for X.509 certificate/key generation, PKCS#12 bundles, certificate and private-key inspection, and PKCS#11 token operations through a single binary.

**When:** Generating or inspecting certificates and PKCS#12 files with readable options, or poking at PKCS#11 tokens, when OpenSSL's flag surface gets in the way.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `sudo apt install gnutls-bin`

**URL:** https://www.gnutls.org

**Alternatives:** OpenSSL, GnuPG





