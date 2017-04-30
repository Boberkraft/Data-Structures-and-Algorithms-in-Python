from progression import Progression
from math import sqrt

class SquareProgression(Progression):

    def __init__(self, val=65536):
        super().__init__(val)

    def _advance(self):
        self._current = sqrt(self._current)


if __name__ == '__main__':
    x = SquareProgression()
    x.print_progression(10)