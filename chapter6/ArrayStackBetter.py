
class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack:
    def __init__(self, maxlen=0):
        self._data = []
        self._size = 0
        if maxlen:
            self._maxlen = maxlen
            self._data = [None for _ in range(maxlen)]

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        if self._maxlen and self._size >= self._maxlen:
            raise Full
        self._data[self._size] = e
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        data = self._data[self._size]
        self._data[self._size] = None
        self._size -= 1
        return data

    def look(self):
        return self._data
