"""
Suppose you are given an n-element sequence, S, containing distinct integers
that are listed in increasing order. Given a number k, describe a
recursive algorithm to find two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?

Pick first number from left.
Pick first number from end.
If their sum is < K:
    pick next on left
    try again
elif its > K
    pick next from end
    try again
elif its == K:
    you found your pair :)
    
Running time O(n/2)

"""


def _find(seq, left, right, k):
    if left >= right:
        return False
    s = seq[left] + seq[right]
    if s < k:
        left += 1
    elif s > k:
        right -= 1
    else:
        return seq[left], seq[right]
    return _find(seq, left, right, k)



def find(seq,k):
    """
    Returns two integers in S that sum to k if sucha pair exist
    
    :param seq: seq of ascending unique integers
    :param k: number to find
    :returns tuple of number that sum to k
    :return: False if not found, 
    """
    return _find(seq, 0, len(seq) - 1, k)

if __name__ == '__main__':
    data = list(range(2,10))
    print(find(data, 7))

