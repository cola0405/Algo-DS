def combination(lst, k):
    res = []
    dfs(lst, [], res, k)
    return res

def dfs(lst, pre, res, k):
    if k == 0:
        # pre only store index
        res.append([lst[idx] for idx in pre])
        return

    start = (0 if len(pre) == 0 else pre[-1] + 1)
    for i in range(start, len(lst)):
        if i not in pre:
            pre.append(i)
            dfs(lst, pre, res, k-1)
            pre.pop()

lst = ['a', 'b', 'c', 'd', 'e']
print(combination(lst, 3))