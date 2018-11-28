#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os

# 你有一个对应于操作系统上一个已打开的 I/O 通道 (比如文件、管道、套接字等)
# 的整型文件描述符，你想将它包装成一个更高层的 Python 文件对象。

fd = os.open('file.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'wt')
f.write('liaogx\n')
f.close()

# 当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭。如果这
# 个并不是你想要的结果，你可以给 open() 函数传递一个可选的 colsefd=False
f = open(fd, 'wt', closefd=False)
