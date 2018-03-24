"""
The min method for the UnsortedPriorityQueue class executes in O(n)
time, as analyzed in Table 9.2. Give a simple modification to the class so
that min runs in O(1) time. Explain any necessary modifications to other
methods of the class.

So i will just store the min value and recalculate it 
when add or remove_min is invoked

"""
from PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    def _recalculate_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        self._min = small

    def __init__(self):
        self._data = PositionalList()
        self._min = self._Item(float('inf'), None)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = self._Item(key, value)
        if key > self._min._key:
            self._min = item
        self._data.add_last(item)

    def min(self):
        item = self._min
        return item._key, item._value

    def remove_min(self):
        p = self._min
        item = self._data.delete(p)
        self._recalculate_min()
        return item._key, item._value
