#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""
保留最后n个元素
"""
from collections import deque


def search(file, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for l in file:
        if pattern in l:
            yield l, previous_lines  # 使用yield表达式的生成器函数，将搜索过程的代码和搜索结果的代码解耦
        previous_lines.append(l)


with open(b'file.txt', mode='r', encoding='utf-8') as f:
    for line, prevlines in search(f, 'Python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')

d = deque()
d.append(1)
d.append("2")
print(len(d))
print(d[0], d[1])
d.extendleft([0])
print(d)
d.extend([6, 7, 8])
print(d)

d2 = deque('12345')
print(len(d2))
d2.popleft()
print(d2)
d2.pop()
print(d2)

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N)
d3 = deque(maxlen=2)
d3.append(1)
d3.append(2)
print(d3)
d3.append(3)
print(d3)
