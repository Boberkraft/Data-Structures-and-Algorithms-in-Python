from progression import Progression

class AbsoluteProgression(Progression):

    def __init__(self, first=2,  second=200):
        super().__init__(first)
        self._second = second

    def _advance(self):
        self._current, self._second = abs(self._second - self._current), self._current


if __name__ == '__main__':
    x = AbsoluteProgression()
    x.print_progression(100)