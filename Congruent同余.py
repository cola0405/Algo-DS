"""
区间和 + 同余

题目链接：https://www.luogu.com.cn/problem/P8649

sj - s(i-1) 即为区间[i,j]的和
区间和 % k==0
即 (sj - s(i-1)) %k == 0
变形得：sj % k = si-1 %k

要统计 区间和 % k == 0的情况
其实只要统计 sj == s(i-1) 的情况即可 (i < j)

以下用s_count来做积累次数

"""

n,k = map(int, input().split())

s = [0]
ans = 0
s_count = [0]*k
for i in range(1,n+1):
    num = int(input())
    s.append((s[i-1] + num) % k)
    ans += s_count[s[i]]
    s_count[s[i]] += 1

print(ans + s_count[0])