import random
import sys

class SuperCipher:
    def __init__(self):
        self.key_len = 4
        self.keyspace = "0123456789"

    def gen_key(self):
        return ''.join(random.choices(self.keyspace, k=self.key_len))

    def encrypt(self, pt, key):
        ct = ""
        for i, c in enumerate(pt):
            key_c = key[i % len(key)]
            ct += chr(ord(c) ^ ord(key_c))
        return ct

    def make_challenge(self, pt):
        key = self.gen_key()
        ct = self.encrypt(pt, key)
        with open("./out/output.txt", "wb") as f:
            f.write(ct.encode())
        return key


maker = SuperCipher()
maker.make_challenge(sys.argv[1])
