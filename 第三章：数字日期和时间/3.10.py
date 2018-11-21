#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 矩阵与线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等等
# NumPy库有一个矩阵对象可以用来解决这个问题

import numpy as np
import numpy.linalg

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print("该矩阵为：\n", m)
print("该矩阵的逆矩阵为：\n", m.T)

v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)  # 矩阵相乘
print('-------------------------------------')

# 可以在numpy.linalg子包中找到更多的操作函数，比如：
print(numpy.linalg.det(m))
print(numpy.linalg.eigvals(m))
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
