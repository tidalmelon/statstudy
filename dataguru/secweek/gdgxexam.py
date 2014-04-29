from __future__ import division
# --*-- coding:utf-8 --*--
import itertools

t = ['w', 'w', 'w', 'w', 'r', 'r']


# 不放回抽样
# 求两次都是红求的概率

# 由于对颜色没有顺序要求，故用组合计算
p_1 = list(itertools.combinations(t, 1))
p_2 = list(itertools.combinations(t, 1))

print p_1
print p_2

# 计算取两次球的所有可能取法，也就是样本空间啦
all_exam = []
for i in p_1:
    for j in p_2:
        all_exam.append((i[0], j[0]))

print all_exam
sum_all = len(all_exam)

print sum_all

# 取到的两个球都是白球的概率
p_ww = [i for i in all_exam if i[0] == i[1] == 'w']
print p_ww
print '取到的两个球都是白球的概率 %s/%s' % (len(p_ww), sum_all)

# 取到的两个球都是红球的概率
p_rr = [i for i in all_exam if i[0] == i[1] == 'r']
print p_rr
print '取到的两个球都是红球的概率 %s/%s' % (len(p_rr), sum_all)

# 取到的两个球颜色相同的概率
p_ss = [i for i in all_exam if i[0] == i[1]]
print p_ss
print '取到的两个球颜色相同的概率 %s/%s' % (len(p_ss), sum_all)

p_atleatr = [i for i in all_exam if i[0] == 'w' or i[1] == 'w']
print p_atleatr
print '取到的两只球至少有一只为白球 %s/%s' % (len(p_atleatr), sum_all)