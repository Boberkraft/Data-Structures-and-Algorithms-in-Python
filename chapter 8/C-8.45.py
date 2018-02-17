"""
Give an O(n)-time algorithm for computing the depths of all positions of
a tree T, where n is the number of nodes of T.
"""


from EulerTour import EulerTour
from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


class xd:
    def travel_tree(self, tree, p, d, depths):

        depths.append(d)
        for child in tree.children(p):
            self.travel_tree(tree, child, d + 1, depths)




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
dep = []
x = xd.travel_tree(t, t.root(), 0, dep)

print(dep)
