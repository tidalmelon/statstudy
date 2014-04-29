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

# for i in space:
#     print i

print '投三个骰子的样本空间大小为', len(space)


small = [i for i in space if 4 <= i[3] <= 10]
big = [i for i in space if 11 <= i[3] <= 17]
same = [i for i in space if i[3] == 0]

num_space = len(space)
num_small = len(small)
num_big = len(big)
num_same = len(same)

p_small = num_small / num_space
p_big = num_big / num_space
p_same = num_same / num_space

print '小的概率', p_small
print '大的概率', p_big
print '三个点数一样', p_same





