"""
There is a simple, but inefficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n−1 times,
where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble sort
function that takes a positional list L as a parameter. What is the running
time of this algorithm, assuming the positional list is implemented with a
doubly linked list?

Its O(N)
"""

from PositionalList import PositionalList


def bubble_sort(l):
    for _ in range(len(l) ):
        cur = l.first()
        x = 1
        while len(l) > x:
            next = l.after(cur)
            if cur.element() > next.element():
                l.swap_position(cur, next)
                x += 1
            x += 1
            cur = l.after(cur)


a = PositionalList()
a.add_last(1)
a.add_last(5)
a.add_last(3)
a.add_last(2)
bubble_sort(a)
# a.swap_position(a.first(),a.last())
# print(len(a))
for x in a:
    print(x)
# [print(x) for x in a]
