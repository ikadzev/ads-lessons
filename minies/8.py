import random


def swap(a, f, s):
    a[f], a[s] = a[s], a[f]


def merge_n_count(f, s):
    cnt = 0
    b = []
    i, j = 0, 0

    while i < len(f) and j < len(s):
        if f[i] < s[j]:
            b.append(f[i])
            i += 1
        else:
            cnt += len(f) - i
            b.append(s[j])
            j += 1
    while i < len(f):
        b.append(f[i])
        i += 1
    while j < len(s):
        b.append(s[j])
        j += 1

    return [cnt, b]


def sort_n_count(first):
    num = len(first)
    if num == 1:
        return [0, first]

    cnt = num // 2
    f = sort_n_count(first[:cnt])
    s = sort_n_count(first[cnt:])
    first = f[1] + s[1]
    count = merge_n_count(first[:cnt], first[cnt:])
    first = count[1]
    return [f[0] + s[0] + count[0], first]


def perm(first):
    loc = 0
    for i in range(len(first) - 1):
        if first[i] > first[i + 1]:
            loc += 1
    glob = sort_n_count(first)
    return glob[0] == loc


numbers = input('циферки через пробел (пусто - рандом): ')
if not numbers:
    n = random.randint(2, 64)
    lst = [random.randint(0, 100) for _ in range(n)]
    print('рандом выбрал ', n, ', рандомный лист - ', lst, sep='')
else:
    str_list = numbers.split()
    lst = [int(i) for i in str_list]
# print('инвертики-конвертики:', sort_n_count(lst))
print(perm(lst))
