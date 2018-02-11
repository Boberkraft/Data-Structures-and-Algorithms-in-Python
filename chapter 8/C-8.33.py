"""
Let T be a (possibly improper) binary tree with n nodes, and let D be the
sum of the depths of all the external nodes of T. Describe a configuration
for T such that D is Ω(n^2). Such a tree would be the worst case for the
asymptotic running time of method height1 (Code Fragment 8.4).

https://cs.stackexchange.com/questions/87336/maximum-sum-of-depths-of-all-external-nodes-in-a-binary-tree
Thanks bruh

Consider a tree that has a chain of length n/2 at the top, where each node has exactly one child. 
Then, the remaining n/2 nodes are attached at the bottom of the chain, as a complete tree of depth log2(n/2)

With this shape, every leaf is at depth n/2+log2(n/2)=Θ(n).
There are about n/4=Θ(n) leaves. So, the sum of the depths of the leaves is E(T)=Θ(n^2).
"""