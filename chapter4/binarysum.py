def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop)//2
        return binary_sum(S, start,mid) + binary_sum(S, mid, stop)

if __name__ == '__main__':
    data = [1,2,3,4]
    print(binary_sum(data, 0 ,len(data)))