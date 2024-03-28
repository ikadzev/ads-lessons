def move(array, index, place):
    if index == place:
        return
    c = array[index]
    step = -1 if place < index else 1
    for i in range(index, place, step):
        array[i] = array[i + step]
    array[place] = c


def insertion_sort_k(lst, k):
    for i in range(k, len(lst)):
        j = i
        while j - k >= 0 and lst[j - k] > lst[j]:
            lst[j - k], lst[j] = lst[j], lst[j - k]  # swap
            j -= k


def wiggle_sort(lst):
    k = 1
    while (3 ** k - 1) // 2 < len(lst):
        k += 1
    while k > 0:
        insertion_sort_k(lst, (3 ** k - 1) // 2)
        k -= 1

    hlen = len(lst) // 2
    hlen += 1 if len(lst) % 2 else 0
    c = hlen - 1

    for i in range(hlen, len(lst)):
        move(lst, i, i - c)
        c -= 1
    return lst


print(wiggle_sort([1, 2, 3, 4, 5, 6, 7]))
