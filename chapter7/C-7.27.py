"""
Give a recursive implementation of a singly linked list class, such that an
instance of a nonempty list stores its first element and a reference to a list
of remaining elements.


it look cool
"""


class Empty(Exception):
    pass


class SingleLinkedList:
    def __init__(self, element=None, rest=None):
        self.element = element
        self.rest = rest
        self.size = 0

    def push(self, el):
        self.rest = SingleLinkedList(self.element, self)
        self.element = el
        self.size += 1

    def pop(self):
        if len(self) < 1:
            raise Empty('The list is empty')
        el = self.element
        self.element = self.rest.element
        self.rest = self.rest.rest
        self.size -= 1
        return el

    def __len__(self):
        return self.size


a = SingleLinkedList()
a.push(1)
a.push(2)
a.push(3)
