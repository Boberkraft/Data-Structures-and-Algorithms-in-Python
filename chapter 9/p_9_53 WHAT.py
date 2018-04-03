"""
Implement the in-place heap-sort algorithm. Experimentally compare its
running time with that of the standard heap-sort that is not in-place.

for inplace i just
Basically added some checks so i can run downheap on a slice of array, not the whole

BUT WHY MY INPLACE is slower than standard implementation?
"""
from HeapPriorityQueue import HeapPriorityQueue
from random import shuffle
from time import time

class InPlaceHeap(HeapPriorityQueue):
    def _downheap(self, j, n=None):
        if n is None:     # and this
            n = len(self) # and this
        if self._has_left(j) :
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left] and right < n: # and this
                    small_child = right
            if self._data[small_child] < self._data[j]:

                if small_child >= n: # added this
                    return           # and this

                self._swap(j, small_child)
                self._downheap(small_child, n)

    def _sort(self):
        for i in range(len(self)):
            self._swap(0, len(self) - i - 1)
            self._downheap(0, len(self) - i - 1)
        return [item._value for item in self._data]

    @classmethod
    def sort(self, data):
        return InPlaceHeap([[item, item] for item in data])._sort()


def pg_srot(c):
    n = len(c)
    h = InPlaceHeap()
    end = []
    for j in range(n):
        element = c.pop()
        h.add(element, element)
    for j in range(n):
        (k, v) = h.remove_min()
        c.append(v)


data = list(range(10000))
shuffle(data)
print('Data shuffled')
print('Standard sorting:')
copy = data[:]

start = time()
pg_srot(copy)
print(time() - start,'s')

print('In place sorting:')
copy = data[:]

start = time()
eq = InPlaceHeap.sort(copy)
print(time() - start,'s')

print('Python sorted():')
copy = data[:]

start = time()
eq = sorted(copy)
print(time() - start,'s')
