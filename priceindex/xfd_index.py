# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import dataguru.firstweek.homework_2 as basic
import loadprice
import os


def staticinfo(tups):
    text = 'mean %s ' % basic.mean(tups[1]) + os.linesep
    text += 'mode %s' % basic.allmode(tups[1]) + os.linesep
    text += 'median %s' % basic.median(tups[1]) + os.linesep
    text += 'var %s' % basic.var(tups[1]) + os.linesep
    text += 'standard var %s' % basic.stdvar(tups[1])
    return text

print 'tomato statisitcs info'.center(60, '#')
name = '番茄'
records = loadprice.getRecords(name)

# 压缩出x y
tups = zip(*records)

# 基本统计量
print staticinfo(tups)

print 'potato statisitcs info'.center(60, '#')
name = '土豆'
records = loadprice.getRecords(name)
tups_1 = zip(*records)
print staticinfo(tups_1)


# 绘图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tups[0], tups[1], 'o-', color='b', label='tomato')
ax.plot(tups_1[0], tups_1[1], 'o-', color='r', label='potato')
# ax.xaxis.set_ticklabels(tups[2]) # 这样设置的是主刻度
ax.xaxis.set_minor_locator(MultipleLocator(1))
# ax.text(tups[0][-1] - datetime.timedelta(days=40), 1, staticinfo(tups), horizontalalignment='left')
fig.autofmt_xdate()
plt.grid()
plt.title('beijing price')
plt.legend()
plt.show()