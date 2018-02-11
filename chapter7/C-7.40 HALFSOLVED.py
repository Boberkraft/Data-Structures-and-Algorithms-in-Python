"""
Describe an efficient method for maintaining a favorites list L, with moveto-front
heuristic, such that elements that have not been accessed in the
most recent n accesses are automatically purged from the list.

The list have a counter.

node have got an variable to save counter status when accessed (when = counter)
counter + 1 on every access
for every access go check the end of list to see if the (counter - when) > n.
If so, delete it.


Reser couter every 1m accesses and adjust nodes counters too.


Is there better solution? idk
"""