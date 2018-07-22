"""
Give a concrete implementation of the pop method in the context of the
MutableMapping class, relying only on the five primary abstract methods
of that class.

pop(self, key, default=<object object at 0x00298030>)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised.
"""

def pop(self, k, *d):
    try:
        value = self[k]
        del self[k]
    except KeyError:
        if len(d) == 0:
           raise KeyError
        if len(d) != 1:
            raise TypeError
        value = d[0]
    return value


