
def reverse(S, start, stop):
    if start >= stop:
        return

    S[start], S[stop-1] = S[stop-1], S[start]
    reverse(S, start + 1, stop - 1)

if __name__ == '__main__':
    data = list(range(9))
    print(data)
    reverse(data, 0, len(data))
    print(data)