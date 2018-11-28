#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import gzip
import bz2

# 读写压缩文件，如gzip,bz2格式压缩文件
# gzip 和 bz2 模块可以很容易的处理这些文件。
# 两个模块都为 open() 函数提供了另外的实现来解决这个问题。 比如，为了以文本形式读取压缩文件，可以这样做：

#  gzip compression
with gzip.open('test1.gzip', 'rt', encoding='utf-8') as f1:
    text = f1.read()
    f1.write(text)

# bz2 compression
with bz2.open('test2.bz2', 'rt', encoding='utf-8') as f2:
    text = f2.read()
    f2.write(text)

# 大部分情况下读写压缩数据都是很简单的。但是要注意的是选择一个正确的文件模式是非常重要的。
# 如果你不指定模式，那么默认的就是二进制模式，如果这时候程序想要接受的是文本数据，那么就会出错。
# gzip.open() 和 bz2.open() 接受跟内置的 open() 函数一样的参数， 包括 encoding，errors，newline 等等。
# 当写入压缩数据时，可以使用compresslevel这个可选的关键字参数来指定一个压缩级别。比如：
with gzip.open('test1.zip', 'wt', compresslevel=5) as f3:
    f3.write(text)

# 默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低。
# 最后一点， gzip.open() 和 bz2.open() 还有一个很少被知道的特性，
# 它们可以作用在一个已存在并以二进制模式打开的文件上。比如，下面代码是可行的：

f = open('test1.gzip', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

# 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，管道和内存中文件等。
