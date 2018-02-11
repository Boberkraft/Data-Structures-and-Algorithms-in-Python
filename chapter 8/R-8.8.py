"""
Answer the following questions so as to justify Proposition 8.8.

a. What is the minimum number of external nodes for a proper binary
tree with height h? Justify your answer.

b. What is the maximum number of external nodes for a proper binary
tree with height h? Justify your answer.

c. Let T be a proper binary tree with height h and n nodes. Show that
log(n+1)−1 ≤ h ≤ (n−1)/2.

d. For which values of n and h can the above lower and upper bounds
on h be attained with equality?

   x
  x x
x x x x
h = 2
n = 7

Look its like couting in binary!
On each level there is 2 times more nodes than on the level before.
nodes = 2^(level)
And in a proper binary tree, every node on the last level are 
externals.


a.
h + 1

There must be at least as many internal nodes as height of the tree.
And from Proposition 8.9 we know that external = internal + 1

b.
2 **(h)
when the tree is complete then on each level there is 2 
times more nodes than on the level before, starting from 1.
The level of a tree equals heigh of a root.

c.
 - (n−1)/2 is the maximum number of nodes on one site of root.
 - log(n + 1) - 1 is the level of the tree in a complete binary tree
 - h is the height of the tree, maximum depths of the tree leafs




Level of a complete tree = h 
because all leafes are on  the same level,  thus every leaf depth 
in this tree are the same and equals the height of the tree.

Level of a complete tree < h.
The height can be the same, but number of nodes can be smaller
and level depends on n.

Worst case:
external = internal + 1
maximum height equals number of internal nodes.
nodes = 2*internals + 1

minimum number of internal nodes 
level <= height
log(2*i+2)-1 <= i
log(2(i+1)) - 1 < =i
1 + log(i+1) - 1 <= i
log(i+1) <= i.
for every i > 1 the height is greater then level.
In not perfect tree if we create 2 subtrees by removing the root, then one of them
will have height h - 1. If both have, split again because at some point one wont have.

Or you can be a count and use google:
https://cs.nyu.edu/courses/fall02/V22.0310-002/lectures/lecture-09.html

:::
1. 
Induction on n the number of nodes in the tree.
Base case n=1: Clearly true for all trees having only one node.

Induction hypothesis: Assume true for all trees having at most k nodes.

Main inductive step: prove the assertion for all trees having k+1 nodes. Let T be a tree with k nodes and let h be the height of T.

Remove the root of T. The two subtrees produced each have no more than k nodes so satisfy the assertion. Since each has height at most h-1, each has at most 2h-1 leaves. At least one of the subtrees has height exactly h-1 and hence has at least h leaves. Put the original tree back together.
One subtree has at least h leaves, the other has at least 1, so the original tree has at least h+1. Each subtree has at most 2h-1 leaves and the original root is not a leaf, so the original has at most 2h leaves.

2.
Same idea. Induction on the number of nodes. Clearly true if T has one node. Remove the root. At least one of the subtrees is height h-1 and hence has at least h-1 internal nodes. Each of the subtrees has height at most h-1 so has at most 2h-1-1 internal nodes. Put the original tree back together. One subtree has at least h-1 internal nodes, the other has at least 1, so the original tree has at least h. Each subtree has at most 2h-1-1 internal nodes and the original root is an internal node, so the original has at most 2(2h-1)+1 = 2h-1-1 internal nodes.
3.
Add parts 1 and 2.
4.
Take the log of part 3.

h = (n-1)/2
If we split the
Minimum
i = (2i)/2
i = i
Maximum:
log(n+1) - 1 = (2i + 1 - 1)/2
log(2i+2) - 1 = i
log(i) = i
for every i > 0 it holds.

d.
Trivial case:
n = 1
h = 0
log(n+1)-1 = h = (n-1)/2
fuck

"""