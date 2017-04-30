from progression import Progression

class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

if __name__ == '__main__':
    x = ArithmeticProgression(3)
    x.print_progression(100)
