# Introduction to Cryptography

## Course Overview

### Objectives

1. learn crypto primitives
2. learn how to use them

### Cryptography is Ubiquitous

* Secure communication
  * https
  * 802.11i WPA2, GSM, Bluetooth
* Disk (EFS, TrueCrypt, FileVault 2)
* Content (CSS (?) (DVD), AACS (?) (Blue-Ray))
* User authentication (/etc/shadow)

HTTPS is really HTTP over SSL/TLS

Secure Communication means

1. No eavesdropping
2. No tampering

### Secure Sockets Layer/TLS

Consists of two main parts:

1. Handshake protocol: **establishes shared secret key using public-key
cryptography**  (we'll cover this in the 2nd half of the course)
2. Record Layer: **transmit data using shared secret key** (ensures
confidentiality and integrity) (first half of course)

Securing files on disk is fundamentally the same as encrypting
communication. In the case of files, the communication is encrypted
to the same person but at a later time.

### Symmetrical Encryption

* m: message (plaintext)
* c: cipher encrypted message (ciphertext)
* k: secret key, shared
* E: encryption algorithm: E(k,m) == c
* D: decryption algorithm: D(k,c) == m

Encryption algorith is publicly known; don't use proprietary
algorithms because they haven't been peer-reviewed and may have
serious flaws.

### Use Cases

* Single use key (one time key)
  - encrypts only one message, e.g. email (new key generated for
      each email)

* Multi use key (many time key)
  - encrypts multiple message, e.g. filesystem encryption, same key
  for multiple files.
  - more overhead (?) required

### Things to Remember

* Cryptography
  - good tool
  - basis for many security mechanismes

* Cryptography is not
  - a panacea for all security problems (software bugs, social
      engineering)
  - secure if implemented or used improperly (WEP is rife with bad
      decisions)
  - something you should invent yourself (it's easy to get wrong)
  (graveyard of bad crypto designs)

