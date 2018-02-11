"""
A useful operation in databases is the natural join. If we view a database
as a list of ordered pairs of objects, then the natural join of databases A
and B is the list of all ordered triples (x,y,z) such that the pair (x,y) is in
A and the pair (y,z) is in B. Describe and analyze an efficient algorithm
for computing the natural join of a list A of n pairs and a list B of m pairs.

If we can sort the database its O(n log n)
"""
from random import shuffle
from copy import copy

def method1(data1, data2):
    # complexity O(n^2)
    new = []
    for a in data1:
        for b in data2:
            if a[1] == b[0]:
                new.append((a[1], a[0], b[1]))
    return new

def method2(data1, data2):
    # complexity O(n)
    # data must be hashable.
    hash = {}
    new = []
    for index, el in enumerate(data1):
        hash[el[1]] = index
    print(hash)
    for el in data2:
        if el[0] in hash:
            new.append((el[0], data1[hash[el[0]]][0], el[1]))
    return new

data_a = [('a', num) for num in range(10)]
data_b = [(num, 'b') for num in range(10)]
shuffle(data_a)
shuffle(data_b)
# print(data_a)
# print(data_b)
# print(method1(copy(data_a), copy(data_b)))
print(method2(copy(data_a), copy(data_b)))

