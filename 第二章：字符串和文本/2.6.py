#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import re

# 字符串忽略大小写的搜索替换
# 为了在文本操作时忽略大小写，你需要在使用re模块的时候给这些操作提供re.IGNORECASE标志参数。比如：

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('pyThon', text, flags=re.IGNORECASE))
print(re.sub('pyThon', 'snAke', text, flags=re.IGNORECASE))


# 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致。
# 为了修复这个，你可能需要一个辅助函数，就像下面的这样：
def matchcase(word):
    def replace(m):  # 这里的m是什么? 以及后面的m.group()是什么?
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
"""
对于一般的忽略大小写的匹配操作，简单的传递一个 re.IGNORECASE 标志参数就已经足够了。
但是需要注意的是，这个对于某些需要大小写转换的Unicode匹配可能还不够，
参考2.10小节，在正则表达式中使用Unicode
"""
