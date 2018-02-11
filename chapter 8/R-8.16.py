"""
Let T be a binary tree with n nodes, and let f() be the level numbering
function of the positions of T, as given in Section 8.3.2.
a. 
Show that, for every position p of T, f(p) ≤ 2^n −2.

b. 
Show an example of a binary tree with seven nodes that attains the
above upper bound on f(p) for some position p.

f(p)
• If p is the root of T, then f(p) = 0.
• If p is the left child of position q, then f(p) = 2 f(q) +1.
• If p is the right child of position q, then f(p) = 2 f(q) +2.

Lets examine 2 cases
The height of the tree is (n-1).
f(p) = 2 f(q) +2

Base cases: 
h   n    f(p)   2^n-2    
0   1    0      0
1   2    2      2
2   3    6      6
3   4    14     14
f(n) = 2^n - 2

We assume that g is a node at height (n-1) > 0
f(h) < 2^(n-1) - 2
f(h) = 2 f(h-1) + 2
f(n+1) = 2 f(n) + 2, n > 1
Applay inductive hypothesis
f(n+1) = 2 * (2^(n-1) - 2) + 2
f(n+1) = 2^(n) - 2

In this case:
f(n+1) = 2^n − 2,
2^(n) - 2 = 2^n − 2

'worst' case:
f(h) < 2^(n-1) - 2
f(h) = 2 f(h-1) +1
f(n+1) = 2 f(n) + 1, n > 1
Apply inductive hypothesis
f(n+1) = 2 * (2^(n-1) - 2) + 1
f(n+1) = 2^(n) - 4 + 1
f(n+1) = 2^(n) - 3

In this case:
f(n+1) < 2^n − 2,
2^(n) - 3 < 2^n −2

b.
        root
          |
        node
          |
        node
          |
        node
          |
        node
          |
        leaf
"""
