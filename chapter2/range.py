from collections import Sequence

class Range(Sequence):
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._length = (stop - start + abs(step) - 1) // step
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __contains__(self, item):
        return (item * self._step % self._length) != 0

    def __getitem__(self, item):
        if item < 0:
            item += len(self)

        if not 0 <= item < self._length:
            raise IndexError('Index out of range')

        return self._start + item * self._step

if __name__ == '__main__':
    print(4 in Range(10), 4 in range(10))
    print(0 in Range(2, 10), 0 in range(1, 10))
    print(-1 in Range(-2, 10), -1 in range(-2, 10))
    print(9999999 in Range(9999999), 9999999 in range(9999999))

    print('-' * 10)
    print(len(Range(-5, 6, 4)), len(range(-5, 6, 4)))
    print(len(Range(5, 0, -1)), len(range(5, 0, -1)))
    print(len(Range(0, 5, 4)), len(range(0, 5, 4)))
    print(len(Range(9, -9, -1)), len(range(9, -9, -1)))
    print(len(Range(-1, 9, 1)), len(range(-1, 9, 1)))
    print(len(Range(2, 10, 2)), len(range(2, 10, 2)))
    print(len(Range(2, 23, 3)), len(range(2, 23, 3)))
    print(len(Range(-32, 23, 1)), len(range(-32, 23, 1)))
    print('-'*10)
    for x in range(5, 0, -1):
        print(x)

