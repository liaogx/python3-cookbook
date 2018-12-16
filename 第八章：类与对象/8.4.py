#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 创建大量对象时节省内存的方法


class Date(object):
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date(2018, 12, 12)

"""
使用 slots 后节省的内存会跟存储属性的数量和类型有关。不过，一般来讲，使用
到的内存总量和将数据存储在一个元组中差不多。为了给你一个直观认识，假设你不使
用 slots 直接存储一个 Date 实例，在 64 位的 Python 上面要占用 428 字节，而如果使
用了 slots，内存占用下降到 156 字节。如果程序中需要同时创建大量的日期实例，那
么这个就能极大的减小内存使用量了。
尽管 slots 看上去是一个很有用的特性，很多时候你还是得减少对它的使用冲动。
Python 的很多特性都依赖于普通的基于字典的实现。另外，定义了 slots 后的类不再支
持一些普通类特性了，比如多继承。大多数情况下，你应该只在那些经常被使用到的用
作数据结构的类上定义 slots (比如在程序中需要创建某个类的几百万个实例对象)。
关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增
加新的属性。尽管使用 slots 可以达到这样的目的，但是这个并不是它的初衷。 __slots__
更多的是用来作为一个内存优化工具。
"""