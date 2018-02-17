"""
The balance factor of an internal position p of a proper binary tree is the
difference between the heights of the right and left subtrees of p. Show
how to specialize the Euler tour traversal of Section 8.4.6 to print the
balance factors of all the internal nodes of a proper binary tree.

See C-8.44 its almost the same!
"""

from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize
from EulerTour import BinaryEulerTour



class newBinaryEulerTour(BinaryEulerTour):
    def _hook_postvisit(self, p, d, path, results):

        if self._tree.is_leaf(p):
            print("node({}) balance is NaN".format(p._node._element))
            return 0
        else:
            l, r = results[0], results[1]
            print("node({}) balance is {}".format(p._node._element, r - l))
            return l + r + 1



t = LinkedBinaryTree()
root = t._add_root(0)
a = t._add_left(root, 1)
b = t._add_right(root, 2)
c = t._add_left(a, 3)
d = t._add_right(a, 4)
# e = t._add_left(d, 5)
"""
     0
  1     2
3  4
"""
parenthesize(t, t.root())
print()
new = newBinaryEulerTour(t)
print(new.execute())

