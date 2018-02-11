"""
Describe a recursive algorithm that counts the number of nodes in a singly
linked list.
"""

def how_many(node):
    if node.next is not None:
        return 1 + how_many(node.next)
    else:
        return 1