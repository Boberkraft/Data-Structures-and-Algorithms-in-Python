from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap.AVAIL

    def _find_slot(self, j, key):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return False, firstAvail
                elif key == self._table[j]._key:
                    return True, j
                j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, key):
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        return self._table[s]._value

    def _bucket_setitem(self, j, key, value):
        found, s = self._find_slot(j, key)
        if not found:
            self._table[s] = self._Item(key, value)
            self._n += 1
        else:
            self._table[s].value = value

    def _bucket_delitem(self, j, key):
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
