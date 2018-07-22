"""
Our implementation of separate chaining in ChainHashMap conserves
memory by representing empty buckets in the table as None, rather than
as empty instances of a secondary structure. Because many ofthese buck-
ets will hold a single item, a better optimization is to have those slots of
the table directly reference the Item instance, and to reserve use of sec-
ondary containers for buckets that have two or more items. Modify our
implementation to provide this additional optimization.

"""
from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):

        if self._table[j] is None:
            self._table[j] = self._Item(k, v)
            self._n += 1
        else:
            if isinstance(self._table[j], self._Item):
                old_item = self._table[j]

                self._table[j] = UnsortedTableMap()
                self._table[j][old_item._key] = old_item._value
                self._n += 1
            else:

                oldsize = len(self._table[j])
                self._table[j][k] = v
                if len(self._table[j]) > oldsize:
                    self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        if isinstance(bucket, self._Item):
            if bucket._key != k:
                raise KeyError
            self._table[j] = None
        else:
            # i dont think that changing it back to single Item instance is
            # good for performance, so lets just leave it as a UnsortedTableMap
            del bucket[k]


    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
