#删除字符串中不需要的字符
#strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作。
# 默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符。比如：
s = ' hello world \n'
print(s.lstrip())
print(s.strip())
print(s.rstrip())
t = '-----hello====='
print(t.strip('-'),t.strip('='),t.lstrip('-'),t.rstrip('='))
#但是需要注意的是去除操作不会对字符串的中间的文本产生任何影响
s = ' hello     world \n'
print(s.strip())
#如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法或者是用正则表达式替换。
import re
print(s.replace(' ',''))
#通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据。
#如果是这样的话，那么生成器表达式就可以大显身手了。比如
'''
with open(filename) as f:
    lines =(line.strip() for line in f)
    for line in lines:
        print(line)

在这里，表达式 lines = (line.strip() for line in f) 执行数据转换操作。
这种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列表中去。
它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。
对于更高阶的strip，你可能需要使用 translate() 方法
'''














