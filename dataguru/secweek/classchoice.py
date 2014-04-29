from __future__ import division
# --*-- coding:utf-8 --*--
import math


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


sum_space = combination(15, 5) * combination(10, 5) * combination(5, 5)
print '样本空间大小', sum_space

good = math.factorial(3)
print '每个班分到一个好学生的样本点数目', good

bad = combination(12, 4) * combination(8, 4) * combination(4, 4)
print '12个其他学生分到3个班的样本点数目', bad

print '15分到3个班,每个班1个优秀生的总数', good * bad

p1 = good * bad / sum_space
print '每个班都有一个好学生的概率', p1