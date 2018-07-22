"""
 Give a concrete implementation of the pop method, in the context of a
MutableSet abstract base class, that relies only on the five core set behav-
iors described in Section 10.5.2.
"""


def pop(self, index):
    for el in self:  # is there a better way to fetch a random key?
        x = el
        self.remove(el)
        return x
    raise KeyError("The set is empty")
