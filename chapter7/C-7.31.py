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
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    class _Position:
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            self._container = container
            self._node = node

    def _make_pos(self, node):
        return self._Position(self, node)

    def __init__(self):
        self._header = self._Node(None, None, self)
        self._size = 0

    def insert_after(self, pos, el):
        if pos._node == self._header._next:
            pos._node = self._header
        if pos._container == self:
            node = pos._node
            self._size += 1
            prev = node._next
            node._next = self._Node(el, prev, self)
            return self._make_pos(node._next)

    def erase_after(self, pos):
        if pos._container == self:
            node = pos._node
            self._size -= 1
            ans = node._next.element
            next = node._next._next
            node._next = next
            return ans

    def beginning(self):
        return self._make_pos(self._header._next)


a = ForwardList()
a.insert_after(a.beginning(), 1)
