"""
Perform experiments to evaluate the efficiency of the remove method of
Python’s list class, as we did for insert on page 205. Use known values so
that all removals occur either at the beginning, middle, or end of the list.
Report your results akin to Table 5.5.

method1, n = 100, time: 2.5033950805664062
method2, n = 100, time: 2.5033950805664062
method3, n = 100, time: 0.0

method1, n = 1000, time: 20.018815994262695
method2, n = 1000, time: 12.511014938354492
method3, n = 1000, time: 2.5022029876708984

method1, n = 10000, time: 187.6819133758545
method2, n = 10000, time: 110.10408401489258
method3, n = 10000, time: 25.022029876708984

method1, n = 100000, time: 1876.8537044525146
method2, n = 100000, time: 1118.5657978057861
method3, n = 100000, time: 345.46971321105957

method1, n = 1000000, time: 21298.48003387451
method2, n = 1000000, time: 13290.578126907349
method3, n = 1000000, time: 5655.554533004761

how do i make good mesurement? I can mesure list creation and then substract that time, 
but this is not acurate.
"""
from time import time


def method1():
    global _data
    data = _data[:]
    data.remove(data[-1])


def method2():
    global _data
    data = _data[:]
    data.remove(data[len(data)//2])

def method3():
    global _data
    data = _data[:]
    data.remove(data[0])

def ctest(func, size):
    tests = 200
    start = time()
    for _ in range(tests):
        func()
    end = time() - start
    end /= tests
    end *= 10**6

    print('{}, n = {}, time: {}'.format(func.__name__,
                                                                    size,
                                                                    end))



if __name__ == '__main__':
    functions = [method1, method2, method3]
    for size in [100, 1000, 10000, 100000, 1000000]:
        _data = [el for el in range(size)]
        for func in functions:
            ctest(func, size)
        print()
