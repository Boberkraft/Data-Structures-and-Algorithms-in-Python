"""
Describe an algorithm, relying only on the BinaryTree operations, that
counts the number of leaves in a binary tree that are the left child of their
respective parent

BinaryEulerTour would be useful here, maybe.

Does LinkedBinaryTree count as BinaryTree?
"""

from LinkedBinaryTree import LinkedBinaryTree


def count_left_children(t, p):
    s = 0
    if t.is_leaf(p):
        return 0
    if t.left(p) is not None:
        s = 1 + count_left_children(t, t.left(p))
    if t.right(p) is not None:
        s += count_left_children(t, t.right(p))
    return s


t = LinkedBinaryTree()
root = t._add_root(2)
l = t._add_left(root, 5)
r = t._add_right(root, 7)
t._add_left(l, 5)
t._add_right(l, 5)
t._add_left(r, 5)
t._add_right(r, 5)
"""
      x
   x     x
  x  x x   x
"""
assert count_left_children(t, t.root()) == 3
print(count_left_children(t, t.root()))
