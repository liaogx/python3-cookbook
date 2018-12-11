#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from urllib.request import urlopen


# 通过闭包将单方法的类转换成函数


class UrlTemplate(object):

    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# 转换成函数

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


# 一般来说，当对象中只有一个方法时，这时使用闭包是更好的选择。
# 这比用类来实现更优雅，此外装饰器也是基于闭包的一中应用场景。

"""
所有函数都有一个 __closure__属性，如果这个函数是一个闭包的话，那么它返回的是一个由 cell 对象 组成的元组对象。
cell 对象的cell_contents 属性就是闭包中的自由变量。
"""
url = urltemplate('liaogx')
print(url.__closure__)
print(url.__closure__[0].cell_contents)  # 访问闭包中的自由变量
