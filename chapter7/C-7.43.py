"""
Describe a method for performing a card shuffle of a list of 2n elements,
by converting it into two lists. A card shuffle is a permutation where a list
L is cut into two lists, L1 and L2, where L1 is the first half of L and L2 is the
second half of L, and then these two lists are merged into one by taking
the first element in L1, then the first element in L2, followed by the second
element in L1, the second element in L2, and so on.

this guestion looks a little bit out of topic
"""


def card_shuffle(l):
    middle = len(l) // 2
    left = l[:middle]
    right = l[middle:]
    new = []
    for i in range(middle):
        new.append(left[i])
        new.append(right[i])
    new += l[2 * middle:]
    return new


print(card_shuffle([1, 2, 3, 4, 5, 6]))
