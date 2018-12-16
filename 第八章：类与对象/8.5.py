#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 在类中封装属性名

class A(object):
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


class B(object):
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super(C).__init__()
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass


"""
_A: 单下划线开头，表示内部实现，但不会阻止外部访问。同样适用于模块名和模块级别函数
__A: 双下划线开头，表示私有的属性或方法，但是这种属性通过继承时无法被覆盖
A_: 单下划线结尾，当定义的变量和某个保留的关键字冲突时

上面提到有两种不同的编码约定 (单下划线和双下划线) 来命名私有属性，那么问
题就来了：到底哪种方式好呢？大多数而言，你应该让你的非公共名称以单下划线开
头。但是，如果你清楚你的代码会涉及到子类，并且有些内部属性应该在子类中隐藏起
来，那么才考虑使用双下划线方案。
"""
