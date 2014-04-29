from __future__ import division
# --*-- coding:utf-8 --*--

t = range(1, 7)
space = []
for a in t:
    for b in t:
        mod = (a + b) % 2
        space.append((a, b, mod))

for a in space:
    print a

beibei = [i for i in space if i[2] == 1]
xiaoliang = [i for i in space if i[2] == 0]

print len(beibei)
print len(xiaoliang)