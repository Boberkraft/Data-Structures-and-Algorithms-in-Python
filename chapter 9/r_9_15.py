"""
Let T be a complete binary tree such that position p stores an element
with key f (p), where f (p) is the level number of p (see Section 8.3.2). Is
tree T a heap? Why or why not?


Yes, because each child will have a position at least greater by 1 or 2 than its parent.

For reminder:
If p is the root of T, then f (p) = 0.
• If p is the left child of position q, then f (p) = 2 f (q)+1.
• If p is the right child of position q, then f (p) = 2 f (q)+2.
"""