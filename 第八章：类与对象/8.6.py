#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import math


# 创建可管理的属性，如增加除修改和访问之外的其它处理逻辑，比如类型检查或合法性验证
# 使用property, 使类的方法能够像属性一样使用


class Person(object):

    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can not delete attribute')


p = Person('liao gao xiang')
print(p.first_name)
p.first_name = 'liaogx'
print(p.first_name)


# del p.first_name


# Properties 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会
# 被实际的存储，而是在需要的时候计算出来。

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return math.pi * self.radius * 2


c = Circle(4.0)
print(c.area, c.diameter, c.perimeter)

"""
在这里，我们通过使用 properties，将所有的访问接口形式统一起来，对半径、直
径、周长和面积的访问都是通过属性访问，就跟访问简单的 attribute 是一样的。如果
不这样做的话，那么就要在代码中混合使用简单属性访问和方法调用。
"""
