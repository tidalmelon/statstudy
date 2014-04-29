# --*-- coding:utf-8 --*--
from __future__ import division
import math


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


# 任选三人，说明是组合问题，因为不牵扯顺序
print '样本空间', combination(10, 3)
# 由于是组合问题,不牵扯顺序，先把5拿出来，然后从[6 7 8 9 10]中选择2个填充另两个位置
print '事件空间(最小号码为5)', combination(5, 2)
print '概率为', combination(5, 2), combination(10, 3)

# 由于是组合问题,不牵扯顺序，先把5拿出来，然后从[1 2 3 4]中选择2个填充另两个位置
print '事件空间(最大号码为5)', combination(4, 2)
print '概率为', combination(4, 2) / combination(10, 3)
