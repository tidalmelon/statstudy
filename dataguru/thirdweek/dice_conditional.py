from __future__ import division
# --*-- coding:utf-8 --*--

t = range(1, 7)

space = []
for a in t:
    for b in t:
        for c in t:
            if a == b == c:
                space.append((a, b, c, 0))
            else:
                space.append((a, b, c, a + b + c))


print '投三个骰子的样本空间大小为', len(space)

print '知道其中一个骰子为3点，的条件概率,就是从样本空间中删掉没有3的，作为新的样本空间，我们假设第一个骰子为3,，，，，，， 假设哪一个骰子为3 是固定的'
# space = [e for e in space if e[0] == 3 or e[1] == 3 or e[2] == 3] 这种做法是错误的，因为看到一个骰子是3,说明这个骰子已经固定了，而不能用或
space = [e for e in space if e[0] == 6]


small = [i for i in space if 4 <= i[3] <= 10]
big = [i for i in space if 11 <= i[3] <= 17]
same = [i for i in space if i[3] == 0]

num_space = len(space)

num_small = len(small)
num_big = len(big)
num_same = len(same)

print num_space, num_small, num_big, num_same


p_small = num_small / num_space
p_big = num_big / num_space
p_same = num_same / num_space

print '小的概率', p_small
print '大的概率', p_big
print '三个点数一样', p_same

# 小的概率 0.486111111111  0.56043956044
# 大的概率 0.486111111111  0.428571428571
# 三个点数一样 0.0277777777778 0.010989010989



