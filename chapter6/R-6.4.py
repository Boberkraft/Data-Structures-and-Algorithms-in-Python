"""
Give a recursive method for removing all the elements from a stack.
"""

from ArrayStack import ArrayStack


def delete(self):
    if not self.is_empty():
        self.pop()
        self.delete_all()


ArrayStack.delete_all = delete
a = ArrayStack()


def test():
    """
    >>> a.push(5)
    >>> a.push(6)
    >>> a.push(7)
    >>> a.look()
    [5, 6, 7]
    >>> a.delete_all()
    >>> a.look()
    []
    """
