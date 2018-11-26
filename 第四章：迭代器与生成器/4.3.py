#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 使用生成器创建性的迭代模式，你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# 为了使用这个函数， 你可以用for循环迭代它或者使用其他接受一个可迭代对象的函数(比如 sum() , list() 等)。示例如下：
for n in frange(0, 4, 0.5):
    print(n)
print(list(frange(0, 1, 0.11)))


# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作。
# 下面是一个实验，向你展示这样的函数底层工作机制：
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


c = countdown(3)
print(c)
print(next(c), next(c), next(c))

# print(next(c))  #Traceback (most recent call last):   File "<stdin>", line 1, in <module> StopIteration
# 一个生成器的主要特征是它只会回应在迭代中使用到的next操作。一旦生成器函数返回退出，迭代终止。
# 我们在迭代中通常使用的for语句会自动处理这些细节，所以你无需担心。
