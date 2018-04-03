"""
Let S be a set of n points in the plane with distinct integer x- and ycoordinates.
Let T be a complete binary tree storing the points from S
at its external nodes, such that the points are ordered left to right by increasing
x-coordinates. For each node v in T, let S(v) denote the subset of
S consisting of points stored in the subtree rooted at v. For the root r of
T, define top(r) to be the point in S = S(r) with maximum y-coordinate.
For every other node v, define top(r) to be the point in S with highest ycoordinate
in S(v) that is not also the highest y-coordinate in S(u), where
u is the parent of v in T (if such a point exists). Such labeling turns T into
a priority search tree. Describe a linear-time algorithm for turning T into
a priority search tree. Implement this approach.

Mam sobie punkty (x, y) z niepowtarzającymi się x i y.
Znajduję się one na płaszczyźnie S.

Niech T będzie drzewem binarym, w którym punikty z S są liścmi i posortowane są
z lewej do prawy dzięki x.

Dla każdego węzła w drzewie, niech S(v) oznacza podzbiór S zawierający jedynie punkty
zawarte w drzewie o korzeniu v.

Dla korzenia r w naszym drzewie, top(r) niech będzie punktem na płaszczyźnie S zawierający
największą współrzędna y.

Dla każdego węzła v -> top(v) jest punktem :
            : z drugą największą współrzędną y top(parent(v))
            : z największą współrzędna y, która nie jest największą dla rodzica v.
            (jeżeli taki punkt istnieje)
             
So i have a plane => S:

9     x                              
8                                  
7               x                    
6         x                          
5           x                        
4             x                      
3       x                            
2                               
1   x                                
0 x                                  
  0 1 2 3 4 5 6 7
        
My tree => T:
                 
         .          
     .       .              
   .   .   .   .     
  0 1 9 3 6 5 4 7 
  
Lets add labeling:

                  
         9         
     3       7             
   1   ?   6   4 
  0 ? ? ? ? 5 ? ? 


Ok i got it!                
         9          
     3       7              
   1       6   4     
  0         5     


Given a tree T => 
         .          
     .       .              
   .   .   .   .     
  0 1 9 3 6 5 4 7
   
Applay this algorithm on root:

def alg(node):
    alg(left(node))
    alg(right(node))
    if node have children:
        lets swap this node with it's greatest proper children
        
        # remember that we are null node, so now check if we have children, 
        # we need to move all of the proper nodes top
        alg(node)
"""
import sys

sys.path.append('..\\chapter 8')
from LinkedBinaryTree import LinkedBinaryTree
from other import intented_parenthetic, parenthesize

class NullNode:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return 'N'.format(self.n)

    def __repr__(self):
        return str(self)


def algorithm(tree, p):
    if tree.left(p) is not None:
        algorithm(tree, tree.left(p))

    if tree.right(p) is not None:
        algorithm(tree, tree.right(p))

    # pick the greatest child
    left = None
    right = None

    if tree.left(p) is not None and not isinstance(tree.left(p).element(), NullNode):
        left = tree.left(p)
    if tree.right(p) is not None and not isinstance(tree.right(p).element(), NullNode):
        right = tree.right(p)

    if left is None and right is None:
        greatest = None
    elif left is not None and right is not None:
        greatest = left if left.element() > right.element() else right
    elif left is None and right is not None:
        greatest = right
    else:
        greatest = left


    # so now we have the greatest node, now swap current node with
    # the greatest child and because we need to check if there are children
    # so we are calling algorithm again on (now moved) p
    if greatest is not None:

        # swap them!
        tree._replace(greatest, tree._replace(p, greatest.element()))
        algorithm(tree, greatest)

"""
     .      
   .   .   
  0 1 9 3 
"""
# preparation part
tree = LinkedBinaryTree()
root = tree._add_root(NullNode('root'))
root_right = tree._add_right(root, NullNode('right'))
root_left = tree._add_left(root, NullNode('left'))

root_left_left = tree._add_left(root_left, 0)
root_left_right = tree._add_right(root_left, 1)

root_right_left = tree._add_left(root_right, 9)
root_right_right = tree._add_right(root_right, 3)

# preparation part end

print('Before:')
parenthesize(tree, tree.root())
algorithm(tree, root)
print('\nAfter:')
parenthesize(tree, tree.root())
#
