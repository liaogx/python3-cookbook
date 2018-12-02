#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


# 问题：你想使用一个 Python 字典存储数据，并将它转换成 XML 格式

from collections import OrderedDict
from xml.etree.ElementTree import Element, tostring


def dict2xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'Google', 'shares': 100, 'price': 490.1}
d = OrderedDict(**s)  # 保持元素的顺序

xml = dict2xml('profile', d)  # 转换结果是一个 Element 实例。

print(tostring(xml))
