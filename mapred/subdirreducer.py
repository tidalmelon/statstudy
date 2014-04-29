#!/usr/bin/python
from operator import itemgetter
import sys

dict_subdir_count = {}

for line in sys.stdin:
    line = line.strip()
    subdir, num = line.split('\t')
    try:
        num = int(num)
        dict_subdir_count[subdir] = dict_subdir_count.get(subdir, 0) + num
    except ValueError:
        pass

sorted_dict_ip_count = sorted(dict_subdir_count.items(), key=itemgetter(0))
for subdir, count in sorted_dict_ip_count:
    print '%s\t%s' % (subdir, count)
