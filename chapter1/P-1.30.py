# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

if __name__ == '__main__':

    while True:
        x = int(input('Write an int > 2: '))
        if x > 2:
            break

    res = 0
    while x < 1:
        res -= 1
        x *= 2
    while x >= 2:
        res += 1
        x /= 2

    max = 1e-13
    fp = 1
    while fp > max:
        fp /= 2
        x *= x
        print(x)
        if x >= 2:
            x /= 2
            res += fp

    print(res)
