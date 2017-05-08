"""
Provide a nonrecursive implementation of the draw interval function for
the English ruler project of Section 4.1.2. There should be precisely 2c−1
lines of output if c represents the length of the center tick. If incrementing
a counter from 0 to 2c −2, the number of dashes for each tick line should
be exactly one more than the number of consecutive 1’s at the end of the
binary representation of the counter
"""

try:
    from ruler import draw_interval
except ImportError:
    print('Sorry no func draw_interval')
    draw_interval = lambda x: x


def iter_draw_interval(c):
    lines = 2**c-1  # lines needed to be printed
    for x in range(lines):
        print('-', end='')
        while x & 1 == 1:
            # if last digit in one
            x = x >> 1  # remove last digit
            print('-', end='')
        print()

if __name__ == '__main__':
    num = 4
    draw_interval(num)
    print('*'*10)
    iter_draw_interval(num)