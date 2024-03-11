def division(n, m):
    outnum, curnum = 0, 0
    n = abs(n)
    for i in range(len(str(n)) - 1, -1, -1):
        curnum *= 10
        curnum += (n // 10**i % 10)
        print(curnum)
        if m > curnum:
            outnum *= 10
            print('too small')
            continue
        d = m
        cnt = 0
        while curnum >= d:
            d += m
            cnt += 1
        d -= m
        outnum *= 10
        outnum += cnt
        curnum = curnum - d
    out = f'output is {outnum}'
    return out

n, m = 999, 11
print(division(n, m))

n, m = 123, 5
print(division(n, m))

n, m = 0, 5
print(division(n, m))