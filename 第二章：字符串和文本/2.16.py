#以指定宽度格式化字符串
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
#下面演示使用 textwrap 格式化字符串的多种方式：
import textwrap
print('①',textwrap.fill(s,70))
print('②',textwrap.fill(s,35))
print('③',textwrap.fill(s,50,initial_indent = '    '))
print('④',textwrap.fill(s,50,subsequent_indent = '    '))

#textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端大小的时候。
# 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。比如：
import os
# a = os.get_terminal_size().columns #次语句将报错，无法获取终端大小，原因不明












