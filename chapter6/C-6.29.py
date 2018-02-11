"""
In certain applications of the queue ADT, it is common to repeatedly
dequeue an element, process it in some way, and then immediately enqueue
the same element. Modify the ArrayQueue implementation to include
a rotate( ) method that has semantics identical to the combination,
Q.enqueue(Q.dequeue( )). However, your implementation should
be more efficient than making two separate calls (for example, because
there is no need to modify size).

personally i think its useless

"""


class Empty(Exception): pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
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

    def rotate(self):
        last_el = (self._front + self._size - 1) % len(self._data)
        before_first = (self._front - 1) % len(self._data)
        self._data[before_first] = self._data[last_el]
        if before_first != last_el:
            self._data[last_el] = None
        self._front = before_first

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


q = ArrayQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
q.rotate()
print(q)