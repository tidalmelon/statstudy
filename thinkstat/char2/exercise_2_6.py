__author__ = 'root'
# --*-- coding:utf-8 --*--
import matplotlib.pyplot as plt
import thinkstat.char1.survey as survey
import itertools
from matplotlib.ticker import MultipleLocator

table = survey.Pregnancies()
table.ReadRecords(data_dir='../data_nsfg')
print 'Num of pregnancies', len(table.records)
#分成两组，一胎 和 其他
firsts = survey.Pregnancies()
others = survey.Pregnancies()
all = survey.Pregnancies()
for rec in table.records:
    if rec.outcome != 1:
        continue
    #去掉未出生的
    all.AddRecord(rec)
    if rec.birthord == 1:
        firsts.AddRecord(rec)
    else:
        others.AddRecord(rec)
print '一胎数量', len(firsts)
print '其他数量', len(others)
#验证方式http://www.icpsr.umich.edu/nsfg6 搜索 birthord


#平均怀孕周期，第一胎 和 其他，差异多大？
g_first = itertools.groupby(sorted([rec.prglength for rec in firsts.records]))
g_other = itertools.groupby(sorted([rec.prglength for rec in others.records]))
g_all = itertools.groupby(sorted([rec.prglength for rec in all.records]))


def returnxy(g):
    t = []
    for i in g:
        c = 0
        for j in i[1]:
            c +=1
        t.append((i[0], c))
    t.sort(key=lambda x: x[0])
    x = []
    y = []
    for i in t:
        x.append(i[0])
        y.append(i[1])
    return x, y


x_f, y_f = returnxy(g_first)
x_o, y_o = returnxy(g_other)
x_a, y_a = returnxy(g_all)

# 长度不一样，统一一下, 可以用all直接统计，但按转最开始的代码来吧
alist = list(x_f)
alist.extend(x_o)
xmin, xmax =  min(alist), max(alist)
x = range(xmin, xmax +1)
yy_f = [0 for i in x]
yy_o = [0 for i in x]
yy_a = [0 for i in x]
# print x

for i in x:
    if i in x_f:
        idx = x_f.index(i)
        yy_f[i] = y_f[idx]
    if i in x_o:
        idx = x_o.index(i)
        yy_o[i] = y_o[idx]
    if i in x_a:
        idx = x_a.index(i)
        yy_a[i] = y_a[idx]

print x
print sum(yy_f), len(yy_f), yy_f
print sum(yy_o), len(yy_o), yy_o
print sum(yy_a), len(yy_a), yy_a


# Num of livebirth 9148
# 一胎数量 4413
# 其他数量 4735

# sum_f = sum(yy_f)
# pmf_f = [float(i) / sum_f for i in yy_f]
#
# sum_o = sum(yy_o)
# pmf_o = [float(i) / sum_o for i in yy_o]
#
# #[0-37] [38-40] [41-]
#
# proEarly_f = sum(pmf_f[0: 38])
# proEarly_o = sum(pmf_o[0: 38])
# relativeRiskEarly = float(proEarly_f) / proEarly_o
# print 'pro early of firsts', proEarly_f
# print 'pro early of others', proEarly_o
# print 'relative risk of early',relativeRiskEarly
# print '这意味着第一胎较其他几胎更早出生的可能性有8%'




