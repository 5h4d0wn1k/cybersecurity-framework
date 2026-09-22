# 🧮 Cryptography Toolkit & Cryptoanalysis

Decode/encode data, identify encodings, and break weak ciphers and RSA on materials you own: CTF crypto, historical ciphers, and flawed implementations. Password recovery lives in 'passwords'.

## Encoding & Decoding

CyberChef ⭐


#### CyberChef ⭐

GCHQ's browser 'Cyber Swiss Army Knife': 480+ chainable operations for decoding/encoding (Base64, hex, URL, Rot13), hashing, XOR and compression, plus the Magic operation that auto-detects and unwraps multi-layer encodings. Entirely client-side, zero install.

**When:** First stop for any blob, hex dump or encoded string: click the Magic icon to auto-decode, then drag operations to peel off the layers you identify.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `preinstalled (web — https://gchq.github.io/CyberChef/)`

**URL:** https://github.com/gchq/CyberChef

**Alternatives:** CyberChef (self-hosted)


#### CyberChef (self-hosted)

The same GCHQ app run from the official pre-built Docker image (or a downloadable static build) so every operation executes inside your own network with no outbound traffic.

**When:** Offline, air-gapped or VM work where the input must never leave your machine - identical recipes and Magic, no internet dependency after the image pull.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `docker run -it -p 8080:8080 ghcr.io/gchq/cyberchef:latest`

**URL:** https://gchq.github.io/CyberChef/

**Alternatives:** CyberChef






## Cipher Attack & Cryptanalysis

xortool ⭐


#### xortool ⭐

Python tool for multi-byte XOR cipher analysis: guesses key length via equality-based scoring, recovers key bytes from the most frequent plaintext character, with charset filtering and known-plaintext (-p) options to confirm candidates.

**When:** Ciphertext is XOR-encoded with an unknown repeating key - feed the raw bytes, let it rank key lengths, then solve for the right length and character.

**Effort:** easy  ·  **Rating:** 5/5

**Install:** `pip3 install xortool`

**URL:** https://github.com/hellman/xortool

**Alternatives:** hash_extender, CrypTool


#### hash_extender

Ron Bowes' C tool for the hash length-extension attack on MD4/MD5/RIPEMD-160/SHA-0/SHA-1/SHA-256/SHA-512/Whirlpool: given a secret-prefix hash, forges a valid hash for appended data without knowing the secret, iterating guessed secret lengths.

**When:** A service signs 'secret || message' with a Merkle-Damgård hash (CTF or your own app) and you can control appended data - produce the new payload+signature pair the server accepts.

**Effort:** medium  ·  **Rating:** 4/5

**Install:** `git clone https://github.com/iagox86/hash_extender && make`

**URL:** https://github.com/iagox86/hash_extender

**Alternatives:** xortool, CrypTool


#### CrypTool

Legacy university/open-source cryptology suite (CrypTool 2.1 + JCrypTool) for experimenting with classical ciphers (Caesar, Vigenère, Enigma, ADFGVX) and their built-in automated cryptanalysis on paste-in text.

**When:** Interactive analysis of historical substitution/transposition ciphers or learning the attack against a classical scheme on your own text, where a GUI beats hand-rolled scripts.

**Effort:** medium  ·  **Rating:** 3/5

**Install:** `download CrypTool 2.1 installer from https://www.cryptool.org/en/ct2/download`

**URL:** https://www.cryptool.org

**Alternatives:** xortool, hash_extender






## RSA Attacks & Factorization

RsaCtfTool ⭐


#### RsaCtfTool ⭐

Python RSA multi-attack harness (60+ attacks): weak-key factorization (Fermat, Pollard rho, ECM, SIQS), lattice attacks on small d (Wiener, Boneh-Durfee), Hastad broadcast, shared-factor pools, ROCA, past-CTF/gimmick primes and Factordb integration; recovers the private key and/or decrypts files.

**When:** Given a weak RSA public key and ciphertext (CTF, lab, keys you own) without knowing the weakness - run the default attack set, then target the specific winning attack.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `git clone https://github.com/RsaCtfTool/RsaCtfTool && cd RsaCtfTool && pip3 install -r requirements.txt`

**URL:** https://github.com/RsaCtfTool/RsaCtfTool

**Alternatives:** Factordb, rsatool


#### Factordb

Online database of integer factorizations with a plain API (https://factordb.com/api?query=N) that returns a number's status (FF/C/PRP) and known factors, including factorized prime records.

**When:** A modulus (or any big integer) may already be factored in the public corpus - script the API from curl; RsaCtfTool queries it automatically via --attack factordb.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `preinstalled (web/API)`

**URL:** https://factordb.com

**Alternatives:** RsaCtfTool, rsatool


#### rsatool

Small Python tool that reconstructs the full RSA key set (n, e, d, p, q, CRT params) and writes an OpenSSL-compatible PEM/DER private key from just (p, q) or (n, d), including n+dp-based factoring.

**When:** After any attack yields p and q (or n+d): turn recovered parameters into a real private key file you can decrypt with, instead of rolling the CRT math by hand.

**Effort:** easy  ·  **Rating:** 4/5

**Install:** `wget -O rsatool.py https://raw.githubusercontent.com/ius/rsatool/master/rsatool.py && pip3 install gmpy2 pyasn1`

**URL:** https://github.com/ius/rsatool

**Alternatives:** Factordb, RsaCtfTool






## Crypto Toolkit (Keys & Encrypt/Decrypt)

OpenSSL ⭐


#### OpenSSL ⭐

The de-facto CLI crypto Swiss-army knife: AES/ChaCha20/RSA/ECDSA encryption and decryption, key generation and parsing (PEM/DER), X.509 cert/genrsa/inspect, digests, and CMS/PKCS#7 envelopes in one command.

**When:** Quick symmetric or asymmetric encrypt/decrypt of your files, dumping or inspecting keys and certificates, and validating algorithm behavior against a standards reference implementation.

**Effort:** medium  ·  **Rating:** 5/5

**Install:** `sudo apt install openssl`

**URL:** https://www.openssl.org

**Alternatives:** GnuPG, GnuTLS certtool


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





