"""
Develop a Python implementation of an adaptable priority queue that is
based on an unsorted list and supports location-aware entries

That was quite easy!
i just implemented update and remove methods!
and in add i just return position of an element!
hehe
"""

from PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase


class Empty(Exception):
    pass


class AdaptableUnsortedPriorityQueue(PriorityQueueBase):
    class Locator(PriorityQueueBase._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def update(self, loc, newkey, newval):
        item = loc.element()
        item._value = newval
        item._key = newkey

    def remove(self, loc):
        item = self._data.remove(loc)
        return item._key, item._value

    def _find_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        return self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return item._key, item._value


    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value

q = AdaptableUnsortedPriorityQueue()
a = q.add(5, 5)
c = q.add(2, 2)
b = q.add(3, 3)
print(q.min())
q.update(b, -1, -1)
print(q.min())