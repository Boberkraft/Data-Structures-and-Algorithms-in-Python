"""
Implement a function, with calling syntax max(L), that returns the maximum
element from a PositionalList instance L containing comparable
elements.
what
"""

from PositionalList import PositionalList

l = PositionalList()

def max(l):
    if len(l) > 1:
        p = l.first()
        ex = p.element
        for _ in range(len(l)-1):
            p = l.after(p)
            if ex < p.element:
                ex = p.element
        return ex

l.add_first(1)
l.add_first(2)
l.add_first(3)
l.add_first(4)
print(max(l))