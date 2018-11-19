#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 转换并同时计算数据
# 一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)
s = sum((x * x for x in nums))
print(s)
s = sum([x * x for x in nums])
print(s)
# Deter if any .py files exit in a directory
import os

files = os.listdir('../../python3-cookbook')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry,no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))  # ???
# Data reuctioin across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
"""
这种方式同样可以达到想要的效果，但是它会多一个步骤，先创建一个额外的列表。
对于小型列表可能没什么关系，但是如果元素数量非常大的时候，
它会创建一个巨大的仅仅被使用一次就被丢弃的临时数据结构。
而生成器方案会以迭代的方式转换数据，因此更省内存。
"""

min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
