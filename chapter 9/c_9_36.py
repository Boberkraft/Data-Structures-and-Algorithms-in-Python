"""
Provide a justification of the time bounds in Table 9.4.



|---------------------|-------------------|
|     Operation       |     Running Time  |
|---------------------|-------------------|
|     len(P),         |                   | 
|     P.is empty( )   |        O(1)       |
|     P.min()         |                   |
|---------------------|-------------------|
|     P.add(k,v)      |       O(logn)∗    |
|---------------------|-------------------|
| P.update(loc, k, v) |       O(logn)     |
|---------------------|-------------------|
|     P.remove(loc)   |       O(logn)∗    |
|---------------------|-------------------|
|     P.remove min()  |       O(logn)*    |
|-----------------------------------------|

∗amortized


Lenght is stored is separete variable.
Fetching it costs constant time

is_empty() is just fetching lenght

min is just fetching first element of an array.

add() is just upheap, and we know that is log n 
remove_min() is just downheap, and we know that is log n
 
remove(loc) is just calls downheap or upheap. In the worst case it will move 
through whole heap, thus O(log n)

update just replaces a number in array and calls downheap or upheap. In the worst case it will move 
through whole heap, thus O(log n)

Everything is amortized because sometimes we need to resize the underlying array,
but from earlier chapter we know that is's O(1)
"""
