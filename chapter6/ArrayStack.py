class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def look(self):
        return self._data


def test():
    """
    >>> S = ArrayStack( )
    >>> S.push(5)
    >>> S.push(3)
    >>> print(len(S))
    2
    >>> print(S.pop( ))
    3
    >>> print(S.is_empty( ))
    False
    >>> print(S.pop( ))
    5
    >>> print(S.is_empty( ))
    True
    >>> S.push(7)
    >>> S.push(9)
    >>> print(S.top( ))
    9
    >>> S.push(4)
    >>> print(len(S))
    3
    >>> print(S.pop( ))
    4
    >>> S.push(6)
    """


if __name__ == '__main__':
    print('elo')
