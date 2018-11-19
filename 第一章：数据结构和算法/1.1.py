#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""
解压序列赋值给多个变量，即解压赋值
"""
data = ['liao', 'gao xiang', 18, (1999, 11, 17)]  # 没错，我只有18岁

first_name, last_name, age, (year, month, day) = data

print(first_name, last_name, age, year, month, day)
