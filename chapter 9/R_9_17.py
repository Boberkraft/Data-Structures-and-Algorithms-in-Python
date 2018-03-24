"""
Let H be a heap storing 15 entries using the array-based representation of
a complete binary tree. What is the sequence of indices of the array that
are visited in a preorder traversal of H? What about an inorder traversal
of H? What about a postorder traversal of H?

Wasn't this think an exercise in chapter with trees?

For visualization: 
                      
              0      
        1           2          
     3     4     5     6             
    7  8  9 10 11 12 13 14
                
                

Lets use imagination!
Preorder    : 0 -> 1 -> 3 -> 7 -> 8 -> 4 -> 9 -> 10 -> 2 -> 5 -> 11 -> 12 -> 6 -> 13 -> 14
Inorder     : 7 -> 3 -> 8 -> 1 -> 9 -> 4 -> 10 -> 0 -> 11 -> 5 -> 12 -> 2 -> 13 -> 6 -> 14
Postorder   : 7 -> 8 -> 3 -> 9 -> 10 -> 4 -> 1 -> 11 -> 12 -> 5 -> 13 -> 14 -> 6 -> 2 -> 0


"""