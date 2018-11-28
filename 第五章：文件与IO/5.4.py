#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 读写字节数据，你想读写二进制文件，比如图片，声音应文件等等。
# 使用模式为rb或wb的open()函数来读取或写入二进制数据。比如：
# Read the entire file as a single byte string
with open('file.txt', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('file.txt', 'wb') as f:
    f.write(b'Hello World!')
# 在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串。
# 类似的，在写入的时候，必须保证参数是以字节形式对外暴露数据的对象(比如字节字符串，字节数组对象等)。
# 在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。
# 特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串。比如：

# Byte string
b = b'HelloWorld'
for c in b:
    print(c)

# 如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作。比如：
with open('file.txt', 'rb') as f:
    data1 = f.read(16)
    text = data1.decode('utf-8')
with open('file.txt', 'wb') as f:
    text2 = 'Hello World'
    f.write(text2.encode('utf-8'))
