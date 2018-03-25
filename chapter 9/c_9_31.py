"""
Give a nonrecursive implementation of the downheap method for the
class HeapPriorityQueue.
"""
from HeapPriorityQueue import HeapPriorityQueue

class NewHeapPriorityQueue(HeapPriorityQueue):

    # def _downheap(self, j):
    #     if self._has_left(j):
    #         left = self._left(j)
    #         small_child = left
    #         if self._has_right(j):
    #             right = self._right(j)
    #             if self._data[right] < self._data[left]:
    #                 small_child = right
    #         if self._data[small_child] < self._data[j]:
    #             self._swap(j, small_child)
    #             self._downheap(small_child)

    def _downheap(self, j):
        while self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
            else:
                break
            j = small_child

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
    (0.3, 'xdd')
    """
    pass