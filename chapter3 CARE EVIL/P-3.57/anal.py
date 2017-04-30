"""
Perform experimental analysis to test the hypothesis that Python’s sorted
method runs in O(nlogn) time on average.
"""
from time import time
from random import shuffle
from math import log



# Converges to zero? Then your guess is too high. Repeat with something smaller (e.g. nlogn)
# Diverges to infinity? Then your guess is too low. Repeat with something bigger (e.g. n^3)
# Converges to a positive constant? Bingo! Your guess is on the money (at least approximates the theoretical complexity for as large n values as you tried)
if __name__ == '__main__':

    for n in range(2, 100000000, 10000):
        test = list(range(int(n)))
        shuffle(test)
        start = time()
        sorted(test)
        elapsed = time() - start
        print('{0:.50f}'.format(elapsed/(n*log(n, 2))))

# it keept increesing and increasing! but never actually larger than 0.000000041