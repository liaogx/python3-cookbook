#固定大小记录的文件迭代
#你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代
#通过下面这个小技巧使用 iter 和 functools.partial() 函数：
from functools import partial
RECORD_SIZE = 32
with open('test.txt','rb') as f:
    records = iter(partial(f.read,RECORD_SIZE),b'')
    for r in records:
        pass

print(int('12345'))
print(int('11111',base=8))
import functools
foo = functools.partial(int,base=8) #生成一个固定参数的新函数
print(foo('111111'))
print('++++++++++++++++++')
def int2(x,base=2):
    return int(x,base)
print(int2('1111'))

list = [1,2,3]

for i in iter(list):
    print(i)

'''
实在是看不下去了，概念完全都不懂
迭代器？生成器？类？对象？属性？方法？
'''




