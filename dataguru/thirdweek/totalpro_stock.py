__author__ = 'root'
# --*-- coding:utf-8 --*--

# 该时区内利率下调的概率为60%， 利率不变的概率为40%，
# 根据经验，在利率下调时某支股票上涨的概率为80% 在利率不变时，这支股票上涨的40%
# 求这支股票的上升概率

#分析 A = {该时区内利率下调的概率为60%} B = {利率不变的概率为40%} A+B=S , AB=0, 所以这是一个划分
# C = {上升}
# P(C) = P(CA) + P(CB） = P(C|A)P(A) + P(C|B)P(B)
#                       = 0.8 * 0.6 + 0.4 * 0.4
print 0.8 * 0.6 + 0.4 * 0.4