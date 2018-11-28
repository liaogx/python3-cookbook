#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os

# 你需要使用路径名来获取文件名，目录名，绝对路径等等

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

# 获取文件名
print(os.path.basename(path))

# 获取文件夹路径
print(os.path.dirname(path))

# split分割
print(os.path.split(path))
print(os.path.splitdrive(path))
print(os.path.splitext(path))
