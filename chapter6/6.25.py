"""
Describe how to implement the queue ADT using two stacks as instance
variables, such that all queue operations execute in amortized O(1) time.
Give a formal proof of the amortized bound.

proof of the amortized bound wasnt so formal

Firstly we need to ignore space and assume that underlying arrays do not shrinks when moving
all elements

As we know expanding underlying array is O(1)* so ignore it.

Assume that adding enqueueing element generates 2 monets.
One monet is spend on assigning a room for number
and another one is to spend in future when moving to 2nd stack.



cost = worst-case sequence complexity/n
i insert n items. Each one of them took O(1)

i need to pop n items. Each of them took O(1) + one O(n) to move from stack to stack.
it cost me 2n, and i did n + 1 operations
O(2n)/n+1 ~= 1

"""

from ArrayStack import ArrayStack


class Empty(Exception):
    pass


class Queue:
    def __init__(self):
        self._in = ArrayStack()
        self._out = ArrayStack()

    def enqueue(self, e):
        self._in.push(e)

    def dequeue(self):
        if self._out.is_empty():
            while not self._in.is_empty():
                self._out.push(self._in.pop())

        if self._out.is_empty():
            raise Empty()
        return self._out.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
