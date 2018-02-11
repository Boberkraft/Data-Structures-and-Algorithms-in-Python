"""
To better model a FIFO queue in which entries may be deleted before
reaching the front, design a PositionalQueue class that supports the complete
queue ADT, yet with enqueue returning a position instance and support
for a new method, delete(p), that removes the element associated
with position p from the queue. You may use the adapter design pattern
(Section 6.1.2), using a PositionalList as your storage.
"""

from PositionalList import PositionalList


class PositionalQueue:
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def enqueue(self, el):
        return self._data.add_first(el)

    def dequeue(self):
        return self._data.delete(self._data.last())

    def delete(self, pos):
        return self._data.delete(pos)

    def before(self, p):
        return self._data.before(p)

    def after(self, p):
        return self._data.after(p)


a = PositionalQueue()
a.enqueue(1)
x = a.enqueue(2)

a.enqueue(3)
a.enqueue(4)
# [4 3 2 1 ->]
print(a.after(x).element())