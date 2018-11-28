#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os
from fnmatch import fnmatch

path = os.path.dirname(os.path.abspath(__file__))
all_ = os.listdir(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO')

# 获取所有的文件
all_files = [file for file in all_ if os.path.isfile(os.path.join(path, file))]
print(all_files)

# 获取所有的目录
all_dirs = [dir for dir in all_ if os.path.isdir(os.path.join(path, dir))]
print(all_dirs)

# 列出目录下所有的python文件
pyfiles = [py for py in all_ if fnmatch(py, '*.py')]
print(pyfiles)

# 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也是很有用的
