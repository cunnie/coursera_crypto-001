# Week1: Introduction

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

Encryption algorithm is publicly known; don't use proprietary
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
  - basis for many security mechanisms
* Cryptography is not
  - a panacea for all security problems (software bugs, social
      engineering)
  - secure if implemented or used improperly (WEP is rife with bad
      decisions)
  - something you should invent yourself (it's easy to get wrong)
  (graveyard of bad crypto designs)



## What is Cryptography?

### Crytpo Core

Secure Communication:

1. Establish secret key
2. communicate securely (confidentiality and integrity)

### But Crypto Can Do Much More

* **digital signatures** (analog signatures suck) (2nd half of course) (hint: the digital signature is a function of the content)
* **anonymous communication** Imagine a user wants to talk about a sensitive topic anonymously (mix net) (it's bidirectional; bob can respond to alice)
* **anonymous digital cash**
  - spend a digital dollar at the bookstore without realizing who Alice is. It's anonymous like cash
  - but what's stopping Alice from making a billion digital copies? Anonymity and security seem to be at odds here. How do we resolve this? We'll talk about it later (hint: if Alice spends the coin once, but the 2nd time her identity is exposed)

### Protocols

* **Elections** The voters would like to compute the majority of the votes without revealing the identity of the voters. Each voter sends an encrypted vote to the election center, but nothing else is revealed about the individual votes.  The election center would like to confirm that the voter is eligible to vote and hasn't already voted. The result is known, but nothing else.
* **Private Auctions** Vicary Auction: highest bidder win; price is the 2nd highest bid. The only things that should become public:
  1. the identity of the highest bidder
  2. the value of the 2nd highest bid
* These problems are examples of **Secure multi-party computation** problems. Inputs are {votes,bids}. One way to do this would be to introduce a "trusted authority" (but this is problematic if it's not a trustworthy authority).

There is a theorem in crypto that anything that *can be done with a trusted authority can also be done without a trusted authority*.

First, we get rid of the authority. Instead, the parties are going to communicate with each other with a certain protocol, and at the end of the communication, the final output will be revealed. This is a surprising fact that we'll see at the end of the class.

### Crypto magic

Some things are "purely magical"

* **privately outsourcing computation** Imagine Alice has a search, she can send an encrypted query, and Google can run the encrypted query and return the encrypted results (and Google has no idea what Alice searched for). This is a fairly recent development (2-3 years ago). This is just theoretical, and it would probably a billion years if you actually tried it.
* **Zero knowledge** (proof of knowledge). N = p&times;q, where p, q are primes. Alice can prove to Bob that she knows that factors of N without revealing what those factors are. In fact, almost any puzzle you know the answer to, you can prove in "zero knowledge". If you've solved a sudoko puzzle, you can prove to Bob that you've solved it without revealing the solution.

### A Rigorous Science

Three steps in cryptography. We're going to go through these steps over and over again in this course. 

1. precisely specify threat model (what does it mean for a signature to be un-forgable)
2. propose a construction
3. prove that breaking construction under threat mode will solve an underlying hard problem (e.g. NP-complete)

## History of Cryptography

David Kahn wrote a great book, *The Code Breakers* (1996) about the history of cryptography from the Babylonian era to the present. I'm going to give a bunch of examples of bad encryption techniques.

* **Symmetric Ciphers**.  Alice and Bob know a secret "K". And they have an encryption algorithm "E" and a decryption algorithm "D"

* m: message (plaintext)
* c: cipher encrypted message (ciphertext)
* k: secret key, shared
* E: encryption algorithm: E(k,m) == c
* D: decryption algorithm: D(k,c) == m

The ciphertext is transmitted via (Internet, filesystem, or whatever). We say these are symmetric because both encryptor and the decryptor use the same key "k".

### A Few Historic Examples

1. Substition Cipher<br />
a &rarr; b<br />
b &rarr; c<br />
c &rarr; d<br />
&hellip;<br />
e.g. E(k,"hal") &rarr; "ibm"

### Caesar Cipher (no key)

Everything is shifted by 3 letters (e.g. a &rarr; d, b &rarr; e, etc&hellip;).

Technically this is not a cipher because there is no key; if an attacker knows the scheme (i.e. the algorithm), he can decrypt/tamper the message.

### How to Break the Substitution Cipher?

How big is the key space? Assuming 26 letters, the answer is 26! (factorial, not exclamation), which is approximately 2<span style="vertical-align: super; font-size: 70%">88</span>. Even though it has a large key space, it is terribly insecure. We're going to use letter frequencies to break it.

1. Use frequency of English letters (we can figure the first three letters)
    * "e" occurs 12.7%
    * "t" occurs 9.1%
    * "a" occurs 8.1%
2. Use frequency of pairs of letters (digrams)
    * "he", "an", "in", "th"
3. Use of frequency of three letters (trigrams)

This lends itself to a worst-possible type of attack: a ciphertext-only attack. There is no point in using the substitution cipher.

### Vigener Cipher

We've moved from the Roman era to the Renaissance, and look at one designed by Vigener (16th Century Rome):

k = C R Y P T O
p = W H A T A N I C E D A Y

---

k = C R Y P T O C R Y P T O C R Y P T
p = W H A T A N I C E D A Y T O D A Y

c = Z Z Z J U C|L U D T U N|W G C Q S

Assume we know the length of the key, then we take the set of first letters (Z, L, W) and use a frequency attack on it. Again with the second set (Z, U, G). e.g. if the most common letter is "H", then we can assume that's the letter "E", and the key's first letter is "C":

* "H" - "E" = "C"

We continue with the second set, third set, etc..., and then we've recovered the key, and then we can decrypt the entire message.

In real life, you might not know the length of the key, so you run the algorithm with a length of 1, then a length of 2, and then a length of 3, and then when you get output that's readable, you know you've broken it.

### Rotor Machines (1870 - 1943)
