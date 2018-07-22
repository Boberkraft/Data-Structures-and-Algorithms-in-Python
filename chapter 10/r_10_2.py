"""
Give a concrete implementation of the items() method in the context of
the MutableMappingclass, relying only on the fiveprimary abstract meth-
ods of that class. What would its running time be if directly applied to the
UnsortedTableMap subclass?
"""

def items(self):
    for key in self:
        yield key, self[key]