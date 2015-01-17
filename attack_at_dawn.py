#!/usr/bin/python
import sys

old_plaintext=0x61747461636b206174206461776e
new_plaintext=0x61747461636b206174206475736b
cipher_text=  0x09e1c5f70a65ac519458e7e53f36

print hex(old_plaintext ^ cipher_text ^ new_plaintext)
