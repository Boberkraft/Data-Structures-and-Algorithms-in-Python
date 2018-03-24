class DoublyLinkedBase:
    class _Note:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Note(None, None, None)
        self._trailer = self._Note(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Note(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element

    def reverse(self):
        node = self._header
        for _ in range(len(self)+2):
            node.next, node.prev = node.prev, node.next
            node = node.prev

        self._header, self._trailer = self._trailer, self._header
