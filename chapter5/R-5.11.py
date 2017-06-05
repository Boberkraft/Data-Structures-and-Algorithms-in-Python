"""Use standard control structures to compute the sum of all numbers in an
n×n data set, represented as a list of lists.

Doing this task if feel a couple of next exercises are like: 
solve one https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science :^)
"""


if __name__ == '__main__':
    n = 10
    data = [[1 for _ in range(n)] for _ in range(n)]

    added = 0
    for row in data:
        for col in row:
            added += col

    print(added)