#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data, indent=4)

print(json.loads(json_str))

"""
总结：
处理字符串
json.dumps() 编码
json.loads() 解码
处理文件
json.dump()  编码
json.load()  解码
"""

# JSON 编码的格式对于 Python 语法而已几乎是完全一样的，除了一些小的差异之
# 外。比如， True 会被映射为 true， False 被映射为 false，而 None 会被映射为 null。下
# 面是一个例子，演示了编码后的字符串效果：

d = {'a': True,
     'b': 'Hello',
     'c': None}
print(json.dumps(d))
