#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from heapq import merge

# 问题：你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in merge(a, b):
    print(c)

# heapq.merge() 需要所有输入序列必须是排过序的。
