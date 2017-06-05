"""
The shuffle method, supported by the random module, takes a Python
list and rearranges it so that every possible ordering is equally likely.
Implement your own version of such a function. You may rely on the
randrange(n) function of the random module, which returns a random
number between 0 and n−1 inclusive.

put all card on desk and then pick one until picked all


How to check that every possible ordering is equally likely?
"""
from random import randint


def shuffle(data):
    for where_1 in range(len(data)):
        where_2 = randint(where_1, len(data)-1)
        data[where_1], data[where_2] = data[where_2], data[where_1]

data = list(range(100))
shuffle(data)
print(data)