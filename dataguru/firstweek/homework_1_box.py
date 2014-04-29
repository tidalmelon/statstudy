# --*-- coding:utf-8 --*--
from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math


def mean(t):
    """均值"""
    return sum(t) / len(t)


def median(t):
    """中位数"""
    arr = sorted(t)
    print arr
    idx = (len(arr) - 1) / 2
    if type(idx) is int:
        return arr[idx], int(idx), None
    if type(idx) is float:
        return mean(arr[int(math.floor(idx)):int(math.ceil(idx)) + 1]), int(math.floor(idx)), int(math.ceil(idx))


def cut3(t, down, up):
    """切成三份，t必须是排好序的"""
    t1 = 0
    t2 = 0
    for i in range(len(t)):
        if t[i] >= down:
            t1 = i
            break
    for i in reversed(range(len(t))):
        if t[i] <= up:
            t2 = i + 1
            break
    return t[0: t1], t[t1: t2], t[t2:]


# 1 排序，找出中位数 median = 5.0
# 2 找出下四分位数，上四分位数 Q1 = 3.0 Q3 = 8.0
# 3 四分位距 IQR = Q3 - Q1 = 5.0
# 4 异常点 err < Q1 - 1.5 * IQR 或者 err > Q3 + 1.5 * IQR
# 5 计算上边缘 除异常点外的数据中的最大值
# 6 计算下边缘 除异常点外的数据中的最小值
# 7 画图


#data = [8, 2, 3, 7, 4, 9, 6, 9, 4, 3]
data = [225, 232, 232, 245, 235, 245, 270, 225, 240, 240, 217, 195, 225, 185, 200, 220, 200, 210, 271, 240, 220, 230,
        215, 252, 225, 220, 206, 185, 227, 236]
data.sort()

med, med1, med2 = median(data)

Q1, q, w = median(data[0: med1 + 1])
Q3, q, w = median(data[med2:])

# 3 四分位距 IQR = Q3 - Q1 = 5.0
IQR = Q3 - Q1

print '中位数：', med
print '下四分位：', Q1
print '上四分位：', Q3
print '四分位距：', IQR

# 4 异常点 err < Q1 - 1.5 * IQR 或者 err > Q3 + 1.5 * IQR
#判断异常点用阈值
downThreshold = Q1 - 1.5 * IQR
upThreshold = Q3 + 1.5 * IQR
errdown, normal, errup = cut3(data, downThreshold, upThreshold)

print '异常阈值下:', downThreshold, '异常阈值上：', upThreshold

# 5 计算上边缘 除异常点外的数据中的最大值
Min = normal[0]
# 6 计算下边缘 除异常点外的数据中的最小值
Max = normal[len(normal) - 1]

print '最小值', Min, '最大值', Max
print errdown, normal, errup

# 7 画图 matplotlib内置的箱线图似乎不准。。。。
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.plot([Q1, Q1], [2, 3], color='b', linewidth=2)
ax.text(Q1, 3.01, 'Q1', horizontalalignment='center', color='green')
ax.plot([Q1, Q1], [1, 2], 'r--')
ax.text(Q1, 1, str(Q1))
ax.plot([Q3, Q3], [2, 3], color='b', linewidth=2)
ax.text(Q3, 3.01, 'Q3', horizontalalignment='center', color='green')
ax.plot([Q3, Q3], [1, 2], 'r--')
# ax.text(Q3, 1, str(Q3))

ax.plot([Q1, Q3], [3, 3], color='b', linewidth=2)
ax.plot([Q1, Q3], [2, 2], color='b', linewidth=2)
ax.plot([med, med], [2, 3], color='b', linewidth=2)

ax.plot([med, med], [1, 2], 'r--')
ax.text(med, 1, str(med))
ax.text(med, 3.01, 'Median', horizontalalignment='center', color='green')

ax.plot([Min, Min], [2, 3], color='b', linewidth=2)
ax.plot([Max, Max], [2, 3], color='b', linewidth=2)

ax.plot([Max, Max], [1, 2], 'r--')
ax.text(Max, 1, str(Max))


ax.plot([Min, Q1], [2.5, 2.5], color='b', linewidth=2)
ax.plot([Q3, Max], [2.5, 2.5], color='b', linewidth=2)
ax.plot([Min, Min], [1, 2], 'r--')
ax.text(Min, 1, str(Min))

ax.plot([Q1, Q3], [1.5, 1.5], 'r--', linewidth=2)
ax.text((Q1 + Q3) / 2, 1.51, 'IQR', horizontalalignment='center', color='red')


ax.text(Min, 3.01, 'Min', horizontalalignment='center', color='green')
ax.text(Max, 3.01, 'Max', horizontalalignment='center', color='green')

note = """Q1: 215.0
median: 225.0
Q3: 240.0
IQR: 25.0
err threshod down: 177.5, no err point
err threshold up: 277.5,  no err point
min 185 max 271"""

ax.text(250, 3.5, note, color='b')


plt.ylim(1, 4)
plt.xlim(downThreshold, upThreshold)
# plt.grid()
plt.show()


