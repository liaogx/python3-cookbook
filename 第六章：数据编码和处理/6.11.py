#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from struct import Struct


# 你想读写一个二进制数组的结构化数据到 Python 元组中

def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.bin', 'wb') as f:
        write_records(records, '<idd', f)

"""
将一个 Python 元组列表写入一个二进制文件，
并使用 struct 将每个元组编码为一个结构体
"""
