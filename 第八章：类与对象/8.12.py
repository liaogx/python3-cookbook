#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


"""
抽象类的一个特点是它不能直接被实例化，抽象类的目的就是让别的类继承它并实现特定的抽象方法
"""


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass
