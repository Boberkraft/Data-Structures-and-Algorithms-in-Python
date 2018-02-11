"""
3 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8).\
"""

from collections import deque
from ArrayQueue import ArrayQueue

d = deque(list(range(10)))
q = ArrayQueue()

for _ in range(len(d)):
    q.enqueue(d.pop())
for _ in range(len(q)):
    d.append(q.dequeue())
print(d)
