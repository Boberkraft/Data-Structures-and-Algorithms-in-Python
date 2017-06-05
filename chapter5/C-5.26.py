"""
Let B be an array of size n ≥ 6 containing integers from 1 to n−5, inclusive,
with exactly five repeated. Describe a good algorithm for finding the
five integers in B that are repeated

is only that five integeres repeated? 
"""
from random import shuffle

def find_rep(data):
    data = sorted(data)
    counter = 0
    last = data[0]  # added variable for clearability
    for i in range(1, len(data)):
        if last == data[i]:
            counter += 1
        else:
            if counter == 5:
                return last
            counter = 0
            last = data[i]
    if counter == 5:
        return last


if __name__ == '__main__':
    data = list(range(1, 10))
    data[5:] = [5] * 5
    shuffle(data)
    print(find_rep(data))
    print(data, len(data))