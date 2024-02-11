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
    
    aa = a[:hlen]
    bb = a[hlen:]
    cc = b[:hlen]
    dd = b[hlen:]
    f = int(aa)*int(cc) if len(aa) == 1 and len(cc) == 1 else algo(aa, cc)
    s = ((int(aa)+int(bb)) * (int(cc) + int(dd))) if len(str(int(aa)+int(bb))) == 1 and len(str(int(cc) + int(dd))) == 1 else algo(int(aa)+int(bb), int(cc) + int(dd))
    t = int(bb)*int(dd) if len(bb) == 1 and len(dd) == 1 else algo(bb, dd)
    
    return (10**length*int(aa)*int(cc) + 10**hlen*(int(aa)*int(dd) + int(bb)*int(cc)) + int(bb)*int(dd))

print(algo(12, 50))