from prefix import *
from time import time
from math import log
functions = [prefix_average1, prefix_average2, prefix_average3]

print(prefix_average1([1,2,3,4,]))
def anal(test):
    ans = []
    for f in functions:
        start = time()
        _ = f(test)
        end = time()
        yield end - start

if __name__ == '__main__':
    for y in range(0, 100):
        x = [1]* int(10**(y/10))
        print('For x = {}'.format(y))
        for out in anal(x):
            out += 0.01
            print(log(out, 10), end='\t')
        print('')
