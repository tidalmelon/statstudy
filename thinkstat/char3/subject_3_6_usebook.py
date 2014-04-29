# --*-- coding:utf-8 --*--
from __future__ import division
import thinkstat.char1.survey as survey
import Cdf
import thinkstat.char2.myplot as myplot

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


cdf_first = Cdf.MakeCdfFromList(wgt_first, 'weight_first')
cdf_other = Cdf.MakeCdfFromList(wgt_other, 'weight_other')

myplot.Cdf(cdf_first)
myplot.Cdf(cdf_other)
myplot.show()