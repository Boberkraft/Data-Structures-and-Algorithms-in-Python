from SortedTableMap import SortedTableMap


class CostPerformanceDatabase:
    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        return self._M.find_le(c)

    def add(self, c, p):
        other = self._M.find_le(c)
        if other is not None and other[1] <= p:
            del self._M[other[0]]
            other - self._M.find_gt(c)
