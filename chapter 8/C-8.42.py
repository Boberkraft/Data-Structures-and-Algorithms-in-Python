"""
Describe how to clone a LinkedBinaryTree instance representing a (not
necessarily proper) binary tree, with use of the add left and add right
methods
"""

from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


def clone(tree1):
    tree2 = LinkedBinaryTree()
    tree2._add_root(tree1._root._element)
    _clone(tree1, tree1.root(), tree2, tree2.root())
    return tree2


def _clone(tree1, t, tree2, p):
    if tree1.left(t) is not None:
        new_left = tree2._add_left(p, tree1.left(t)._node._element)
        _clone(tree1, tree1.left(t), tree2, new_left)

    if tree1.right(t) is not None:
        new_right = tree2._add_right(p, tree1.right(t)._node._element)
        _clone(tree1, tree1.right(t), tree2, new_right)


t = LinkedBinaryTree()
root = t._add_root(0)
a = t._add_left(root, 1)
b = t._add_right(root, 2)
c = t._add_left(a, 3)
d = t._add_right(a, 4)
# e = t._add_left(d, 5)

parenthesize(t, t.root())
new = clone(t)
print()
parenthesize(new, new.root())
