
class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def _get_num(self, k):
        return self._seq[k]

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._get_num(self._k)
        else:
            self._k = -1
            raise StopIteration()
    def __iter__(self):
        return self

if __name__ == '__main__':
    my = SequenceIterator([1,2,3,4,5,6])
    print(my)
    for x in my:
        print(x)
