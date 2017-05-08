"""
Develop a nonrecursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring
"""

def power(x, n):
    result = 1
    while n > 2:
        if n % 2 == 1:
            x = x * x
        n = n//2
        x = x * x

    return x*x

if __name__ == '__main__':
    print(power(2,8))
    print(2**8)