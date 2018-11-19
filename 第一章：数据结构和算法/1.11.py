#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 关于命名切片

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)

# 方法二避免了大量无法理解的硬编码下标，使得你的代码更加清晰可读
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 6, 2)
print(items[a])
print(items[2:4])

print(a.start, a.stop, a.step)  # 开始，结束，间隔信息

s = 'liaogaoxiang'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
