"""
A slicing floor plan divides a rectangle with horizontal and vertical sides
using horizontal and vertical cuts. (See Figure 8.25a.) A slicing floor plan
can be represented by a proper binary tree, called a slicing tree, whose
internal nodes represent the cuts, and whose external nodes represent the
basic rectangles into which the floor plan is decomposed by the cuts. (See
Figure 8.25b.) The compaction problem for a slicing floor plan is defined
as follows. Assume that each basic rectangle of a slicing floor plan is
assigned a minimum width w and a minimum height h. The compaction
problem is to find the smallest possible height and width for each rectangle
of the slicing floor plan that is compatible with the minimum dimensions

of the basic rectangles. Namely, this problem requires the assignment of
values h(p) and w(p) to each position p of the slicing tree such that:



w(p) = |        w        => if p is a leaf whose basic rectangle has min width of w
       
       | max(w(l), w(r)) => if p is an internal position, assosiated with a horizontal
                            cut, with left child l and right child r
       
       | w(l) + w(r)     => if p is an internal position, assosiated with a 
                            vertical cut, with child l and right child r
                        
                        
                        
h(p) = |        h        => if p is a leaf whose basic rectangle has min height of h
       
       |   h(l) + h(r)   => if p is an internal position, assosiated with a horizontal
                            cut, with left child l and right child r
       
       | max(h(l), h(r)) => if p is an internal position, assosiated with a 
                            vertical cut, with child l and right child r
                            
                            
    
Design a data structure for slicing floor plans that supports the operations:

• Create a floor plan consisting of a single basic rectangle.

• Decompose a basic rectangle by means of a horizontal cut.

• Decompose a basic rectangle by means of a vertical cut.

• Assign minimum height and width to a basic rectangle.

• Draw the slicing tree associated with the floor plan.

• Compact and draw the floor plan.

+---------------+----------------+                          
|      E        |      F         |                          
|               |                |    
|-----------+---+-------+--------+              
|           |           |        |         
|           |           |        |              
|           |           |        |          
|           |    C      |   D    |        
|    A      |           |        |      
|           |           |        |            
|           |-----------+--------|     
|           |                    |    
|           |          B         |  
+-----------+--------------------+                           


                 +---+
                 |   |
        +------> | _ | <----------------------+
        |        |   |                        |
        |        +---+                        |
        |                                     |
      +-+-+                                 +-+-+
      |   |                                 |   |
  +-> | | | <-+                         +-> | | | <-+
  |   |   |   |                         |   |   |   |
  |   +---+   |                         |   +---+   |
+-+-+       +-+-+                     +-+-+       +-+-+
|   |       |   |                     |   |       |   |
| A |   +-> | _ | <-+                 | E |       | F |
|   |   |   |   |   |                 |   |       |   |
+---+   |   +---+   |                 +---+       +---+
      +-+-+       +-+-+
      |   |       |   |
      | B |   +-> | | | <-+
      |   |   |   |   |   |
      +---+   |   +---+   |
            +-+-+       +-+-+
            |   |       |   |
            | C |       | D |
            |   |       |   |
            +---+       +---+
"""