"""
The indented parenthetic representation of a tree T is a variation of the
parenthetic representation of T (see Code Fragment 8.25) that uses indentation
and line breaks as illustrated in Figure 8.24. Give an algorithm that
prints this representation of a tree.
"""
from LinkedBinaryTree import LinkedBinaryTree

def intented_parenthetic(tree, p, ind=0):
    print(' '*ind + p.element(), end='')
    if not tree.is_leaf(p):
        print('(')
    else:
        print()
    for child in tree.children(p):
        intented_parenthetic(tree, child, ind + 1)
    if not tree.is_leaf(p):
        print(' ' * ind + ')')



t = LinkedBinaryTree()
n0 = t._add_root('Sales')
n1 = t._add_left(n0, 'International')
n2 = t._add_right(n0, "Domestic")
n3 = t._add_left(n1, "Australia")
n4 = t._add_right(n1, "Asia")
# e = t._add_left(d, 5)

intented_parenthetic(t, t.root())
print()