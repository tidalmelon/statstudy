__author__ = 'root'
# --*-- coding:utf-8 --*--
import matplotlib.pyplot as pyplot

labels = ('food', 'cloth', 'travel', 'education', 'medical', 'other')
pyplot.pie([2500, 1000, 500, 800, 400, 600], labels=labels)
pyplot.show()