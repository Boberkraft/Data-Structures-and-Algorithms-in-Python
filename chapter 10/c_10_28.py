"""
 On page 406 of Section 10.1.3, we give an implementation of the method
setdefault as it might appear in the MutableMapping abstract base class.
While that method accomplishes the goal in a general fashion, its effi-
ciency is less than ideal. In particular, when the key is new, there will be
a failed search due to the initial use of getitem , and then a subse-
quent insertion via setitem . For a concrete implementation, such as
the UnsortedTableMap, this is twice the work because a complete scan
of the table will take place during the failed getitem , and then an-
other complete scan of the table takes place due to the implementation of
setitem . Abetter solution is fortheUnsortedTableMapclass to over-
ride setdefault to provide a direct solution that performs a single search.
Give such an implementation of UnsortedTableMap.setdefault."""


from MapBase import MapBase

class UnsortedTableMap(MapBase):
    # ...
    def setdefault(self, key, default):
        for item in self._table:
            if key == item._key:
                return item._value

        self._table.append(self._Item(key, default))
