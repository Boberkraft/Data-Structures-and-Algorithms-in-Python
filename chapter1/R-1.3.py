# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution

def minmax(data):
    max = data[0]
    min = data[0]
    for num in data:
        if max < num:
            max = num
        if min > num:
            min = num
    return min, max


if __name__ == '__main__':
    print(minmax([1,2,-1,10,6]))
