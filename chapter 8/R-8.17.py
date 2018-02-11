"""
Show how to use the Euler tour traversal to compute the level number
f(p), as defined in Section 8.3.2, of each position in a binary tree T.
"""

from EulerTour import BinaryEulerTour
from LinkedBinaryTree import LinkedBinaryTree

class LevelTour(BinaryEulerTour):
    def _hook_invisit(self, p, d, path):
        ans = 0
        for val in path:
            ans = 2 * ans + val + 1
        print(p.element(),ans)

t = LinkedBinaryTree()
root = t._add_root(0)
l = t._add_left(root, 1)
r = t._add_right(root, 2)
t._add_left(l, 3)
t._add_right(l, 4)
t._add_left(r, 5)
t._add_right(r, 6)
"""
      x
   x     x
  x  x x   x
"""

a = LevelTour(t)
a.execute()
