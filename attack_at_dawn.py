#!/usr/bin/python
import sys

old_plaintext=0x61747461636b206174206461776e
new_plaintext=0x61747461636b206174206475736b
cipher_text=  0x6c73d5240a948c86981bc294814d

print hex(old_plaintext ^ cipher_text ^ new_plaintext)
