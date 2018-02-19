"""
Implement the tree ADT using a linked structure as described in Section
8.3.3. Provide a reasonable set of update methods for your tree.
"""

from Tree import Tree


class LinkedTree(Tree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, childs = None):
            self._element = element
            self._parent = parent
            if childs is None:
                self._children = []
            else:
                self._children = list(childs)

    class Position(Tree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

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

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def _add_child(self, p, el):
        node = self._validate(p)
        self._size += 1
        node._children.append(self._Node(el, node))
        return self.Position(self, el)

    def is_root(self, p):
        node = self._validate(p)
        return node is self._root

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield child


