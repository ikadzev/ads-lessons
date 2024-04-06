def get_bit_length(number: int) -> int:
    b_len = 0
    while number != 0:
        number = n >> 1
        b_len += 1
    return b_len


def division_bit(to_divide: int, division: int) -> str:
    if division == 0:
        return f'init is {to_divide} and {division}, div is infinity...'
    out_num, cur_num = 0, 0
    length = get_bit_length(to_divide)
    to_divide = abs(to_divide)
    for i in range(length):
        cur_num = cur_num << 1
        mask = 1 << (length - i - 1)
        cur_num += (mask & to_divide) >> (length - i - 1)
        if division > cur_num:
            out_num *= 2
            continue
        d = division
        cnt = 0
        while cur_num >= d:
            cnt += 1
            d += division
        d -= division
        out_num *= 2
        out_num += cnt
        cur_num = cur_num - d
    out = f'init is {to_divide} and {division}, div is {out_num}, rem is {to_divide - out_num * division}'
    return out


n, m = 999, 11
print(division_bit(n, m))

n, m = 123, 5
print(division_bit(n, m))

n, m = 0, 5
print(division_bit(n, m))

n, m = 5, 0
print(division_bit(n, m))
