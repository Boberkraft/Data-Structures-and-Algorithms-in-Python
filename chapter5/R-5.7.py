"""
Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive,
with exactly one repeated. Describe a fast algorithm for finding the
integer in A that is repeated.

i think there was a question like this before.
My solution is O(n)
1. a <- Sum all the numbers
2. b <- Use formula for sumarization (n^2 + n)/2
3. answer = a - b
"""