#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import time


# 递归算法
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + f(n - 2)


# 非递归算法
def f2(n):
    a, b = -1, 1
    for i in range(n + 1):
        a, b = b, a + b

    return b


# if __name__ == '__main__':
#     start = time.time()
#     f(10000)
#     end = time.time()
#     print(end - start)
print(f(1000))