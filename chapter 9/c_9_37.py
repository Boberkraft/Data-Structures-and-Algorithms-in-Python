"""
Give an alternative analysis of bottom-up heap construction by showing
the following summation is O(1), for any positive integer h:

sum (x ^ i) for i...h
x = 1/2

sum (x ^ i) for i...h < sum (x ^ i) for i...inf
                      < (1)/(1 - 1/2) = 2, infinite sum of a geometric series
                      2 is O(1)
"""
