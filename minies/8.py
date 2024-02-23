import random

def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]


def merge_n_count(f, s):
    count = 0
    b = []
    i, j = 0, 0
    while i < len(f) and j < len(s):
        if f[i] < s[j]:
            b.append(f[i])
            i += 1
        else:
            count += len(f) - i
            b.append(s[j])
            j += 1
    while i < len(f):
        b.append(f[i])
        i += 1
    while j < len(s):
        count += len(f) - i
        b.append(s[j])
        j += 1
    return count, b


def sort_n_count(lst):
    n = len(lst)
    if n == 1:
        return 0

    cnt = n // 2
    f = sort_n_count(lst[:cnt])
    s = sort_n_count(lst[cnt:])
    count, lst = merge_n_count(lst[:cnt], lst[cnt:])
    return f + s + count


numbers = input('циферки через пробел (пусто - рандом): ')
if not numbers:
    n = random.randint(2, 64)
    lst = [random.randint(0, 100) for _ in range(n)]
    print('рандом выбрал ', n, ', рандомный лист - ', lst, sep='')
else:
    str_list = numbers.split()
    lst = [int(i) for i in str_list]
print('инвертики-конвертики:', sort_n_count(lst))
