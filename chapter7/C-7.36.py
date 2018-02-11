"""
Give a complete implementation of the positional list ADT using a doubly
linked list that does not include any sentinel nodes.
"""


class DoublyLinkedBase:
    class _Node:
        def __init__(self, el, prev, next):
            self.element = el
            self.prev = prev
            self.next = next

    class _Position:
        def __init__(self, node, container):
            self._node = node
            self.element = node.element
            self._container = container

    def _make_position(self, node):
        return self._Position(node, self)

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def add_first(self, el):
        self._size += 1
        if self._head is None:
            self._head = self._Node(el, None, None)
            self._tail = self._head
        else:
            new = self._Node(el, None, self._head)
            self._head.prev = new
            self._head = new
        return self._make_position(self._head)

    def add_last(self, el):
        self._size += 1
        if self._head is None:
            self._head = self._Node(el, None, None)
            self._tail = self._head
        else:
            new = self._Node(el, self._tail, None)
            self._tail.next = new
            self._tail = new
        return self._make_position(self._tail)

    def first(self):
        return self._make_position(self._head)

    def last(self):
        return self._make_position(self._tail)

    def _insert_between(self, el, pre, after):
        self._validate(pre)
        self._validate(after)
        self._size += 1
        if pre is after:
            # the fuck
            raise ValueError()
        new = self._Node(el, pre._node, after._node)
        pre.next = new
        pre.after = new

    def _validate(self, pos):
        if pos._container != self:
            raise TypeError()

    def _delete_node(self, pos):
        self._validate(pos)
        node = pos._node
        el = node.element
        if self._head == self._tail == node:
            self._head = self._tail = None
        elif node == self._head:
            self._head = node.next
        elif node == self._tail:
            self._tail = node.prev
        else:
            prev = node.prev
            next = node.next
            next.prev = prev
            prev.next = next
            node.next = node.prev = node.element = None
        pos._container = None
        return el

    def add_after(self, el, pos):
        self._validate(pos)
        node = pos._node
        if node is self._tail:
            new = self._Node(el, node, None)
            node.next = new
            self._tail = new
        else:
            new = self._Node(el, node, node.next)
            node.next.prev = new
            node.next = new

    def add_before(self, el, pos):
        self._validate(pos)
        node = pos._node
        if node is self._head:
            new = self._Node(el, None, node)
            node.prev = new
            self._head = new
        else:
            new = self._Node(el, node.prev, node)
            node.prev.next = new
            node.prev = new


if __name__ == '__main__':
    a = DoublyLinkedBase()
    a.add_first(1)
    a.add_first(2)
    a.add_first(3)
    x = a.first()
    a.add_be(33,x)
    print(a.first().element)
