"""
We can simplify parts of our LinkedBinaryTree implementation if we
make use of of a single sentinel node, referenced as the sentinel member
of the tree instance, such that the sentinel is the parent of the real root of
the tree, and the root is referenced as the left child of the sentinel. Furthermore,
the sentinel will take the place of None as the value of the left
or right member for a node without such a child. Give a new implementation
of the update methods delete and attach, assuming such a
representation.
"""


def _delete(self, p):
    node = self._validate(p)

    if self.num_children(p) == 2:
        raise ValueError('p has two children')
    child = node._left if node._left else node._right

    child._parent = node._parent

    if node is self._root:
        self._header._left = child._parent
    else:
        parent = node._parent
        if node is parent._left:
            parent._left = child
        else:
            parent._right = child
    self._size -= 1
    node._parent = node
    return node._element


def _attach(self, p, t1, t2):
    node = self._validate(p)

    if not self.is_leaf(p):
        raise ValueError('positino must be leaf')
    if not type(self) is type(t1) is type(t2):
        raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)

    node._left = t1._header._left
    node._right = t1.header._left

    t1._root = None
    t1._size = 0
    t2._root = None
    t2._size = 0
