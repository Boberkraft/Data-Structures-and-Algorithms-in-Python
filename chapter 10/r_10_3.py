"""
Give a concrete implementation of the items() method directly within the
UnsortedTableMap class, ensuring that the entire iteration runs in O(n)
time
"""

from UnsortedTableMap import UnsortedTableMap


class NewUnsortedTableMap(UnsortedTableMap):
    def items(self):
        for item in self._table:
            yield item._key, item._value