#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 带有外部状态的生成器函数，你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。


from collections import deque


class LineHistory(object):

    def __init__(self, lines, hisline=3):
        self.lines = lines
        self.history = deque(maxlen=hisline)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            yield line
            self.history.append((lineno, line))

    def clear(self):
        self.history.clear()

    def copy(self):
        self.history.copy()


with open('file.txt', 'r', encoding='utf-8') as f:
    lines = LineHistory(f)
    for l in lines:
        if 'Python' in l:
            for lineno, line in lines.history:
                print("{}: {}".format(lineno, line))
