#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 字典中的键映射多个值
from collections import defaultdict

d = defaultdict(list)
print(d)
d['a'].append([1, 2, 3])
d['b'].append(2)
d['c'].append(3)

print(d)

d = defaultdict(set)
print(d)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)
