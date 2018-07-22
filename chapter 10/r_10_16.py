"""
Give a pseudo-code description of an insertion into a hash table that uses
quadratic probing to resolve collisions, assuming we also use the trick of
replacing deleted entries with a special “deactivated entry” object.
"""

mult = 0
while True:

    if table[i] in (None, _AVAIL):
        break

    i = (ii + mult * mult ) % size

# i is index
