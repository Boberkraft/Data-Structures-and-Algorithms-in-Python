"""
Give a simple adapter that implements our queue ADT while using a
collections.deque instance for storage
"""

from collections import deque


class queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def pop(self):
        return self._data.pop()

    def first(self):
        return self._data[0]

