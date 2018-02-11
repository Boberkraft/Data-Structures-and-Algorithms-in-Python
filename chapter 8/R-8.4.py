"""
What is the running time of a call to T. height2(p) when called on a
position p distinct from the root of T? (See Code Fragment 8.5.)

def height2(self, p): # time is linear in size of subtree
    ”””Return the height of the subtree rooted at Position p.”””
    if self.is leaf(p):
        return 0
    else:
        return 1 + max(self. height2(c) for c in self.children(p))

O(h)
where h is the number of nodes in a subtree rooted at a position p

or
#  ignore
#  where h is the  maximum numbers of nodes between position p - subtree rooted at
#  that position and its leafs + 1

"""
