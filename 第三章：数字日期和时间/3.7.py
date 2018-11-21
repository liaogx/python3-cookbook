#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import math

# 无穷大与NaN，你想创建或测试正无穷、负无穷或NaN(非数字)的浮点数
# Python中没有特殊的语法来表示这些特殊的浮点值，但是可以使用float()来创建它们。比如：
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)

# 为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数
print(math.isinf(a), math.isinf(b), math.isnan(c))
# 无穷大数在执行数学计算的时候会传播，比如：
print(a + 45, a * 10, 10 / a)
# 但是有些操作时未定义的并会返回一个NaN结果。比如：
print(a / a, a + b)
# NaN值会在所有操作中传播，而不会产生异常。比如：
print(c + 23, c / 2, c * 2, math.sqrt(c))
# NaN值的一个特别的地方时它们之间的比较操作总是返回False。比如：
c = float('nan')
d = float('nan')
print(c == d, c is d)

"""
由于这个原因，测试一个NaN值得唯一安全的方法就是使用 math.isnan() ，也就是上面演示的那样。
有时候程序员想改变Python默认行为，在返回无穷大或NaN结果的操作中抛出异常。
fpectl 模块可以用来改变这种行为，但是它在标准的Python构建中并没有被启用，
它是平台相关的，并且针对的是专家级程序员。
"""
