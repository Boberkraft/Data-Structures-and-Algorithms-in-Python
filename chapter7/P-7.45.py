
"""
An array A is sparse if most of its entries are empty (i.e., None). A list
L can be used to implement such an array efficiently. In particular, for
each nonempty cell A[i], we can store an entry (i,e) in L, where e is the
element stored at A[i]. This approach allows us to represent A using O(m)
storage, where m is the number of nonempty entries in A. Provide such
a SparseArray class that minimally supports methods getitem (j) and
setitem (j, e) to provide standard indexing operations. Analyze the
efficiency of these methods.

If implemented using normal list then we can insert using
insertion sort
and
search using binary search.

Inserting element O(n)
searching O(log n)

If we dont use any algorithm and just push at the end
it will be O(n) searching and O(1) inserting

im lazy and did only second method
"""
from PositionalList import PositionalList


class SparseArray:
    def __init__(self):
        self._data = PositionalList()

    def __getitem__(self, item):
        for i, e in self._data:
            if i == item:
                return e

    def __setitem__(self, key, value):
        self._data.add_first((key, value))


a = SparseArray()
a[3] = 1
a[2] = 2
a[10] = 3

print(a[3], a[2], a[10])
