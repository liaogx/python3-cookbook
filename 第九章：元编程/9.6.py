#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import time
import gevent


def task():
    gevent.sleep(1)


if __name__ == "__main__":
    start = time.time()
    coroutins = []
    for _ in range(1000000):
        coroutins.append(gevent.spawn(task))
    gevent.joinall(coroutins)

    print(time.time() - start)
