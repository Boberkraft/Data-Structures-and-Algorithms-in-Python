"""
Algorithm preorder draw draws a binary tree T by assigning x- and ycoordinates
to each position p such that x(p) is the number of nodes preceding
p in the preorder traversal of T and y(p) is the depth of p in T.
    
    a. Show that the drawing of T produced by preorder draw has no pairs
    of crossing edges.
    
    b. Redraw the binary tree of Figure 8.22 using preorder draw
    
a)
Because children from the same node have the same dept (d + 1), and preorder assures that 
the x pos is continulsy increasing, never going back in terms of x. Leaving behind sibling children



Does anybody have good induction solution?
if node have only one child -> No cross
if node have 2 child -> (root) (root.child1) (root.child2)


lets assume true for x > 2:
    placing a new child we search for the last node on graph (x = k) and add one
    and y = depth 
    lets add a node 
    
    we want to be the k + 1
    we want to be at depth parent + 1. Parent can only be one depth higher. 
"""