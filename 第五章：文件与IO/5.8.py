#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 固定大小记录的文件迭代
# 你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代
# 通过下面这个小技巧使用 iter 和 functools.partial() 函数：
from functools import partial

RECORD_SIZE = 32
with open('file.txt', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

print(int('12345'))
print(int('11111', base=8))

foo = partial(int, base=8)  # 生成一个固定参数的新函数
print(foo('111111'))
print('++++++++++++++++++')


def int2(x, base=2):
    return int(x, base)


print(int2('1111'))

# iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个
# 标记值，它会创建一个迭代器。这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止。
