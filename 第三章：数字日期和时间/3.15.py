#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 字符串转换为日期，你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便在上面执行非字符串操作。
from datetime import datetime

text = '2017-1-1'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(y)
print(z)
print(z - y)
# datetime.strptime() 方法支持很多的格式化代码， 比如 %Y 代表4位数年份， %m 代表两位数月份。
# 还有一点值得注意的是这些格式化占位符也可以反过来使用，将日期输出为指定的格式字符串形式。
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)
"""
还有一点需要注意的是， strptime() 的性能要比你想象中的差很多，
因为它是使用纯Python实现，并且必须处理所有的系统本地设置。
如果你要在代码中需要解析大量的日期并且已经知道了日期字符串的确切格式，
可以自己实现一套解析方案来获取更好的性能。
比如，如果你已经知道所以日期格式是 YYYY-MM-DD ，你可以像下面这样实现一个解析函数：
"""


def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))


print(parse_ymd(text))
# 实际测试中，这个函数比datetime.strptime()快7倍多。如果你要处理大量的涉及到日期的数据的话，那么最好考虑下这个方案！
