"""
Repeat Exercise C-10.28 for the ChainHashMap class.
"""
from HashMapBase import HashMapBase
from UnsorterTableMap import UnsorterTableMap


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsorterTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

    def setdefault(self, key, default):
        j = self._hash_function(key)
        if self._table[j] is None:
            # no need for return...
            return self._bucket_setitem(j, key, default)
        else:
            return self._bucket_getitem(j, key)
