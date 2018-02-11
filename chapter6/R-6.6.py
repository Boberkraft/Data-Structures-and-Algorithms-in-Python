"""
Give a precise and complete definition of the concept of matching for
grouping symbols in an arithmetic expression. Your definition may be
recursive

Go from left to right. Every grouping symbol must begin with oppening and the ending.
At any given time there cannot be more ending than oppenings of the same type.
Diference of opening and ending symbols must be 0
There cannot be difrent type of ending than last type of oppening encountered
(to prevent e.g. [2+(3-]+1)  )
"""

