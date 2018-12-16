#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 使用Mixins扩展类功能，如添加日志、唯一性设置、类型检查


def LoggedMapping(cls):
    """ 第二种方式：使用类装饰器"""
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict(dict):
    pass


"""
对于混入类，有几点需要记住。首先是，混入类不能直接被实例化使用。其次，混
入类没有自己的状态信息，也就是说它们并没有定义 __init__() 方法，并且没有实例
属性。这也是为什么我们在上面明确定义了 __slots__ = () 。
"""
