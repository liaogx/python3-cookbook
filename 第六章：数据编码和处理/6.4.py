#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from xml.etree.ElementTree import iterparse


# 增量式解析大型xml文件，通过迭代器和生成器使用尽可能少的内存

def parse_and_remove(filename, path):
    path_part = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)

    tag_stack, elem_stack = [], []

    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_part:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


for d in parse_and_remove('sample.xml', 'row/row'):
    address, status, latitude, longitude = map(lambda x: d.findtext(x), ('address', 'status', 'latitude', 'longitude'))
    print(f"{address}----{status}\t\t{latitude}----{longitude}")
