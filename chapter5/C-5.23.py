"""
Based on the discussion of page 207, develop an experiment to compare
the efficiency of Python’s list comprehension syntax versus the construction
of a list by means of repeated calls to append.

list comprehension is about 2 times faster

method1, n = 1000000 elements per second:16,513,190, time: 0.06055765151977539
method2, n = 1000000 elements per second:8,896,219, time: 0.11240730285644532
"""
from time import time


def method1(n):
    return [el for el in range(n)]

def method2(n):
    out = []
    for el in range(n):
        out.append(el)
    return out

def ctest(func, n):
    tests = 5
    start = time()
    for _ in range(tests):
        func(n)
    end = time() - start
    end /= tests
    print('{}, n = {} elements per second:{:,.0f}, time: {}'.format(func.__name__,
                                                                          n,
                                                                          n/(end),
                                                                          end))



if __name__ == '__main__':
    functions = [method1, method2]
    for func in functions:
        ctest(func, 10**6)
