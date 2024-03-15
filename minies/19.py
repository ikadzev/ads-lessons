class Pyro:
    def __init__(self, array=None):
        self.main = []
        self.main_len = 0
        if array is not None:
            for i in array:
                self.append(i)

    def append(self, new):
        self.main.append(new)
        self.main_len += 1
        if len(self.main) != 1:
            n = self.main_len - 1
            while n != 0 and self.main[n] < self.main[(n - (2 - n % 2)) // 2]:
                swp = (n - (2 - n % 2)) // 2
                swap(self.main, n, swp)
                n = swp

    def pop_min(self):
        if self.main_len == 0:
            return None
        swap(self.main, 0, -1)
        ret = self.main.pop()
        self.main_len -= 1
        n = 0
        if self.main_len <= 1:
            return ret
        while n * 2 + 1 < self.main_len:
            if n * 2 + 2 < self.main_len:
                if self.main[n] > self.main[n * 2 + 1] and self.main[n] > self.main[n * 2 + 2]:
                    if self.main[n * 2 + 1] > self.main[n * 2 + 2]:
                        swap(self.main, n, n * 2 + 2)
                        n = n * 2 + 2
                        continue
                    else:
                        swap(self.main, n, n * 2 + 1)
                        n = n * 2 + 1
                        continue
                else:
                    if self.main[n] > self.main[n * 2 + 1]:
                        swap(self.main, n, n * 2 + 1)
                        n = n * 2 + 1
                        continue
                    elif self.main[n] > self.main[n * 2 + 2]:
                        swap(self.main, n, n * 2 + 2)
                        n = n * 2 + 2
                        continue
                    else:
                        break
            elif self.main[n] > self.main[n * 2 + 1]:
                swap(self.main, n, n * 2 + 1)
                break
            else:
                break
        return ret


def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]


p = Pyro([-8, -6, -2, -6, -4])
p.pop_min()
print(p.main)
