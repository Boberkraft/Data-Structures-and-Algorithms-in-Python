"""
Given the set of element {a,b,c,d,e, f } stored in a list, show the final state
of the list, assuming we use the move-to-front heuristic and access the elements
according to the following sequence: (a,b,c,d,e, f,a,c, f,b,d,e)
"""

from FavoritesListMTF import FavoritesListMTF

l = FavoritesListMTF()
l.access("a")
l.access("b")
l.access("c")
l.access("d")
l.access("e")
l.access("f")
print(l)
l.access("a")
l.access("c")
l.access("f")
l.access("b")
l.access("d")
l.access("e")
print(l)

# e d b f a