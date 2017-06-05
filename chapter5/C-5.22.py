"""
Develop an experiment to compare the relative efficiency of the extend
method of Python’s list class versus using repeated calls to append to
accomplish the equivalent task

extend is about 10 times faster.
"""
from time import time


def method1():
    global _data
    data = _data[:]
    out = []
    for el in data:
        out.append(el)
    return out

def method2():
    global _data
    data = _data[:]
    out = []
    out.extend(data)
    return out


def ctest(func):
    tests = 5
    start = time()
    for _ in range(tests):

        func()
    end = time() - start
    end /= tests
    print('{}, n = {} merging per second:{:,.0f}, time: {}'.format(func.__name__,
                                                                          10 ** 6,
                                                                          10 ** 6/(end),
                                                                          end))

_data = [el for el in range(9*10 ** 6)]

if __name__ == '__main__':
    functions = [method1, method2]
    for func in functions:
        ctest(func)
