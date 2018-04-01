"""
Give an alternative implementation of the pq sort function, from Code
Fragment 9.7, that accepts a key function as an optional parameter
"""

from HeapPriorityQueue import HeapPriorityQueue


def pg_srot(C, key=lambda a: a):
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(key(element), element)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)

