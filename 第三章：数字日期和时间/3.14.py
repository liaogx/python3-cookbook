#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 计算当前月份的日期范围

import calendar

from datetime import datetime, date, timedelta


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


# 有了这个就可以很容易的在返回的日期范围上面做循环操作了：
first_day, last_day = get_month_range()
print(first_day, last_day)

while first_day < last_day:
    print(first_day)
    first_day += timedelta(days=1)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2016, 1, 1), datetime(2016, 2, 1), timedelta(hours=6)):
    print(d)
