#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化


class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._format = {
            'ymd': '{d.year}-{d.month}-{d.day}',
            'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}-{d.month}-{d.year}'
        }

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        return self._format[format_spec].format(d=self)


d = Date(2018, 12, 12)
print(format(d))
print(format(d, 'mdy'))
