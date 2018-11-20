#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import re

# 字符串匹配和搜索
"""
如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，
比如str.find(),str,endswith(),str.startswith()或者类似的方法：
"""
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'), text.endswith('yeah'), text.find('no'))

# 对于复杂的匹配则需要使用正则表达式和re模块
text1 = '12/29/2016'
text2 = 'Dec 29,2016'

if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else:
    print('No')
if re.match(r'\d+/\d+/\d+', text2):
    print('Yes')
else:
    print('No')

# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
date_pat = re.compile(r'\d+/\d+/\d+')
if date_pat.match(text1):
    print('Yes')
else:
    print('No')

if date_pat.match(text2):
    print('Yes')
else:
    print('No')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(date_pat.findall(text))
"""
在定义正则式的时候，通常会利用括号去捕获分组。
捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来。
"""
date_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = date_pat.match('12/29/2016')
print(m, m.group(0), m.group(1), m.group(2), m.group(3))

month, day, year = m.groups()
print(month, day, year)
print(date_pat.findall(text))

for month, day, year in date_pat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

"""
findall()方法会搜索文本并以列表的形式返回所有的匹配。
如果你想以迭代的方式返回匹配，可以使用finditer()方法来替代
"""
for m in date_pat.finditer(text):
    print('\t', m.groups())

"""
关于正则表达式理论的教程已经超出了本书的范围。 不过，这一节阐述了使用re模块进行匹配和搜索文本的最基本方法。
核心步骤就是先使用 re.compile() 编译正则表达式字符串， 然后使用 match() , findall() 或者 finditer() 等方法。

当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 r'(\d+)/(\d+)/(\d+)' 。
这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。
如果不这样做的话，你必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)' 。

需要注意的是 match() 方法仅仅检查字符串的开始部分。
它的匹配结果有可能并不是你期望的那样。比如：

>>> m = date_pat.match('11/27/2012abcdef')
>>> m
<_sre.SRE_Match object at 0x1005d27e8>
>>> m.group()
'11/27/2012'
>>>
如果你想精确匹配，确保你的正则表达式以$结尾，就像这么这样：

>>> date_pat = re.compile(r'(\d+)/(\d+)/(\d+)$')
>>> date_pat.match('11/27/2012abcdef')
>>> date_pat.match('11/27/2012')
<_sre.SRE_Match object at 0x1005d2750>
>>>
最后，如果你仅仅是做一次简单的文本匹配/搜索操作的话，
可以略过编译部分，直接使用 re 模块级别的函数。比如：

>>> re.findall(r'(\d+)/(\d+)/(\d+)', text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>>
但是需要注意的是，如果你打算做大量的匹配和搜索操作的话，最好先编译正则表达式，然后再重复使用它。
模块级别的函数会将最近编译过的模式缓存起来，因此并不会消耗太多的性能，
但是如果使用预编译模式的话，你将会减少查找和一些额外的处理损耗。
"""
