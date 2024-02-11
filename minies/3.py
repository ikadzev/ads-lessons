x = int(input('Needed number: '))
init_n = int(input('Number of elements: '))
lst = []
print('Elements: ', end='')
for _ in range(init_n):
    lst.append(int(input()))
n = [0, init_n]
for _ in range(10):
    cent = (n[0] + n[1]) // 2
    print(lst, cent)
    if lst[cent] != x:
        if lst[cent] > x:
            n[1] = cent
        else:
            n[0] = cent
    else:
        n = cent+1
        break
print(n)