"""
 Our HashMapBase class maintains a load factor λ ≤ 0.5. Reimplement
that class to allow the user to specify the maximum load, and adjust the
concrete subclasses accordingly

so i only added load factor parameter
"""


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121, load_factor=0.5):
        # ...
        self._load_factor = load_factor

    def __setitem__(self, key, value):
        # ...
        if self._n > len(self._table) * self._load_factor:
            self._resize(2 * len(self._table) - 1)

