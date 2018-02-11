"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
"""

from LinkedStack import LinkedStack


def give_second_to_last(q):
    if len(q) > 0:
        note = q._head
        for x in range(len(q) - 2):
            note = note.next
        return note


q = LinkedStack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
x = give_second_to_last(q)
print(x.element)
