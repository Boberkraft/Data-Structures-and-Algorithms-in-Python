"""
Exercise C-5.29 introduces the notion of a natural join of two databases.
Describe and analyze an efficient algorithm for computing the natural join
of a linked list A of n pairs and a linked list B of m pairs

It is still as simple as before?
A is
header -> (1, a) <-> (42, b) <->(425 c) <->(11, d) <- trailer
b is
header -> (d, 0) <-> (c, 33) <->(a, 11) <->(a, 321) <- trailer

and we need to make a new list of elements with the same b.
header -> (1, a, 11) <-> (1, a, 321) <-> (425, c, 33) <-> (11, d, 0)<- trailer
Its O(n^2). Lets assume that all elements in node_a[1] and node_b[0] are the same.
eq.
  A        B
(1, a)  (a, 11)
(2, a)  (a, 12)
(3, a)  (a, 13)
(4, a)  (a, 14)
(5, a)  (a, 15)
(6, a)  (a, 16)

"""
from PositionalList import PositionalList
from collections import defaultdict

a = PositionalList()
b = PositionalList()
a.add_first((1, "a"))
a.add_first((2, "b"))
a.add_first((3, "c"))

b.add_first(("a", 99))
b.add_first(("c", 69))


def make_dict(l, f):
    serching_for = defaultdict(list)  # there can be more than one common element
    # adding to dict
    pos = l.first()
    while pos is not None:
        serching_for[f(pos.element())].append(pos)
        pos = l.after(pos)
    return serching_for


a_dict = make_dict(a, lambda x: x[1])  # grab only 2 cell
b_dict = make_dict(b, lambda x: x[0])  # grab only 1 cell

# common elements
common = set(a_dict) & set(b_dict)

# extract common elements
end = PositionalList()
for com in common:
        for a_pos in a_dict[com]:
            for b_pos in b_dict[com]:
                a, b, c = a_pos.element()[0], com, b_pos.element()[1]
                end.add_first((a, b, c))

# lets see the result
[print(el) for el in end]
