# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

def squere(n):
    return sum([num*num for num in range(1, n)])

if __name__ == '__main__':
    print(squere(5))
