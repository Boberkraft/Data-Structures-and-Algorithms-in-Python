"""
Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
"""

def product(m,n):
    if n == 1:
        return m
    return m + product(m, n-1)

if __name__ == '__main__':
    print(product(10,5))