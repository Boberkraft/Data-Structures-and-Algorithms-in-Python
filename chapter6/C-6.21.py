"""
Show how to use a stack S and a queue Q to generate all possible subsets
of an n-element set T nonrecursively.

Use the stack to store the elements yet to be used to generate
subsets and use the queue to store the subsets generated so far.


Hmmm the truth is that i only used queue
"""

from collections import deque


def gen(T):
    # its basicly more complex and worse gen2
    s = [set()]
    q = deque()
    for el in T:
        s.append({el})
        q.appendleft({el})
        for _ in range(len(q) - 1):
            new = {el}
            old = q.pop()
            new = new.union(old)
            s.append(new)
            q.appendleft(new)
            q.appendleft(old)
    return s


def gen2(T):
    # not using any stack and queue ;/
    s = [set()]
    for el in T:
        for x in range(len(s)):
            s.append(s[x].union({el}))
    return s


s = gen2({1, 2, 3, 4})
s1 = gen({1, 2, 3, 4})

print('Stack:')
print(s, len(s))
print(s1, len(s1))
