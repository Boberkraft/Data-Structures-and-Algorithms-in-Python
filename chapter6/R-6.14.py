"""
Repeat the previous problem using the deque D and an initially empty
stack S.
"""

from collections import deque
from ArrayStack import ArrayStack

d = deque(list(range(10)))
q = ArrayStack()

for _ in range(len(d)):
    q.push(d.pop())
for _ in range(len(q)):
    d.appendleft(q.pop())
print(d)
