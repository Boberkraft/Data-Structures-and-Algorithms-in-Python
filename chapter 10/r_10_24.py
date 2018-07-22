"""
Give a pseudo-code description of the delitem map operation when
using a skip list.
"""

def __del__(self, el):
    p = SkipSearch(k) # find you element
    if p.element() == el:
        x = p
        while True: # for every block
            if x is None:
                break
            connect(before(x), after(x))
            x = above(p)
    else:
        raise ValueError
