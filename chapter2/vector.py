from copy import deepcopy

class Vector:

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = [0] * len(d)
            for index, x in enumerate(d):
                self._coords[index] = x


    def __len__(self):
        return len(self._coords)

    def __getitem__(self, key):
        return self._coords[key]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def check_dim(self, other):
        if len(self) != len(other):
            raise ValueError('Dimenions must agree')

    def __add__(self, other):
        self.check_dim(other)

        result = Vector(len(self))
        for key in range(len(self)):
            result[key] = self[key] + other[key]
        return result

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.check_dim(other)

        result = Vector(len(self))
        for key in range(len(self)):
            result[key] = self[key] - other[key]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __mul__(self, other):
        try:
            iter(other)
        except TypeError:
            result = Vector(len(self))
            result._coords = self._coords[:]
            for index in range(len(result)):
                result[index] *= other
            return result
        else:
            return self._mul_vectors(other)

    def _mul_vectors(self, other):
        print('xd')
        self.check_dim(other)
        result = 0
        for index in range(len(other)):
            result += self[index] * other[index]
        return result

    def __rmul__(self, other):
        return self * other

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return Vector(len(self)) - self

    def __str__(self):
        return '<{}>'.format(str(self._coords)[1:-1])

if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(total)
    print(u)
    print(v)
    print(u - v - v)
    print(-u)
    print(u + [1, 2, 3, 4, 1])
    print([1, 2, 3, 4, 1] + u)
    print(u * 3)
    print(3 * u)
    print(u*u)
    print(Vector([1,2,3]))
