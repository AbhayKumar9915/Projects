# A Deque is the optimized list (Doubly ended queue)
from collections import deque

queue = deque([1, 2, 'Abhay', True, False])

print(queue)
queue.append('RightAppend')
print(queue)
queue.appendleft('LeftAppend')
print(queue)
print(queue.count(0))
queue.pop()
print(queue)
queue.popleft()
print(queue)
