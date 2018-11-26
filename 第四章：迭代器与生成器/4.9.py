#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想迭代遍历一个集合中元素的所有可能的排列或组合

from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']

for p in permutations(items, r=3):  # r<len(items), 表示每一个排列组合中元素的个数
    print(f"permutations: {p}")

for p in combinations(items, r=3):
    print(f"combinations: {p}")

for p in combinations_with_replacement(items, r=3):
    print(f"combinations_with_replacement: {p}")
