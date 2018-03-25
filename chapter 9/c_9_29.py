"""
Reimplement the SortedPriorityQueue using a Python list. Make sure to
maintain remove min’s O(1) performance.

Ideally i should use deque, and it can be implelented using list.

The only minus in deque is that its hard to insert elements into, but you can ignore that.

"""
from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = 0
        while walk < len(self._data) and newest < self._data[walk]:
            walk += 1
        if walk == 0:
            self._data.insert(0, newest)
        else:
            self._data.insert(walk, newest)

    def min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        item = self._data[-1]
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        item = self._data.pop()
        return item._key, item._value

if __name__ == '__main__':
    x = SortedPriorityQueue()
    x.add(30, '30')
    x.add(20, '20')
    x.add(80, '80')
    x.add(40, '40')
    x.add(80, '80')

    print()
    print(x.remove_min())