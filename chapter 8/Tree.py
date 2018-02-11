from collections import deque

class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subClass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subClass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subClass')

    def parent(self):
        raise NotImplementedError('must be implemented by subClass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subClass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subClass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subClass')

    def is_root(self, p):
        raise NotImplementedError('must be implemented by subClass')

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        return self.preorder()

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            fringe = deque()
            fringe.appendleft(self.root())
            while len(fringe) > 0:
                p = fringe.pop()
                yield p
                for c in self.children(p):
                    fringe.appendleft(c)


    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p in None:
            p = self.root()
        return self._height2(p)

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
