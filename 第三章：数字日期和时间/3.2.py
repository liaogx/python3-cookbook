#执行精确的浮点数运算
#浮点数的一个普遍问题是它们并不能精确的表示十进制数。
#并且，即使是最简单的数学运算也会产生小的误差，比如：
a = 1.1
b = 2.2
print(a+b == 3.3)
'''
这些错误是由底层CPU和IEEE 754标准通过自己的浮点单位去执行算术时的特征。
由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。
'''
#如果你想更加精确（并能容忍一定的性能损耗），你可以使用decimal模块
from decimal import Decimal
a = Decimal('1.1')
b = Decimal('2.2')
print(Decimal(a+b))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
    ctx.prec = 50
    print(a/b)

#减法删除以及大数和小数的加分运算所带来的影响。比如：
nums1 = [1.23e+18,1,-1.23e+18]
nums2 = [1.23e+18,-1.23e+18,1]
print(sum(nums1),sum(nums2))
#上面的错误可以利用math.fsum()所提供的更精确计算能力来解决：
import math
print(math.fsum(nums1),math.fsum(nums2))












