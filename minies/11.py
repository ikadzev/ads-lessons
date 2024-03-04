def move(array, index, place):
    if index == place:
        return
    c = array[index]
    step = -1 if place < index else 1
    for i in range(index, place, step):
        array[i] = array[i + step]
    array[place] = c


def flag(array):
    colors = [0, 0, 0]
    n = 0
    while n != len(array):
        color = array[n]
        move(array, n, colors[color])
        colors[color] += 1
        if color <= 1:
            colors[2] += 1
            if color == 0:
                colors[1] += 1
        n += 1

arr = [2,0,2,1,1,0]
flag(arr)
print(arr)
