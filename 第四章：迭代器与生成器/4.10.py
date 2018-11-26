#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想在迭代一个序列的同时跟踪正在被处理的元素索引, 使用enumerate()函数

from collections import defaultdict

my_list = ['a', 'b', 'c']

for n, s in enumerate(my_list, start=1):  # start表示开始的计数值
    print(n, s)

# 这种情况在你遍历文件时想在错误消息中使用行号定位时候非常有用：
with open('file.txt', 'r', encoding='utf-8') as f:
    for no, line in enumerate(f):
        if 'error' in line:
            print(f"{no}: {line}")

# 统计一篇文章里面每个单词出现的次数
with open('TOEFL.txt', 'r', encoding='utf-8') as f2:
    word_summard = defaultdict(int)
    for no, line in enumerate(f2):
        words = (w.strip().lower() for w in line.split())
        for word in words:
            word_summard[word] += 1
    print(word_summard)
