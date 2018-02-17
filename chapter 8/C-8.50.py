"""
Design algorithms for the following operations for a binary tree T:
    • preorder next(p): Return the position visited after p in a preorder
    traversal of T (or None if p is the last node visited).
    
    • inorder next(p): Return the position visited after p in an inorder
    traversal of T (or None if p is the last node visited).
    
    • postorder next(p): Return the position visited after p in a postorder
    traversal of T (or None if p is the last node visited).
    
What are the worst-case running times of your algorithms?
"""

from LinkedBinaryTree import LinkedBinaryTree
from other import parenthesize


t = LinkedBinaryTree()
n0 = t._add_root(0)
n1 = t._add_left(n0, 1)
n2 = t._add_right(n0, 2)
n3 = t._add_left(n1, 3)
n4 = t._add_right(n1, 4)
# e = t._add_left(d, 5)

parenthesize(t, t.root())
print()


def preorder_next(tree, p):
    parent = p._parent
    if p._left is not None:
        return p._left
    elif p._right is not None:
        return p._right
    else:
        if p is tree._root:
            print('root')
            return None
    if parent._right == p:

        parent = parent._parent

    if parent is None:
        return None
    while parent._right is None:
        print('The parent is', parent._element)

        if parent is tree._root:
            return None
        parent = parent._parent
    return parent._right

def inorder_next(tree, p):
    if p is None:
        return None

    while p == p._parent._right:
        p = p._parent
    else:
        p = p._parent


    while True:
        p = p._right
        if p._left is None:
            return p



def postorder_next(tree, p):
    if p is tree._root:
        return None
    parent = p._parent
    while True:
        # print('Checking for', parent._element)
        if parent is None:
            return None
        if p is parent._left:
            if parent._right is not None:
                return parent._right
        p = parent
        parent = parent._parent

"""
         0
      1     2
    3  4
"""
# el = preorder_next(t, n2._node)
# el = postorder_next(t,n2._node)
el = inorder_next(t, n3._node)


if el is None:
    print('None')
else:
    print(el._element)

