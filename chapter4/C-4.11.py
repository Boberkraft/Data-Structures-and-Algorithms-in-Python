"""
Describe an efficient recursive function for solving the element uniqueness
problem, which runs in time that is at most O(n2) in the worst case
without using sorting.
"""

def unique(seq, start, stop):
    """It cheack every availivable pari
    
    but its not real recursive!"""

    if start == stop:
        return True

    for i in range(start+1, stop):
        if seq[start] == seq[i]:
            return False

    return unique(seq, start+1, stop)




if __name__ == '__main__':
    seq = list(range(60))
    seq[33] = 2
    print(unique(seq, 0, len(seq)))
