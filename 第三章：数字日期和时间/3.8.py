#分数运算，fractions模块可以被用来执行包含分数的数学运算。比如：
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a+b,a*b,a/b)
c = a * b
print(c.numerator,c.denominator,float(c))
print(c.limit_denominator(8)) ## Limiting the denominator of a value

#Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
'''
在大多数程序中一般不会出现分数的计算问题，但是有时候还是需要用到的。
比如，在一个允许接受分数形式的测试单位并以分数形式执行运算的程序中，
直接使用分数可以减少手动转换为小数或浮点数的工作。
'''











