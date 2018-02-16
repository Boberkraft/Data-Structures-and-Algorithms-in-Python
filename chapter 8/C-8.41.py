"""
Describe how to clone a LinkedBinaryTree instance representing a proper
binary tree, with use of the attach method.
"""
from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


def clone(t, p):
    tree = LinkedBinaryTree()
    tree._add_root(p._node._element)
    if t.num_children(p) == 2:

        left = clone(t, t.left(p))
        right = clone(t, t.right(p))
        tree._attach(tree.root(), left, right)
    return tree


t = LinkedBinaryTree()
root = t._add_root(0)
a = t._add_left(root, 1)
b = t._add_right(root, 2)
c = t._add_left(a, 3)
d = t._add_right(a, 4)
# e = t._add_left(d, 5)

parenthesize(t, t.root())
x = clone(t, t.root())
print()
parenthesize(x, x.root())
