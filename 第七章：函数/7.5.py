#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 函数的默认参数的值仅仅在函数定义的时候赋值一次！

x = 1


def spam(a, b=x):
    print(a, b)


spam(1)
x = 2
spam(2)

x = 3
spam(3)
