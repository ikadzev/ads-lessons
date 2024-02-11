x = int(input('Needed number: '))
lst = input('List (space-splitted): ').split()
init_n = len(lst)
for i in range(init_n): 
    try:
        lst[i] = int(lst[i])
    except ValueError:
        print('NaN')
        exit(0)
n = [0, init_n]
while True:
    cent = (n[0] + n[1]) // 2
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
# WIP!!!!