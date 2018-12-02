#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import pandas

rats = pandas.read_csv('rats.csv', skipfooter=1)

rats['Current Activity'].unique()

"""
Pandas 是一个拥有很多特性的大型函数库，我在这里不可能介绍完。但是只要你
需要去分析大型数据集合、对数据分组、计算各种统计量或其他类似任务的话，这个函
数库真的值得你去看一看
"""
