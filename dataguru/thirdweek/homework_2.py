# --*-- coding:utf-8 --*--
from __future__ import division
import math


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


# 根据定义：
# 所有的组合 （黑，黑）（黑，黑） （白，白） （白，白） （白，黑）(黑，白）
# 增加信息：上面为黑  则样本空间为： （黑，黑） （黑，黑） （黑，白）
# 由定义知，背面也为黑的概率为：P= 2/3

#
cards = [('b', 'b'), ('w', 'w'), ('b', 'w')]

print combination(100, 13), combination(100, 37)

a = combination(100, 13) * combination(100, 37)

b = combination(100, 1) * combination(100, 1)

print a / b



