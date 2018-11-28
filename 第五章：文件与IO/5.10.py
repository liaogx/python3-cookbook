#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 内存映射的二进制文件，你想内存映射一个二进制文件到一个可变字节数组中，
# 目的可能是为了随机访问它的内容或者是原地做些修改。
# 使用mmap模块来内存映射文件。下面是一个工具函数，向你演示了如何打开一个文件并以一种便捷方式内存映射这个文件。

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RANDOM)
    return mmap.mmap(fd, size, access=access)


# 为了使用这个函数，你需要有一个已创建并且内容不为空的文件。
# 下面是一个例子，教你怎样初始创建一个文件并将其内容扩充到指定大小：
size = 10000
with open('data.bin', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')
