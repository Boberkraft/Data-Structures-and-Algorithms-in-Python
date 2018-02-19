# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

# coming back in time: i cant look at this
def is_even(k):
    start = k
    while True:
        k -= 2
        if k < 0:
            return False
        elif k == 0:
            return True


def is_even2(k):
    return bool(k ^ 0)


if __name__ == '__main__':
    print(is_even(12))
    print(is_even2(10))
