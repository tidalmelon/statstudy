# --*-- coding:utf-8 --*--
from __future__ import division
import thinkstat.char1.first as first
import thinkstat.char1.survey as survey
import thinkstats


def mean(t):
    return sum(t) / len(t)

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
mu_first = mean([rec.prglength for rec in firsts.records])
mu_other = mean([rec.prglength for rec in others.records])

print 'first babies mean', mu_first
print 'other babies mean', mu_other
print 'difference in days by mean', abs(mu_first - mu_other) * 7, 'difference in hours', abs(mu_first - mu_other) * 7 * 24
# Mean gestation in weeks:
# First babies 38.6009517335
# Others 38.5229144667
# Difference in days 0.546260867443

import math
stdvar_first = math.sqrt(thinkstats.Var([rec.prglength for rec in firsts.records]))
stdvar_other = math.sqrt(thinkstats.Var([rec.prglength for rec in others.records]))

print 'standard var first', stdvar_first
print 'standard var other', stdvar_other
print 'difference in days by mean', abs(stdvar_first - stdvar_other)