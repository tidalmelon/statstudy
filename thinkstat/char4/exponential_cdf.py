__author__ = 'root'
# --*-- coding:utf-8 --*--
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2, 1000)

y = 1 - np.e ** (-2 * x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)

plt.grid()
plt.show()