"""
Two ordered trees T' and T'' are said to be isomorphic if one of the following
holds:
• Both T' and T'' are empty.
• The roots of T' and T'' have the same number k ≥ 0 of subtrees, and
the ith such subtree of T' is isomorphic to the ith such subtree of T''
for i = 1, . . . ,k.
Design an algorithm that tests whether two given ordered trees are isomorphic.
What is the running time of your algorithm?

#my first attempt 


Good?


"""


# MY FIRST ATTEMPT --------------------------------
# Worst case: they are almost identical and have the same number of nodes:
def is_isomorphic(a, b):
    if a is b is None:
        return True

    if a is None or b is None:
        return False

    # can i sort them by name?
    if len(a.children()) == len(b.children()):
        for a_child in a:
            found = False
            for b_child in b:
                if is_isomorphic(a_child, b_child) and is_isomorphic(b_child, a_child):
                    found = True
                    break
            if found is False:
                # Cannot find pair for this child
                return False
    return True

# i dropped this idea because i didnt knew how to calculate complexity ;ppp

# ------------------------------------------------------


# Worst case: The number of nodes in the larger tree ;/
# my problem is that i cannot get an idea how to at the same time compere 2 trees on the same level.
# and esentially to

def _do_sum(node, this_level, common_levels):
    # increase level array if needed
    if len(common_levels) <= this_level:
        common_levels.append([])

    # sum this node
    common_levels[this_level] += 1

    # is a leaf, drop!
    if node.children is None:
        return 0

    for child in node.children:
        common_levels[this_level] += _do_sum(child, this_level, common_levels)


def is_isomorphic2(TreeA, TreeB):
    # Im a genius? Its only O(N) ok im not
    sum_A = []
    sum_B = []
    _do_sum(TreeA, 0, sum_A)
    _do_sum(TreeB, 0, sum_B)
    return sum_A == sum_B
