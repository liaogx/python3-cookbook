#保留最后n个元素
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# Example use on a file
# with open(r'../../cookbook/somefile.txt') as f:
#     for line, prevlines in search(f, 'python', 5):
#         for pline in prevlines:
#             print(pline, end='')
#         print(line, end='')
#         print('-' * 20)

d = deque()
d.append(1)
d.append("2")
print(len(d))
print(d[0],d[1])
d.extendleft([0])
print(d)
d.extend([6, 7, 8])
print(d)

d2 = deque('12345')
print(len(d2))
d2.popleft()
print(d2)
d2.pop()
print(d2)

d3 = deque(maxlen=2)
d3.append(1)
d3.append(2)
print(d3)
d3.append(3)
print(d3)








