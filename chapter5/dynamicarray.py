import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __str__(self):
        return '[' + ', '.join([str(self._A[i]) for i in range(self._n)]) + ']'

    def __repr__(self):
        return '{} Size: {}, Capacity: {}'.format(self, len(self), self._capacity)
    def __getitem__(self, item):
        if not -self._n <= item < self._n:
            raise IndexError('Invalid index')
        if item < 0:
            item = self._n + item
        return self._A[item]


    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2* self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            # self._resize(2 * self._capacity)
            B = self._make_array(2 * self._capacity)
        for j in range(self._n, k, -1):
            self.B[j] = self._A[j-1]
        self.B[k] = value
        self._A = B
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()



if __name__ == '__main__':
    a = DynamicArray()
    a.append(1)
    a.append(2)
    a.append(3)
    for x in a:
        print(x)
    print(a[-1])
    print(a[-2])
    print(a[-3])
    print('Testing pop')
    b = DynamicArray()
    for num in range(10):
        b.append(num)
    for _ in range(10):
        print(b.pop(), 'n =', b._n)