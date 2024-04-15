import copy
import random
import funcs


def quick_sort_lomuto(array, s=0, f=-1):
    if f == -1:
        f = len(array)
    if f - s <= 1:
        return
    pivot = random.randint(s, f - 1)
    indexs = funcs.flag(array, array[pivot], s, f)
    quick_sort_lomuto(array, s, indexs[0])
    quick_sort_lomuto(array, indexs[1] + 1, f)


def quick_sort_hoar(array, s=0, f=-1):
    if f == -1:
        f = len(array) - 1
    if f <= s:
        return
    pivot_i = random.randint(s, f)
    pivot = array[pivot_i]

    i, j = s, f
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            break
        funcs.swap(array, i, j)
        i += 1
        j -= 1

    quick_sort_hoar(array, s, j)
    quick_sort_hoar(array, j + 1, f)


for i in range(10000):
    lst = [random.randint(1, 100) for _ in range(100)]
    s_lst = sorted(lst)
    quick_sort_hoar(lst) if i % 2 else quick_sort_lomuto(lst)
    if s_lst != lst:
        print('Error!')
        exit(1)
