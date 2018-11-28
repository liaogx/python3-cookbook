#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os


# 关于打印不合法的文件名

def bad_filename(filename):
    """打印编码位置的文件名"""
    return repr(filename)[1:-1]


files = os.listdir('.')

# 科学有正确的文件名打印操作
for f in files:
    try:
        print(f)
    except UnicodeEncodeError:
        print(bad_filename(f))
