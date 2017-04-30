# The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20,...,100.


def calc_prob(people):
    prob = 1
    for x in range(people):
        prob *= (365 - x)/(365)
    return 1 - prob


def _test():
    for people in range(5, 101, 5):
        print('{} => {}'.format(people, calc_prob(people)))


if __name__ == '__main__':
    _test()
