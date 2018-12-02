#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想在关系型数据库中查询、增加或删除记录。

import sqlite3

stocks = [
    ('Google', 100, 490.1),
    ('Apple', 50, 545.75),
    ('Facebook', 150, 7.45),
    ('HPQ', 75, 33.2),
]

db = sqlite3.connect('python3-cookbook.db')
c = db.cursor()
# 创建数据库
# c.execute('create table portfolio (symbol text, shares integer, price real)')
# db.commit()

# 插入多条数据
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# 查询操作
for row in db.execute('select * from portfolio'):
    print(row)
