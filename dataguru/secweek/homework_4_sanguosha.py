# --*-- coding:utf-8 --*--
from __future__ import division
import math

cards = ['主公', '忠臣', '反贼', '内奸']

coms = []
for a in cards:
    for b in cards:
        if a != b:
            coms.append((a, b))

for c in coms:
    print ' '.join(c)

print '根据定义'.center(50, '#')
print '组合数为（根据定义，手工组合）', len(coms)

print '数学公式'.center(50, '#')
######################################################################################################


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

print '组合数为（用数学公式算）', combination(4, 1) * combination(3, 1)
print '不会互相攻击的只有 主公：忠臣, 其概率为：', 2 / len(coms)

print combination(2, 1) * combination(1, 1)

#######################################################################################################

