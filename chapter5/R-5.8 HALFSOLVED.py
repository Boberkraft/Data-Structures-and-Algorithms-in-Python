"""Experimentally evaluate the efficiency of the pop method of Python’s list
class when using varying indices as a parameter, as we did for insert on
page 205. Report your results akin to Table 5.5.

yes. i see. its to fast! How to time it?

K = 0,	    size = 100,	     time_elapsed = 0.2504110336303711 ms
K = 50,	    size = 100,	     time_elapsed = 0.1508951187133789 ms
K = 99,	    size = 100,      time_elapsed = 0.099945068359375 ms
K = 0,	    size = 1000,     time_elapsed = 0.2989768981933594 ms
K = 500,	size = 1000,   	 time_elapsed = 0.2019643783569336 ms
K = 999,	size = 1000,   	 time_elapsed = 0.24979114532470706 ms
K = 0,	    size = 10000,    time_elapsed = 1.7492055892944336 ms
K = 5000,	size = 10000,    time_elapsed = 0.6993293762207031 ms
K = 9999,	size = 10000,	 time_elapsed = -0.5014896392822266 ms
K = 0,	    size = 100000,   time_elapsed = 38.274502754211426 ms
K = 50000,	size = 100000,	 time_elapsed = 13.511872291564941 ms
K = 99999,	size = 100000,	 time_elapsed = -0.5959033966064453 ms
K = 0,	    size = 1000000,	 time_elapsed = 498.03407192230225 ms
K = 500000,	size = 1000000,	 time_elapsed = 34.91640090942383 ms
K = 999999,	size = 1000000,	 time_elapsed = 7.15031623840332 ms


"""
from time import time


def anal(where, size):
    tests = 10000
    start = time()
    for _ in range(tests):
        data = [None] * size
        data.pop(where)
    elapsed = time() - start
    wasted = time()
    for _ in range(tests):
        data = [None] * size
    wasted = time() - wasted
    total = elapsed - wasted
    total /= tests
    print('K = {},\t size = {},\t time_elapsed = {} seconds'.format(where,
                                                                size,
                                                                total*10**6))

for x in range(2, 7):
    size = 10 ** x
    anal(0, size)
    anal(size // 2, size)
    anal(size - 1, size)