"""
Give a complete ArrayDeque implementation of the double-ended queue
ADT as sketched in Section 6.3.2.
"""


class Empty(Exception): pass


class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Quue is empty')
        return self._data[self._front]

    def pop(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def append_left(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        before_first = (self._front - 1) % len(self._data)
        self._front = before_first
        self._data[before_first] = e
        self._size += 1

    def pop_left(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def append(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        return str(self._data)

q = Deque()
q.append_left(1)
q.append_left(2)
q.append_left(3)
print(q)
q.append(5)
q.append(6)
q.append(7)
print(q)
q.pop()
q.pop_left()
print(q)