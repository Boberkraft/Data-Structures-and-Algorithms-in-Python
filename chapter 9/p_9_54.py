"""
Use the approach of either Exercise C-9.42 or C-9.43 to reimplement the
top method of the FavoritesListMTF class from Section 7.6.2. Make sure
that results are generated from largest to smallest.

"""
from random import randint
from HeapPriorityQueue import HeapPriorityQueue

from FavoritesList import FavoritesList
from PositionalList import PositionalList


class FavoritesListMTF(FavoritesList):
    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Ilegal value for k")

        temp = HeapPriorityQueue([[-item._count, item._value] for item in self._data])

        for _ in range(k):
            _, val = temp.remove_min()
            yield val

def test():
    """
    >>> x = FavoritesListMTF()
    >>> x.access('a')
    >>> x.access('a')
    >>> x.access('b')
    >>> x.access('e')
    >>> x.access('b')
    >>> x.access('b')
    >>> x.access('b')
    >>> x.access('e')
    >>> x.access('c')
    >>> x.access('d')
    >>> x.access('e')
    >>> x.access('e')
    >>> x.access('f')
    >>> print(x)
    (f:1), (e:4), (d:1), (c:1), (b:4), (a:2)
    >>> for var in x.top(3):
    ...  print(var)
    e
    b
    a
    """

