#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


def print_result(result):
    print(f'Got: {result}')


def add(x, y):
    return x + y


def apply_sync(func, args, *, callback):
    result = func(*args)
    callback(result)


apply_sync(add, (2, 3), callback=print_result)


# 方法一：为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数。

class ResultHandler(object):

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f'[{self.sequence}] Got: {result}')


r = ResultHandler()
apply_sync(add, (2, 3), callback=r.handler)
apply_sync(add, (20, 30), callback=r.handler)


# 方法二：作为类的替代，可以使用一个闭包捕获状态值

def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f'[{sequence}] Got: {result}')

    return handler


handler = make_handler()
apply_sync(add, (200, 300), callback=handler)


# 方法三：使用协程实现，通过send方法作为回调函数

def send_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f'[{sequence}] Got: {result}')


handler2 = send_handler()
next(handler2)
apply_sync(add, (2000, 3000), callback=handler2.send)
apply_sync(add, (2000, 3000), callback=handler2.send)