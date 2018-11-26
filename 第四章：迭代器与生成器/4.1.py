#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 手动遍历迭代器，你想遍历一个可迭代对象的所有元素，但不是想使用for循环
# 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。 比如，下面的例子手动读取一个文件中的所有行：


def manual_iter():
    with open('file.txt', 'r', encoding='utf-8') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


manual_iter()
# 通常来讲， StopIteration 用来指示迭代的结尾。 然而，如果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。 下面是示例：
print('\n==============')
with open('file.txt', 'r', encoding='utf-8') as f2:
    while True:
        line2 = next(f2, None)
        if line2 is None:
            break
        print(line2, end='')

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

G = (sum(row) for row in M)  # create a generator of row sums
# Run the iteration protocol
print('\n============')
print(next(G))
print(next(G))
print(next(G))
