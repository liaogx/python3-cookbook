#字符串开头或结尾匹配
#检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))
#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给startswith()或者endswith()方法
import os
filename = os.listdir('.')
print([name for name in filename if name.endswith('.py')])
print(any(name.endswith('.py') for name in filename))

from urllib.request import urlopen
def read_data(name):
    if name.startswith('http:','https:','ftp:'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

'''
startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和结尾的检查。
类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅
'''
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

#也可以使用正则表达式的方式实现
import re
a = re.match('http:|https:|ftp:',url)
print(a)
'''
最后提一下，当和其他操作比如普通数据聚合相结合的时候 startswith()和endswith()
方法是很不错的。比如，下面这个语句检查某个文件夹中是否存在指定的文件类型：
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
'''


