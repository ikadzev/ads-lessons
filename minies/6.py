def insertion_sort_k(lst, k):
    for i in range(k, len(lst)):
        j = i
        while j - k >= 0 and lst[j - k] > lst[j]:
            lst[j - k], lst[j] = lst[j], lst[j - k]  # swap
            j -= k
    return lst


def wiggle_sort(lst):
    k = 1
    while (3 ** k - 1) // 2 < len(lst):
        k += 1
    while k > 0:
        lst = insertion_sort_k(lst, (3 ** k - 1) // 2)
        k -= 1

    hlen = len(lst) // 2
    hlen += 1 if len(lst) % 2 else 0
    f_half = lst[:hlen]
    s_half = lst[hlen:]

    new_lst = []
    for i in range(hlen - 1):
        new_lst.append(f_half[i])
        new_lst.append(s_half[i])
    new_lst.append(f_half[-1])
    if len(lst) % 2 == 0:
        new_lst.append(s_half[-1])
    return new_lst


print(wiggle_sort([1, 5, 1, 1, 6]))
