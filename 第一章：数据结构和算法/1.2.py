#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""
解压可迭代对象赋值给多个变量
"""

data = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = data  # Python2 不支持*赋值

print(name, email, phone_numbers)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

print(uname, homedir, sh)


# 递归实现分割法
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
