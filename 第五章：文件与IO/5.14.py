#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os
import sys

# 你想使用原始文件名执行文件的 I/O 操作也就是说文件名并没有经过系统默认编码去解码或编码过。
print(sys.getfilesystemencoding())

with open('jalape\xf1o.txt', 'wb') as f:
    f.write(b'Spicy!')

print(os.listdir(b'.'))

"""
正如你所见，在最后两个操作中，当你给文件相关函数如 open() 和 os.listdir()
传递字节字符串时，文件名的处理方式会稍有不同。
"""
