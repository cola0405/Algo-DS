def fastPow(a, b):
    res = 1
    while b:
        if b&1:
            res *= a
        a *= a
        b >>= 1
    return res

print(fastPow(2,3))