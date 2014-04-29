# --*-- coding:utf-8 --*--
# from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

labels = ('', 'food', 'cloth', 'travel', 'education', 'medical', 'other')
x = [10, 20, 30, 40, 50, 60]
#为了显示文字到正确位置，把坐标轴向左移动了5个单位
x = [i + 5 for i in x]
y = [2500, 1000, 500, 800, 400, 600]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x, y, width=10)

# ax.xaxis.set_major_locator(MultipleLocator(5))
#ax.xaxis.set_ticklabels(labels)
plt.show()