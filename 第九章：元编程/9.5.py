#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import time
from threading import Thread


def task():
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    threads = []
    for _ in range(1000000):
        t = Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(time.time() - start)
