"""
Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L
that contains all the nodes of L followed by all the nodes of M.
"""

def conc(L, M):
    head = L._header
    for _ in range(len(L) - 1):
        head = head.next

    head.next = M._header
