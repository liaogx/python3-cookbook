#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 打印输出至文件中
# 你想将 print() 函数的输出重定向到一个文件中去。
with open('file.txt', 'at', encoding='utf-8') as f:
    print('Hello World!', file=f)

"""
关于输出重定向到文件中就这些了。
但是有一点要注意的就是文件必须是以文本模式打开。
如果文件是二进制模式的话，打印就会出错。
"""
