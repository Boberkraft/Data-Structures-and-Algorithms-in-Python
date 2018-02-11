from DoublyLinkedBase import DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next.element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev.element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header.next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer.prev)


