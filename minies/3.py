x = int(input('Needed number: '))
init_n = int(input('Number of elements: '))
lst = []
print('Elements: ', end='')
for _ in range(init_n):
    lst.append(int(input()))
n = [0, init_n]
while True:
    cent = (n[0] + n[1]) // 2
    print(lst, cent, n)
    if lst[cent] != x:
        if abs(n[0]-n[1]) == 1:
            n = -1
            break
        if lst[cent] > x:
            n[1] = cent
        else:
            n[0] = cent
    else:
        n = cent
        break
print(n)