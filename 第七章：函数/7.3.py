#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 给函数增加元信息


def add(x: int, y: int) -> int:
    """
    :param x:
    :param y:
    :return:
    """
    return x + y


"""
python 解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟
没有加注解之前的效果也没有任何差距
"""
