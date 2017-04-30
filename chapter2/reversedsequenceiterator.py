from sequenceiterator import SequenceIterator

class ReversedSequenceIterator(SequenceIterator):

    def __init__(self, seq):
        super().__init__(seq)

    def _get_num(self, k):
        return super()._get_num(-(k + 1))

if __name__ == '__main__':
    seq = ReversedSequenceIterator([1,2,3,4,5,6])
    for x in seq:
        print(x)
