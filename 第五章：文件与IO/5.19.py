#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import tempfile
from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile

# 你需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。

with TemporaryFile('w+t', encoding='utf-8') as f:
    f.write('liaogx\n')
    f.write('Python')
    f.seek(0)
    print(f.read())
"""
TemporaryFile() 的第一个参数是文件模式，通常来讲文本模式使用 w+t ，二进
制模式使用 w+b 。这个模式同时支持读和写操作，在这里是很有用的，因为当你关闭
文件去改变模式的时候，文件实际上已经不存在了
"""

# 命名的临时文件，且关闭文件时不删除
with NamedTemporaryFile('w+t', encoding='utf-8', delete=False) as f:
    f.write(f.name)

# 创建临时目录

with TemporaryDirectory() as dirname:
    print('dirname is: ', dirname)

# 通常来讲，临时文件在系统默认的位置被创建，比如 /var/tmp 或类似的地方。为
# 了获取真实的位置，可以使用 tempfile.gettempdir() 函数
print(tempfile.gettempdir())

# 所有和临时文件相关的函数都允许你通过使用关键字参数 prefix 、 suffix 和 dir
# 来自定义目录以及命名规则。比如：

f = NamedTemporaryFile(prefix='temp', suffix='.log', encoding='utf-8', delete=False,
                       dir=r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO')
