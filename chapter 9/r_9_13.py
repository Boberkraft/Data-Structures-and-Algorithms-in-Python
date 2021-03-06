"""
Illustrate the execution of the in-place heap-sort algorithm on the following
input sequence: (2,5,16,4,10,23,39,18,26,15).

oh shit my imagination!

Firstly lets build up a heap 
(          x
    x,          x,
  x,    x,  x,   x,
18,26,  15)

(          x,
    x,          x,
  4,    10,  23,   39,
18,26,  15)

(          x,
    x,          x,
  4,    10,  23,   39,
18,26,  15)

(          x,
    5,          16,
  4,    10,  23,   39,
18,26,  15)


Swap 5 and 3
(          x,
    4,          16,
  5,    10,  23,   39,
18,26,  15)

(          2,
    4,          16,
  5,    10,  23,   39,
18,26,  15)

Ok! the heap is constructed!
(2,4,16,5,10,23,39,18,26,15)

Take away 2
(          2,
    4,          16,
  5,    10,  23,   39,
18,26,  15)

(          15,
    4,          16,
  5,    10,  23,   39,
18,26,  #2)


(          4,
    15,          16,
  5,    10,  23,   39,
18,26,  #2)


(          4,
    5,          16,
  15,    10,  23,   39,
18,26,  #2)


(          4,
    5,          16,
  15,    10,  23,   39,
18,26,  #2)

Take away 4
(          26,
    5,          16,
  15,    10,  23,   39,
18,#4,  #2)

(          5,
    26,          16,
  15,    10,  23,   39,
18,#4,  #2)

(          5,
    10,          16,
  15,    26,  23,   39,
18,#4,  #2)

Take away 5
(          18,
    10,          16,
  15,    26,  23,   39,
#5,#4,  #2)

(          10,
    18,          16,
  15,    26,  23,   39,
#5,#4,  #2)

(          10,
    15,          16,
  18,    26,  23,   39,
#5,#4,  #2)

Take away 10
(          10,
    15,          16,
  18,    26,  23,   39,
#5,#4,  #2)

(          39,
    15,          16,
  18,    26,  23,   #10,
#5,#4,  #2)

(          15,
    39,          16,
  18,    26,  23,   #10,
#5,#4,  #2)

(          15,
    18,          16,
  39,    26,  23,   #10,
#5,#4,  #2)

Take away 15
(          23,
    18,          16,
  39,    26,  #15,   #10,
#5,#4,  #2)

(          16,
    18,          23,
  39,    26,  #15,   #10,
#5,#4,  #2)

Take away 16
(          18,
    26,          23,
  39,    #16,  #15,   #10,
#5,#4,  #2)


Take away 18
(          39,
    26,          23,
  #18,    #16,  #15,   #10,
#5,#4,  #2)


(          23,
    26,          39,
  #18,    #16,  #15,   #10,
#5,#4,  #2)

Take away 23
(          39,
    26,          #23,
  #18,    #16,  #15,   #10,
#5,#4,  #2)

(          26,
    39,          #23,
  #18,    #16,  #15,   #10,
#5,#4,  #2)

Take away 26
(          39,
    #26,          #23,
  #18,    #16,  #15,   #10,
#5,#4,  #2)

Take away 39
(          #39,
    #26,          #23,
  #18,    #16,  #15,   #10,
#5,#4,  #2)
=> Its sorted!
(#39,#26,#23,#18,#16,#15,#10,#5,#4,#2)


Maybe writing a program to visualize this would be faster than manually writing this?
Who knows...
"""