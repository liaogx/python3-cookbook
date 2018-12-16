#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 改变对象的字符串显示


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'repr: {self.x} and {self.y}'

    def __str__(self):
        return f'str: {self.x} and {self.y}'


p = Pair(1, 2)
print(p)

# 自定义 __repr__() 和 __str__() 通常是很好的习惯，因为它能简化调试和实例输出。
