"""
Describe how to implement the stack ADT using a single queue as an
instance variable, and only constant additional local memory within the
method bodies. What is the running time of the push(), pop(), and top()
methods for your design?

for push just enqueue an element

for pop do enqueue(dequeue) x (len(queue) - 1)
and then one return enqueue()

for top do enqueue(dequeue) x (len(queue) - 1)
and then x = dequeue()
enqueue(x)
return x


Push -> O(1) like in normal amortized list

pop -> O(n) because you need to call enqueue and dequeue n times
even when underlying queue shrinks its still O(n) because you can do a chenge
when n elements are moved to another list (n - 1 moves)

top -> O(n) same as pop
"""