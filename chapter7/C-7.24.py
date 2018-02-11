"""
Give a complete implementation of the stack ADT using a singly linked
list that includes a header sentinel.

its so wrong that i do not even know on what end add this header
"""


class Empty(Exception):
    pass


class LinkedStack:
    class _Note:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = self._Note(None, None)
        self._tail = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head.next = self._Note(e, self._head.next)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head.next.element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head.next.element
        self._head.next = self._head.next.next
        self._size -= 1
        return answer

    def __repr__(self):
        s = '['
        h = self._head.next
        for _ in range(len(self)):
            s += str(h.element) + ','
            h = h.next
        s += ']'
        return s


a = LinkedStack()
a.push(1)
print(a._head.next.element)
a.push(2)
print(a._head.next.next.element)
a.push(3)
print(a)
