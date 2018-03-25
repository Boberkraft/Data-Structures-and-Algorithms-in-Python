"""
Give a nonrecursive implementation of the upheap method for the class
HeapPriorityQueue.
"""
from HeapPriorityQueue import HeapPriorityQueue

class NewHeapPriorityQueue(HeapPriorityQueue):

    # def _uphead(self, j):
    #     parent = self._parent(j)
    #     if j > 0 and self._data[j] < self._data[parent]:
    #         self._swap(j, parent)
    #         self._upheap(parent)

    def _uphead(self, j):
        while j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._swap(j, self._parent(j))
            j = self._parent(j)

def test_heap():
    """
    >>> x = NewHeapPriorityQueue()
    >>> x.add(1, 'ada')
    >>> x.add(3, 'bet')
    >>> x.add(2, 'zet')
    >>> x.remove_min()
    (1, 'ada')
    >>> x.remove_min()
    (2, 'zet')
    >>> x.add(0.3, 'xdd')
    >>> x.remove_min()
    (0.3, 'bet')
    """
    pass

