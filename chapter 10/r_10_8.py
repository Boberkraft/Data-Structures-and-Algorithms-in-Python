"""
What would be a good hash code for a vehicle identification number that
is a string of numbers and letters of the form “9X9XX99X9XX999999,”
where a “9” represents a digit and an “X” represents a letter?

...

move letters at the front (but don't haven order)
XXXXXX99999999999
and then calculate XXXXXX as number in base 26 (without 0-9)
    a -> 0
    b -> 1
    c -> 2
    d -> 3
       ...
and replace said XXXXXX with it.

bravo!
"""
