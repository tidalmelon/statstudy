# --*-- coding:utf-8 --*--
from __future__ import division
import math
import itertools


def mean(t):
    """均值"""
    return sum(t) / len(t)


def median(t):
    """中位数"""
    arr = sorted(t)
    idx = (len(arr) - 1) / 2
    if type(idx) is int:
        return arr[idx]
    if type(idx) is float:
        return mean(arr[int(math.floor(idx)):int(math.ceil(idx)) + 1])


def getfreq(t):
    """获取t中每个值及其出现次数"""
    arr = sorted(t)
    alist = []
    for k, g in itertools.groupby(arr):
        alist.append((len(list(g)), k))
    alist.sort(key=lambda x: x[0], reverse=True)
    return alist


def allmode(t):
    """众数"""
    if not t:
        return None
    arr = getfreq(t)
    if arr[0][0] == 1:
        return None
    else:
        for k, g in itertools.groupby(arr, key=lambda x: x[0]):
            return [t[1] for t in g]


def rangejc(t):
    """极差"""
    if not t:
        return None
    return max(t) - min(t)


def var(t):
    """总体方差"""
    if not t:
        return None
    mu = mean(t)
    return sum([e ** 2 for e in t]) / len(t) - mu ** 2


def svar(t):
    """样本方差"""
    if not t:
        return None
    mu = mean(t)
    return sum([(x - mu) ** 2 for x in t]) / (len(t) - 1)


def stdvar(t):
    """标准差"""
    if not t:
        return None
    return math.sqrt(var(t))


if __name__ == '__main__':
    astr = '93 62 51 93 75 82 93 62 65 51'
    astr = '1 2 3 4 5'
    alist = [int(e) for e in astr.split()]
    print '均值:', mean(alist)
    print '中位数:', median(alist)
    print '众数:', allmode(alist)
    print '极差:', rangejc(alist)
    print '总体方差:', var(alist)
    print '样本方差', svar(alist)
    print '标准差:', stdvar(alist)
