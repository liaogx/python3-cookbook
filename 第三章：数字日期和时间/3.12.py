#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# 基本的日期和时间转换
# 执行不同时间单位的转换和计算，可以使用datatime模块。为了表示一个时间段，可以创建一个timedelta实例，如：

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days, c.seconds, c.seconds / 3600)  # c.total_seconds()如何计算的？？？
# 如果你想表示指定的日期和时间，先创建一个datetime实例然后使用标准的数学运算来操作它们。比如：

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
print((b - a).days)

print(datetime.today() + timedelta(minutes=10))
# 在计算的时候需要注意datetime会自动处理闰年。比如：
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print((a - b).days)

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

"""
对大多数基本的日期和时间处理问题， datetime 模块以及足够了。
如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等，可以考虑使用 dateutil模块
许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替。
但是，有一点需要注意的就是，它会在处理月份(还有它们的天数差距)的时候填充间隙。看例子最清楚：
"""

print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))
b = datetime(2012, 12, 21)
print(b - a)

d = relativedelta(months=+2, days=+28)
print(d.months, d.days)
