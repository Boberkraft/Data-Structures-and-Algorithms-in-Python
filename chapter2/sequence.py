from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def __eq__(self, other):
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __lt__(self, other):
        for j in range(len(self)):
            if self[j] > other[j]:
                return True
        return False

    def index(self, val):

        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('Value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


if __name__ == '__main__':
    # XD