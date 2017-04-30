# Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.

def squere_odd(n):
    return sum(num * num for num in range(1, n) if num % 2 == 1)

if __name__ == '__main__':
    print(squere_odd(5))