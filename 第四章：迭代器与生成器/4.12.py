#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from collections import ChainMap
from itertools import chain

# 不同集合上元素的迭代
a = [1, 2, 3, 4]
b = ('x', 'y', 'z')
c = {1, 'a'}

# 方法一，使用chain
for i in chain(a, b, c):
    print(i)
print('--------------')
# 方法二，使用chainmap
for j in ChainMap(a, b, c):
    print(j)

# 这两种均为节省内存，效率更高的迭代方式
