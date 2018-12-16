#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想实现一个状态机或者是在不同状态下执行操作的对象，但是又不想在代码中
# 出现太多的条件判断语句。


class Connection(object):
    """普通方案，好多个判断语句，效率低下"""

    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Noe open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


"""
如果代码中出现太多的条件判断语句的话，代码就会变得难以维护和阅读。这里的
解决方案是将每个状态抽取出来定义成一个类。
"""
