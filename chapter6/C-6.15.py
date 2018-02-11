"""
Suppose Alice has picked three distinct integers and placed them into a
stack S in random order. Write a short, straight-line piece of pseudo-code
(with no loops or recursion) that uses only one comparison and only one
variable x, yet that results in variable x storing the largest of Alice’s three
integers with probability 2/3. Argue why your method is correct.

Its like having 2 chances.

Normaly withoud any trick change to quess is 1/3 because one answer is true and
three not.

So using comparasion you can eliminate one number  (1/3) and add it to your probability.
If you think it should be 1/2
think about this situation:
you have 100 number.
What is the probability that the last number is largest? 1/100,
So check first 99 numbers.
and you have 99 % that you can get good answer
"""

from ArrayStack import ArrayStack
from random import shuffle

s = ArrayStack()
data = list(range(3))
shuffle(data)
for x in data:
    s.push(x)
x = s.pop()
x = max(x, s.pop())
print(s.look(), x)
