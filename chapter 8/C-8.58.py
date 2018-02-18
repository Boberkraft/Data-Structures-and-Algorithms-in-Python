"""
Let T be a tree with n positions. Define the lowest common ancestor
(LCA) between two positions p and q as the lowest position in T that has
both p and q as descendants (where we allow a position to be a descendant
of itself ). Given two positions p and q, describe an efficient algorithm for
finding the LCA of p and q. What is the running time of your algorithm?

Number of nodes 'between' p an q
"""

from LinkedBinaryTree import LinkedBinaryTree
from other import intented_parenthetic

t = LinkedBinaryTree()
n0 = t._add_root(0)
n1 = t._add_left(n0, 1)
n2 = t._add_right(n0, 2)
n3 = t._add_left(n1, 3)
n4 = t._add_right(n1, 4)
# e = t._add_left(d, 5)
"""
     0
   1   2
 3  4
"""
ROMAN_NUMBER = 1


def LCA(tree, p, q):
    def update_node(node, d1, d2):
        while d1 > d2:
            node = tree.parent(node)
            d1 -= 1
        return node

    depth_p = tree.depth(p)
    depth_q = tree.depth(q)
    p = update_node(p, depth_p, depth_q)
    q = update_node(q, depth_q, depth_p)

    while p != q:
        p = tree.parent(p)
        q = tree.parent(q)
    return q


intented_parenthetic(t, t.root())
print()
x = LCA(t, n1, n3)
print(x.element())
# print(x)
