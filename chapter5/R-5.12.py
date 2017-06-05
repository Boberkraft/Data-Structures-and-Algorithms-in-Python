"""Describe how the built-in sum function can be combined with Python’s
comprehension syntax to compute the sum of all numbers in an n×n data
set, represented as a list of lists

I will just do it!"""


if __name__ == '__main__':
    n = 10
    data = [[1 for _ in range(n)] for _ in range(n)]

    print(sum([sum(row) for row in data]))
    