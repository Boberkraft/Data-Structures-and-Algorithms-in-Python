"""
When using a linked-tree representation for a heap, an alternative method
for finding the last node during an insertion in a heap T is to store, in the
last node and each leaf node of T, a reference to the leaf node immediately
to its right (wrapping to the first node in the next lower level for the
rightmost leaf node). Show how to maintain such references in O(1) time
per operation of the priority queue ADT assuming that T is implemented
with a linked structure.



We need to store a reference to a node that starts a layer, so 
when the space on current layer is exhausted we can start new layer fairly
easy.

And we need to store a reference to the last node. 

Each node needs to have a reference to its left and right `sibling`, but 
the exerices states that i only the right one...
"""

































