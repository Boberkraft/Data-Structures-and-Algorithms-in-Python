"""
What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop().

3, 8, 2, 1, 6, 7, 4, 9
"""

from ArrayStack import ArrayStack

def test():
    """
    >>> a = ArrayStack()
    >>> a.push(5)
    >>> a.push(3)
    >>> print(a.pop())
    3
    >>> a.push(2)
    >>> a.push(8)
    >>> print(a.pop())
    8
    >>> print(a.pop())
    2
    >>> a.push(9)
    >>> a.push(1)
    >>> print(a.pop())
    1
    >>> a.push(7)
    >>> a.push(6)
    >>> print(a.pop())
    6
    >>> print(a.pop())
    7
    >>> a.push(4)
    >>> print(a.pop())
    4
    >>> print(a.pop())
    9
    """