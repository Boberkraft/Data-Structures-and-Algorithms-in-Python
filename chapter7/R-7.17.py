"""
In the FavoritesListMTF class, we rely on public methods of the positional
list ADT to move an element of a list at position p to become the first element
of the list, while keeping the relative order of the remaining elements
unchanged. Internally, that combination of operations causes one node to
be removed and a new node to be inserted. Augment the PositionalList
class to support a new method, move to front(p), that accomplishes this
goal more directly, by relinking the existing node.
"""

from FavoritesList import FavoritesList
from PositionalList import PositionalList


class FavoritesListMTF(FavoritesList):
    def _move_up(self, p):
        # if p != self._data.first():
        #     self._data.add_first(self._data.delete(p))
        if p != self._data.first():
            # repair neighborughood
            node = p._node
            node.prev.next, node.next.prev = node.next.prev, node.prev.next
            # move to front
            node.prev = node.container._header
            node.next = node.prev.next
            node.container._header.next, node.container._header.next.prev = node, node

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Ilegal value for k")

        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            highPos = temp.fist()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)
