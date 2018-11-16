#复数的数学运算
#复数可以用使用函数 complex(real, imag) 或者是带有后缀j的浮点数来指定。比如：
a = complex(2,4)
b = 3 - 5j
print(a,a+b,a/b,abs(a))
print(a.real,a.imag)
#如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块：
import cmath
print(cmath.sin(a),cmath.cos(a),cmath.exp(a))

#Python中大部分与数学相关的模块都能处理复数。 比如如果你使用 numpy ，可以很容易的构造一个复数数组并在这个数组上执行各种操作：
import numpy as np
a = np.array([2+3j,4+5j,6-7j,8+9j])
print(a)
print(a+2)
print(np.sin(a))
#Python的标准数学函数确实情况下并不能产生复数值，
# 因此你的代码中不可能会出现复数返回值。比如：math.sqrt(-1)会报错
import cmath
print(cmath.sqrt(-1))


