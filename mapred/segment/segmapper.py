__author__ = 'root'
# --*-- coding:utf-8 --*--
import sys
import jieba
from operator import itemgetter
import os
import datetime
# cat /data/data/dataguru/*/* | python segmapper.py | sort | python segreducer.py
for line in sys.stdin:

    # 过滤垃圾字符
    if not line:
        continue
    if line == '\n':
        continue
    line = line.strip()

    seg_list = jieba.cut(line, cut_all=False)
    dict = {}
    for word in seg_list:
        word = word.strip()
        if word not in dict:
             #initialize
            dict[word] = 0
        else:
            #sum
            dict[word] += 1
    sorted_list = sorted(dict.items(), key=itemgetter(1))
    for word, c in sorted_list:
        # 确保里面没有\t
        word = word.replace('\t', '')
        if not word:
            continue
        print '%s\t%s' % (word.encode('utf-8'), c)


# start = datetime.datetime.now()
# dir = '/data/data/dataguru/'
# filelist = []
# for root, dirs, files in os.walk(dir):
#     for name in files:
#         f = os.path.join(root, name)
#         filelist.append(f)
#
# o_f = open('words.txt', 'w')
# counter = 0
# for f in filelist:
#     print counter
#     counter += 1
#     with open(f, 'r') as mf:
#         while 1:
#             lines = mf.readlines()
#             if not lines:
#                 break
#             for line in lines[2:]:
#                 if line == '\n':
#                     continue
#                 line = line.strip()
#                 seg_list = jieba.cut(line, cut_all=False)
#                 res = "/ ".join(seg_list)
#                 # print line
#                 # print res
#             #o_f.write(line + os.linesep)
#             o_f.write(f + os.linesep)
#             o_f.write(line + os.linesep)
#             o_f.write(res.encode('utf-8') + os.linesep)
# o_f.close()
# end = datetime.datetime.now()
# interval = end - start
# print interval.total_seconds()
# print 'run over'