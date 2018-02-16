"""
Add support in LinkedBinaryTree for a method, swap(p,q), that has the
effect of restructuring the tree so that the node referenced by p takes the
place of the node referenced by q, and vice versa. Make sure to properly
handle the case when the nodes are adjacent.
"""

from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


class newLinkedBinaryTree(LinkedBinaryTree):
    def _swap(self, p, q):
        def is_left(m):
            return m._parent._left is m

        p = self._validate(p)
        q = self._validate(q)
        print("\nElements")
        print(p._parent._element, q._element)
        print(q._parent._element, p._element)

        node_1 = p
        node_2 = q

        if node_1 is self._root:
            self._root = node_2
            node_2._parent = None
        elif is_left(node_1):
            node_1._parent._left = node_2
        else:
            node_1._parent._right = node_2

        if node_2 is self._root:
            self._root = node_1
            node_1._parent = None
        elif is_left(node_2):
            print(node_2._element)
            print()
            print(node_2._parent == node_1)
            node_2._parent._left = node_1
            print(node_1._left._element)

        else:
            node_2._parent._right = node_1


        node_2._left, node_1._left = node_1._left, node_2._left
        node_2._right, node_1._right = node_1._right, node_2._right



t = newLinkedBinaryTree()
root = t._add_root(0)
a = t._add_left(root, 1)
b = t._add_left(a, 2)
c = t._add_left(b, 3)
d = t._add_left(c, 4)
e = t._add_left(d, 5)
# t._add_right(x, 4)
# r = t._add_right(root, 3)
# t._add_left(l, 4)
# x = t._add_right(l, 5)
# t._add_left(r, 6)
# t._add_right(r, 7)

parenthesize(t, t.root())

t._swap(b, d)


print('root is', t._root._element)
parenthesize(t, t.root())

e = e._node
print(e._element)
print(e._parent._element)
print(e._parent._parent._element)
print(e._parent._parent._parent._element)
print(e._parent._parent._parent._parent._element)
"""
      1
   l     3
  4  x 6   7
"""
# assert count_left_children(t, t.root()) == 3
