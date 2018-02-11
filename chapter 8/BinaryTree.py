from Tree import Tree


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subClass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subClass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def position(self):
        return self.inorder()

    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
