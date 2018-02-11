from FavoritesList import FavoritesList
from PositionalList import PositionalList

class FavoritesListMTF(FavoritesList):
    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

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
