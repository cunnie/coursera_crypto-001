import sys
import unittest

# to run unittests: python -m unittest cry

class TestCipherFunctions(unittest.TestCase):

#    def setUp(self):
#        x = 0

    def test_isprintable(self):
        self.assertFalse(isprintable(31))
        self.assertTrue(isprintable(32))
        self.assertTrue(isprintable(127))
        self.assertFalse(isprintable(128))

    def test_random(self):
	self.assertEqual( len(random()), 16)
	self.assertEqual( len(random(12)), 12)

    def test_strxor(self):
	#self.assertEqual(strxor("61", "00"), "61")
	True

    def is_hex(self):
	self.assertTrue(is_hex(""))

#    def test_decrypt(self):
#        True #self.assert(decrypt('\0',"asdf"))

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    #print
    #print c.encode('hex')
    return c

def decrypt(key, cipher_hex):
    c = strxor(key, cipher_hex.decode('hex'))
    #print
    #print c
    return c

def main():
    get_key()



def isprintable(a):
    if (a > 31) and (a < 128):
        return True
    return False

def get_key():
    # cycle through all 16 bytes of the key
    for key in xrange(KEY_SIZE):
        # for this byte of the key, cycle through 0..255
            for key_byte in xrange(255):
                # go through each cipher
                for cipher in CIPHERS:
                    print "",
            # start your
            #for k_sub_n
            #if  cipher[0:2],
        #break

def decrypt(key,ciphertext):
    plaintext = ("0x" + strxor(a,b)).decode("hex")
    print plaintext.printable
    return plaintext

def test():
  suite = unittest.TestLoader().loadTestsFromTestCase(cry.TestCipherFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)

#main()
#    key = random(1024)
#    ciphertexts = [encrypt(key, msg) for msg in MSGS]

#print "asdf"
#print encrypt('aaaaa',"Brian")
