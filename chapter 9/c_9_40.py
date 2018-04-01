"""
Implement a heapreplace method for the HeapPriorityQueue class, with
semantics akin to that described for the heapq module in Section 9.3.7.
"""
from HeapPriorityQueue import HeapPriorityQueue


class newHeap(HeapPriorityQueue):
    def heapreplace(self, key, value):

        min_key, min_val = self.min()
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
    >>> x.heapreplace(1,1)
    (2, 2)
    >>> x.heapreplace(3,3)
    (1, 1)
    """
    pass