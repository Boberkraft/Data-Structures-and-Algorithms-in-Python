"""
Add support in LinkedBinaryTree for a method, delete subtree(p), that
removes the entire subtree rooted at position p, making sure to maintain
the count on the size of the tree. What is the running time of your implementation?


Runnig time is O(x) where x is the number of nodes is a tree rooted at p.
"""

from LinkedBinaryTree import LinkedBinaryTree


class newLinkedBinaryTree(LinkedBinaryTree):
    def remove_tree(self, p):
        node = self._validate(p)
        self._size -= _count_nodes(node)
        self._delete(p)


def _count_nodes(node):
    value = 0
    if node.left() is not None:
        value += _count_nodes(node.left()) + 1
    if node.right() is not None:
        value += _count_nodes(node.right()) + 1

    return value


a = newLinkedBinaryTree()
