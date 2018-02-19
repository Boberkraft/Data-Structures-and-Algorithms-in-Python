"""
The memory usage for the LinkedBinaryTree class can be streamlined by
removing the parent reference from each node, and instead having each
Position instance keep a member, path, that is a list of nodes representing
the entire path from the root to that position. (This generally saves memory
because there are typically relatively few stored position instances.)
Reimplement the LinkedBinaryTree class using this strategy
"""

from BinaryTree import BinaryTree
from copy import copy

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node, path):
            self._container = container
            self._node = node
            self._path = path

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node, path):
        return self.Position(self, node, path) if node is not None else None

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        if len(p._path) == 0:
            # its a root
            return None
        last = p._path[-1]
        new_path = copy(p._path)[:-1]
        return self._make_position(last, p)

    def left(self, p):
        node = self._validate(p)
        new_path = copy(p._path).append(node)
        return self._make_position(node._left, new_path)

    def right(self, p):
        node = self._validate(p)
        new_path = copy(p._path).append(node)
        return self._make_position(node._right, new_path)

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root, [])

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child Exists')
        self._size += 1
        node._left = self._Node(e)
        new_path = copy(p._path).append(node)
        return self._make_position(node._left, new_path)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child Exists')
        self._size += 1
        node._right = self._Node(e)
        new_path = copy(p._path).append(node)
        return self._make_position(node._right, new_path)
