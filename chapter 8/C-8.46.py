"""
The path length of a tree T is the sum of the depths of all positions in T.
Describe a linear-time method for computing the path length of a tree T.

look C-9.45
"""


class xd:
    def travel_tree(self, tree, p, d):
        sum = 0
        for child in tree.children(p):
            sum += self.travel_tree(tree, child, d + 1)
        return sum


sum = xd.travel_tree(tree, tree.root(), 0)
