def unique3(S, start, stop):
    what = data[start: stop]
    if stop - start <= 1:
        return True
    elif not unique3(S, start, stop-1):
        return False
    elif not unique3(S, start+1, stop):
        return False
    else:
        return S[start] != S[stop - 1]

if __name__ == '__main__':
    # it is realy sloow
    data = [1,2]
    # data[3] = 1
    print(unique3(data, 0, len(data)))