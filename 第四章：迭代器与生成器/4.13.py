#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import os
import fnmatch
import gzip
import bz2
import re

# 问题，你想以数据管道 (类似 Unix 管道) 的方式迭代处理数据。比如，你有个大量的数据
# 需要处理，但是不能将它们一次性放入内存中。可以使用生成器实现数据处理管道
""" 文件格式如下
foo/
access-log-012007.gz
access-log-022007.gz
access-log-032007.gz
...
access-log-012008
bar/
access-log-092007.bz2
...
access-log-022008
"""


def gen_find(filepat, top):
    """
    查找符合Shell正则匹配的目录树下的所有文件名
    :param filepat: shell正则
    :param top: 目录路径
    :return: 文件绝对路径生成器
    """
    for path, _, filenames in os.walk(top):
        for file in fnmatch.filter(filenames, filepat):
            yield os.path.join(path, file)


def gen_opener(filenames):
    """
    每打开一个文件生成就生成一个文件对象，调用下一个迭代前关闭文件
    :param filenames: 多个文件绝对路径组成的可迭代对象
    :return: 文件对象生成器
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'r', encoding='utf-8')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'r', encoding='utf-8')
        else:
            f = open(filename, 'r', encoding='utf-8')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    将输入序列拼接成一个很长的行序列。
    :param iterators:
    :return: 返回生成器所产生的所有值
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    使用正则匹配行
    :param pattern: 正则匹配
    :param lines: 多行
    :return: 结果生成器
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == "__main__":
    filenames = gen_find('*.py', '.')
    files = gen_opener(filenames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)liaogaoxiang', lines)
    for line in pylines:
        print(line)
