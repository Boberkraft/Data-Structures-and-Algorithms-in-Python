"""
Describe a nonrecursive algorithm for enumerating all permutations of the
numbers {1,2,...,n} using an explicit stack.

Use a stack to reduce the problem to that of enumerating all
permutations of the numbers {1,2,...,n−1}.

Nonrecursive?
Oh

I just got an idea for norecursive algorithm and writen it XD
Of curse you can use stack for it but im lazy
"""
from ArrayStackBetter import ArrayStack
from math import factorial


def permutate(what):
    to_permutate = [what[0]]
    permutations = []
    digits = what[1:]
    for number in digits:
        for to in to_permutate:
            for index in range(len(to) + 1):
                permutations.append(to[:index] + number + to[index:])
        to_permutate = []
        to_permutate, permutations = permutations, to_permutate
    return to_permutate


# def permutate_stack(what):
#     # fixed lenght
#     size = factorial(len(what))
#     to_permutate = ArrayStack(size)
#     permutations = ArrayStack(size)
#     digits = what[1:]
#     to_permutate.push(what[0])
#
#     for number in digits:
#         while not to_permutate.is_empty():
#             to = to_permutate.pop()
#             for index in range(len(to) + 1):
#                 permutations.push(to[:index] + number + to[index:])
#         to_permutate, permutations = permutations, to_permutate
#         to_permutate._size = 0  # like in deque
#
#     return to_permutate


perms = permutate(['1', '2', '3', '4'])

print(perms, len(perms))
