"""
Given a class, PriorityQueue, that implements the minimum-oriented priority
queue ADT, provide an implementation of a MaxPriorityQueue class
that adapts to provide a maximum-oriented abstraction withmethods add,
max, and remove max. Your implementation should not make any assumption
about the internal workings of the original PriorityQueue class,
nor the type of keys that might be used.
"""

from HeapPriorityQueue import HeapPriorityQueue

class MaxPriorityQueue:
    class _Key:
        def __init__(self, k):
            self.k = k

        def __lt__(self, other):
            return self.k > other.k

        def __gt__(self, other):
            return self.k < other.k

    def __init__(self):
        self._queue = HeapPriorityQueue()

    def add(self, key, value):
        self._queue.add(self._Key(key), value)

    def max(self):
        k, v = self._queue.min()
        return k.k, v

    def remove_max(self):
        k, v = self._queue.remove_min()
        return k.k, v


def test():
    """
    >>> x = MaxPriorityQueue()
    >>> x.add(4, 4)
    >>> x.add(5, 5)
    >>> x.add(2, 2)
    >>> x.add(6, 6)
    >>> x.add(2, 2)
    >>> x.remove_max()
    (6, 6)
    """

