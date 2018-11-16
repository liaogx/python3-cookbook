#在字符串中处理html和xml
import html
s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s,quote=True))
print(html.escape(s,quote=False))
#如果你正在处理的是ASCII文本，并且想将非ASCII文本对应的编码实体嵌入进去，
# 可以给某些I/O函数传递参数 errors='xmlcharrefreplace' 来达到这个目。比如：
s = 'Spicy Jalapeño'
print(s,s.encode('ascii',errors='xmlcharrefreplace'))
#有时候，如果你接收到了一些含有编码值的原始文本，需要手动去做替换，
# 通常你只需要使用HTML或者XML解析器的一些相关工具函数/方法即可。比如：
s= 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

'''
在生成HTML或者XML文本的时候，如何正确的转换特殊标记字符是一个很容易被忽视的细节。
特别是当你使用 print() 函数或者其他字符串格式化来产生输出的时候。
使用像 html.escape() 的工具函数可以很容易的解决这类问题。

如果你想以其他方式处理文本，还有一些其他的工具函数比如xml.sax.saxutils.unescapge()可以帮助你。
然而，你应该先调研清楚怎样使用一个合适的解析器。 比如，如果你在处理HTML或XML文本，
使用某个解析模块比如html.parse或xml.etree.ElementTree已经帮你自动处理了相关的替换细节。
'''













