# --*-- coding:utf-8 --*--
from __future__ import division
import thinkstat.char1.survey as survey
import itertools
import matplotlib.pyplot as plt


def Config(**options):
    """Configures the plot.

    Pulls options out of the option dictionary and passes them to
    title, xlabel, ylabel, xscale, yscale, xticks, yticks, axis, legend,
    and loc.
    """
    title = options.get('title', '')
    plt.title(title)

    xlabel = options.get('xlabel', '')
    plt.xlabel(xlabel)

    ylabel = options.get('ylabel', '')
    plt.ylabel(ylabel)

    if 'xscale' in options:
        plt.xscale(options['xscale'])

    if 'xticks' in options:
        plt.xticks(options['xticks'])

    if 'yscale' in options:
        plt.yscale(options['yscale'])

    if 'yticks' in options:
        plt.yticks(options['yticks'])

    if 'axis' in options:
        plt.axis(options['axis'])

    loc = options.get('loc', 0)
    legend = options.get('legend', True)
    if legend:
        plt.legend(loc=loc)

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

wgt_first = [rec.totalwgt_oz for rec in firsts.records if rec.totalwgt_oz != 'NA']
wgt_other = [rec.totalwgt_oz for rec in others.records if rec.totalwgt_oz != 'NA']


def rendercdf(t):
    t.sort()
    N = len(t)
    g = [[i[0], len(list(i[1]))] for i in itertools.groupby(t)]
    x, y = zip(*g)
    print len(x), len(y)
    return [i for i in x], [sum(y[0:i+1]) / N for i in range(len(y))]


x_f, y_f = rendercdf(wgt_first)
x_o, y_o = rendercdf(wgt_other)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_f, y_f, label='first baby')
ax.plot(x_o, y_o, label='other baby')
plt.legend()
plt.show()