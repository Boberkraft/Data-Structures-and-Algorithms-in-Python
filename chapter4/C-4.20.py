"""
Given an unsorted sequence, S, of integers and an integer k, describe a
recursive algorithm for rearranging the elements in S so that all elements
less than or equal to k come before any elements larger than k. What is
the running time of your algorithm on a sequence of n values?

i coud sort -> n log n

or create 2 list and append new numbers to them. At the end merging them

ok i have new idea.
Have 2 searchers that search from left and right
if left searcher finds number >= k, 
he starts right searcher thats returns to him index of num lesser than k

every my 
"""

def _solve(seq, k, left, right):
    if left < right:
        if seq[left] >= k:
            if seq[right] < k:
                # swap
                seq[left], seq[right] = seq[right], seq[left]
            else:
                # move right searcher to left and try again
                _solve(seq, k, left, right - 1)
                return  # end live here
        # nothing to swap
        _solve(seq, k, left + 1, right)

def solve(seq, k):
    _solve(seq, k, 0, len(seq)-1)

if __name__ == '__main__':
    data = list(range(10,0, -1))
    print(data)
    solve(data, 5)
    print(data)




