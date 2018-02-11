"""
Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order.
"""

from ArrayStack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


data = ArrayStack()
[data.push(x) for x in list(range(10))]
s1 = ArrayStack()
s2 = ArrayStack()

transfer(data, s1)
transfer(s1, s2)
transfer(s2, data)
print(data.look())
