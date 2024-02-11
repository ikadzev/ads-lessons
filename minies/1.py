# m = input('M: ')
# n = input('N: ')

# try:
#     _, _ = int(n), int(m)
# except ValueError:
#     print('NaN')
    
def division(n, m):
    outnum, curnum = '', ''
    noo = 0 # number of operations
    for i in n:
        if i == '-':
            continue
        print('cursor:', i)
        curnum += i
        noo += 1
        if int(m) > int(curnum):
            print('curnum too small\n')
            continue
        d = int(m)
        curint = int(curnum)
        cnt = 0
        print('current:', curint)
        while curint >= d:
            d += int(m)
            cnt += 1
            noo += 2
        d -= int(m)
        outnum += str(cnt)
        curnum = str(curint - d)
        noo += 3
        print('deducted:', d, '\ncurrent out:', outnum, '\ncurrent:', curnum)
        print()
    if not outnum:
        outnum = 0
    out = f'output is {int(outnum)}, number of operations is {noo}'
    return out

n, m = '999', '11'
print(division(n, m))

n, m = '123', '5'
print(division(n, m))

n, m = '0', '5'
print(division(n, m))