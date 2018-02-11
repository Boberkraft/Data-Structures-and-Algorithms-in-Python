"""
Two ordered trees T' and T'' are said to be isomorphic if one of the following
holds:
• Both T' and T'' are empty.
• The roots of T' and T'' have the same number k ≥ 0 of subtrees, and
the ith such subtree of T' is isomorphic to the ith such subtree of T''
for i = 1, . . . ,k.
Design an algorithm that tests whether two given ordered trees are isomorphic.
What is the running time of your algorithm?



def is_isomorphic(a,b):
    if a == b == None
        return True
    if a == None or b == None):
        return False
    
    
    #can i sort them by name?
    if len(a.children()) ==  len(b.children()):
        for a_child in a:
            found = False
            for b_child in b:
                if is_isomorphic(a_child, b_child) and is_isomorphic(b_child, a_child):
                    found = True
                    break
            if found is False:
                #Cannot find pair for this child
                return False
    return True

Good?
Worst case: they are almost identical have the same number of nodes:

aaaand i dont know

"""