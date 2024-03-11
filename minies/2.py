def algo(a, b):
    length = max(len(str(a)), len(str(b)))
    length += length % 2
    hlen = length // 2
    
    aa = a // 10**hlen
    bb = a % 10**hlen
    cc = b // 10**hlen
    dd = b % 10**hlen
    f = aa*cc if aa // 10 == 0 and cc // 10 == 0 else algo(aa, cc)
    s = ((aa + bb) * (cc + dd)) if (aa + bb) // 10 == 0 and (cc + dd) // 10 == 0 else algo(aa + bb, cc + dd)
    t = bb*dd if bb // 10 == 0 and dd // 10 == 0 else algo(bb, dd)

    return (10**length * f + 10**hlen * (s - t - f) + t)

print(algo(348, 574))