"""
Describe in detail how to swap two nodes x and y (and not just their contents)
in a singly linked list L given references only to x and y. Repeat
this exercise for the case when L is a doubly linked list. Which algorithm
takes more time?

We need to know a node BEFORE x and y.
For each node in each list we need to check if reference to next node is our node x. If it is change the reference to y and cheange y.next to x.next.
Remeber to store x.next.


Doubly linked list:
        if a.next == b or a.prev == b:
            # they are adjustend
            print('adjustend')
            bef_a, af_b = a.prev, b.next
            bef_a.next = b
            af_b.prev = a
            a.prev, a.next, b.prev, b.next = b, b.next, a.prev, a

        else:
            a.prev.next = b
            a.next.prev = b

            b.prev.next = a
            b.next.prev = a
            a.prev, a.next, b.prev, b.next = b.prev, b.next, a.prev, a.next



It have constant time in the case of doubly linked list.
"""
