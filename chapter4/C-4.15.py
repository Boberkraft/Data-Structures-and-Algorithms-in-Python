"""
Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets).

Thats suspicious easy :|
"""
from copy import deepcopy

def _subsets(s):
    """returns subset of s excluding empty set
    
    :param s: set
    :return: yields every subset of s (including s, excluding empty set)
    """
    if len(s) > 0:
        yield s
        s.pop()
        yield from _subsets(s)

def subsets(s):
    s = deepcopy(s)
    yield from _subsets(s)

if __name__ == '__main__':
    data = set(range(10))
    for subset in subsets(data):
        print(subset)

