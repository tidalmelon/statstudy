__author__ = 'root'
import itertools

print "permutations".center(60, '#')
t = range(1, 10)
p = itertools.permutations(t, 3)
print type(p)
res = list(p)
print len(res)
print res

print "combinnations".center(60, '#')
c = itertools.combinations(t, 3)
print type(c)
resc = list(c)
print len(resc)
print resc