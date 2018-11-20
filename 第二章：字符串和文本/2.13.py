#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 字符串对齐,可以使用字符串的ljust(),rjust()和center()方法
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20, "*"))
# 函数 format()同样可以用来很容易的对齐字符串。你要做的就是使用 <,>或者^字符后面紧跟一个指定的宽度
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '*^20s'))
# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中。比如：
print('{:>10s} {:#>10}'.format('hello', 'world'))
# format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用。比如，你可以用它来格式化数字
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
"""
在老的代码中，你经常会看到被用来格式化文本的 % 操作符。比如：

>>> '%-20s' % text
'Hello World         '
>>> '%20s' % text
'         Hello World'
>>>
但是，在新版本代码中，你应该优先选择format()函数或者方法。
format()要比 % 操作符的功能更为强大。
并且format()也比使用ljust(), rjust()或center()方法更通用，
因为它可以用来格式化任意对象，而不仅仅是字符串。
"""
