"""
Write a key function for nonnegative integers that determines order based
on the number of 1’s in each integer’s binary expansion.
"""

def count_bits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count

class _Key:
    def __init__(self, k):
        self.k = k

    def __lt__(self, other):
        return count_bits(self.k) < count_bits(other.k)

    def __gt__(self, other):
        return count_bits(self.k) > count_bits(other.k)
