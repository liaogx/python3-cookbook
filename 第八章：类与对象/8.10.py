#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""
使用延时计算属性，你想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。但
是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
"""

import math


# 定义一个延迟属性的一种高效方法是通过使用一个描述器类


class lazyproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return math.pi * self.radius * 2


c = Circle(4.0)
print(c.radius, c.area, c.perimeter)
print(c.radius, c.area, c.perimeter)

"""
仔细观察你会发现消息 Computing area 和 Computing perimeter 仅仅出现一次
很多时候，构造一个延迟计算属性的主要目的是为了提升性能
"""
