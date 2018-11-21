#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import random

# 随机选择，想从一个序列中抽取若干元素，或者想生成几个随机数
# random模块有大量的函数用来产生随机数和随机选择元素。比如，要想从一个序列中随机的抽取一个元素，可以使用random.choice():


values = [1, 2, 3, 4, 5, 6]
print(random.choice(values), random.choice(values), random.choice(values), random.choice(values), random.choice(values), random.choice(values))
# 为了提取出N个不同元素的样本用来做进一步的操作，可以使用 random.sample() ：
print(random.sample(values, 2), random.sample(values, 2), random.sample(values, 2), random.sample(values, 2))
# 如果你仅仅只是想打乱序列中元素的顺序，可以使用 random.shuffle() ：
random.shuffle(values)
print(values)

# 生成随机整数，请使用 random.randint() ：
print(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

# 为了生成0到1范围内均匀分布的浮点数，使用 random.random() ：
print(random.random(), random.random(), random.random())

# 如果要获取N位随机位(二进制)的整数，使用 random.getrandbits()
print(random.getrandbits(10))  # 二进制的10位

# random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子。比如：
print(random.seed())  # Seed based on system time or os.urandom()
print(random.seed(12345))  # Seed based on integer given
print(random.seed(b'bytedata'))  # Seed based on byte data

"""
除了上述介绍的功能，random模块还包含基于均匀分布、高斯分布和其他分布的随机数生成函数。
比如， random.uniform() 计算均匀分布随机数， random.gauss() 计算正态分布随机数。 对于其他的分布情况请参考在线文档。
在 random 模块中的函数不应该用在和密码学相关的程序中。如果你确实需要类似的功能，可以使用ssl模块中相应的函数。
比如， ssl.RAND_bytes() 可以用来生成一个安全的随机字节序列。
"""
print(random.uniform(a=10, b=20))  # [a, b) or [a, b]之间生成一个均匀分布随机数
print(random.gauss(mu=1, sigma=3.14))  # 计算正态分布随机数
