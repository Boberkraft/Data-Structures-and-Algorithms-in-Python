"""
Given a proper binary tree T, define the reflection of T to be the binary
tree T' such that each node v in T is also in T', but the left child of v in T
is v’s right child in T' and the right child of v in T is v’s left child in T'.
Show that a preorder traversal of a proper binary tree T is the same as the
postorder traversal of T’s reflection, but in reverse order.

pre
     0
    1 2  -> 0 1 2

REFLECITON

post 
    0
   2 1  -> 2 1 0
   
reverse post
        -> 0 1 2
        
ok i see that it works

If node dont have leafes then its correct
if node have left and right childs then:
    preorder visits v -> left -> right

    postorder visits left -> right -> v
    
    lets swap children
    postorder visits right -> left -> v
    
    lets reverse the `direction`
    postorder yeilds v -> left -> right
    AND ITS THE SAME AS preorder visits OF UNCHANGED CHILDS
    
"""