"""
0 Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 had been implemented as:
for k in range(self. size):
self. data[k] = old[k] # rather than old[walk]
Give a clear explanation of what could go wrong.

If the ArrayQueue have ever been dequeued it will have elements on wrong positions.
Especialy if the ArrayQueue have wraped arround
"""

