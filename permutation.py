# O(n!)

def permutation(lst, k):
    res = []
    dfs(lst, [], res, k)
    return res

def dfs(lst, pre, res, k):
    if k == 0:
        tmp = []
        for inx in range(len(pre)):
            tmp.append(pre[inx])
        res.append(tmp)
    for i in range(len(lst)):
        if i not in pre:
            pre.append(i)
            dfs(lst, pre, res, k-1)
            pre.pop()
    return res

lst = ['a', 'b', 'c', 'd', 'e']
print(permutation(lst, 3))