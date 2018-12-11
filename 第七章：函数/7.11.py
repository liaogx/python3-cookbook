#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from queue import Queue
from functools import wraps


# 内联回调函数
def apply_sync(func, args, *, callback):
    result = func(*args)
    callback(result)


class Async(object):

    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)  # 使用wraps不改变被装饰函数的属性(name或者docstring)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)  # put表示入队列
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_sync(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


if __name__ == '__main__':
    import multiprocessing

    pool = multiprocessing.Pool()
    apply_sync = pool.apply_async

    test()
