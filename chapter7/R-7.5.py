"""
Implement a function that counts the number of nodes in a circularly
linked list.
"""
from CircularQueue import CircularQueue


def count_nodes(q):
    quan = 0
    if not q.is_empty():
        top = q.first()
        quan += 1
        q.rotate()
        while q.first() != top:  # sad that it returns element not node
            quan += 1
            q.rotate()
    return quan


def count_nodes_pro(q):
    return len(q)


q = CircularQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(count_nodes(q))
