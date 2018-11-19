#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""'
字典运算，怎么在字典中执行一些计算操作，比如求最小值、最大值、排序等等
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

print(min_price, max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(prices_sorted)

prices_and_names = zip(prices.values(), prices.keys())
# zip() 函数创建的是一个只能访问一次的迭代器
print(min(prices_and_names))  # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

print(min(prices), min(prices.keys()), min(prices.values()))
# min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
a = min(prices, key=lambda k: prices[k])  # Returns 'FB'
b = max(prices, key=lambda k: prices[k])  # Returns 'AAPL'
print(a, b)
# 如果还想要得到最小值，你又得执行一次查找操作
c = min_value = prices[min(prices, key=lambda k: prices[k])]
print(c)

"""
前面的 zip() 函数方案通过将字典”反转”为(值，键)元组序列来解决了上述问题。 当比较两个元组的时候，值会先进行比较，然后才是键。 这样的话你就能通过一条简单的语句就能很轻松的实现在字典上的求最值和排序操作了。

需要注意的是在计算操作中使用到了(值，键)对。当多个实体拥有相同的值的时候，键会决定返回结果。 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：

>>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
>>> min(zip(prices.values(), prices.keys()))
(45.23, 'AAA')
>>> max(zip(prices.values(), prices.keys()))
(45.23, 'ZZZ')
>>>
"""

print(zip(("a", "b", "c"), (1, 2, 3)))
print(list(zip(("a", "b", "c"), (1, 2, 3))))
print(dict(zip(("a", "b", "c"), (1, 2, 3, 4))))
print(list(zip(("a", "b", "c", "d"), (1, 2, 3))))
print(list(zip(("a", "b"), (1, 2, 3))))
