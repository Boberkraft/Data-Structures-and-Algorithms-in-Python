"""
Describe an in-place version of the selection-sort algorithm for an array
that uses only O(1) space for instance variables in addition to the array.
"""


def insertion_sort(data):
    for i in range(1, len(data)):
        offset = i
        while offset - 1 >= 0 and data[offset - 1] > data[offset]:
            data[offset - 1], data[offset] = data[offset], data[offset - 1]
            offset -= 1
