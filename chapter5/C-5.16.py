"""
Implement a pop method for the DynamicArray class, given in Code Fragment
5.3, that removes the last element of the array, and that shrinks the
capacity, N, of the array by half any time the number of elements in the
array goes below N/4.
"""

from dynamicarray import DynamicArray

class NewArray(DynamicArray):
    def pop(self):
        el = self[-1]
        self._A[self._n] = None
        self._n -= 1
        if self._n/4 > self._capacity:
            # shrink the array
            self._resize(self._capacity/2)
        return el

