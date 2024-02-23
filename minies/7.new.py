DEBUG_RETURN = 0
DEBUG_SORT = 0
DEBUG_MERGE = 0


def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]


def merge(lst, f, len_f, s, len_s, buff):
    assert len(lst) - buff >= len_f + len_s
    while len_f and len_s:
        if lst[f] < lst[s]:
            swap(lst, f, buff)
            f += 1
            len_f -= 1
        else:
            swap(lst, s, buff)
            s += 1
            len_s -= 1
        buff += 1
    while len_f:
        swap(lst, f, buff)
        f += 1
        len_f -= 1
        buff += 1
    while len_s:
        swap(lst, s, buff)
        s += 1
        len_s -= 1
        buff += 1
    print('return after merge, lst =', lst, 'f, s =', f, s, 'len =', len_f, len_s, 'b =', buff) if DEBUG_MERGE else None
    return lst


def sort(lst, s=0, e=None):
    e = e if e else len(lst)
    n = e - s
    assert n != 0
    if n == 1:
        return lst
    if n == 2:
        swap(lst, s, e - 1) if lst[s] > lst[e - 1] else None
        return lst

    cent = n // 2
    lst = sort(lst, 0, cent // 2)
    lst = sort(lst, cent // 2, cent)
    lst = merge(lst, 0, cent // 2, cent // 2, cent // 2, cent)

    ln = [cent // 2, cent]
    while ln[1] - ln[0] != 1:
        lst = sort(lst, ln[0] + ln[0] // 2, ln[1])
        lst = merge(lst, ln[0], ln[0] // 2, ln[0] + ln[0] // 2, ln[0] // 2, 0)
        lst = merge(lst, s, ln[0], ln[1], n - ln[1], ln[0])
        ln = [ln[0] // 2, ln[1] // 2]
    lst = sort(lst, ln[0] + ln[0] // 2, ln[1])
    lst = merge(lst, ln[0], ln[0] // 2, ln[0] + ln[0] // 2, ln[0] // 2, 0)
    lst = merge(lst, s, ln[0], ln[1], n - ln[1], ln[0])
    i = 0
    while lst[i] > lst[i + 1]:
        swap(lst, i, i+1)
        i += 1
    return lst


numbers = '24 11 32 15 6 14 17 9'  # 36 16 18 33 5 10 29 25'
str_list = numbers.split()
int_list = [int(i) for i in str_list]
print(sort(int_list))
