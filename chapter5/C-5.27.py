"""
Given a Python list L of n positive integers, each represented with k =
ceil(log n)+ 1 bits, describe an O(n)-time method for finding a k-bit integer
not in L.

"""
from math import log2, ceil
from random import shuffle
from random import randrange

def find_missing(data):
    def ar_seq(n, first, last):
        """
        https://mathbitsnotebook.com/Algebra2/Sequences/SSArithmetic.html
        number of terms times the average of the first and last terms    
        """
        n = int(n)
        first = int(first)
        last = int(last)
        return (n*(first + last))/2

    bits = ceil(log2(len(data))) + 1
    # sum of all k bits numbers
    sum_all_k_bits = ar_seq(2**(bits-1), 2 ** (bits - 1), 2 ** bits - 1)
    return int(sum_all_k_bits) - sum(data)

if __name__ == '__main__':

    n = 16
    data = list(range(n, n * 2))
    shuffle(data)
    print('Removing:', data.pop())

    missing = find_missing(data)
    print('Missing:', missing)
