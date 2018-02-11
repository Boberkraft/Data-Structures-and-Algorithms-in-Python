"""
Design an ADT for a two-color, double-stack ADT that consists of two
stacks—one “red” and one “blue”—and has as its operations color-coded
versions of the regular stack ADT operations. For example, this ADT
should support both a red push operation and a blue push operation. Give
an efficient implementation of this ADT using a single array whose capacity
is set at some value N that is assumed to always be larger than the
sizes of the red and blue stacks combined.

hmm
"""


class Empty(Exception):
    pass


class ColoredDoubleStack:
    DEFAULT_SIZE = 2

    def __init__(self):
        self._data = [None] * ColoredDoubleStack.DEFAULT_SIZE
        self._red_top = 0
        self._blue_top = -1

    def _check_size(self):
        size = len(self._data)
        actual = self._red_top - self._blue_top - 1
        if actual == size:
            self._resize(size * 2)
        if 0 < actual * 4 < size:
            self._resize(size // 2)

    def red_pop(self):
        if self._red_top == 0:
            raise Empty()
        self._check_size()

        self._data[self._red_top] = None
        self._red_top -= 1

    def blue_pop(self):
        if self._red_top == -1:
            raise Empty()
        self._check_size()

        self._data[self._blue_top] = None
        self._blue_top += 1

    def red_push(self, el):
        self._check_size()
        self._data[self._red_top] = el
        self._red_top += 1

    def blue_push(self, el):
        self._check_size()
        self._data[self._blue_top] = el
        self._blue_top -= 1

    def _resize(self, cap):
        print('Expanding:', cap)
        old = self._data
        self._data = [None] * cap
        for x in range(self._red_top):
            self._data[x] = old[x]
        for x in range(self._blue_top+1, 0):
            self._data[x] = old[x]

    def __str__(self):
        return str(self._data)


q = ColoredDoubleStack()
q.blue_push(1)
q.blue_push(1)
q.red_push(6)
q.red_push(7)
q.red_push(8)

print(q)
