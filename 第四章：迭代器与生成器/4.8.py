#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。

from itertools import dropwhile, islice

# 使用dropwhile时，你给它传递一个函数对象和一个可迭代对象。
# 它会返回一个迭代器对象，丢弃原有序列中直到函数返回 Flase 之前的所有元素，然后返回后面所有元素。

# 跳过开始部分的注释行，注意是开始部分，后面有注释行的话依然会输出
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in dropwhile(lambda l: l.startswith("#"), f):
        print(line, end=' ')

# 这个例子是基于根据某个测试函数跳过开始的元素。如果你已经明确知道了要跳
# 过的元素的个数的话，那么可以使用 itertools.islice() 来代替。比如：
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# None 参数指定了你要获取从第 3 个到最
# 后的所有元素，如果 None 和 3 的位置对调，意思就是仅仅获取前三个元素恰恰相反，
# (这个跟切片的相反操作 [3:] 和 [:3] 原理是一样的)。
