#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import csv
from collections import namedtuple

# 通过writer对象写入CSV文件
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]
with open('stocks.csv', 'w', encoding='utf-8') as f3:
    f_csv = csv.writer(f3)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 通过DictWriter对象写入CSV文件
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]
with open('stocks.csv', 'w', encoding='utf-8') as f4:
    f_csv = csv.DictWriter(f4, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

with open('stocks.csv', 'r', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        if r:
            row = Row(*r)
            print(row.Symbol, row.Price)  # 使用命名元组

# 将数据读取到一个字典序列中
with open('stocks.csv', 'r', encoding='utf-8') as f2:
    f_csv = csv.DictReader(f2)
    for row in f_csv:
        print(row)

# 说白了，本小节就是要讲解csv模块中4个函数的用法：reader, writer, DictReader, DictWriter

# csv 产生的数据都是字符串类型的，它不会做任何
# 其他类型的转换。如果你需要做这样的类型转换，你必须自己手动去实现
col_types = [str, float, str, str, float, int]
with open('stocks.csv', 'r', encoding='utf-8') as f5:
    f_csv = csv.reader(f5)
    headers = next(f_csv)
    for row in f_csv:
        if row:  # 跳过[], 空行
            row = tuple(convert(value) for convert, value in zip(col_types, row))
            print(row)
