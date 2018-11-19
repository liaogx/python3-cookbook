#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""
怎样实现一个按优先级排序的队列？并且在这个队列上面每次pop操作总是返回优先级最高的那个元素
"""
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0  # 确保同等优先级的元素正确排序

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)


q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 5)
q.push('spam0', 4)
q.push('spam1', 4)
q.push('grok', 2)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
"""
这一小节我们主要关注 heapq 模块的使用。
函数 heapq.heappush() 和 heapq.heappop() 分别在队列 _queue 上插入和删除第一个元素，
并且队列_queue保证第一个元素拥有最小优先级(1.4节已经讨论过这个问题)。
heappop() 函数总是返回”最小的”的元素，这就是保证队列pop操作返回正确元素的关键。
另外，由于push和pop操作时间复杂度为O(log N)，其中N是堆的大小，因此就算是N很大的时候它们运行速度也依旧很快。
在上面代码中，队列包含了一个 (-priority, index, item) 的元组。
优先级为负数的目的是使得元素按照优先级从高到低排序。
这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
index 变量的作用是保证同等优先级元素的正确排序。
通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
而且， index变量也在相同优先级元素比较的时候起到重要作用。
"""
