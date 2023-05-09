def fastPow(a,b):
    if b == 0:
        return 1

    if b%2 == 0:
        res = fastPow(a, b//2)
        return res * res
    else:
        res = fastPow(a, (b-1)//2)
        return a * res * res

print(fastPow(2,3))