#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 使用匿名函数捕获外层作用域的变量

x = 10
a = lambda y: x + y
y = 20
b = lambda y: x + y

print(a(10), b(10))

"""
这其中的奥妙在于 lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不
是定义时就绑定，这跟函数的默认值参数定义是不同的。
"""
