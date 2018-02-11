class EulerTour:
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if not self._tree.is_empty():
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * ' ' + str(p.element()))


class PreoderPrintIndentedLabelTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j + 1) for j in path)
        print(2 * d * ' ' + label, p.element())


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)


# --------------------------------
# Binary Tree

class BinaryEulerTour(EulerTour):
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d + 1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class BinaryLayout(BinaryEulerTour):
    _count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1
