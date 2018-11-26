#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


from collections import Iterable

print("包含 yield from 语句的递归生成器")


def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from flatten(i)
        else:
            yield i


items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)

print("不使用yield from的递归生成器")


def flatten2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for x in flatten2(x):  # 这里依然需要使用递归
                yield x
        else:
            yield x


for x in flatten2(items):
    print(x)
