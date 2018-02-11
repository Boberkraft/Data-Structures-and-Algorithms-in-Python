"""
9 Give a proof by induction of Proposition 8.9.

Proposition 8.9:
In a nonempty proper binary tree T, with nE external nodes and
nI internal nodes, we have nE = nI +1.

n = nodes of a tree

(*) e = i + 1 
Let n = 1, then:
There is one external node.

n = e + i
n = 1, e = 1, i = 0
So (*) holds for n = 1

Let T be a tree with n + 1 nodes

If we remove a root from tree, then we are creating 2 subtrees.
One of then have size at least 1 if so, it is external node, 
and the other tree size must be  n - 2, lets call it S.
Now 
The root of a tree n > 2 must be internal node, so we removed
one internal and one external from its size (2 nodes).
Lets put it together again.
(n - 2) = (e - 1) + (i - 1)
S = T - i - e
so
T = S + i + e.

There will be one onenoded tree that matches our base case.

e = i + 1



"""