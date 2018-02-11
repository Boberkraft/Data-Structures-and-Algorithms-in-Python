"""
Describe how to implement the double-ended queue ADT using two stacks
as instance variables. What are the running times of the methods?

append_left = O(1)
append = O(1)

pop_left = worst case O(n), best case O(1)
pop = worst case O(n), best case O(1)
"""


class Empty(Exception):
    pass


class Deque:
    def __init__(self):
        self._left = []
        self._right = []

    def __len__(self):
        return len(self._left) + len(self._right)

    def __str__(self):
        return str(self._left + self._right)

    def append_left(self, e):
        self._left.append(e)

    def append(self, e):
        self._right.append(e)

    def pop_left(self):
        if len(self) == 0:
            return Empty()
        if len(self._left) == 0:
            while len(self._right) > 0:
                self._left.append(self._right.pop())
        return self._left.pop()

    def pop(self):
        if len(self) == 0:
            return Empty()
        if len(self._right) == 0:
            while len(self._left) > 0:
                self._left.append(self._left.pop())
        return self._right.pop()

a = Deque()
a.append(2)
a.append(3)
a.append(4)
print(a)
a.append_left(1)
print(a)
a.pop_left()
a.pop()
print(a)