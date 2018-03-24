"""
Is there a heap H storing seven entries with distinct keys such that a preorder
traversal of H yields the entries of H in increasing or decreasing
order by key? How about an inorder traversal? How about a postorder
traversal? If so, give an example; if not, say why.

Pre Order
    ascending:
        1
      2   5
     3 4 6 7
    descending:
        cannot be done, because the first element visited by preorder traversal is root, and it contains
        the smallest element.
        
In Order 
    ascending:
        cannot be done, because the first element visited by inorder traversal is a leaf, and it can
        contains largest element, not smallest
    descending:
            1
          5   4
         7 6 5 6
        cannot be done, because the middle element visited by inorder traversal is root, and it contains
        the smallest element.
        
Post Order 
    ascending:
        cannot be done, because last element visited by post order traversal is root, and it contains
        the smallest element.
    descending:
        1
      5   2
     7 6 4 3

"""