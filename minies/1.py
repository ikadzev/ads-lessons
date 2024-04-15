def get_bit_length(number: int) -> int:
    b_len = 0
    while number != 0:
        number = number >> 1
        b_len += 1
    return b_len


def division_bit(to_divide: int, division: int) -> str:
    if division == 0:
        return f'init is {to_divide} and 0, div is infinity...'
    out_num, cur_num = 0, 0
    sign = -1 if to_divide >= 0 > division or to_divide < 0 <= division else 1
    to_divide_abs = abs(to_divide)
    division_abs = abs(division)
    length = get_bit_length(to_divide_abs)
    for i in range(length):
        cur_num = cur_num << 1
        mask = 1 << (length - i - 1)
        cur_num += (mask & to_divide_abs) >> (length - i - 1)
        out_num *= 2
        if division_abs <= cur_num:
            out_num += 1
            cur_num = cur_num - division_abs
    out = f'init is {to_divide} and {division}, div is {out_num * sign}, rem is {to_divide - out_num * division * sign}'
    return out


n, m = 999, 11
print(division_bit(n, m))

n, m = 123, 5
print(division_bit(n, m))

n, m = 0, 5
print(division_bit(n, m))

n, m = 5, 0
print(division_bit(n, m))

n, m = 50, 25
print(division_bit(n, m))

n, m = -50, 25
print(division_bit(n, m))

n, m = 50, -25
print(division_bit(n, m))

n, m = -50, -25
print(division_bit(n, m))
