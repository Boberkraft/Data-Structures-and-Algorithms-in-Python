"""
The introduction of Section 6.1 notes that stacks are often used to provide
“undo” support in applications like a Web browser or text editor. While
support for undo can be implemented with an unbounded stack, many
applications provide only limited support for such an undo history, with a
fixed-capacity stack. When push is invoked with the stack at full capacity,
rather than throwing a Full exception (as described in Exercise C-6.16),
a more typical semantic is to accept the pushed element at the top while
“leaking” the oldest element from the bottom of the stack to make room.
Give an implementation of such a LeakyStack abstraction, using a circular
array with appropriate storage capacity. This class should have a public
interface similar to the bounded-capacity stack in Exercise C-6.16, but
with the desired leaky semantics when full.

Its like deque with limited capacity! why i cannot just use it ;/
"""
class Empty(Exception):
    pass


class Full(Exception):
    pass

class NoMaxlen(Exception):
    pass

class LeakyStack:
    DEFAULT_CAPACITY = 5

    def __init__(self, maxlen):
        if maxlen:
            self._data = [None] * maxlen
        else:
           raise NoMaxlen
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

    def push(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

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

a = LeakyStack(3)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a)