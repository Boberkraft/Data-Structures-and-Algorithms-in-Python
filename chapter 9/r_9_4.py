"""
An airport is developing a computer simulation of air-traffic control that
handles events such as landings and takeoffs. Each event has a time stamp
that denotes the time when the event will occur. The simulation program
needs to efficiently perform the following two fundamental operations:
• Insert an event with a given time stamp (that is, add a future event).
• Extract the event with smallest time stamp (that is, determine the
next event to process).
Which data structure should be used for the above operations? Why?


Priority Queue!
Why? Because w are at a chapter with priority queues... of course...

But in reality its because we need to extract events with the lowest timestamp, 
and this is exactly the purpose of PriorityQueue(TM).
Just imagine that lower timestamp is the key of an event.

We need to have a way to extract item with the smallest key, and insert new items.
"""