#映射名称到序列元素
#addr,joined相当于名称，sub相当于序列
from collections import namedtuple
Subscriber = namedtuple('a',['addr','joined'])
sub = Subscriber('liaogx@liaogx.com','2016--12-25')
print(sub)
print(sub.addr,sub.joined)
'''
命名元组的一个主要用途是将你的代码从下标操作中解脱出来。
因此，如果你从数据库调用中返回了一个很大的元组列表，
通过下标去操作其中的元素， 当你在表中添加了新的列的时候你的代码可能就会出错了。
但是如果你使用了命名元组，那么就不会有这样的顾虑。
为了说明清楚，下面是使用普通元组的代码：
'''
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

#下标操作通常会让代码表意不清晰，并且非常依赖记录的结构。 下面是使用命名元组的版本：
Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

'''
_replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，
它是一个非常方便的填充数据的方法。 你可以先创建一个包含缺省值的原型元组，
然后使用 _replace() 方法创建新的值被更新过的实例。比如：
'''
Stock = namedtuple('Stock',['name','shares','price','date','time'])
#Create a prototype instance
stock_prototype = Stock('',0,0.0,None,None)

#Function to convert a dictionary to a Stock
def dic_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dic_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dic_to_stock(b))



