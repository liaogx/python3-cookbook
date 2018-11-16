#通过某关键字排序一个字典列表
'''
通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
'''
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
for i in rows_by_fname:
    print(i)
print('1-------------------------')
rows_by_uid = sorted(rows, key=itemgetter('uid'))
for j in rows_by_uid:
    print(j)
print('2-------------------------')
rows_by_ = sorted(rows, key=itemgetter('lname','fname'))
for k in rows_by_:
    print(k)
print('3-------------------------')
# itemgetter() 有时候也可以用 lambda 表达式代替
rows_by_fname = sorted(rows,key = lambda a:a['fname'])
for n in rows_by_fname:
    print(i)
print('4-------------------------')
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
for m in rows_by_lfname:
    print(m)
print('5-------------------------')
#但是，使用 itemgetter() 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 itemgetter() 方式
#最后，不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数
print(min(rows,key=itemgetter('lname')))
print('6-------------------------')
print(max(rows,key=itemgetter('uid')))