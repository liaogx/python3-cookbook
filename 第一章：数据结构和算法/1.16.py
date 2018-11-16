#过滤序列元素
#你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

#过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
# 比如，在一列数据中你可能不仅想找到正数，而且还想将不是正数的数替换成指定的数。
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])
print([n if n > 0 else 0 for n in mylist])

'''
另外一个值得关注的过滤工具就是 itertools.compress() ，
它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
然后输出 iterable 对象中对应选择器为 True 的元素。
当你需要用另外一个相关联的序列来过滤某个序列的时候，
这个函数是非常有用的。 比如，假如现在你有下面两列数据：
'''
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
a = list(compress(addresses,more5))
print('\t',a)




















