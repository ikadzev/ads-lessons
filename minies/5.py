def insertion_sort_k(lst, k):
    for i in range(k, len(lst)):
        j = i
        while j - k >= 0 and lst[j - k] < lst[j]:
            lst[j - k], lst[j] = lst[j], lst[j - k]  # swap
            j -= k
    return lst


def h_index(citations):
    if len(citations) == 1:
        if citations[0] >= 1:
            return 1
        else:
            return 0

    k = 1
    while (3**k-1)//2 < len(citations):
        k += 1
    while k > 0:
        citations = insertion_sort_k(citations, (3**k-1)//2)
        k -= 1

    print(citations)
    for i in range(len(citations)):
        for j in citations[:(i + 1)]:
            if j < i + 1:
                return i
    return len(citations)


print(h_index([3,0,6,1,5]))
