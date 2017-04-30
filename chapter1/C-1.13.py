# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def reverse(seq):
    for index in range(len(seq)-1, -1, -1):
        yield seq[index]

if __name__ == '__main__':
    print(list(reverse('abcd')))
    print(list(reversed('abcd')))

