# But Al Khwarizmi knew another way to multiply, a method which is used today in some
# European countries. To multiply two decimal numbers x and y, write them next to each
# other, as in the example below. Then repeat the following: divide the first number by 2,
# rounding down the result (that is, dropping the .5 if the number was odd), and double the
# second number. Keep going till the first number gets down to 1. Then strike out all the rows
# in which the first number is even, and add up whatever remains in the second column.


def mul(x, y):
    if x == 0:
        return 0
    if x % 2 == 0:
        return mul(x//2, y*2) + 0
    else:
        return mul(x//2, y*2) + y

def mul2(x ,y):
    if y == 0:
        return 0
    z = mul2(x, y//2)
    if y % 2 == 0:
        return 2 * z
    else:
        return x + 2*z

def mul3(x, y):
    base = x
    for _ in range(y-1):
        x += base
    return x

if __name__ == '__main__':
    print(mul(11, 13))
    print(mul2(13, 11))
    print(mul3(13, 11))

