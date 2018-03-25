"""
Professor Idle suggests the following solution to the previous problem.
Whenever an item is inserted into the queue, it is assigned a key that is
equal to the current size of the queue. Does such a strategy result in FIFO
semantics? Prove that it is so or provide a counterexample.

Funny think is that i firstly wanted to do it this way ;p
 
Lets consider this sequence:
add(a) -> 1
add(b) -> 2
add(c) -> 3
add(d) -> 4
add(e) -> 5

remove_min() -> a
remove_min() -> b
remove_min() -> c
remove_min() -> d

add(f) -> 2

remove_min() -> ?
So now, what should you get?
You inserted e earlier whan f, but f have a lower key!

So:
remove_min() -> f
but should:
remove_min() -> e
"""
