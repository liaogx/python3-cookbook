#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os
from time import ctime

# 测试文件是否存在
print(os.path.exists('/etc/passwd'))
print(os.path.exists(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py'))

# 是否是文件
print(os.path.isfile(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py'))

# 是否是目录
print(os.path.isdir(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO'))

# 是否是连接
print(os.path.islink(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO'))

# 真实路径
print(os.path.relpath(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO'))

# 获取文件的大小，上次访问时间，创建时间，修改时间
print(os.path.getsize(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py'))
print(ctime(os.path.getatime(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py')))
print(ctime(os.path.getmtime(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py')))
print(ctime(os.path.getctime(r'C:\Users\liao\PycharmProjects\python3-cookbook\第五章：文件与IO\5.1.py')))
