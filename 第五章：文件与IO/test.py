#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# def manual_iter():
#     with open('test.txt') as f:
#         try:
#             while True:
#                 line = next(f, None)
#                 if not line:
#                     break
#                 print(line, end='')
#         except StopIteration:
#             pass
#
#         else:
#             print('\n', 'bad')
#
#         finally:
#             print('\n', 'good')
#
# manual_iter()
# class Node(object):
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
# root = Node(0)
# child1 = Node(1)
# child2 = Node(2)
# root.add_child(child1)
# root.add_child(child2)
# print(root, type(child1), child2)
#
# # Outputs Node(1), Node(2)
# for ch in root:
#     print(ch)
#
# def frang(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
#
# for n in frang(1, 2, 0.1):
#     print(n)
#
# # print(list(frang(0, 1, 0.125)))
#
# def generator(n):
#     try:
#         while n > 0:
#             yield n
#             n -= 1
#     except StopIteration:
#         pass
#
#     finally:
#         print('done')
#
# num = generator(3)
# print(next(num))
# print(next(num))
# print(next(num))
# class Test(object):
#     def prt(sef):
#         print(sef)
#         print(sef.__class__)
#
# t = Test()
# Test.prt(t)

# a = [1, 2, 3, 4, 5]
# for x in reversed(a):
#     print(x)

# with open('test.txt') as f:
#     for line in reversed(list(f)):
#         print(line, end='')

# 自定义类实现正反向迭代
# class CountDown(object):
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1
#
#     def __reversed__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
# for x in CountDown(30):
#     print(x)
#
# for y in reversed(CountDown(30)):
#     print(y)

# from collections import deque
# dq = deque(maxlen=10)
# with open('test.txt', encoding='utf8') as f:
#     for line_number, content in enumerate(f, start=1):
#         dq.append((line_number, content))
# print(dq)
#
# from collections import deque
#
#
# class LineHistory(object):
#
#     def __init__(self, lines, hislen=3):
#         self.lines = lines
#         self.history = deque(maxlen=hislen)
#
#     def __iter__(self):
#         for line_number, line_ in enumerate(self.lines, 1):  # 文件也可以使用enumerate函数
#             self.history.append((line_number, line_))  # 向deque队列中添加元组数据
#             yield line_  # 返回每一行的数据
#
#     def clear(self):
#         self.history.clear()  # 清空deque队列

# with open('test.txt', encoding='utf8') as f:
#     lines = LineHistory(f)
#     for line in lines:
#         if 'python' in line:
#             for lineno, hline in lines.history:
#                 print('{}:{}'.format(lineno, hline), end='')
#     # 或者：
#     # it = iter(lines)
#     # print(next(it), end='')
#     # print(next(it), end='')
#     # print(next(it), end='')

# class Singleton(object):
#
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super(Singleton, cls).__new__(cls)
#         return cls.__instance
#
#     def __init__(self, number):
#         self.number = number
#
# s1 = Singleton(2)
# s2 = Singleton(6)
# print(s1, s1.number)
# print(s2, s2.number)


# l1 = ['liaO', 'GAO', 'xianG']
#
# def f(name):
#     first = name[0].upper()
#     rest = name.lower()[1:]
#     return first + rest
#
# l2 = list(map(f, l1))
# print(l2)

# li = []
#
# for x in range(10):
#
#     def func():
#
#         return x
#
#     li.append(func)
#
# print(li)
# print(li[0]())


# def outer():
#     count = 10
#
#     def inner():
#         nonlocal count
#         count = 20
#         print('inner:', count)
#     inner()
#     print('outer:', count)
#
# outer()


