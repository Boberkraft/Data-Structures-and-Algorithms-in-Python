"""
 Describe how to perform a removal from a hash table that uses linear
probing to resolve collisions where we do not use a special marker to
represent deleted elements. That is, we must rearrange the contents so that
it appears that the removed entry was never inserted in the first place.

We can store int the _Item object information about oryginal position:
so then we can go right of the deleted item and check if it should be moved

OR
rehash all values on the right of the removed object, stopping on first None
 
"""