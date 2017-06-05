"""
Give a formal proof that any sequence of n append or pop operations on
an initially empty dynamic array takes O(n) time, if using the strategy
described in Exercise C-5.16.

Array shrinking takes O(n), and the array shrinks always at the starting point where
an ressizing before started(n), still leaving place for appending n items without resizing.
. is nonempty element
, is empty element
................................ 32/0
shrinking occurs
........,,,,,,,, 8/8

expands at
1
2
4
8
16
32
64
128
256
512
1024

and 4k shrinks at 2k to k
1
4
16
64
256
1024


"""