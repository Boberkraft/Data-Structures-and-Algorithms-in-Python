"""
In Section 5.4.2, we described four different ways to compose a long
string: (1) repeated concatenation, (2) appending to a temporary list and
then joining, (3) using list comprehension with join, and (4) using generator
comprehension with join. Develop an experiment to test the efficiency
of all four of these approaches and report your findings

method1, n = 50000 concatenations per second:6,396
method2, n = 50000 concatenations per second:9,756
method3, n = 50000 concatenations per second:20,770
"""
from time import time


def method1(n):
    out = ''
    for _ in range(n):
        out += 't'

def method2(n):
    out = []
    for _ in range(n):
        out.append('t')
    ''.join(out)

def method3(n):
    ''.join(['t' for _ in range(n)])

def method4(n):
    """So fast!"""
    out = []
    for _ in range(n):
        out += ('t',)
    ''.join(out)

def method5(n):
    ['t'] * n


def ctest(func, n):
    tests = 1
    start = time()
    for _ in range(tests):
        func(n)
    end = time() - start
    end /= tests
    print('{}, n = {} concatenations per second:{:,.0f}, time: {}'.format(func.__name__,
                                              n,
                                              n/(end),
                                              end))

if __name__ == '__main__':
    functions = [method1, method2, method3, method4, method5]
    for func in functions:
        ctest(func, 15*10**6)