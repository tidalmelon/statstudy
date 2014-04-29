# --*-- coding:utf-8 --*--

# P(ABC) = P(C|AB)P(B|A)P(A) 乘法公式，其实就是不断破解条件概率的公式


# 由定义的方式来计算

first = [0, 1]
second = [0] * 7 + [1] * 3
third = [0] * 9 + [1]

print first
print second
print third

print '样本空间大小', 2 * 10 * 10

print '未摔破的样本点为', 1 * 3 * 1

print '未摔破的概率为 3/200'