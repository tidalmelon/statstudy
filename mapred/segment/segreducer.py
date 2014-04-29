# --*-- coding:utf-8 --*--
from operator import itemgetter
import sys
import os

dict_word_count = {}

mf = open('wordcount.txt', 'w')
f_err = open('err.txt', 'a')
for line1 in sys.stdin:
    line = line1.strip()

    try:
        word, num = line.split('\t')
        num = int(num)
        # 这个方法挺酷的哦
        dict_word_count[word] = dict_word_count.get(word, 0) + num
    except Exception, e:
        #print line1
        f_err.write(line1 + os.linesep)
        print e

sorted_dict_ip_count = sorted(dict_word_count.items(), key=itemgetter(1), reverse=True)
for word, count in sorted_dict_ip_count:
    res = '%s\t%s' % (word, count)
    print res
    mf.write(res + os.linesep)

sumres = '%s\t%s' % ('sum of single ip', len(sorted_dict_ip_count))
print sumres
mf.write(sumres + os.linesep)
mf.close()
f_err.close()