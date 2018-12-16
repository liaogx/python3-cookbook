#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import bisect
import collections

"""
你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确
定到底要实现哪些方法。
"""


# 继承collections的Sequence类，实现元素按照顺序存储：


class StoredItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        """bisect保证在排序列表中插入元素后依然保持顺序"""
        bisect.insort(self._items, item)


s = StoredItems([3, 5, 34, 2])
print(list(s))
s.add(22)
print(list(s))

"""
使用 collections 中的抽象基类可以确保你自定义的容器实现了所有必要的方法。
并且还能简化类型检查。你的自定义容器会满足大部分类型检查需要。
collections 中很多抽象类会为一些常见容器操作提供默认的实现，这样一
来你只需要实现那些你最感兴趣的方法即可。
"""
