"""
Let T be a binary tree with n positions. Define a Roman position to be
a position p in T, such that the number of descendants in p’s left subtree
differ from the number of descendants in p’s right subtree by at most 5.
Describe a linear-time method for finding each position p of T, such that
p is not a Roman position, but all of p’s descendants are Roman.

defining not linear time algorithm would be a challenge!
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
   2   0
 0  0
"""
ROMAN_NUMBER = 1


def find_romanians(tree, p):
    if tree.is_leaf(p):
        return True, 0

    was1, left = find_romanians(tree, t.left(p))
    was2, right = find_romanians(tree, t.right(p))
    left += 1
    right += 1
    print('Descendants:', left, right, 'for node:', p.element())

    if abs(left - right) <= ROMAN_NUMBER:
        # is roman
        return True, left + right
    elif was1 is was2 is True:
        # isnt roman
        # but was!
        print('Node({}) is the theshold'.format(p.element()))
        return False, left + right
    print('Returning!')
    return False, 0


intented_parenthetic(t, t.root())
print()
x = find_romanians(t, n0)
# print(x)
