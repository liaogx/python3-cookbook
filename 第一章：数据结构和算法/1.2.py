'''
1.1 解压序列赋值给多个变量
1.2 解压可迭代对象赋值给多个变量
'''
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print("foo",x,y)
def do_bar(s):
    print("bar",s)

for tag,*tags in records:
    if tag == 'foo':
        do_foo(*tags)
    elif tag == 'bar':
        do_bar(*tags)












