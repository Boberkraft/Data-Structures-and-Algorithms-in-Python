"""
Implement a heappushpop method for the HeapPriorityQueue class, with
semantics akin to that described for the heapq module in Section 9.3.7
"""
from HeapPriorityQueue import HeapPriorityQueue


class newHeap(HeapPriorityQueue):
    def heappushpop(self, key, value):
        if self.is_empty():
            return key, value

        min_key, min_val = self.min()
        if value < min_val:
            return key, value
        else:
            self._data[0] = self._Item(key, value)
            self._downheap(0)
            return min_key, min_val


def test():
    """
    >>> x = newHeap()
    >>> x.add(4, 4)
    >>> x.add(5, 5)
    >>> x.add(6, 6)
    >>> x.add(2, 2)
    >>> x.heappushpop(1,1)
    (1, 1)
    >>> x.heappushpop(3,3)
    (2, 2)
    """
    pass
