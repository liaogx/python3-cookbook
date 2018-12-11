#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 返回多个值的函数


def my_fun():
    return 1, 2, 3


a, b, c = my_fun()

print(a, b, c)

# 尽管 my_fun() 看上去返回了多个值，实际上是先创建了一个元组然后返回的。
