#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import base64

# 你需要使用 Base64 格式解码或编码二进制数据。

name = b'liaogx'

a = base64.b64encode(name)
print(a.decode('ascii'))

# 解码
print(base64.b64decode(a))

# Base64 编码仅仅用于面向字节的数据比如字节字符串和字节数组。
