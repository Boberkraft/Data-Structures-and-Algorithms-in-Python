"""Prove that when using a dynamic array that grows and shrinks as in the
previous exercise, the following series of 2n operations takes O(n) time:
n append operations on an initially empty array, followed by n pop operations.

n append operation takes O(n) time (book proven it before)

Shrinking the array with pop have fallowing series.
...
256
64
16
4
1

So to shrink array of size 4k to size k we need k cyber dollars to create new array + we need k dollars to 
move k elements from larger array to smaller. Overall 2k cyber dollars.
Since 4k - k involve using 3k elements lets charge every pop operation with 2/3 cyber dollars.
Poping n elements takes 2/3 n time. 2/3 n < c n, for c = 2. 2/3 n is O(n)

Appending n elements takes O(n) time
Poping n elements takes O(n) time
O(n) + O(n) is O(n).
"""


