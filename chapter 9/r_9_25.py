"""
Complete Figure 9.9 by showing all the steps of the in-place heap-sort
algorithm. Show both the array and the associated heap at the end of each
step.


(     9,
   7,    5,
2,   6,     4)


MOVE OUT
(     4,
   7,    5,
2,   6,     #9)

DOWNHEAP
(     7,
   4,    5,
2,   6,     #9)

DOWNHEAP
(     7,
   6,    5,
2,   4,     #9)


MOVE OUT
(     4,
   6,    5,
2,   #7,     #9)

DOWNHEAP
(     6,
   4,    5,
2,   #7,     #9)


MOVE OUT
(     2,
   4,    5,
#6,   #7,     #9)

DOWNHEAP
(     5,
   4,    2,
#6,   #7,     #9)


MOVE OUT
(     2,
   4,    #5,
#6,   #7,     #9)

DOWNHEAP
(     4,
   2,    #5,
#6,   #7,     #9)


MOVE OUT
(     2,
   #4,    #5,
#6,   #7,     #9)


MOVE OUT
(     #2,
   #4,    #5,
#6,   #7,     #9)









"""
