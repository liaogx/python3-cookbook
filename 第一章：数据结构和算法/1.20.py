#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 合并多个字典和映射
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# 现在假设你必须在两个字典中执行查找操作
# (比如先从 a 中找，如果找不到再在 b 中找)。
# 一个非常简单的解决方案就是使用collections模块中的ChainMap类
from collections import ChainMap

c = ChainMap(a, b)

print(c)
a['x'] = 11  # 使用ChainMap时，原字典做了更新，这种更新会合并到新的字典中去

print(c)  # 按顺序合并两个字典
print(c['x'])
print(c['y'])
print(c['z'])
"""
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。
然后，这些字典并不是真的合并在一起了，
ChainMap 类只是在内部创建了一个容纳这些字典的列表
并重新定义了一些常见的字典操作来遍历这个列表。
大部分字典操作都是可以正常使用的，比如：
>>> len(c)
3
>>> list(c.keys())
['x', 'y', 'z']
>>> list(c.values())
[1, 2, 3]
>>>
如果出现重复键，那么第一次出现的映射值会被返回。
因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
"""

# 对于字典的更新或删除操作影响的总是列中的第一个字典。
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']将出现报错

# ChainMap对于编程语言中的作用范围变量（比如globals,locals等）
# 是非常有用的。事实上，有一些方法可以使它变得简单：
values = ChainMap()  # 默认会创建一个空字典
print('\t', values)
values['x'] = 1
values = values.new_child()  # 添加一个空字典
values['x'] = 2
values = values.new_child()
values['x'] = 30
# values = values.new_child()
print(values, values['x'])  # values['x']输出最后一次添加的值
values = values.parents  # 删除上一次添加的字典
print(values['x'])
values = values.parents
print(values)

"""
作为ChainMap的替代，你可能会考虑使用 update() 方法将两个字典合并。比如：
这样也能行得通，但是它需要你创建一个完全不同的字典对象(或者是破坏现有字典结构)。
同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。
"""
a = {'x': 1, 'y': 2}
b = {'y': 2, 'z': 3}
merge = dict(b)
merge.update(a)
print(merge['x'], merge['y'], merge['z'])
a['x'] = 11
print(merge['x'])


def f(x): return x % 2 != 0 and x % 3 != 0


a = filter(f, range(5, 25))
