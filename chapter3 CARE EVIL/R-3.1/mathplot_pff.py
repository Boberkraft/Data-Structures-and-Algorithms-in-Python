
from pylab import *
from math import log
import math
import matplotlib.pyplot as plt


def f_1(n):
    """FUNCTION 8n"""
    return n * 8

def f_2(n):
    """FUNCTION 4n log n"""
    return 4 * n * log(n, 2)

def f_3(n):
    """FUNCTION 2 n^2"""
    return 2 * n**2

def f_4(n):
    """FUNCTION n^3"""
    return n ** 3

def f_5(n):
    """FUNCTION 2^n"""
    return 2**n

plt.yscale('log')
plt.xscale('log')

if __name__ == '__main__':
    xes = [10**exp for exp in range(3)]
    functions = [f_1, f_2, f_3, f_4, f_5]
    for function in functions:
        print(function.__doc__)
        for x in xes:
            x += 1
            plt.plot(function(x), x)



plt.show()