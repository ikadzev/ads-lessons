from funcs import swap, merge


def sort(lst, s=0, e=-1):
    e = e if e != -1 else len(lst)

    n = e - s
    assert n > 0
    if n < 8:
        for i in range(e - 2, s - 1, -1):
            t = i
            while t < e - 1 and lst[t] > lst[t + 1]:
                swap(lst, t, t + 1)
                t += 1
        return

    end_first = s + n // 4
    end_second = s + n // 2
    buff = e - n // 2

    sort(lst, s, end_first)
    sort(lst, end_first, end_second)
    merge(lst, s, end_first, end_first, end_second, buff)

    while buff - s > 2:
        n = end_first - s
        sort(lst, s, end_first)
        merge(lst, s, end_first, buff, e, buff - n)
        buff = buff - n
        end_first = (s + (end_first - s) // 2) or 1

    merge(lst, s, s + 1, buff, e, buff - 1)

    while s < e - 1 and lst[s] > lst[s + 1]:
        swap(lst, s, s + 1)
        s += 1

    return


numbers = '15 74 14 27 33 40 5 44 57 45 4 97 49 3 31 54 79 13 86 4 30 48 66 36 27 71 89 15 74 14'
lst = [int(i) for i in numbers.split()]
print(len(lst))
sort(lst)
print(lst)
