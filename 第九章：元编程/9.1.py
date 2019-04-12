#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import time


def tail(file):
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:  # 跳过空行
                time.sleep(0.1)  # 保证实时读取
                continue
            yield line


def grep(lines, text):
    for line in lines:
        if text in line:
            yield line


f = tail('test.py')
lines = grep(f, 'python')
for line in lines:
    print(line)
