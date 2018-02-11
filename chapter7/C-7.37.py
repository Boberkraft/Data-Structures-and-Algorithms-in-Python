"""
Implement a function that accepts a PositionalList L of n integers sorted
in nondecreasing order, and another value V, and determines in O(n) time
if there are two elements of L that sum precisely toV. The function should
return a pair of positions of such elements, if found, or None otherwise
"""

from PositionalList import PositionalList


def find_pair(l, v):
    start, end = l.first(), l.last()
    while 1:
        start_val, end_val = start.element(), end.element()
        if end_val > v:
            end = l.before(end)
        elif end_val + start_val < v:
            start = l.after(start)
            if start is None:
                return None
        elif end_val + start_val > v:
            return None
        else:
            print('its a match', end_val, start_val)
            return end_val, start_val


a = PositionalList()
for b in range(0,100,3):
    a.add_last(b)


find_pair(a, 33)