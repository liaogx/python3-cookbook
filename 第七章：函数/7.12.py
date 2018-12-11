#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 访问闭包中定义的变量


def sample():
    n = 0

    # 闭包函数
    def func():
        print(f'n={n}')

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # 设置函数的属性
    func.get_n = get_n
    func.set_n = set_n

    return func


f = sample()
f.set_n(10)
print(f.get_n())
