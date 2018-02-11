"""
Describe a nonrecursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a
counter.) What is the running time of this method?

O(n)
"""

from LinkedDeque import LinkedDeque


def middle(q):
    start = q._header
    end = q._trailer
    while True:
        if end is start.prev or end is start:
            return start
        end = end.prev
        start = start.next


q = LinkedDeque()
q.insert_first(1)
q.insert_first(2)
q.insert_first(3)
q.insert_first(4)

a = middle(q)
print(a.element)
