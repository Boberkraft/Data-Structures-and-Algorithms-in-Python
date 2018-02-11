"""
4 Repeat the previous process using recursion. Your method should not
contain any loops. How much space does your method use in addition to
the space used for L?

It depents where is element. If it do not exist addidionals space equals n.
if its first it is O(1)

"""


class PositionalList(DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        @property
        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Positon type")
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, succesor):
        node = super()._insert_between(e, predecessor, succesor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        return self._insert_between(e, self._trainer.prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def _find(self, p, el):
        if p is None:
            return False
            if p.element is el:
                return True
            else:
                return self._find(self.after(p))

    def find(self, e):
        p = self.first()
        return self._find(p, el)
