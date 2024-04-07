def swap(array: list[int], first: int, second: int) -> None:
    array[first], array[second] = array[second], array[first]


def flag(array: list[int]) -> None:
    length = len(array)
    i = 0
    colors = [0, 0, length - 1]
    while i < length and i <= colors[2]:
        if array[i] == 0:
            if i != colors[0]:
                swap(array, i, colors[0])
            colors[0] += 1
            colors[1] += 1
            swappable = colors[0] - 1
        elif array[i] == 1:
            colors[1] += 1
            swappable = i
        elif array[i] == 2:
            if i != colors[2]:
                swap(array, i, colors[2])
            colors[2] -= 1
            swappable = colors[2] + 1
        else:
            print('Wrong value in array!')
            exit(1)
        if swappable == i:
            i += 1


# arr = [2, 2, 2, 2]
arr = [2, 0, 1]
flag(arr)
print(arr)
