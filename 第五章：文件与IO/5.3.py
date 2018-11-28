#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 使用其他分隔符或行终止符打印，你想使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符。
# 可以使用在 print() 函数中使用 sep 和 end 关键字参数，以你想要的方式输出。比如：
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=' - ', end='!!\n')
# 使用 end 参数也可以在输出中禁止换行。比如：
for x in range(10):
    print(x, end=' ')
# 当你想使用非空格分隔符来输出数据的时候，给 print() 函数传递一个 sep 参数是最简单的方案。
# 有时候你会看到一些程序员会使用 str.join() 来完成同样的事情。比如：
print(', '.join(('ACME', '50', '91.5')))

# str.join() 的问题在于它仅仅适用于字符串。这意味着你通常需要执行另外一些转换才能让它正常工作。比如：
row = ('ACME', 50, 91.5)
print(' , '.join(str(x) for x in row))

# 你当然可以不用那么麻烦，仅仅只需要像下面这样写：
print(*row, sep=' , ')
