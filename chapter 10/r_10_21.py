"""
Consider the following variant of the find index method from Code Frag-
ment 10.8, in the context of the SortedTableMap class:

-> find_index1
            
    
Does this always produce the same result as the original version? Justify
your answer.

Yes

Because in new code it finds the searching item like the old code, 
but when it stumbles upon it, then the new top is  

"""

"""
Search for 5 with new code
0 1 2 3 4[5]6 7 8 9 10, [5, 0, 10]
0 1[2]3 4               [5, 0, 4]
     [3]4               [5, 3, 4]
       [4]              [5, 4, 4]
        OH ITS 5        [5, 5, 4]
-------- -> goes to narrowest margin possible on the left side,
 ant then boom report high + 1. and i think low  should work too...
 
 
with oryginal code
0 1 2 3 4[5]6 7 8 9 10, [5, 0, 10]
          OH ITS 5
"""


def find_index1(table, k, low, high):
    if high < low:
        return low
    else:
        mid = (low + high) // 2
        if k > table[mid]:
            return find_index1(table, k, mid + 1, high)
        else:
            return find_index1(table, k, low, mid - 1)


def find_index(table, k, low, high):
    if high < low:
        return high + 1  # no element qualifies
    else:
        mid = (low + high) // 2
        if k == table[mid]:
            return mid  # found exact match
        elif table[mid] < k :
            return find_index(table, k, mid + 1, high)
        else:
            return find_index(table, k, low, mid - 1)  # Note: may return mid

functions = [find_index1, find_index]

for func in functions:
    x = func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 0, 10)
    print(x)
