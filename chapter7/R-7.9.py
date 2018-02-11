"""
Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list L

"""
from LinkedDeque import LinkedDeque


def conc(L, M):
    middle = L._header.next
    head = L._header

    M._trailer.prev.next = middle
    middle.prev = M._trailer.prev
    head.next = M._header.next
    head.next.prev = head

    L._size += M._size


l = LinkedDeque()
l.insert_first(1)
l.insert_first(2)
l.insert_first(3)
m = LinkedDeque()
m.insert_first(9)
m.insert_first(8)
m.insert_first(7)
conc(l, m)

for _ in range(len(l)):
    print(l.delete_first())
