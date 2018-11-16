'''
字典排序，使用 collections 模块中的 OrderedDict 类。
在迭代操作的时候它会保持元素被插入时的顺序
'''
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# d['bar'] = 22 #对于一个已经存在的键，重复赋值不会改变键的顺序
for key in d:
    print(key,d[key])

print(d)

import json
print(json.dumps(d))
'''
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。
对于一个已经存在的键的重复赋值不会改变键的顺序。
需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，
因为它内部维护着另外一个链表。 所以如果你要构建一个需要大量
OrderedDict 实例的数据结构的时候
(比如读取100,000行CSV数据到一个 OrderedDict 列表中去)，
那么你就得仔细权衡一下是否使用 OrderedDict
带来的好处要大过额外内存消耗的影响。
'''












