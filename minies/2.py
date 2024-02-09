def algo(a, b):
    a, b = str(a), str(b)
    length = max(len(a), len(b))
    if length % 2:
        length += 1
    hlen = int(length * 0.5)
    if len(a) != length:
        a = '0' * (length - len(a)) + a
    if len(b) != length:
        b = '0' * (length - len(b)) + b
    print(a, b, length)
    aa = a[:hlen]
    bb = a[hlen:]
    cc = b[:hlen]
    dd = b[hlen:]
    return (10**length*int(aa)*int(cc) + 10**hlen*(int(aa)*int(dd) + int(bb)*int(cc)) + int(bb)*int(dd))

print(algo(12, 5))