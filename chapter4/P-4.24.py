"""
Write a program for solving summation puzzles by enumerating and testing
all possible configurations. Using your program, solve the three puzzles
given in Section 4.4.3.
"""
from copy import copy


def puzzle_solver(a, b, aplusb, max_letters = None):
    """Max letter is range of numbers you want to use
    eq. to solve some + more = money you need range of 10
    """
    letters = set().union(a, b, aplusb)
    letters = list(letters)
    # print(letters, len(letters))
    if max_letters is not None:
        for _ in range(10 - max_letters):
            # adds letters to ocupy free space
            letters.append(' ')

    def make_val(word, comb):
        """Makes a number from letters with given values"""
        val = 0
        for index, letter in enumerate(word[::-1]):
            if letter != ' ':
                val += comb.find(letter) * 10 ** index
        return val

    def check(comb):
        """Checks if combination makes its job"""
        a_val = make_val(a, comb)
        b_val = make_val(b, comb)
        aplusb_val = make_val(aplusb, comb)
        return a_val + b_val == aplusb_val

    def gen_perms(k, S, U):
        """Generates every possible permutation without repetiton"""

        for e in U:
            new_U = copy(U)
            new_U.remove(e)
            yield from gen_perms(k-1, S + e, new_U)

        if k == 0: # ok. no more letters
            if check(S):
                # combination S is valid
                yield S  # solution found
    # # l
    # def gen_perms2(k, S, U):
    #     """Generates every possible permutation without repetiton"""
    #
    #     for e in copy(U):
    #         U.remove(e)
    #         if k == 0:  # ok. no more letters
    #             if check(S):
    #                 # combination S is valid
    #                 yield S  # solution found
    #         else:
    #             yield from gen_perms(k - 1, S + e, U)




    # it start here
    return gen_perms(len(letters), '', set(letters))


if __name__ == '__main__':
    p = []
    counter = 1
    # for answer in puzzle_solver('send', 'more', 'money'):
    for answer in puzzle_solver('cat', 'dog', 'pig'):
        if answer not in p:
            print('{0:<3}'.format(counter), answer)
            counter += 1
            p.append(answer)



