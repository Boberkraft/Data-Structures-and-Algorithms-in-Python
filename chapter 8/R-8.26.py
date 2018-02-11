"""
6 The collections.deque class supports an extend method that adds a collection
of elements to the end of the queue at once. Reimplement the
breadthfirst method of the Tree class to take advantage of this feature
"""
from Tree import Tree
from collections import deque


class Tree(Tree):
    def breadthfirst(self):
        if not self.is_empty():
            fringe = deque()
            fringe.appendleft(self.root())
            while len(fringe) > 0:
                p = fringe.popleft()
                yield p
                fringe.extend(self.children(p))

# good?