DEBUG_RETURN = 0
DEBUG_SORT = 0
DEBUG_MERGE = 0


def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]


def merge(lst, f, len_f, s, len_s, buff):
    # b = []
    # i, j = 0, 0
    # while i < len(f) and j < len(s):
    #     if f[i] < s[j]:
    #         b.append(f[i])
    #         i += 1
    #     else:
    #         b.append(s[j])
    #         j += 1
    # while i < len(f):
    #     b.append(f[i])
    #     i += 1
    # while j < len(s):
    #     b.append(s[j])
    #     j += 1
    # print('returning after merge, b =', b) if DEBUG_RETURN else None
    # return b
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


def old_sort(lst):
    n = len(lst)
    if n == 1:
        print('returning after n=1, lst =', lst) if DEBUG_RETURN else None
        return lst
    if n == 2:
        if lst[0] > lst[1]:
            swap(lst, 0, 1)
        print('returning after n=2, lst=', lst) if DEBUG_RETURN else None
        return lst

    cnt = n // 2
    print('sorting f, lst =', lst, 'cnt =', cnt) if DEBUG_SORT else None
    f = sort(lst[:cnt])
    print('sorting s, lst =', lst, 'cnt =', cnt) if DEBUG_SORT else None
    s = sort(lst[cnt:])
    print('merging, f =', f, 's =', s, 'cnt =', cnt) if DEBUG_MERGE else None
    lst = merge(f, s)
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
    # if n == 3:
    #     for i in range(3):
    #         for j in range(i):
    #             if lst[i] < lst[j]:
    #                 swap(lst, i, j)
    #     return lst

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


numbers = '24 11 32 15 6 14 17 9' # 36 16 18 33 5 10 29 25'
# numbers = '8 7 6 5 4 3 2 1'
str_list = numbers.split()
int_list = [int(i) for i in str_list]
print(sort(int_list))
