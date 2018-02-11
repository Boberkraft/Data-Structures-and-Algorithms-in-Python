"""
Let T be a (not necessarily proper) binary tree with n nodes, and let E(T) be
the sum of the depths of all the external nodes of T. Show that if T has the
minimum number of external nodes possible, then E(T) is O(n) and if T has
the maximum number of external nodes possible, then E(T) is O(n log n).


So lets consider 2 trees:
0      x
1    x   x
2  x  x x x
and
    x
    x
    x

In case 1 the number of leafs is 2 ^ (log(n+1)-1):
On the last level every node have the same depth that equals 2*height of tree
height of the tree = log2(n+1) - 1
sum of depths of the nodes:
2*(log2(n+1) - 1) *(log2(n+1) - 1) is Ω(n^2)

2*(log2(n+1) * 2*(-1) *(log2(n+1) - 1) is Ω(n^2)
(n+1) * 1/2 *(log2(n+1) - 1) is Ω(n^2)
O(n) * O(1) * O(log 2) is Ω(n^2)
O(n log n)


In case 2 the number of leafs is 1.
Because of that the sum of all externals nodes equals to
depth of that particulary node.
Because every node is ancestor of this leaf, its depth is
n - 1
n - 1 < n ==> O(n)


"""