# class C(object):
#     def __init__(self, a):
#         print('C', a)
#
#
# class D(C):
#     def __init__(self, a):
#         super(D, self).__init__(a)
#
# D(8)
#
# from enum import Enum, unique
# # 第一个参数 Month 表示的是该枚举类的类名，第二个tuple参数，表示的是枚举类的值
# # Enum的成员均为单例（Singleton），并且不可实例化，不可更改
# Month = Enum('Month', ('January', 'February', 'March', 'April', 'May', 'June',
#                        'July', 'August', 'September', 'October', 'November', 'December'))
#
# print(Month, type(Month))  # 枚举类的类名
# print(Month.__members__)  # 与Month.__members__.items()结果相同
# print(Month.__members__.keys())
# print(Month.__members__.values())
# print(Month.__members__.items())
# for name, member in Month.__members__.items():
#     print(name, member, member.value)
# print(Month, Month.January, Month.January.value)
#
#
# @unique  # @unique 装饰器可以帮助我们检查保证没有重复值
# class User(Enum):
#     a = 11
#     b = 22
#     c = 33
#
# print(User.a.name, User.a.value, User.a, type(User.a))  # name是关键字？
# print(User.__members__)
# print(User.__members__.items())
# print(User.__members__.values())
# print(User.__members__.keys())

# result = []
# for x in range(10):
#     for y in range(5):
#         if x * y > 10:
#             result.append((x, y))
#
# print(result)
#
# def func():
#     for i in range(5):
#         for j in range(5):
#             if i != j:
#                 for k in range(5):
#                     if j != k:
#                         yield (i, j, k)
#
# a = func()
# print(next(a))
# print(next(a))
#
# print(__name__)
#
#
# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property  # 将一个方法用属性的方式来访问
#     def area1(self):
#         return 3.14 * self.radius ** 2
#
#     def area2(self):
#         return 3.14 * self.radius ** 2
#
# c = Circle(4)
# print(c.radius)
# print(c.area1)
# print(c.area2())
# print(c.__dict__)
#
#
# class Parrot(object):
#     def __init__(self):
#         self._voltage = 100000
#
#     @property
#     def voltage(self):
#         """Get the current voltage."""
#         return self._voltage
#
#     @voltage.setter
#     def voltage(self, new_value):
#         self._voltage = new_value
#
#
# if __name__ == "__main__":
#     # instance
#     p = Parrot()
#     # similarly invoke "getter" via @property
#     print(p.voltage)
#     # update, similarly invoke "setter"
#     p.voltage = 12
#     print(p.voltage)


# class Normal(object):
#     def __init__(self):
#         self.__x = None
#
#     @property
#     def xx(self):
#         print('getx(): self.__x=', self.__x)
#         return self.__x
#
#     @xx.setter
#     def xx(self, value):
#         self.__x = value
#         print('setx()')
#
#     @xx.deleter
#     def xx(self):
#         print('delx()')
#         del self.__x
#
#
# tN = Normal()
# tN.xx = 10
# tN.xx
# del tN.xx


# class Example(object):
#
#     def __init__(self):
#         self.__x = None
#
#     @property
#     def xx(self):
#         print('Getter: ', self.__x)
#
#     @xx.setter
#     def xx(self, value):
#         self.__x = value
#         print('setter')
#
#     @xx.deleter
#     def xx(self):
#         del self.__x
#         print('deltter')
#
# a = Example()
# a.xx = 10
# a.xx
# del a.xx

# 不使用中间变量交换a, b两个数的值
# a = 11
# b = 22
# # 方法一，使用加减法
# print(a, b)
# a = a + b
# b = a - b
# a = a - b
# print(a, b)
#
# # 方法二，使用异或运算
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)
#
# from collections import deque
# string = 'liaogx'
#
# def string1(s):
#     return s[::-1]
#
#
# def string2(s):
#     pass
#
#
# def string3(s):
#     if len(s) == 1:
#         return s
#     return string3(s[1:]) + s[0]
#
#
# def string4(s):
#     d = deque()
#     d.extendleft(s)
#     return ''.join(d)
#
#
# def string5(s):
#     l = len(s)
#     temp = ''
#     for i in range(l):
#         temp = temp + ''.join(list(s)[l-i-1])
#     return temp
#
#
# def string6(s):
#     return ''.join(s[i] for i in range(len(s)-1, -1, -1))
#
#
# def string7(s):
#     d = deque()
#     for i in s:
#         d.appendleft(i)
#     return ''.join(d)
#
#
# print(string1(string))
# print(string2(string))
# print(string3(string))
# print(string4(string))
# print(string5(string))
# print(string6(string))
# print(string7(string))
#
# # 转换一个矩阵
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print([row[0] for row in a])
# # print([row[1] for row in a])
# # print([row[2] for row in a])
# print([[row[col] for row in a] for col in range(len(a[0]))])
#
# a = [1, 2, 33]
# b = [11, 2, 3]
#
# import random
# list1 = [x for x in range(10, 0, -2)]
# list2 = [x for x in range(0, 10, 3)]
#
#
# def qsort(L):
#     if len(L) < 2:
#         return L
#     pivot_element = random.choice(L)
#     smaller = [i for i in L if i < pivot_element]
#     larger = [i for i in L if i > pivot_element]
#     return qsort(smaller) + [pivot_element] + qsort(larger)
#
# print(set(qsort(list1 + list2)))

