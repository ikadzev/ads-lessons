from random import randint
from funcs import flag


def swap(array, f, s):
    array[f], array[s] = array[s], array[f]


def quick_sort(array, pivot):
    length = len(array)
    i = 0
    colors = [0, length - 1]
    while i < length and i <= colors[1]:
        if array[i] < pivot:
            if i != colors[0]:
                swap(array, i, colors[0])
            colors[0] += 1
            swappable = colors[0] - 1
        elif array[i] == pivot:
            swappable = i
        else:
            if i != colors[1]:
                swap(array, i, colors[1])
            colors[1] -= 1
            swappable = colors[1] + 1
        if swappable == i:
            i += 1
    return array, colors


def kth(array, k):
    if len(array) == 1:
        return array[0]
    pivot = randint(0, len(array) - 1)
    p = flag(array, array[pivot])[1][0]
    if p == k:
        return array[p]
    elif p > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)


def oil(array):
    return kth(array, len(array) // 2)


oil_list = [2, 7, 8, 1, 3]
print(oil(oil_list) == sorted(oil_list)[len(oil_list) // 2])

oil_list = [66, 12, 24, 23, 67, 41, 26, 30, 57, 68]
print(oil(oil_list) == sorted(oil_list)[len(oil_list) // 2])

oil_list = [84, 86, 60, 96, 16, 42, 16, 25, 49, 21, 97, 6, 20, 95, 39, 15, 76, 61, 42, 76, 54, 78, 23, 63, 41, 83, 4, 8,
            16, 53, 25, 5, 41, 99, 81, 24, 5, 45, 26, 29, 26, 91, 87, 90, 84, 11, 56, 22, 43, 68, 39, 91, 39, 99, 59,
            75, 68, 61, 64, 15, 94, 47, 39, 99, 15, 42, 78, 43, 67, 48, 80, 97, 44, 69, 55, 97, 6, 11, 76, 52, 64, 25,
            90, 30, 69, 9, 44, 89, 59, 83, 31, 19, 31, 80, 39, 32, 64, 21, 74, 55]
print(oil(oil_list) == sorted(oil_list)[len(oil_list) // 2])
