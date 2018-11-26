#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。

from itertools import islice


def count(n):
    while True:
        yield n
        n -= 1


for x in islice(count(10), 1, 4):
    print(x)

"""
迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道 (并
且也没有实现索引)。函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍
历并丢弃直到切片开始索引位置的所有元素。然后才开始一个个的返回元素，并直到切
片结束索引位置。
这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。必须考虑到
迭代器是不可逆的这个事实。所以如果你需要之后再次访问这个迭代器的话，那你就得
先将它里面的数据放入一个列表中。
"""
