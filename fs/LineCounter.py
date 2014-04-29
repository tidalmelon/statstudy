__author__ = 'root'
import re
import os

# (?<ip>\\d+\\.\\d+\\.\\d+\\.\\d+).*?\"\\w+ (?<subdir>.*?)
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?"\w+ (?P<subdir>.*?) ')

dir = '/home/hadoop/Sep-2013/Sep-2013-9/dongxicheng.org.log.1'
fw = open('res.txt', 'w')
with open(dir, 'r') as myf:
    while True:
        line = myf.readline()
        if not line:
            break
        #print line
        match = pat.search(line)
        if match:
            fw.write(match.group('ip') + '\t' + match.group('subdir') + os.linesep)
            print match.group('ip'), match.group('subdir')
        else:
            print line
fw.close()