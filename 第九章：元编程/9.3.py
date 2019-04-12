#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

for i in range(10):
    print(i)
    # break  # 遇到break则else不执行
else:
    print('done')

import gevent
from gevent import socket

urls = ['www.google.com', 'www.liaogx.com', 'www.google.com']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)
print([job.value for job in jobs])
