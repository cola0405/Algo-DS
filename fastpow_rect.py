def mul(a, b):
    res = [[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            s = 0
            for k in range(len(a[0])):
                s += a[i][j]*b[j][i]
            res[i][j] = s
    return res


def fastPow(a, b):
    res = [item for item in a]
    while b:
        if b&1:
            res = mul(res, a)
        a = mul(a, a)
        b >>= 1
    return res

a = [[1,1], [1,1]]
print(fastPow(a,2))