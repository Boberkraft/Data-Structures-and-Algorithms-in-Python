"""
 Repeat Exercise C-10.28 for the ProbeHashMap class.
"""

from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    # ...
    def setdefault(self, key, default):
        found, s = self._find_slot(key, key)
        if found:
            return self._table[s]._value

        self._table[s] = self._Item(key, default)
        self._n += 1
