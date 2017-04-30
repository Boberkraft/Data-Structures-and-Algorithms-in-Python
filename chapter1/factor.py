from math import sqrt

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n//k
        k += 1
    if k * k == n:
        yield k

def factors_my(n):
    k = 1
    while k < sqrt(n):
        if n % k == 0:
            yield k
            yield n//k
        k += 1
    if k * k == n:
        yield k

if __name__ == '__main__':
    for fac in factors_my(25):
        print(fac)
