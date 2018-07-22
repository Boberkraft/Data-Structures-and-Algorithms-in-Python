"""
 Perform experiments on our ChainHashMap and ProbeHashMap classes
to measure its efficiency using random key sets and varying limits on the
load factor (see Exercise R-10.15)

...

 Our HashMapBase class maintains a load factor λ ≤ 0.5. Reimplement
that class to allow the user to specify the maximum load, and adjust the
concrete subclasses accordingly.

At Load:0.8+ the probehashmap is worse
"""
from random import randint
from itertools import product
from time import time
from random import shuffle
from ChainHashMap import ChainHashMap
from ProbeHashMap import ProbeHashMap

data = [randint(0, 1000000000) for num in range(1000000)]

load_factors = (
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
)

size_factors = (
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
)

for size, load in product(size_factors, load_factors):
    print('\nSize:{}, Load:{}'.format(size, load))

    for method in (ChainHashMap, ProbeHashMap):
        obj = method(load_factor=load)
        start = time()
        for el in data[:size]:
            obj[el] = None
        end = time() - start
        print('-> {}\t {:.2f}s'.format(method.__name__, end))
