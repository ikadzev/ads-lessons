import random
from math import log


class Filter:
    class Hash:
        def __init__(self, m):
            self.m = m
            self.a = [random.randint(0, m - 1) for _ in range(4)]

        def __call__(self, ip):
            return (ip[0] * self.a[0] + ip[1] * self.a[1] + ip[2] * self.a[2] + ip[3] * self.a[3]) % self.m

    def __init__(self, num, error):
        self.hash_num = 1
        while (1 / (2 ** self.hash_num)) > error:
            self.hash_num += 1
        self.hashes = []
        self.elem_size = int(self.hash_num / log(2))
        self.size = self.elem_size * num
        self._init_hashes()
        self.count = 0
        self.bits = 0
        self.max = num

    def _init_hashes(self):
        for _ in range(self.hash_num):
            self.hashes.append(self.Hash(self.size))

    def insert(self, num):
        if self.count >= self.max:
            exit(1)
        self.count += 1
        for h in self.hashes:
            temp = 1 << h(num)
            self.bits |= temp

    def lookup(self, num):
        for h in self.hashes:
            if (self.bits >> h(num)) % 2 == 0:
                return 0
        return 1


if __name__ == '__main__':
    flter = Filter(10, 0.3)
    for i in range(5):
        flter.insert([i, i, i, i])
    print(flter.lookup([1, 1, 1, 1]))
    print(flter.lookup([2, 2, 2, 2]))
    print(flter.lookup([3, 3, 3, 3]))
    print(flter.lookup([4, 4, 4, 4]))
    print(flter.lookup([1, 0, 0, 0]))
