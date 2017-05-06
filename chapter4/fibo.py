import sys

def bad_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
    if n == 1:
        return 1, 0
    else:
        a, b = good_fibonacci(n-1)
        return a+b, a

def fib(n):
    if n == 1:
        return 1, 0
    else:
        a, b = fib(n - 1)
        return a+b, a
if __name__ == '__main__':
    print(good_fibonacci(7))
    print(fib(7))