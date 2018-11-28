#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import io
import urllib.request

# 如何增加或改变一个已打开文件的编码

u = urllib.request.urlopen('https://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')  # 或者是其它编码
text = f.read()

print(text)
