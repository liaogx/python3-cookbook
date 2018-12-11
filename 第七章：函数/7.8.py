#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import math
from functools import partial


# 减少可调用对象的参数个数

def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)  # 把a = 1固定了

s1(2, 3, 4)

s2 = partial(spam, d=42)

s2(1, 2, 3)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


# 假设你有一个点的列表来表示 (x,y) 坐标元组。你可以使用下面的
# 函数来计算两点之间的距离：

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


# 示例一：现在假设你想以某个点为基点，根据点和基点之间的距离来排序所有的这些点
pt = (5, 5)
points.sort(key=partial(distance, pt))  # partial(distance, pt)把第一个参数p1固定成了(5, 5)
print(points)


# 示例二： partial() 通常被用来微调其他库函数所使用的回调函数的参数。例
# 如，下面是一段代码，使用 multiprocessing 来异步计算一个结果值，然后这个值被
# 传递给一个接受一个 result 值和一个可选 logging 参数的回调函数
def output_result(result, log=None):
    if log is None:
        log.debug(f"Got {result}")


def add(x, y):
    return x + y


if __name__ == "__main__":
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
