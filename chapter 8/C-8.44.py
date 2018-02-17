"""
Give an efficient algorithm that computes and prints, for every position p
of a tree T, the element of p followed by the height of p’s subtree.
"""

from EulerTour import EulerTour
from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


class xd:
    def travel_tree(self, tree, p, height):

        best = height
        for child in tree.children(p):
            new_size = self.travel_tree(tree, child, 0)
            best = max(best, new_size)
        if not tree.is_leaf(p):
            best += 1
        print("Node {} have height {}".format(p._node._element, best))
        return best


t = LinkedBinaryTree()
root = t._add_root(0)
a = t._add_left(root, 1)
b = t._add_right(root, 2)
c = t._add_left(a, 3)
d = t._add_right(a, 4)
e = t._add_left(d, 5)
"""
     0
  1     2
3  4
    5

"""
parenthesize(t, t.root())
print()
xd = xd()
x = xd.travel_tree(t, t.root(), 0)

print()
