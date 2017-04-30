# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n

def squere(n):
    sum = 0
    for num in range(1, n):
        sum += num * num
    return sum

if __name__ == '__main__':
    # 1 4 9 16
    print(squere(5))
