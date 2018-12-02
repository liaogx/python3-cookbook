#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from xml.etree.ElementTree import parse, Element

# 问题：你想读取一个 XML 文档，对它最一些修改，然后将结果写回 XML 文档。

doc = parse('sample.xml')
root = doc.getroot()

e = Element('test')
e.text = 'This is a test'
root.insert(0, e)

doc.write('sample.xml', xml_declaration=True)

"""
修改一个 XML 文档结构是很容易的，但是你必须牢记的是所有的修改都是针对
父节点元素，将它作为一个列表来处理。例如，如果你删除某个元素，通过调用父节
点的 remove() 方法从它的直接父节点中删除。如果你插入或增加新的元素，你同样使
用父节点元素的 insert() 和 append() 方法。还能对元素使用索引和切片操作，比如
element[i] 或 element[i:j]
"""
