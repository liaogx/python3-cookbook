#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import re

# 字节字符串上的字符串操作
# 你想在字节字符串上执行普通的文本操作(比如移除，搜索和替换)。
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
# 这些操作也同样适用于字节组。比如：
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 使用正则表达式匹配字节字符窜，但是正则表达式本身必须也是字节串。比如：
data = b'FOO:BAR,SPAM'

print(re.split(b'[:,]', data))

# 大多数情况下，在文本字符串上的操作均可用于字节字符串。然而，这里
# 也有一些需要注意的不同点，首先，字节字符串的索引操作放回整数而不是单独字符。必须：
a = 'Hello World'
print(a[0], a[1])
b = b'Hello World'
print(b[0], b[1])

# 字节字符串不会提供一个美观的字符串表示，也不能很好的打印出来，除非它们
# 先被解码为一个文本字符串。类似的，也不存在任何适用于字节字符串的格式化操作
s = b'Hello World'
print(s)
print(s.decode('ascii'))

"""
最后提一点，一些程序员为了提升程序执行的速度会倾向于使用字节字符串而不是文本字符串。
尽管操作字节字符串确实会比文本更加高效(因为处理文本固有的Unicode相关开销)。
这样做通常会导致非常杂乱的代码。你会经常发现字节字符串并不能和Python的其他部分工作的很好，
并且你还得手动处理所有的编码/解码操作。 坦白讲，如果你在处理文本的话，
就直接在程序中使用普通的文本字符串而不是字节字符串。不做死就不会死！
"""
