def counting_sort(sorts, digit=None):
    if digit:
        sorts, digit = digit, sorts
    c = [0] * (max(sorts) + 1)
    for i in sorts:
        c[abs(i)] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    res = [0] * len(sorts)
    for i in range(len(sorts) - 1, -1, -1):
        res[c[abs(sorts[i])] - 1] = digit[i] if digit else sorts[i]
        c[abs(sorts[i])] -= 1
    return res


def lsd_sort(sorts):
    for i in range(len(str(sorts[0])) - 1, -1, -1):
        digit = [ord(str(j)[i]) for j in sorts]
        sorts = counting_sort(sorts, digit)
    return sorts


lst = 'ab ee fd it lo'.split()
print(lsd_sort(lst))
