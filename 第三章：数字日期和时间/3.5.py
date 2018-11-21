#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import struct

# 字节到大整数的打包与解包，比如：
# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。
# 假设你的程序需要处理一个拥有128位长的16个元素的字节字符串。比如：
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# 为了将bytes解析为整数，使用int.from_bytes()方法，并向下面这样指定字节顺序：
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
# 为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面这样指定字节数和字节顺序：
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))  # 16代表什么意思？

hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

# 字节顺序规则(little或big)仅仅指定了构建整数时的字节的低位高位排列方式。 我们从下面精心构造的16进制数的表示中可以很容易的看出来：
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))
# 如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。 如果需要的话，
# 你可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
# 如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。
# 如果需要的话，你可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
x = 523 ** 23
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1

print(nbytes)
print(x.to_bytes(nbytes, 'little'))

fp = open('file.txt', 'wb')
# 按照上面的格式将数据写入文件中
# 这里如果string类型的话，在pack函数中就需要encode('utf-8')
name = b'lily'
age = 18
sex = b'female'
job = b'teacher'

# int类型占4个字节
fp.write(struct.pack('4si6s7s', name, age, sex, job))
fp.flush()
fp.close()

# 将文件中写入的数据按照格式读取出来
fd = open('file.txt', 'rb')
# 21 = 4 + 4 + 6 + 7
print(struct.unpack('4si6s7s', fd.read(21)))
fd.close()
