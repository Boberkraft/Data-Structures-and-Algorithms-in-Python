"""
Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division
"""


def int_log(num, counter=0):
    if num > 1:
        return int_log(num//2, counter+1)
    else:
        return counter

if __name__ == '__main__':
    num = 2**64
    print(int_log(num))