from funcs import swap, merge

DEBUG_MERGE = 0
DEBUG_SORT = 0
DEBUG_RETURN = 0


def sort(lst, s=0, e=-1):
    e = e if e != -1 else len(lst)
    print('sorting', lst[s:e], 'in', lst) if DEBUG_SORT else None

    n = e - s
    assert n != 0
    if n == 1:
        return lst
    if n < 4:
        for i in range(e - 2, s - 1, -1):  # insertion sort
            t = i
            while t < e - 1 and lst[t] > lst[t + 1]:
                swap(lst, t, t + 1)
                t += 1
        print('sorted', lst[s:e], 'in', lst) if DEBUG_RETURN else None
        return lst

    start = s
    s += n % 4
    cent = (s + e) // 2
    quat = (s + cent) // 2

    lst = sort(lst, s, quat)
    lst = sort(lst, quat, cent)
    merge(lst, s, quat, quat, cent, cent)

    ln = [quat, cent]
    while ln[0] - s > 1:
        lst = sort(lst, s, ln[0])
        merge(lst, s, ln[0], ln[1], e, ln[0])
        ln[1] = ln[0] + (ln[0] - s) % 2
        ln[0] = (s + ln[1]) // 2

    for i in range(ln[1] - 1, start - 1, -1):
        t = i
        while t < e - 1 and lst[t] > lst[t + 1]:
            swap(lst, t, t + 1)
            t += 1
    return lst


numbers = '15 74 14 27 33 40 5 44 57 45 4 97 49 3 31 54 79 13 86 4 30 48 66 36 27 71 89'
str_list = numbers.split()
int_list = [int(i) for i in str_list]
print(sort(int_list))