# """
# 静态函数(@staticmethod): 即静态方法,主要处理与这个类的逻辑关联, 如验证数据;
# 类函数(@classmethod):即类方法, 更关注于从类中调用方法, 而不是在实例中调用方法, 如构造重载;
# 成员函数: 实例的方法, 只能通过实例进行调用;
#
# """
# class A(object):
#
#     _g = 1
#
#     def foo(self, x):
#         print('executing foo(%s, %s)' % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print('executing class_foo(%s, %s)' % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print('executing static_foo(%s)' % ( x))
#
# a = A()
# a.foo(1)
# a.class_foo(1)
# A.class_foo(1)
# a.static_foo(1)
# A.static_foo('hi')
# print(a.foo)
# print(a.class_foo)
# print(a.static_foo)
#
# """
# 具体应用:
# 比如日期的方法, 可以通过实例化(__init__)进行数据输出;
# 可以通过类方法(@classmethod)进行数据转换;
# 可以通过静态方法(@staticmethod)进行数据验证;
# """
#
# class Date(object):
#     day = 0
#     month = 0
#     year = 0
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def display(self):
#         return "{0}*{1}*{2}".format(self.day, self.month, self.year)
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date = cls(day, month, year)
#         return date
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
#
# date1 = Date(12, 11, 2014)
# date2 = Date.from_string('11-13-2014')
# print(date1.display())
# print(date2.display())
# print(date2.is_date_valid('11-10-2014'))
# print(Date.is_date_valid('11-13-2014'))


# class A(object):
#
#     _dict = dict()
#
#     def __new__(cls, *args, **kwargs):
#         if 'key' in cls._dict:
#             print('exists')
#             return A._dict['key']
#         else:
#             print('NEW')
#             return object.__new__(cls)
#
#     def __init__(self):
#         print('init')
#         A._dict['key'] = self
#
# a1 = A()
# a2 = A()

# class Foo(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Foo object is %s' % self.name
#
#     __repr__ = __str__
#
# a = Foo('liagox')
# print(a)
# print(str(a))
#
#
# class Fib(object):
#
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):  # 返回迭代器本身
#         return self
#
#     def __next__(self):  # 返回容器的下一个元素
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __getitem__(self, item):
#         x, y = 1, 1
#         for i in range(item):
#             x, y = y, x + y
#         return x
#
# fib = Fib()
# for i in fib:
#     if i > 100:
#         break
#     print(i)
#
# print(fib[5], type(fib))  # fib数列第6个数为8


# class Fib2(object):
#     def __getitem__(self, item):
#         a, b = 1, 1
#         if isinstance(item, slice):
#             start, stop, step = item.start, item.stop, item.step
#             print(step)
#             L = []
#             for i in range(stop):
#                 if i >= start:
#                     if i in range(start, stop, step):
#                         L.append(a)
#                 a, b = b, a + b
#                 # return L  #       思考：如果reuturn写在for循环中，会是什么后果？
#             return L
#         if isinstance(item, int):
#             for _ in range(item):
#                 a, b = b, a + b
#             return a
#
# fib2 = Fib2()
# print(fib2[1:10:2])


