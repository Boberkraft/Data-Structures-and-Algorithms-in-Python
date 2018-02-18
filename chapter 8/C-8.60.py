"""
Suppose each position p of a binary tree T is labeled with its value f (p) in
a level numbering of T. Design a fast method for determining f (a) for the
lowest common ancestor (LCA), a, of two positions p and q in T, given
f (p) and f (q). You do not need to find position a, just value f (a).
def find_lca(one, q):
    f = lambda x: bin(x + 1)[2:]
    one = f(one)
    q = f(q)
    ans = []
    one, q = max(one, q), min(one, q)
    for i in range(len(one)):
        if one[i] == q[i]:
            ans.append(one[i])
        else:
            break

    return int(''.join(ans), 2) - 1
"""

from math import log2
from math import floor


def find_lca2(p, q):
    # a comment
    bits = lambda x: floor(log2(x)) + 1
    p, q = max(p, q), min(p, q)
    q += 1
    p += 1
    q = q << bits(p) - bits(q)
    ans = 0
    last_bit = 2 ** (bits(q) - 1)
    while True:
        if q & last_bit == p & last_bit:
            ans += (q & last_bit)
            ans = ans << 1
            last_bit = last_bit >> 1
        else:
            ans = ans >> bits(q)
            return ans - 1


left = 20
right = 15
# x = find_lca(left, right)
# print('lca =', x)
x = find_lca2(left, right)
print('lca =', x)
