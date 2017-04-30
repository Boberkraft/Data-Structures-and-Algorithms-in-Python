# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def squere_odd(n):
    sum = 0
    for num in range(1, n):
        if num % 2 == 1:
            sum += num * num
    return sum

if __name__ == '__main__':
    # 1 9
    print(squere_odd(5))