"""
Suppose two binary trees, T1 and T2, hold entries satisfying the heap-order
property (but not necessarily the complete binary tree property). Describe
a method for combining T1 and T2 into a binary tree T, whose nodes hold
the union of the entries in T1 and T2 and also satisfy the heap-order property.
Your algorithm should run in time O(h1 +h2) where h1 and h2 are
the respective heights of T1 and T2.

So i do not need to satisfy the complete binary tree property? Niceee

Make a new tree using T1 as left subtree and T2 as right subtree.

Move last item to root and do downheap().
 
It's O(x), where x is the height of T1 or T2
"""
