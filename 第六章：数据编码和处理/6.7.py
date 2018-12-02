#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


# 你想解析某个 XML 文档，文档中使用了 XML 命名空间。

class XMLNamespaces(object):
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


"""
最后一点，如果你要处理的 XML 文本除了要使用到其他高级 XML 特性外，还要
使用到命名空间，建议你最好是使用 lxml 函数库来代替 ElementTree 。例如， lxml
对利用 DTD 验证文档、更好的 XPath 支持和一些其他高级 XML 特性等都提供了更
好的支持。这一小节其实只是教你如何让 XML 解析稍微简单一点。
"""
