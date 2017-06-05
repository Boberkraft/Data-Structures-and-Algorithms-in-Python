"""
Consider a variant of Exercise C-5.16, in which an array of capacity N, is
resized to capacity precisely that of the number of elements, any time the
number of elements in the array goes strictly below N/2. Show that there
exists a sequence of n operations that requires Ω(n2) time to execute.

Do 9 appends
and then one pop
"""

from dynamicarray import DynamicArray

class NewArray(DynamicArray):
    def pop(self):
        el = self[-1]
        self._A[self._n] = None
        self._n -= 1
        if self._n <= self._capacity/2:
            # shrink the array
            self._resize(self._n)
        return el

if __name__ == '__main__':
    array = NewArray()
    for x in range(8):
        array.append(x)
    print(repr(array))
    array.append(66)
    print(repr(array))
    array.pop()
    print(repr(array))
    array.append(66)
    print(repr(array))


