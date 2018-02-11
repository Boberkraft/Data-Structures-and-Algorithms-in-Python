"""
Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list.
"""


def check(a, b):
    next = a.next
    while next is not None:
        if next == b:
            return True
        next = next.next
    return False
