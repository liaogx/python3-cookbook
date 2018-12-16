#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 实现属性的代理访问，将某个实例的属性访问代理到内部的另一个实例中去，
# 目的可能是作为继承的一个替代方法或者实现代理模式

class A(object):
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1(object):
    """简单的代理"""

    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2(object):
    """使用__getattr__代理大量方法"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        return getattr(self._a, item)





