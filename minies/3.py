x = int(input('Needed number: '))
n = int(input('Number of elements: '))
lst = []
print('Elements: ', end='')
for _ in range(n):
    lst.append(int(input()))
while True:
    cent = n // 2
    print(lst, cent)
    if lst[cent] != x:
        if lst[cent] > x:
            lst = lst[:cent]
        else:
            lst = lst[cent:]
        n = len(lst)
    else:
        lst = cent+1
        break
print(lst)