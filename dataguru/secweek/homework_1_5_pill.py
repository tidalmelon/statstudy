# --*-- coding:utf-8 --*--
from __future__ import division
import itertools
import math


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# 0 normal 1 安慰剂
space = [(i, 0) for i in range(1, 6)] + [(i, 1) for i in range(6, 11)]

# 任取5片 （跟顺序无关，你取的  0 1 2 3 4 和 取  4 3 2 1 0 是同一个样本， 故此为组合问题）
c = itertools.combinations(space, 5)
c = list(c)

# 统计‘至少有2片是安慰剂的概率’
count = 0
for i in c:
    # print i
    res = reduce(lambda x, y: (0, x[1] + y[1]), i)
    if res[1] >= 2:
        count += 1
print '计算机模拟'.center(100, '#')
print '其中至少2片是安慰剂的样本点 数量为', count
print '总的样本数', len(c)
print '概率是', float(count) / len(c)

print '数学计算'.center(100, '#')
print '取到安稳剂为0次和1次的 数量', combination(5, 0) * combination(5, 5) + combination(5, 1) * combination(5, 4)
sum_math = combination(10, 5) - (combination(5, 0) * combination(5, 5) + combination(5, 1) * combination(5, 4))
print '至少两片是安慰剂的 数量', sum_math
print '总的样本数', combination(10, 5)
print '概率是', float(sum_math) / combination(10, 5)

print '从中每次取1片，做不放回抽样，求前3次都取到安慰剂的概率,【前三次】 说明这是一个排列问题'

print '计算机模拟'.center(100, '#')
c = list(itertools.permutations(space, 10))
print '样本空间', len(c)

# 统计前三次都取到安慰剂的次数
count_third = 0
for d in c:
    if 1 == d[0][1] == d[1][1] == d[2][1]:
        count_third += 1
print '事件，前3次为安慰剂的次数为', count_third

print '概率为', float(count_third) / len(c)

print '数学计算'.center(100, '#')


# def combination(n, r):
#     return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)

print '样本空间', permutation(10, 10)
print '事件，前3次为安慰剂的次数为', permutation(5, 3) * permutation(7, 7)
print '概率为', (permutation(5, 3) * permutation(7, 7)) / permutation(10, 10)