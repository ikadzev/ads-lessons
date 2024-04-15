import time


def counting_sort(sorts, digit=None):
    if digit:
        sorts, digit = digit, sorts
    c = [0] * (max(sorts) + 1)
    for i in sorts:
        c[abs(i)] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    res = [0] * len(sorts)
    for i in range(len(sorts) - 1, -1, -1):
        res[c[abs(sorts[i])] - 1] = digit[i] if digit else sorts[i]
        c[abs(sorts[i])] -= 1
    return res


def lsd_sort(sorts):
    if not sorts:
        return sorts
    for i in range(len(str(sorts[0])) - 1, -1, -1):
        digit = [ord(str(j)[i]) for j in sorts]
        sorts = counting_sort(sorts, digit)
    return sorts


alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = ''
for i in range(1000):
    lst += ((alphabet[i:] + alphabet[:i]) * 500)[::-1]
    lst += ' '
lst = lst.split()
t = time.time()
lsd_sort(lst)
print(time.time() - t)
t = time.time()
sorted(lst)
print(time.time() - t)
