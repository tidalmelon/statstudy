# --*-- coding:utf --*--
from __future__ import division
import matplotlib.pyplot as plt


def drange(start, stop, step):
    r = start
    while r <= stop:
    #while r < stop:
        yield r
        r += step


def inrange(e, start, end):
    if start <= e < end:
        return True
    return False


alist = [225, 232, 232, 245, 235, 245, 270, 225, 240, 240, 217, 195, 225, 185, 200, 220, 200, 210, 271, 240, 220, 230,
         215, 252, 225, 220, 206, 185, 227, 236]
#tmp = sorted(alist)
#print tmp
# 计算组距
# 计算频率f
# 计算频率f/n
# 计算 f/n / deierta

# 统计频率f 将数据映射到 drange(179.5, 279.5, 20) 各区间中，并统计命中次数
kv = [[e, 0] for e in drange(179.5, 279.5, 20)]
for e in alist:
    if inrange(e, kv[0][0], kv[1][0]):
        kv[0][1] += 1
    elif inrange(e, kv[1][0], kv[2][0]):
        kv[1][1] += 1
    elif inrange(e, kv[2][0], kv[3][0]):
        kv[2][1] += 1
    elif inrange(e, kv[3][0], kv[4][0]):
        kv[3][1] += 1
    else:
        kv[4][1] += 1

print kv
N = len(alist)
# 计算频率 f/n / deierta
kf = [[e[0], (e[1] / N) / 20] for e in kv]
print kf

x = [e[0] for e in kf]
y = [e[1] for e in kf]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x, y, width=20)
ax.xaxis.set_ticks(x)

ax.text(229.5, 0.022, '0.021666666666666667', horizontalalignment='center')
ax.text(269.5, 0.0034, '0.003333333333333333', horizontalalignment='center')
ax.text(189.5, 0.005, '0.005', horizontalalignment='center')
ax.text(209.5, 0.01, '0.01', horizontalalignment='center')
ax.text(249.5, 0.01, '0.01', horizontalalignment='center')

plt.xlim(159.5, 299.5)
plt.title('Frequency histograms')
plt.xlabel('weight')
plt.ylabel('frequency')
plt.grid()
plt.show()

