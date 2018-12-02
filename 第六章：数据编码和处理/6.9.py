#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import binascii
import base64

# 你想将一个十六进制字符串解码成一个字节字符串或者将一个字节字符串编码成
# 一个十六进制字符串。

s = b'liaogx'

print(binascii.b2a_hex(s))  # 将字节字符串转换成十六进制

s2 = b'68656C6C6F'

print(base64.b16decode(s2))  # 将十六进制字符串编码变成字节字符串

# 还有一点需要注意的是编码函数所产生的输出总是一个字节字符串。如果想强制
# 以 Unicode 形式输出，你需要增加一个额外的界面步骤。例如：
print(base64.b16decode(s2).decode('ascii'))
