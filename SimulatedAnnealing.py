# 利用模拟退火求函数最大值
# 需要在一个非常大的搜索空间中寻找最优解时
# 模拟退火算法是一种有效的方法

import math
import random

def func(x):
    return math.sin(x)

x = 0
T = 100
alpha = 0.99
stopping_T = 1e-8
stopping_iter = 10000

best_x = 0
max_val = func(0)
val = max_val
delta = 0
i = 0
while T > stopping_T and i < stopping_iter:
    x += random.uniform(-1, 1)
    new_val = func(x)
    delta = new_val - val

    # get better val or probability fit
    if delta > 0 or math.exp(delta/T) > random.random():
        val = new_val
        if new_val > max_val:
            max_val = new_val
            best_x = x
    i += 1
    T *= alpha

print(best_x, max_val)






