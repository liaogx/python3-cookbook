#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 使用命名的关键字参数


def recv(maxsize, *, block):
    print(f"I received a message, the size is {maxsize}, it's block is {block}'")


# recv(2014, True)  #  TypeError
recv(1024, block=True)
