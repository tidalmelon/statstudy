__author__ = 'root'
# --*-- coding:utf-8 --*--

# 一次处理一个字符
astr = 'abcddef'
print list(astr)

for c in astr:
    print c


def consoleprint(c):
    print c

[consoleprint(c) for c in astr]

print '----------------------------'
result = map(lambda x: (x, 1), astr)
print result