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
for rec in table.records:
    if rec.outcome != 1:
        continue
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

# print x_f
# print x_o
# 长度不一样，统一一下
alist = list(x_f)
alist.extend(x_o)
xmin, xmax =  min(alist), max(alist)
x = range(xmin, xmax +1)
yy_f = [0 for i in x]
yy_o = [0 for i in x]
# print x

for i in x:
    if i in x_f:
        idx = x_f.index(i)
        yy_f[i] = y_f[idx]
    if i in x_o:
        idx = x_o.index(i)
        yy_o[i] = y_o[idx]

print x
print yy_f
print yy_o

fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
# ax.plot(x, yy_o, x, yy_f)
ax.bar(x, yy_f, width=0.5, label='first bb')
ax.bar([i + 0.5 for i in x], yy_o, width=0.5, color='r', label='other bb')
plt.grid()
plt.legend()
plt.show()


