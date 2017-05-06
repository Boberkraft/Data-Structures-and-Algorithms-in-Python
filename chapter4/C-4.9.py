"""
Write a short recursive Python function that finds the minimum and maximum
values in a sequence without using any loops.
"""
counter = [0,0]

def min_max(seq):
    global counter
    counter[0] += 1

    if len(seq) == 1:
        return seq[0], seq[0]

    if seq[-1] > seq[-2]:
        local_min = seq[-2]
        local_max = seq[-1]
    else:
        local_min = seq[-1]
        local_max = seq[-2]

    if len(seq) > 2:
        other_max, other_min = min_max(seq[:-2])
        if other_max > local_min:
            local_max = other_max
        if other_min < local_max:
            local_min = other_min

    return local_max, other_min

def min_max2(seq, low, high):
    global counter
    counter[1] += 1

    middle = (high+low)//2
    if low + 1 >= high:
        if seq[low] > seq[high]:
            return seq[low], seq[high]
        else:
            return seq[high], seq[low]
    else:
        max_l, min_l = min_max2(seq, low, middle)
        max_r, min_r = min_max2(seq, middle+1, high)
        if max_r > max_l:
            max_l = max_r

        if min_r < min_l:
            min_l = min_r

        return max_l, min_l


if __name__ == '__main__':
    data = list(range(999))
    print(min_max(data))
    print(min_max2(data, 0, len(data)-1))
    print(counter)




