"""
Implement a function with signature transfer(S, T) that transfers all elements
from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T.

Its a joke?
"""

from ArrayStack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


def test():
    """
    >>> S = ArrayStack()
    >>> S.push(5)
    >>> S.push(7)
    >>> T = ArrayStack()
    >>> T.push(9)
    >>> transfer(S, T)
    >>> T.look()
    [9, 7, 5]
    """
