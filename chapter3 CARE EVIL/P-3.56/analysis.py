from examples import *
from time import time
from math import log
functions = [example5]

def anal(test1, test2):
    ans = []
    for f in functions:
        start = time()
        _ = f(test1, test2)
        end = time()
        yield end - start

if __name__ == '__main__':
    for y in range(0, 100):
        x = [1]* int(10**(y/10))
        print('For x = {}'.format(y))
        for out in anal(x, x):
            out += 0.01
            print(log(out, 10), end='\t')
        print('')
