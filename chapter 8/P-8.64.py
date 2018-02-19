"""
Implement the binary tree ADT using the array-based representation described
in Section 8.3.2.
"""
from BinaryTree import BinaryTree


class ArrayBinaryTree(BinaryTree):
    class _Node:
        def __init__(self, el, index):
            self._element = el
            self._index = index

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) == type(other) and self._node is other._node

    def __init__(self):
        self._size = 0
        self._root = None
        self._container = []

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _update_index(self, index):
        if index >= len(self):
            self._container += [None] * (index - len(self) + 1)

    def _make_position(self, index):
        return self.Position(self, self._container[index]) if self._container[index] is not None else None

    def _left_index(self, index):
        return 2 * index + 1

    def _right_index(self, index):
        return 2 * index + 2

    def _parent_index(self, index):
        return index // 2

    def left(self, p):
        node = self._validate(p)
        key = self._left_index(node._index)
        self._update_index(key)
        return self._make_position(key)

    def right(self, p):
        node = self._validate(p)
        key = self._right_index(node._index)
        self._update_index(key)
        return self._make_position(key)

    def parent(self, p):
        node = self._validate(p)
        key = self._right_index(node._index)
        self._update_index(key)
        if key >= 0:
            return self._make_position(key)
        else:
            return None

    def root(self):
        return self._container[0]

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Root exists")
        self._container = self._Node(e, 0)
        return self._make_position(0)

    def _add_left(self, p, e):
        node = self._validate(p)
        key = self._left_index(node._index)
        self._container[key] = self._Node(e, key)
        self._update_index(key)
        return self._make_position(key)

    def _add_right(self, p, e):
        node = self._validate(p)
        key = self._right_index(node._index)
        self._container[key] = self._Node(e, key)
        self._update_index(key)
        return self._make_position(key)
