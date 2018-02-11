"""
Let T be an n-node binary tree that may be improper. Describe how to
represent T by means of a proper binary tree T with O(n) nodes.

How to transform improper binary tree to proper?
Or by using null nodes where needed to create proper binary tree?


By the way, if the tree doesnt have any nodes, whatis its hight?
"""


class NullNode:
    pass


def make_it_proper(tree):
    # assume non empty tree
    h = tree.height()
    _create_null(tree, tree.root(), h)


def _create_null(tree, node, height):
    if height > 0:
        if tree.left(node) is None:
            node = tree._add_left(node, NullNode)
        if tree.right(node) is None:
            tree._add_right(node, NullNode)
        _create_null(tree, tree.left(node), height - 1)
        _create_null(tree, tree.right(node), height - 1)
       