#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 二八十六进制整数
# 为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用bin(),oct()或hex()函数：
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
# 另外，如果你不想输出0b,0o或者0x的前缀的话，可以使用 format()函数。比如：
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
# 如果你想产生一个无符号值，你需要增加一个指示最大位长度的值。比如为了显示32位的值，可以像下面这样写：
x = -1234
print(format(2 ** 32 + x, 'b'))
print(format(2 ** 32 + x, 'x'))
"""
大多数情况下处理二进制、八进制和十六进制整数是很简单的。 只要记住这些转换属于整数和其对应的文本表示之间的转换即可。永远只有一种整数类型。
最后，使用八进制的程序员有一点需要注意下。 Python指定八进制数的语法跟其他语言稍有不同。比如，如果你像下面这样指定八进制，会出现语法错误：
>>> import os
>>> os.chmod('script.py', 0755)
    File "<stdin>", line 1
        os.chmod('script.py', 0755)
                            ^
SyntaxError: invalid token
>>>
需确保八进制数的前缀是 0o ，就像下面这样：
>>> os.chmod('script.py', 0o755)
"""
