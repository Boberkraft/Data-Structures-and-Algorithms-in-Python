"""
 What is the expected running time of the methods for maintaining a max-
ima set if we insert n pairs such that each pair has lower cost and perfor-
mance than one before it? What is contained in the sorted map at the end
of this series of operations? What if each pair had a lower cost and higher
performance than the one before it?

It depends on used data structure!
using SortedTableMap
Former:
Using a table its O(n^2) and it cointains all pairs
because it used binary search!

second:
O(n) and there is only one element  

When using skip list
Former:
For every inserted element in need to check if there is one with better performance
for the same cost. Since every element is sorted, then we only need to chect the first ->
we then see that we cant really compare the first element and that that we need to insert,
 we just put it at the front.
 
So O(n) 

Second:
O(n)

"""