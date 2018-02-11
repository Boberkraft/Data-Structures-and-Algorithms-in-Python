"""
Answer the previous question for the case when T is a proper binary tree
with more than one node


Is it possible that the preorder traversal of T visits 
the nodes in the same order as the postorder traversal of T?
Still nope

is it possible that the preorder traversal of T visits 
the nodes in the reverse order of the postorder traversal of T?

Lets consider this tree:
        A
      /  \
     B    C
PRE: ABC
Post: BCA

Postorder and Preorder both firstly scan left subtree.
If they both work on the same half living the other for later,
then how postorder can swap places with the right site?

"""