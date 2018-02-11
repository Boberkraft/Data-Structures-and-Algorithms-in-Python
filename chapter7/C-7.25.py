"""
Give a complete implementation of the queue ADT using a singly linked
list that includes a header sentinel.
"""

class Empty(Exception):
    pass


class LinkedQueue:
    class _Note:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._header = self._Note(None, None)
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head.element

    def enqueue(self, e):
        newest = self._Note(e, None)
        if self.is_empty():
            self._header.next = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._header.next.element
        self._header.next = self._header.next.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def __repr__(self):
        s = '['
        h = self._header.next
        for _ in range(len(self)):
            s += str(h.element) + ','
            h = h.next
        s += ']'
        return s

q = LinkedQueue()
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
print(q)