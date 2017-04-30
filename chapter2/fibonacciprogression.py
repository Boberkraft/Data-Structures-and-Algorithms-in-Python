from progression import Progression

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev =  second - first

    def _advance(self):
        a = self._prev
        b = self._current
        self._prev, self._current = b, a + b

if __name__ == '__main__':
    x = FibonacciProgression()
    x.print_progression(100)
