"""
Although we have used a doubly linked list to implement the positional
list ADT, it is possible to support the ADT with an array-based implementation.
The key is to use the composition pattern and store a sequence
of position items, where each item stores an element as well as that element’s
current index in the array. Whenever an element’s place in the array
is changed, the recorded index in the position must be updated to match.
Given a complete class providing such an array-based implementation of
the positional list ADT. What is the efficiency of the various operations?

I dont like being inefficient

add first O(n)
add last O(1)
add_after O(n)
add_before O(n)
swap O(1)
"""


class PositionalList:
    class _Node:
        def __init__(self, el, index):
            self.element = el
            self.index = index

    def __init__(self):
        self._data = []
        self._size = 0

    def add_last(self, el):

        new = self._Node(el, self._size)
        self._data.append(new)

        self._size += 1
        return new

    def add_first(self, value):
        new = self._Node(value, 0)
        for el in self._data:
            el.index += 1
        self._data.insert(0, new)
        self._size += 1
        return new

    def add_after(self, p, value):
        new = self._Node(value, p.index + 1)
        for el in self._data[p.index + 1:]:
            el.index += 1
        self._data.insert(p.index + 1, new)
        self._size += 1
        return new

    def __str__(self):
        return '[{}]'.format(', '.join([str(x.element) for x in self._data]))


x = PositionalList()
x.add_first(1)
pointer = x.add_first(2)
x.add_first(3)
print(x)
x.add_after(pointer, 33)
print(x)