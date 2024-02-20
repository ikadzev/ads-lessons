DEBUG_RETURN = 0
DEBUG_SORT = 0
DEBUG_MERGE = 0


def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]


def merge(f, s):
    b = []
    i, j = 0, 0
    while i < len(f) and j < len(s):
        if f[i] < s[j]:
            b.append(f[i])
            i += 1
        else:
            b.append(s[j])
            j += 1
    while i < len(f):
        b.append(f[i])
        i += 1
    while j < len(s):
        b.append(s[j])
        j += 1
    print('returning after merge, b =', b) if DEBUG_RETURN else None
    return b


def sort(lst):
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


numbers = '20 1 28 26 14 29 37 7 10 35 5 11 15 25 22 40'
str_list = numbers.split()
int_list = [int(i) for i in str_list]
print(sort(int_list))
