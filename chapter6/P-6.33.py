"""
Give a complete ArrayDeque implementation of the double-ended queue
ADT as sketched in Section 6.3.2.
"""


class Empty(Exception): pass
class Full(Exception): pass

class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        if maxlen is None:
            self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        else:
            self._data = [None] * maxlen
        self._size = 0
        self.maxlen = maxlen
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

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

    def appendleft(self, e):
        if self.maxlen and self.maxlen == self._size:
            before_first = (self._front - 1) % len(self._data)
            self._front = before_first
            self._data[before_first] = e
        else:
            if self._size == len(self._data):
                self._resize(2 * len(self._data))
            before_first = (self._front - 1) % len(self._data)
            self._front = before_first
            self._data[before_first] = e
            self._size += 1

    def popleft(self):
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

    def rotate(self, times):
        for _ in times:
            last_el = (self._front + self._size - 1) % len(self._data)
            before_first = (self._front - 1) % len(self._data)
            self._data[before_first] = self._data[last_el]
            if before_first != last_el:
                self._data[last_el] = None
            self._front = before_first

    def _resize(self, cap):
        cap = self.maxlen if cap > self.maxlen else cap
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        return str(self._data)

    def __getitem__(self, key):
        if key >= 0:
            where = (self._front + key) % len(self._data)
        else:
            where = (self._front + self._size - abs(key)) % len(self._data)
        return self._data[where]

    def __setitem__(self, key, value):
        if key >= 0:
            where = (self._front + key) % len(self._data)
        else:
            where = (self._front + self._size - abs(key)) % len(self._data)
        self._data[where] = value

    def clear(self):
        self.__init__()

    def count(self, e):
        matches = 0
        for num in range(self._size):
            if self[num] == e:
                matches += 1
        return matches


q = ArrayDeque(maxlen=2)
q.appendleft(1)
print(q)
q.appendleft(2)
print(q)
q.appendleft(3)
print(q)

