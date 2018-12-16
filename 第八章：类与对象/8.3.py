#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 让对象支持上线文管理协议，定义__exit__和__enter__方法

import socket
from collections import deque
from functools import partial

"""
定义一个Socket TCP网络连接，是的连接和关闭使用with语句自动完成
"""


class LazyConnection(object):

    def __init__(self, address, family=socket.AF_INET, type_=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type_
        self.sock = None

    def __enter__(self):
        """建立socket连接"""
        if self.sock is not None:
            raise RuntimeError('Already connected!')
        self.sock = socket.socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        关闭socket连接
        :param exc_type: 异常类型
        :param exc_val: 异常值
        :param exc_tb: 追溯信息
        :return:
        """
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed

"""
当需要嵌套使用with语句的时候
"""


class LazyConnection2(object):

    def __init__(self, address, family=socket.AF_INET, type_=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type_
        self.connections = deque()

    def __enter__(self):
        """建立socket连接"""
        sock = socket.socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        关闭socket连接
        :param exc_type: 异常类型
        :param exc_val: 异常值
        :param exc_tb: 追溯信息
        :return:
        """
        self.connections.pop().close()


conn = LazyConnection2(('www.python.org', 80))  # 允许嵌套使用with语句建立多个连接
with conn as s1:
    pass
    with conn as s2:
        pass

"""
在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是
很普遍的。这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正
确运行。例如，如果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生
死锁。通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免
这些问题，因为 __exit__() 方法可以让你无需担心这些了。
"""
