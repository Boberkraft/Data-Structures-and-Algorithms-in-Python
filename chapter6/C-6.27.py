"""
Suppose you have a stack S containing n elements and a queue Q that is
initially empty. Describe how you can use Q to scan S to see if it contains a
certain element x, with the additional constraint that your algorithm must
return the elements back to S in their original order. You may only use S,
Q, and a constant number of other variables.

Is there any other method to do this?
"""
from collections import deque

q = deque()
s = list(range(10))

size = len(s)
while len(s) > 0:
    x = s.pop()
    if x == 5:
        size -= 1
        continue
    q.appendleft(x)

for _ in range(size):
    s.append(q.pop())

for _ in range(size):
    q.appendleft(s.pop())

for _ in range(size):
    s.append(q.pop())

print(s)
