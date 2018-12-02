#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from xml.etree.ElementTree import parse
from urllib.request import urlopen

# 从一个简单的xml文档中提取数据

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()

"""
xml.etree.ElementTree.parse() 函数解析整个 XML 文档并将其转换成一个文
档对象。然后，你就能使用 find() 、 iterfind() 和 findtext() 等方法来搜索特定的
XML 元素了。这些函数的参数就是某个指定的标签名，例如 channel/item 或 title
"""
