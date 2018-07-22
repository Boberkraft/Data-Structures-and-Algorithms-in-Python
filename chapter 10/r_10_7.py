"""
 Our Position classes for lists and trees support the eq method so that
twodistinct position instances areconsidered equivalentifthey refer to the
same underlying node in a structure. For positions to be allowed as keys
in a hash table, there must be a definition for the hash method that
is consistent with this notion of equivalence. Provide such a hash
method.



"""


class Position:

    # ...
    def hash(self):
        return hash(self._element._key)
