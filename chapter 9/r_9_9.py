"""
Give an example of a worst-case sequence with n elements for insertionsort,
and show that insertion-sort runs in Ω(n2) time on such a sequence.

Reversed sequence

Because at each `insertion` it needs to go through single item in 'sorted' part.
 
 Firsty 0
 then   1
 then   2
 then   3
  ...
then   n - 3
then   n - 2
then   n - 1

Summing 
1 + 2 + 3 + 4 + ... + (n - 1) => n * n/2 => O(n^2)
 
"""