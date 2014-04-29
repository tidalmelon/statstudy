from __future__ import division
# --*-- coding:utf-8 --*--
import itertools
import copy
t = ['w', 'w', 'w', 'w', 'r', 'r']

# 计算样本空间
all_exam = []
for i in range(len(t)):
    f = t[i]
    arr = copy.copy(t)
    del arr[i]
    for s in arr:
        all_exam.append((f, s))


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