"""
Modify the experiment from Code Fragment 5.1 in order to demonstrate
that Python’s list class occasionally shrinks the size of its underlying array
when elements are popped from a list.
"""
from sys import getsizeof

data = []
size = 40

data = [None] * size

for _ in range(len(data)):
    print('Size:', len(data), 'Allocated bytes:', getsizeof(data))
    data.pop()
