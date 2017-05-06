def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1

if __name__ == '__main__':
    a = list(range(25))
    print(a)
    reverse_iterative(a)
    print(a)