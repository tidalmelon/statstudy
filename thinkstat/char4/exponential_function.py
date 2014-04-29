__author__ = 'root'
# --*-- coding:utf-8 --*--
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2, 1000)
# 指数函数，变量是指数，即上面的
y = np.exp(x)

y_1 = (1 / np.e) ** x

y_zhishu = 3 * (np.e ** (-x * 3))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, x, y_1, x, y_zhishu)
plt.grid()
plt.show()
