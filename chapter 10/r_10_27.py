"""
What abstraction would you use to manage a database of friends’ birth-
days in order to support efficient queries such as “find all friends whose
birthday is today” and “find the friend who will be the next to celebrate a
birthday”?

I would use skiplist + the key is a date.
If we can ignore the leap year then key can be days from 1 January.
Otherwise something like a tuple with a special comparison function:
(1, 12)
(1, 14)
[...]
(12, 27)

"""