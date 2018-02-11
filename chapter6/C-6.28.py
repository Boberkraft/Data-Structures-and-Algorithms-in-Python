"""
Modify the ArrayQueue implementation so that the queue’s capacity is
limited to maxlen elements, where maxlen is an optional parameter to the
constructor (that defaults to None). If enqueue is called when the queue
is at full capacity, throw a Full exception (defined similarly to Empty).
"""


class Empty(Exception): pass


class Full(Exception): pass


class ArrayQueue:
    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._data = [None] * 10
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

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._maxlen == self._size:
            raise Full()
        if self._size == len(self._data):
            if self._maxlen and (len(self._data) * 2) > self._maxlen:
                self._resize(self._maxlen)
            else:
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

    def look(self):
        return self._data


q = ArrayQueue(2)
q.enqueue(1)
q.enqueue(2)
print(q.look())
