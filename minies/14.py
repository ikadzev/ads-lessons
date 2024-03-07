from random import randint


def move(array, index, place):
    if index == place:
        return
    c = array[index]
    step = -1 if place < index else 1
    for i in range(index, place, step):
        array[i] = array[i + step]
    array[place] = c


def swap(array, f, s):
    array[f], array[s] = array[s], array[f]


def fast_sort(array, pivot):
    indexs = [0, 1, 1]
    swap(array, pivot, 0)
    pivot = array[0]
    n = 1
    while n != len(array):
        if array[n] < pivot:
            index = 0
        elif array[n] == pivot:
            index = 1
        else:
            index = 2
        move(array, n, indexs[index])
        indexs[index] += 1
        if index <= 1:
            indexs[2] += 1
            if index == 0:
                indexs[1] += 1
        n += 1
    return indexs[0]


def kth(array, k):
    if len(array) == 1:
        return array[0]
    pivot = randint(0, len(array) - 1)
    p = fast_sort(array, pivot)

    if p == k:
        return array[p]
    elif p > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)


def oil(array):
    array = [i[1] for i in array]
    return kth(array, len(array) // 2)


oil_list = [[1, 2], [4, 7], [3, 8], [2, 1], [5, 3]]
print(oil(oil_list))
