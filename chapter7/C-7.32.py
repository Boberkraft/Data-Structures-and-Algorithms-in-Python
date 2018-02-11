"""
Design a forward list ADT that abstracts the operations on a singly linked
list, much as the positional list ADT abstracts the use of a doubly linked
list. Implement a ForwardList class that supports such an ADT
"""


class ForwardList:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next', '_container'  # streamline memory usage

        def __init__(self, element, next, cont):  # initialize node's fields
            self.element = element  # reference to user's element
            self._next = next  # reference to next node


    def __init__(self):
        self._header = None
        self._size = 0
        self._cursor = None

    def forward(self):
        self.cursor = self.cursor._next

    def go_to(self, x):
        self.cursor = x

    def beginning(self):
        return self._header


