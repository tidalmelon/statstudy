# --*-- coding:utf-8 --*--
from __future__ import division
import math


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)


# 任选200人，说明是组合问题，因为不牵扯顺序
print '样本空间', (combination(400, 90) * combination(1100, 110)) / combination(1500, 200)

print combination(8, 2), combination(10, 2)


print permutation(8, 1) * permutation(2, 1) + permutation(2, 1) * permutation(1, 1), permutation(10, 2)

