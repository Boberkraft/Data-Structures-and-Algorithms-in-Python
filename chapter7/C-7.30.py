"""
Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT
using a singly linked list for storage

Its bad optylamized

"""


class Full(Exception):
    pass
class Empty(Exception):
    pass

class LeakyStack:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self, size=10):
        self._head = None
        self._size = 0
        self._max_size = size

    def push(self, el):
        self._head = self._Node(el, self._head)
        if self._size == self._max_size:
            if self._max_size > 1:
                prev = self._head
                next = prev._next
                while 1:
                    if next is None:
                        prev._next = None
                        break
                    prev = next
                    next = next._next
            else:
                self._head._next._next = None

        else:
            self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty('The stack is empty')
        val = self._head._element
        self._head = self._head._next
        return val

a = LeakyStack(3)
a.push(1)
a.push(2)
a.push(3)
a.push(3)
a.push(3)
print(a.pop())
print(a.pop())
print(a.pop())