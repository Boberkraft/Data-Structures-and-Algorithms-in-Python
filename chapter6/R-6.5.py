"""
Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order
"""
from ArrayStack import ArrayStack

def reverse(data):
    s = ArrayStack()
    for x in data:
        s.push(x)
    for x in range(len(data)):
        data[x] = s.pop()

data = list(range(10))
reverse(data)
print(data)