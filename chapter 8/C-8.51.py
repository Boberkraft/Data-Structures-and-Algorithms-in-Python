"""
To implement the preorder method of the LinkedBinaryTree class, we relied
on the convenience of Python’s generator syntax and the yield statement.
Give an alternative implementation of preorder that returns an explicit
instance of a nested iterator class. (See Section 2.3.4 for discussion
of iterators.)


def preorder(self):
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):
            yield p


"""

def _subtree_preorder(self, p):
    yield p
    for c in self.children(p):
        for other in self._subtree_preorder(c):
            yield other


class Ite:
    def __init__(self, tree, pos):
        self.tree = tree
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self):
        for child in self.tree.children(self.pos):
            for other in Ite(self.tree, child):
                return other
        raise StopIteration
        # IT SHOULD WORK YEEEAAA

