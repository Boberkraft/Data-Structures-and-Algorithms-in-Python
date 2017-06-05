from random import shuffle
from copy import copy

def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


def insertion_sort_reversed(A):
    for k in range(len(A)-1, -1, -1):

        cur = A[k]
        j = k
        while j > 0 and A[j - 1] < cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


if __name__ == '__main__':
    data = list(range(10))
    shuffle(data)

    print('Random data:', data)

    insert = copy(data)
    insertion_sort(insert)
    print('Normal insertion_sort:', insert)

    insert_reversed = copy(data)
    insertion_sort_reversed(insert_reversed)
    print('not normal insertion_sort:', insert_reversed)