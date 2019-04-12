#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


class Fib(object):
    """"""

    def __init__(self, n):
        self.pre = 0
        self.cur = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0:
            self.pre, self.cur = self.cur, self.pre + self.cur
            return self.cur
        else:
            raise StopIteration


f = Fib(10)
print([i for i in f])
