#用Shell通配符匹配字符串
'''
你想使用Unix Shell中常用的通配符去匹配文本字符串
fnmath模块提供了两个函数--fnmath()和fnmatchcase(),可以用来实现这样的匹配
'''
from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txT'))
#fnmatch()函数使用底层操作系统的大小写敏感规则（不同的操作系统是不一样的，如Mac电脑上严格匹配大小写，Windows上不匹配大小写）来匹配模式
print(fnmatch('foo.txt','?oo.txt'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])

#这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的。 比如，假设你有一个街道地址的列表数据
address = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in address if fnmatchcase(addr,'* ST')])
print([addr for addr in address if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])

'''
fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
'''







