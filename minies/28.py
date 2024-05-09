import random
from math import log


class Filter:
    class Hash:
        def __init__(self, m):
            self.m = m
            self.a = [random.randint(0, m - 1) for _ in range(4)]

        def __int__(self, ip):
            return (ip[0] * self.a[0] + ip[1] * self.a[1] + ip[2] * self.a[2] + ip[3] * self.a[3]) % self.m

    def __init__(self, num, error):
        self.hash_num = 1
        while 1 / (2 ^ self.hash_num) > error:
            self.hash_num += 1
        self.hashes = []
        self.size = self.hash_num / log(2)
        self._init_hashes()
        self.count = 0
        self.bits = [0 for _ in range(num * self.size)]
        self.max = num

    def _init_hashes(self):
        for _ in range(self.hash_num):
            self.hashes.append(self.Hash(self.size))

    def insert(self, num):
        if self.count >= self.max:
            exit(1)
        self.count += 1
        for hashsh in self.hashes:
            self.bits[hashsh(num)] = 1

    def lookup(self, num):
        for hashsh in self.hashes:
            if self.bits[hashsh(num)] == 0:
                return 0
        return 1
