#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


import pickle
import time
import threading

# 你需要将一个 Python 对象序列化为一个字节流，以便将它保存到一个文件、存储
# 到数据库或者通过网络传输它。

# 1.将对象保存到文件中
data = 'my file content'
f = open('pickle_file.txt', 'wb')
pickle.dump(data, f)
f.close()

# 2.将对象转换为字符串
s = pickle.dumps(data)
print(s)

# 3.从字节流中恢复对象
print(pickle.loads(s))

"""
有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象，
比如打开的文件，网络连接，线程，进程，栈帧等等。用户自定义类可以通过提供
__getstate__() 和 __setstate__() 方法来绕过这些限制。如果定义了这两个方法，
pickle.dump() 就会调用 __getstate__() 获取序列化的对象。类似的，__setstate__()
在反序列化时被调用。为了演示这个工作原理，下面是一个在内部定义了一个线程但仍
然可以序列化和反序列化的类：
"""


class Countdown(object):
    """可以被序列化和反序列化的类"""

    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.deamon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minux', self.n)
            self.n -= 1
            time.sleep(0.1)

    def __getstate__(self):
        return self.n

    def __setstate__(self, state):
        self.__init__(state)


c = Countdown(30)

f2 = open('file3.txt', 'wb')
pickle.dump(c, f2)
f2.close()

f3 = open('file3.txt', 'rb')
pickle.load(f3)
