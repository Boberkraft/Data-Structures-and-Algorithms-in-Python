"""
 Show the result of Exercise R-10.9, assuming collisions are handled by
quadratic probing, up to the point where the method fails.

By the exercise it sounds like this isn't going to be finite!
so no paint :c

...
WHY IT WORKS

... now i saw 16, and 5

...
it fails for 5

it checks (1,2,3,7,9,10) and nothing else

"""
from time import sleep

table = [None] * 11

for x in [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]:
    h = (3 * x + 5)  # <- will mod here change outcome? i think no. Lets check
    mul = 0  # power of 2
    while True:
        hh = (h + mul * mul) % 11
        if table[hh] is None:
            table[hh] = x
            break
        print(mul*mul, h)
        print(hh, 'not empty!', 'for ', x, '[mul =', mul, ']')
        mul += 1
    print(table)
