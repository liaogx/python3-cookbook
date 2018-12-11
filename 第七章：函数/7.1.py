#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'


def avg(first, *rest):  # first是位置参数，也叫必选参数
    return first + sum(rest) / len(rest) + 1


def b(x, *args, y, **kwargs):
    """
    :param x: 必选参数
    :param args: 任意参数
    :param y: 命名关键字参数
    :param kwargs: 关键字参数
    :return:
    """
    pass
