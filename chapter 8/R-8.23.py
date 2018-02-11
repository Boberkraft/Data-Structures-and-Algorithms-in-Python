"""
Let T be an ordered tree with more than one node. Is it possible that the
preorder traversal of T visits the nodes in the same order as the postorder
traversal of T? If so, give an example; otherwise, explain why this cannot
occur. Likewise, is it possible that the preorder traversal of T visits the
nodes in the reverse order of the postorder traversal of T? If so, give an
example; otherwise, explain why this cannot occur

The preorderd traversal perform action on parent nodes before children
The postorder travelsina preform actions on children ignoring parents.

Is it possible that the preorder traversal of T visits 
the nodes in the same order as the postorder traversal of T?
NO BECAUSE for tree with n > 1 there is at least one child and one parent. 

-------------------------------
is it possible that the preorder traversal of T visits 
the nodes in the reverse order of the postorder traversal of T?

Lets consider this tree:
        A
        |
        B
        |
        C
        
Preorder yields:    ABC
Postorder yields:   CBA

"""