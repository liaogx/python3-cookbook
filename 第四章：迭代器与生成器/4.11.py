#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from itertools import zip_longest

# 你想同时迭代多个序列，每次分别从一个序列中取一个元素

x = [1, 5, 4, 2, 10]
y = [101, 78, 37, 15, 62, 99]

for i in zip(x, y):  # 已短的序列为主
    print(i)

print("-------------")

for j in zip_longest(x, y):  # 以长的序列为主
    print(j)

# zip() 会创建一个迭代器来作为结果返回。如果你需要将结对
# 的值存储在列表中，要使用 list() 函数

print(zip(x, y), zip_longest(x, y))
print(list(zip(x, y)), dict(zip_longest(x, y)))