# class Point1(object):
#
#     def __init__(self):
#         self.coordinate = {}
#
#     def __getitem__(self, item):  # 使对象(类的实例)可以像列表一样使用下标访问,默认返回None
#         return self.coordinate.get(item)
#
#     def __setitem__(self, key, value):
#         self.coordinate[key] = value        # 此处不用return
#
#     def __delitem__(self, key):
#         del self.coordinate[key]
#         print('del %s' % key)
#
#     def __len__(self):
#         return len(self.coordinate)
#
#     def __str__(self):
#         return 'coordinate is: %s' % self.coordinate
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#
#     def __getattr__(self, item):  # 当访问不存在的属性时调用
#         pass
#
#     __repr__ = __str__
#
# p = Point1()
# p['a'] = 11
# p['b'] = 22
# print(p, len(p))
# del p['a']
# print(p, len(p))
# print(p.coordinate)
# print(p())      # 对象后面加()执行call方法
#
#
# print('← +++++++++ →')
#
#
# class _List(object):
#
#     def __init__(self, _list):
#         self._list = _list
#
#     def __getitem__(self, item):
#         if isinstance(item, int) or isinstance(item, slice):
#             return self._list[item]
#
# c = _List([_ for _ in range(10)])
# print(c['a'])

# class Point3(object):
#
#     __slots__ = ('x', 'y', 'z')  # 限制类能添加的属性，同时会限制__dict__
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __getattr__(self, item):
#         raise AttributeError(u'没有这个属性了')
#
#     def __setattr__(self, *args, **kwargs):
#         print('setattr')
#         return object.__setattr__(self, *args, **kwargs)
#
#     def __delattr__(self, *args, **kwargs):
#         print('delattr')
#         return object.__delattr__(self, *args, **kwargs)
#
# p = Point3(3, 4)  # 相当于p.x = 3 p.y = 4,会两次调用setattr方法
# print(p.x)
# del p.y
# # print(p.y)  #触发raise异常
# p.z = 5
# # print(p.__dict__)
#
#
# class Exam1(object):
#     def __init__(self, score):
#         self._score = score
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if 0 <= value <= 100:
#             self._score = value
#         else:
#             raise EOFError(u'请设置正确分数')
#
# e1 = Exam1(59)
# print(e1.get_score())
# e1.set_score(80)
# print(e1.get_score())
#
#
# class Exam2(object):
#
#     def __init__(self, score):
#         self._score = score
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if 0 <= value <= 100:
#             self._score = value
#         else:
#             raise EOFError(u'请设置正确分数')
#
# e2 = Exam2(69)
# print(e2.score)
# e2.score = 99
# print(e2.score)
#
#
# class Animal(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print('My name is %s' % self.name)
#
#
# class Dog(Animal):
#
#     def greet(self):
#         super(Dog, self).greet()        # super的一个最常见用法可以说是在子类中调用父类的初始化方法
#         print('A dog')
#
# a = Dog('doge')
# a.greet()

# import time
# # start_time = time.time()
# # for a in range(0,1001):
# #     for b in range(0, 1001):
# #         for c in range(0, 1001):
# #             if (a+b+c==1000) and (a**2 + b**2 == c**2):
# #                 print('a={0}, b={1}, c={2}'.format(a, b, c))
# # end_time = time.time()
# # print(u'共计用时：{0}'.format(end_time - start_time))
#
#
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0, 1001-a):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print('a={0}, b={1}, c={2}'.format(a, b, c))
# end_time = time.time()
# print(u'共计用时：{0}'.format(end_time - start_time))

from timeit import Timer


def t1():
    li = [_ for _ in range(10000)]


def t2():
    li = list(_ for _ in range(10000))


def t3():
    li = []
    for i in range(10000):
        # li = li + [i]       # Python中'+='被优化，相当于直接在li上append
        li += [i]


def t4():
    li = []
    for i in range(10000):
        li.append(i)


def t5():
    li = []
    for i in range(10000):
        li.extend([i])


def t6():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer1 = Timer("t1()", "from __main__ import t1")
timer2 = Timer("t2()", "from __main__ import t2")
timer3 = Timer("t3()", "from __main__ import t3")
timer4 = Timer("t4()", "from __main__ import t4")
timer5 = Timer("t5()", "from __main__ import t5")
timer6 = Timer("t6()", "from __main__ import t6")
print('列表推导式用时：', timer1.timeit(1000))
print('tuple转list用时：', timer2.timeit(1000))
print('list相加用时：', timer3.timeit(1000))
print('append用时：', timer4.timeit(1000))
print('extend用时：', timer5.timeit(1000))
print('insert用时：', timer6.timeit(1000))
