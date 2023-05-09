# 题目链接:https://www.luogu.com.cn/problem/P1147

"""
对一个给定的自然数M，求出所有的连续的自然数段(每一段至少有两个数)，
这些连续的自然数段中的全部数之和为M
1998 +1999 +2000 +2001 + 2002 = 10000

输入：
10000

输出：
18 142
297 328
388 412
1998 2002

"""

m = int(input())

l = 1
res = l
for r in range(2, m//2+2):
    res += r
    while res > m:
        res -= l
        l += 1
    if res == m:
        print(l, r)