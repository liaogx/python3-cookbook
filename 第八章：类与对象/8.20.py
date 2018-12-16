#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 通过字符串调用对象方法

import math
import operator


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point {self.x} {self.y}'

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


"""
当你需要通过相同的参数多次调用某个方法时，使用 operator.methodcaller 就很方便了。
"""

points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))

print(points)
