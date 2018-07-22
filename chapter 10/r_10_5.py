"""
 Reimplement the UnsortedTableMap class from Section 10.1.5, using the
PositionalList class from Section 7.4 rather than a Python list.
"""
import sys
sys.path.append('../chapter7')

from PositionalList import PositionalList
from MapBase import MapBase

class UnsortedTableMap(MapBase):

    def __init__(self):
        self._data = PositionalList()

    def __getitem__(self, k):
        for item in self._data:
            if k == item.element()._key:
                return item.element()._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, key, value):
        for item in self._data:
            if key == item.element()._key:
                self._data.replace(item, self._Item(key, value))
                return

        self._data.add_first(self._Item(key, value))

    def __delitem__(self, key):
        for item in self._data:
            if key == item.element()._key:
                self._data.delete(item)
                return
        raise KeyError("Key Error: " + repr(key))

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item.element()._key
