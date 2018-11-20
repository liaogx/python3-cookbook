#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from collections import namedtuple

import re

# 字符串令牌解析
# 你有一个字符串，想从左至右将其解析为一个令牌流。
text = 'foo = 23 + 42 * 10'

NAME = r'(?P<NAME>[a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join((NAME, NUM, PLUS, TIMES, EQ, WS)))

# 在上面的模式中，?P<TOKENNAME>用于给一个模式命名，供后面使用。
"""
下一步，为了令牌化，使用模式对象很少被人知道的scanner()方法。这个方法会创建一个
scanner对象，在这个对象上不断的调用match()方法会一步步的扫描目标文本，每步一个匹配。
下面是颜色一个scanner对象如何工作的例子

>>> scanner = master_pat.scanner('foo = 42')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('NAME', 'foo')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('WS', ' ')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('EQ', '=')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('WS', ' ')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('NUM', '42')
>>> scanner.match()
>>>
"""


# 实际使用这种技术的时候，可以很容易的像下面这样将上述代码打包到一个生成器中：
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
