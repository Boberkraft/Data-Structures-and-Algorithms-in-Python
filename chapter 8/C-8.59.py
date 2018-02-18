"""
Let T be a binary tree with n positions, and, for any position p in T, let d_p
denote the depth of p in T. The distance between two positions p and q
in T is d_p + d_q − 2d_a, where a is the lowest common ancestor (LCA) of p
and q. The diameter of T is the maximum distance between two positions
in T. Describe an efficient algorithm for finding the diameter of T. What
is the running time of your algorithm?

Pick a random node (lets say root), and calculate a node with is the farthest from it (lets name it Jhony).
Now lets find for Johny a node with is the farthest from `him`.

O(n)
im lazy because our tree representation isn't a very good choice for my solution 
"""