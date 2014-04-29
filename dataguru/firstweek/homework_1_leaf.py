__author__ = 'root'
# --*-- coding:utf-8 --*--
data = [225, 232, 232, 245, 235, 245, 270, 225, 240, 240, 217, 195, 225, 185, 200, 220, 200, 210, 271, 240, 220, 230,
        215, 252, 225, 220, 206, 185, 227, 236]

data = [185, 185, 195, 200, 200, 206, 210, 215, 217, 220, 220, 220, 225, 225, 225, 225, 227, 230, 232, 232, 235,
        236, 240, 240, 240, 245, 245, 252, 270, 271]

step = 10
intervals = [(i, [], []) for i in range(180, 280, step)]

#分组
for t in intervals:
    d = t[0]
    vals = t[1]
    leafs = t[2]
    for dd in data:
        mod = dd % d
        if mod < 10:
            vals.append(dd)
            leafs.append(mod)

print '分组信息'.center(50, '#')
for t in intervals:
    print t[0], '|', t[1], '|', t[2]

print '茎叶图'.center(50, '#')

for t in intervals:
    print t[0] / 10, '|', ''.join([str(e) for e in t[2]])

print '茎叶图'.center(50, '#')